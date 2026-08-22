#!/usr/bin/env python3
"""Fail-closed semantic validator for terminal-agent assignment records.

Validation is evidence only. A VALID result grants no repository, runtime,
Council, or Operator authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

MOVE_OPERATIONS = {"MOVE", "RENAME"}
RENAME_STATUS_CODES = {"R", "C"}


class AssignmentValidationError(ValueError):
    pass


def canonical_digest(value: Any) -> str:
    encoded = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def content_digest(value: str) -> str:
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def _timestamp(value: str, field: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, ValueError) as exc:
        raise AssignmentValidationError(f"{field} must be an ISO 8601 timestamp") from exc
    if parsed.tzinfo is None:
        raise AssignmentValidationError(f"{field} must include a timezone")
    return parsed


def report_binding(record: dict[str, Any]) -> dict[str, Any]:
    """Canonical object binding the inspection report to checkout identity.

    Hashing the report alone allows authorization evidence to be replayed against
    a different assignment, repository, branch, or head. The digest therefore
    covers the identity fields that define what was actually inspected.
    """
    return {
        "schema_version": record["schema_version"],
        "assignment_id": record["assignment_id"],
        "repository": record["repository"],
        "branch": record["branch"],
        "head_sha": record["head_sha"],
        "base_ref": record.get("base_ref"),
        "inspection_before_write": record["inspection_before_write"],
        "inspection_report": record["inspection_report"],
    }


def authorized_scope(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "authorized_files": record["authorized_files"],
        "authorized_commands": record["authorized_commands"],
        "external_effects": record["external_effects"],
    }


def status_capture(incident: dict[str, Any]) -> dict[str, Any]:
    """Canonical status capture covering the raw text and its parsed records."""
    return {
        "worktree_status": incident["worktree_status"],
        "worktree_status_record": incident["worktree_status_record"],
    }


def _scope_identities(entries: list[dict[str, Any]], field: str) -> set[tuple[str, str, str | None]]:
    seen_paths: set[str] = set()
    identities: set[tuple[str, str, str | None]] = set()
    for entry in entries:
        path = entry["path"]
        operation = entry["operation"]
        destination = entry.get("destination_path")
        if path in seen_paths:
            raise AssignmentValidationError(
                f"{field} declares more than one operation class for {path}"
            )
        seen_paths.add(path)
        if operation in MOVE_OPERATIONS:
            if not destination:
                raise AssignmentValidationError(
                    f"{field} entry for {path} declares {operation} without a destination_path"
                )
            if destination == path:
                raise AssignmentValidationError(
                    f"{field} entry for {path} declares {operation} onto itself"
                )
        elif destination is not None:
            raise AssignmentValidationError(
                f"{field} entry for {path} declares a destination_path for {operation}"
            )
        identities.add((path, operation, destination))
    return identities


def _status_identities(records: list[dict[str, Any]]) -> set[str]:
    """Every path identity named by the structured status capture.

    Rename and copy entries contribute both source and destination identities so
    a move cannot be laundered into an unrelated single-path claim.
    """
    identities: set[str] = set()
    for entry in records:
        xy = entry["xy"]
        path = entry["path"]
        original = entry.get("original_path")
        if set(xy) & RENAME_STATUS_CODES:
            if not original:
                raise AssignmentValidationError(
                    f"status record {xy} for {path} omits its original_path"
                )
            if original == path:
                raise AssignmentValidationError(
                    f"status record {xy} for {path} names itself as its original_path"
                )
            if original in identities:
                raise AssignmentValidationError(f"duplicate status record path {original}")
            identities.add(original)
        elif original is not None:
            raise AssignmentValidationError(
                f"status record {xy} for {path} must not declare an original_path"
            )
        if path in identities:
            raise AssignmentValidationError(f"duplicate status record path {path}")
        identities.add(path)
    return identities


def _validate_authorization_validity(
    authorization: dict[str, Any], evidence_times: list[tuple[str, datetime]]
) -> None:
    status = authorization["status"]
    if status != "ACTIVE":
        raise AssignmentValidationError(
            f"authorization status is {status}; only ACTIVE authorization supports implementation or verification"
        )
    if authorization["superseded_by"] is not None:
        raise AssignmentValidationError("an ACTIVE authorization must not name a superseding reference")

    authorized_at = _timestamp(authorization["authorized_at"], "authorization.authorized_at")
    valid_until = _timestamp(authorization["valid_until"], "authorization.valid_until")
    if valid_until <= authorized_at:
        raise AssignmentValidationError("authorization.valid_until must be later than authorized_at")
    for field, moment in evidence_times:
        if moment > valid_until:
            raise AssignmentValidationError(f"{field} is later than authorization.valid_until")


def _validate_bootstrap(record: dict[str, Any]) -> None:
    bootstrap = record["bootstrap_provenance"]
    changes = bootstrap["preexisting_changes"]
    _status_identities(changes)
    if bootstrap["worktree_clean"] and changes:
        raise AssignmentValidationError(
            "bootstrap_provenance claims a clean worktree while recording pre-existing changes"
        )
    if not bootstrap["worktree_clean"] and not changes:
        raise AssignmentValidationError(
            "bootstrap_provenance claims an unclean worktree without recording any pre-existing change"
        )


def _validate_verification(record: dict[str, Any], authorized_paths: set[str]) -> None:
    scope = record["verification_scope"]
    for check in scope["declared_checks"]:
        if check not in record["authorized_commands"]:
            raise AssignmentValidationError(
                f"verification check {check!r} is not an authorized command"
            )
    overlap = sorted(set(scope["artifact_paths"]) & authorized_paths)
    if overlap:
        raise AssignmentValidationError(
            "verification artifact scope must not include implementation source paths: "
            + ", ".join(overlap)
        )


def _validate_handoff(record: dict[str, Any]) -> None:
    handoff = record["handoff_report"]
    _scope_identities(handoff["changed_paths"], "handoff_report.changed_paths")
    if handoff["worktree_state"] == "CLEAN" and handoff["changed_paths"]:
        raise AssignmentValidationError(
            "handoff_report claims a clean worktree while reporting changed paths"
        )


def validate_semantics(record: dict[str, Any]) -> None:
    phase = record["phase"]
    incident = record.get("premature_mutation")

    if incident is not None and phase != "BLOCKED_PREMATURE_MUTATION":
        raise AssignmentValidationError(
            "a premature mutation forces BLOCKED_PREMATURE_MUTATION until a separate disposition record"
        )

    _validate_bootstrap(record)

    report = record.get("inspection_report")
    if report is not None:
        _scope_identities(report["proposed_files"], "inspection_report.proposed_files")
    authorized_identities = _scope_identities(record["authorized_files"], "authorized_files")
    authorized_paths = {path for path, _operation, _destination in authorized_identities}
    authorized_paths |= {
        destination
        for _path, _operation, destination in authorized_identities
        if destination is not None
    }

    if phase in {"IMPLEMENTATION_AUTHORIZED", "VERIFICATION"}:
        authorization = record["authorization"]
        events = record["phase_transition"]["events"]
        report_event, authorization_event = events

        binding_digest = canonical_digest(report_binding(record))
        scope_digest = canonical_digest(authorized_scope(record))
        if report_event["report_binding_digest"] != binding_digest:
            raise AssignmentValidationError("inspection report binding digest mismatch")
        if authorization_event["report_binding_digest"] != binding_digest:
            raise AssignmentValidationError(
                "authorization event is not bound to the inspected assignment identity"
            )
        if authorization["report_binding_digest"] != binding_digest:
            raise AssignmentValidationError(
                "authorization is not bound to the inspected assignment identity"
            )
        if authorization_event["authorization_reference"] != authorization["reference"]:
            raise AssignmentValidationError("authorization reference mismatch")
        if authorization_event["scope_digest"] != authorization["scope_digest"]:
            raise AssignmentValidationError("authorization scope digests disagree")
        if scope_digest != authorization["scope_digest"]:
            raise AssignmentValidationError("authorized scope digest mismatch")

        reported_at = _timestamp(report["reported_at"], "inspection_report.reported_at")
        report_recorded_at = _timestamp(events[0]["recorded_at"], "report event recorded_at")
        authorized_at = _timestamp(authorization["authorized_at"], "authorization.authorized_at")
        authorization_recorded_at = _timestamp(
            events[1]["recorded_at"], "authorization event recorded_at"
        )
        if report_recorded_at < reported_at:
            raise AssignmentValidationError("report event predates report completion")
        if authorized_at != authorization_recorded_at:
            raise AssignmentValidationError("authorization timestamp is not bound to its event")
        if authorized_at <= report_recorded_at:
            raise AssignmentValidationError("authorization is not subsequent to the recorded report")

        evidence_times = [("authorization event recorded_at", authorization_recorded_at)]
        if phase == "VERIFICATION":
            verified_at = _timestamp(
                record["verification_scope"]["verified_at"], "verification_scope.verified_at"
            )
            if verified_at < authorization_recorded_at:
                raise AssignmentValidationError(
                    "verification predates the recorded implementation authorization"
                )
            evidence_times.append(("verification_scope.verified_at", verified_at))
        _validate_authorization_validity(authorization, evidence_times)

        if phase == "VERIFICATION":
            _validate_verification(record, authorized_paths)

    if phase == "HANDOFF_PENDING_DISPOSITION":
        _validate_handoff(record)

    if incident is not None:
        if canonical_digest(status_capture(incident)) != incident["status_capture_digest"]:
            raise AssignmentValidationError("worktree status capture digest mismatch")
        status_paths = _status_identities(incident["worktree_status_record"])
        changed_paths = set(incident["changed_paths"])
        evidence_paths = [item["path"] for item in incident["diff_evidence"]]
        if len(evidence_paths) != len(set(evidence_paths)):
            raise AssignmentValidationError("duplicate diff evidence path")
        if status_paths != changed_paths:
            raise AssignmentValidationError(
                "captured status paths must exactly equal the declared changed paths"
            )
        if set(evidence_paths) != changed_paths:
            raise AssignmentValidationError("diff evidence must cover exactly every changed path")
        for item in incident["diff_evidence"]:
            if not item["capture"]:
                raise AssignmentValidationError(f"empty diff capture for {item['path']}")
            if content_digest(item["capture"]) != item["capture_sha256"]:
                raise AssignmentValidationError(f"diff digest mismatch for {item['path']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    record = json.loads(args.record.read_text(encoding="utf-8"))
    validate_semantics(record)
    print(f"VALID: {args.record}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
