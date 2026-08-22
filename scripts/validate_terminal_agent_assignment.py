#!/usr/bin/env python3
"""Fail-closed semantic validator for terminal-agent assignment records."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any


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


def authorized_scope(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "authorized_files": record["authorized_files"],
        "authorized_commands": record["authorized_commands"],
        "external_effects": record["external_effects"],
    }


def validate_semantics(record: dict[str, Any]) -> None:
    phase = record["phase"]
    incident = record.get("premature_mutation")

    if incident is not None and phase != "BLOCKED_PREMATURE_MUTATION":
        raise AssignmentValidationError(
            "a premature mutation forces BLOCKED_PREMATURE_MUTATION until a separate disposition record"
        )

    if phase in {"IMPLEMENTATION_AUTHORIZED", "VERIFICATION"}:
        report = record["inspection_report"]
        authorization = record["authorization"]
        events = record["phase_transition"]["events"]
        report_event, authorization_event = events

        report_digest = canonical_digest(report)
        scope_digest = canonical_digest(authorized_scope(record))
        if report_event["inspection_report_digest"] != report_digest:
            raise AssignmentValidationError("inspection report digest mismatch")
        if authorization_event["inspection_report_digest"] != report_digest:
            raise AssignmentValidationError("authorization event is not bound to the inspection report")
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

    if incident is not None:
        if content_digest(incident["worktree_status"]) != incident["worktree_status_sha256"]:
            raise AssignmentValidationError("worktree status digest mismatch")
        changed_paths = set(incident["changed_paths"])
        evidence_paths = [item["path"] for item in incident["diff_evidence"]]
        if len(evidence_paths) != len(set(evidence_paths)):
            raise AssignmentValidationError("duplicate diff evidence path")
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
