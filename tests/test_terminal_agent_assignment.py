import copy
import importlib.util
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker, ValidationError


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_terminal_agent_assignment.py"
SPEC = importlib.util.spec_from_file_location("terminal_assignment", MODULE_PATH)
terminal_assignment = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(terminal_assignment)

SCHEMA = json.loads(
    (ROOT / "docs/orchestration/terminal-agent-assignment.schema.json").read_text()
)
EXAMPLE = json.loads(
    (ROOT / "docs/orchestration/terminal-agent-assignment.example.json").read_text()
)

VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def rebind(record):
    """Recompute the digests a well-formed record would carry."""
    scope_digest = terminal_assignment.canonical_digest(
        terminal_assignment.authorized_scope(record)
    )
    binding_digest = terminal_assignment.canonical_digest(
        terminal_assignment.report_binding(record)
    )
    record["authorization"]["scope_digest"] = scope_digest
    record["authorization"]["report_binding_digest"] = binding_digest
    events = record["phase_transition"]["events"]
    events[0]["report_binding_digest"] = binding_digest
    events[1]["report_binding_digest"] = binding_digest
    events[1]["scope_digest"] = scope_digest
    return record


def authorized_record(authorized_files=None):
    record = copy.deepcopy(EXAMPLE)
    record["phase"] = "IMPLEMENTATION_AUTHORIZED"
    record["mutation_posture"] = "SCOPED_WRITE"
    record["authorized_files"] = authorized_files or [
        {"path": "src/app/theia/page.tsx", "operation": "MODIFY", "destination_path": None}
    ]
    record["authorized_commands"] = ["npm test -- theia"]
    record["authorization"] = {
        "reference": "AUTH-001",
        "authorized_at": "2026-08-22T12:05:00Z",
        "authorized_by": "Operator",
        "status": "ACTIVE",
        "valid_until": "2026-08-22T18:00:00Z",
        "superseded_by": None,
        "scope_digest": "sha256:" + "0" * 64,
        "report_binding_digest": "sha256:" + "0" * 64,
    }
    record["phase_transition"] = {
        "events": [
            {
                "event": "INSPECTION_REPORT_RECORDED",
                "recorded_at": "2026-08-22T12:01:00Z",
                "report_binding_digest": "sha256:" + "0" * 64,
            },
            {
                "event": "IMPLEMENTATION_AUTHORIZED",
                "recorded_at": "2026-08-22T12:05:00Z",
                "report_binding_digest": "sha256:" + "0" * 64,
                "authorization_reference": "AUTH-001",
                "scope_digest": "sha256:" + "0" * 64,
            },
        ]
    }
    return rebind(record)


def verification_record():
    record = authorized_record()
    record["phase"] = "VERIFICATION"
    record["mutation_posture"] = "VERIFICATION_ARTIFACTS_ONLY"
    record["verification_scope"] = {
        "verified_at": "2026-08-22T12:30:00Z",
        "declared_checks": ["npm test -- theia"],
        "artifact_paths": ["reports/theia-typecheck.log"],
    }
    return record


def incident_record(status_records, changed_paths, diff_paths):
    record = copy.deepcopy(EXAMPLE)
    record["phase"] = "BLOCKED_PREMATURE_MUTATION"
    record["mutation_posture"] = "NO_FURTHER_MUTATION"
    capture = "+changed\n"
    incident = {
        "detected_at": "2026-08-22T12:02:00Z",
        "changed_paths": changed_paths,
        "mutation_source": "formatter",
        "worktree_status": "".join(
            f"{entry['xy']}{entry['path']}\n" for entry in status_records
        ),
        "worktree_status_record": status_records,
        "status_capture_digest": "sha256:" + "0" * 64,
        "diff_evidence": [
            {
                "path": path,
                "capture": capture,
                "capture_sha256": terminal_assignment.content_digest(capture),
            }
            for path in diff_paths
        ],
        "preserved_in_place": True,
    }
    incident["status_capture_digest"] = terminal_assignment.canonical_digest(
        terminal_assignment.status_capture(incident)
    )
    record["premature_mutation"] = incident
    return record


def modified(xy, path, original_path=None):
    return {"xy": xy, "path": path, "original_path": original_path}


class TerminalAssignmentTests(unittest.TestCase):
    def assert_semantically_invalid(self, record):
        with self.assertRaises(terminal_assignment.AssignmentValidationError):
            terminal_assignment.validate_semantics(record)

    def assert_schema_invalid(self, record):
        with self.assertRaises(ValidationError):
            VALIDATOR.validate(record)

    # ---- baseline validity ----

    def test_report_example_is_schema_and_semantically_valid(self):
        VALIDATOR.validate(EXAMPLE)
        terminal_assignment.validate_semantics(EXAMPLE)

    def test_authorized_record_is_valid(self):
        record = authorized_record()
        VALIDATOR.validate(record)
        terminal_assignment.validate_semantics(record)

    def test_verification_record_is_valid(self):
        record = verification_record()
        VALIDATOR.validate(record)
        terminal_assignment.validate_semantics(record)

    # ---- P1: report digest bound to assignment identity ----

    def test_rejects_report_binding_replayed_across_identity_fields(self):
        for field, value in [
            ("assignment_id", "THEIA-OTHER-2026-08-22"),
            ("repository", "mirrornode/other-repo"),
            ("branch", "feature/other"),
            ("head_sha", "f" * 40),
            ("base_ref", "release"),
            ("inspection_before_write", False),
        ]:
            with self.subTest(field=field):
                record = authorized_record()
                self.assertNotEqual(record[field], value)
                record[field] = value
                self.assert_semantically_invalid(record)

    def test_rejects_report_binding_replayed_after_report_edit(self):
        record = authorized_record()
        record["inspection_report"]["findings"].append("undeclared addition")
        self.assert_semantically_invalid(record)

    def test_rejects_authorization_not_bound_to_report_binding(self):
        record = authorized_record()
        record["authorization"]["report_binding_digest"] = "sha256:" + "1" * 64
        self.assert_semantically_invalid(record)

    def test_rejects_unbound_report_digest_on_authorization_event(self):
        record = authorized_record()
        record["phase_transition"]["events"][1]["report_binding_digest"] = "sha256:" + "0" * 64
        self.assert_semantically_invalid(record)

    def test_rejects_unbound_authorization_reference(self):
        record = authorized_record()
        record["phase_transition"]["events"][1]["authorization_reference"] = "AUTH-OTHER"
        self.assert_semantically_invalid(record)

    def test_rejects_scope_changed_after_authorization(self):
        record = authorized_record()
        record["authorized_files"].append(
            {"path": "src/undeclared.ts", "operation": "MODIFY", "destination_path": None}
        )
        self.assert_semantically_invalid(record)

    def test_rejects_authorization_not_subsequent_to_report(self):
        record = authorized_record()
        record["authorization"]["authorized_at"] = "2026-08-22T12:00:00Z"
        record["phase_transition"]["events"][1]["recorded_at"] = "2026-08-22T12:00:00Z"
        self.assert_semantically_invalid(record)

    # ---- P2: file operation classes ----

    def test_modify_authorization_does_not_validate_other_operation_classes(self):
        baseline = authorized_record()
        for operation in ["DELETE", "MOVE", "RENAME", "CREATE", "RESTORE"]:
            with self.subTest(operation=operation):
                record = copy.deepcopy(baseline)
                entry = record["authorized_files"][0]
                entry["operation"] = operation
                entry["destination_path"] = (
                    "src/app/theia/moved.tsx" if operation in {"MOVE", "RENAME"} else None
                )
                self.assert_semantically_invalid(record)

    def test_rejects_bare_path_file_scope_entries(self):
        record = authorized_record()
        record["authorized_files"] = ["src/app/theia/page.tsx"]
        self.assert_schema_invalid(record)

    def test_rejects_conflicting_operation_classes_for_one_path(self):
        record = authorized_record(
            authorized_files=[
                {"path": "src/a.ts", "operation": "MODIFY", "destination_path": None},
                {"path": "src/a.ts", "operation": "DELETE", "destination_path": None},
            ]
        )
        self.assert_semantically_invalid(record)

    def test_rejects_move_without_destination(self):
        record = authorized_record()
        record["authorized_files"][0]["operation"] = "MOVE"
        self.assert_schema_invalid(record)

    def test_rejects_destination_on_non_move_operation(self):
        record = authorized_record()
        record["authorized_files"][0]["destination_path"] = "src/elsewhere.ts"
        self.assert_schema_invalid(record)

    def test_rejects_unknown_operation_class(self):
        record = authorized_record()
        record["authorized_files"][0]["operation"] = "CHMOD"
        self.assert_schema_invalid(record)

    def test_move_scope_is_valid_with_destination(self):
        record = authorized_record(
            authorized_files=[
                {
                    "path": "src/app/theia/page.tsx",
                    "operation": "MOVE",
                    "destination_path": "src/app/theia/index.tsx",
                }
            ]
        )
        VALIDATOR.validate(record)
        terminal_assignment.validate_semantics(record)

    # ---- P2: incident status cross-check ----

    def test_incident_with_matching_structured_status_is_valid(self):
        record = incident_record(
            [modified(" M", "src/a.ts")], ["src/a.ts"], ["src/a.ts"]
        )
        VALIDATOR.validate(record)
        terminal_assignment.validate_semantics(record)

    def test_rejects_status_naming_unrelated_path(self):
        record = incident_record(
            [modified(" M", "src/other.ts")], ["src/a.ts"], ["src/a.ts"]
        )
        self.assert_semantically_invalid(record)

    def test_rejects_status_omitting_a_changed_path(self):
        record = incident_record(
            [modified(" M", "src/a.ts")], ["src/a.ts", "src/b.ts"], ["src/a.ts", "src/b.ts"]
        )
        self.assert_semantically_invalid(record)

    def test_rejects_status_with_extra_path(self):
        record = incident_record(
            [modified(" M", "src/a.ts"), modified(" M", "src/b.ts")],
            ["src/a.ts"],
            ["src/a.ts"],
        )
        self.assert_semantically_invalid(record)

    def test_rejects_duplicate_status_path(self):
        record = incident_record(
            [modified(" M", "src/a.ts"), modified("M ", "src/a.ts")],
            ["src/a.ts"],
            ["src/a.ts"],
        )
        self.assert_semantically_invalid(record)

    def test_rename_status_requires_both_identities(self):
        valid = incident_record(
            [modified("R ", "src/new.ts", "src/old.ts")],
            ["src/new.ts", "src/old.ts"],
            ["src/new.ts", "src/old.ts"],
        )
        VALIDATOR.validate(valid)
        terminal_assignment.validate_semantics(valid)

        destination_only = incident_record(
            [modified("R ", "src/new.ts", "src/old.ts")],
            ["src/new.ts"],
            ["src/new.ts"],
        )
        self.assert_semantically_invalid(destination_only)

    def test_rejects_rename_status_without_original_path(self):
        record = incident_record(
            [modified("R ", "src/new.ts")], ["src/new.ts"], ["src/new.ts"]
        )
        self.assert_schema_invalid(record)

    def test_rejects_original_path_on_non_rename_status(self):
        record = incident_record(
            [modified(" M", "src/a.ts", "src/old.ts")], ["src/a.ts"], ["src/a.ts"]
        )
        self.assert_schema_invalid(record)

    def test_rejects_tampered_status_capture_digest(self):
        record = incident_record(
            [modified(" M", "src/a.ts")], ["src/a.ts"], ["src/a.ts"]
        )
        record["premature_mutation"]["worktree_status_record"] = [
            modified(" M", "src/a.ts"),
            modified(" M", "src/b.ts"),
        ]
        self.assert_semantically_invalid(record)

    def test_rejects_invalid_diff_digest(self):
        record = incident_record(
            [modified(" M", "src/a.ts")], ["src/a.ts"], ["src/a.ts"]
        )
        record["premature_mutation"]["diff_evidence"][0]["capture_sha256"] = "sha256:" + "0" * 64
        self.assert_semantically_invalid(record)

    def test_rejects_duplicate_diff_evidence_path(self):
        record = incident_record(
            [modified(" M", "src/a.ts")], ["src/a.ts"], ["src/a.ts"]
        )
        record["premature_mutation"]["diff_evidence"].append(
            copy.deepcopy(record["premature_mutation"]["diff_evidence"][0])
        )
        self.assert_semantically_invalid(record)

    def test_premature_mutation_forces_blocked_state(self):
        record = authorized_record()
        record["premature_mutation"] = incident_record(
            [modified(" M", "src/a.ts")], ["src/a.ts"], ["src/a.ts"]
        )["premature_mutation"]
        self.assert_semantically_invalid(record)

    # ---- authorization validity, revocation, supersession ----

    def test_rejects_revoked_authorization(self):
        record = authorized_record()
        record["authorization"]["status"] = "REVOKED"
        rebind(record)
        self.assert_semantically_invalid(record)

    def test_rejects_superseded_authorization(self):
        record = authorized_record()
        record["authorization"]["status"] = "SUPERSEDED"
        record["authorization"]["superseded_by"] = "AUTH-002"
        rebind(record)
        self.assert_semantically_invalid(record)

    def test_rejects_expired_authorization_at_verification(self):
        record = verification_record()
        record["authorization"]["valid_until"] = "2026-08-22T12:10:00Z"
        rebind(record)
        self.assert_semantically_invalid(record)

    def test_rejects_validity_window_ending_before_authorization(self):
        record = authorized_record()
        record["authorization"]["valid_until"] = "2026-08-22T12:00:00Z"
        rebind(record)
        self.assert_semantically_invalid(record)

    def test_rejects_active_authorization_naming_successor(self):
        record = authorized_record()
        record["authorization"]["superseded_by"] = "AUTH-002"
        rebind(record)
        self.assert_schema_invalid(record)

    # ---- verification is not implementation ----

    def test_rejects_verification_writing_implementation_source(self):
        record = verification_record()
        record["verification_scope"]["artifact_paths"] = ["src/app/theia/page.tsx"]
        self.assert_semantically_invalid(record)

    def test_rejects_verification_running_undeclared_check(self):
        record = verification_record()
        record["verification_scope"]["declared_checks"] = ["npm run deploy"]
        self.assert_semantically_invalid(record)

    def test_rejects_verification_with_scoped_write_posture(self):
        record = verification_record()
        record["mutation_posture"] = "SCOPED_WRITE"
        self.assert_schema_invalid(record)

    def test_rejects_verification_without_declared_scope(self):
        record = verification_record()
        record["verification_scope"] = None
        self.assert_schema_invalid(record)

    def test_rejects_verification_predating_authorization(self):
        record = verification_record()
        record["verification_scope"]["verified_at"] = "2026-08-22T12:02:00Z"
        self.assert_semantically_invalid(record)

    # ---- handoff report ----

    def test_handoff_requires_completion_report(self):
        record = copy.deepcopy(EXAMPLE)
        record["phase"] = "HANDOFF_PENDING_DISPOSITION"
        record["mutation_posture"] = "NO_FURTHER_MUTATION"
        self.assert_schema_invalid(record)

    def test_valid_handoff_report_is_accepted(self):
        record = copy.deepcopy(EXAMPLE)
        record["phase"] = "HANDOFF_PENDING_DISPOSITION"
        record["mutation_posture"] = "NO_FURTHER_MUTATION"
        record["handoff_report"] = {
            "reported_at": "2026-08-22T12:45:00Z",
            "final_head_sha": "0123456789abcdef0123456789abcdef01234567",
            "worktree_state": "UNCOMMITTED_CHANGES_PRESERVED",
            "changed_paths": [
                {
                    "path": "src/app/theia/page.tsx",
                    "operation": "MODIFY",
                    "destination_path": None,
                }
            ],
            "checks_run": [{"command": "npm test -- theia", "result": "PASS"}],
            "unresolved_findings": [],
            "external_mutations_performed": [],
            "next_disposition_required": "Operator disposition on commit and push.",
        }
        VALIDATOR.validate(record)
        terminal_assignment.validate_semantics(record)

    def test_rejects_handoff_claiming_clean_worktree_with_changes(self):
        record = copy.deepcopy(EXAMPLE)
        record["phase"] = "HANDOFF_PENDING_DISPOSITION"
        record["mutation_posture"] = "NO_FURTHER_MUTATION"
        record["handoff_report"] = {
            "reported_at": "2026-08-22T12:45:00Z",
            "final_head_sha": "0123456789abcdef0123456789abcdef01234567",
            "worktree_state": "CLEAN",
            "changed_paths": [
                {"path": "src/a.ts", "operation": "MODIFY", "destination_path": None}
            ],
            "checks_run": [{"command": "npm test -- theia", "result": "PASS"}],
            "unresolved_findings": [],
            "external_mutations_performed": [],
            "next_disposition_required": "Operator disposition.",
        }
        self.assert_semantically_invalid(record)

    # ---- bootstrap provenance ----

    def test_bootstrap_provenance_is_required(self):
        record = copy.deepcopy(EXAMPLE)
        del record["bootstrap_provenance"]
        self.assert_schema_invalid(record)

    def test_rejects_clean_worktree_claim_with_recorded_changes(self):
        record = copy.deepcopy(EXAMPLE)
        record["bootstrap_provenance"]["preexisting_changes"] = [modified(" M", "src/a.ts")]
        self.assert_semantically_invalid(record)

    def test_rejects_unclean_worktree_claim_without_recorded_changes(self):
        record = copy.deepcopy(EXAMPLE)
        record["bootstrap_provenance"]["worktree_clean"] = False
        self.assert_semantically_invalid(record)

    def test_rejects_bootstrap_without_instruction_files(self):
        record = copy.deepcopy(EXAMPLE)
        record["bootstrap_provenance"]["instruction_files"] = []
        self.assert_schema_invalid(record)

    # ---- read-only phases stay read-only ----

    def test_read_only_phase_rejects_any_authorized_scope(self):
        for field, value in [
            ("authorized_files", [{"path": "src/a.ts", "operation": "MODIFY", "destination_path": None}]),
            ("authorized_commands", ["npm test"]),
            ("external_effects", ["network write"]),
        ]:
            with self.subTest(field=field):
                record = copy.deepcopy(EXAMPLE)
                record[field] = value
                self.assert_schema_invalid(record)


if __name__ == "__main__":
    unittest.main()
