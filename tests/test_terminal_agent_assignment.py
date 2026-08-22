import copy
import importlib.util
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


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


def authorized_record():
    record = copy.deepcopy(EXAMPLE)
    record["phase"] = "IMPLEMENTATION_AUTHORIZED"
    record["mutation_posture"] = "SCOPED_WRITE"
    record["authorized_files"] = ["src/lib/theia.ts"]
    record["authorized_commands"] = ["npm test -- theia"]
    scope_digest = terminal_assignment.canonical_digest(
        terminal_assignment.authorized_scope(record)
    )
    report_digest = terminal_assignment.canonical_digest(record["inspection_report"])
    record["authorization"] = {
        "reference": "AUTH-001",
        "authorized_at": "2026-08-22T12:05:00Z",
        "authorized_by": "Operator",
        "scope_digest": scope_digest,
    }
    record["phase_transition"] = {
        "events": [
            {
                "event": "INSPECTION_REPORT_RECORDED",
                "recorded_at": "2026-08-22T12:01:00Z",
                "inspection_report_digest": report_digest,
            },
            {
                "event": "IMPLEMENTATION_AUTHORIZED",
                "recorded_at": "2026-08-22T12:05:00Z",
                "inspection_report_digest": report_digest,
                "authorization_reference": "AUTH-001",
                "scope_digest": scope_digest,
            },
        ]
    }
    return record


class TerminalAssignmentTests(unittest.TestCase):
    def assert_semantically_invalid(self, record):
        with self.assertRaises(terminal_assignment.AssignmentValidationError):
            terminal_assignment.validate_semantics(record)

    def test_report_example_is_schema_and_semantically_valid(self):
        Draft202012Validator(SCHEMA, format_checker=FormatChecker()).validate(EXAMPLE)
        terminal_assignment.validate_semantics(EXAMPLE)

    def test_authorized_record_is_valid(self):
        record = authorized_record()
        Draft202012Validator(SCHEMA, format_checker=FormatChecker()).validate(record)
        terminal_assignment.validate_semantics(record)

    def test_rejects_unbound_authorization_reference(self):
        record = authorized_record()
        record["phase_transition"]["events"][1]["authorization_reference"] = "AUTH-OTHER"
        self.assert_semantically_invalid(record)

    def test_rejects_unbound_report_digest(self):
        record = authorized_record()
        record["phase_transition"]["events"][1]["inspection_report_digest"] = "sha256:" + "0" * 64
        self.assert_semantically_invalid(record)

    def test_rejects_scope_changed_after_authorization(self):
        record = authorized_record()
        record["authorized_files"].append("src/undeclared.ts")
        self.assert_semantically_invalid(record)

    def test_rejects_authorization_not_subsequent_to_report(self):
        record = authorized_record()
        record["authorization"]["authorized_at"] = "2026-08-22T12:00:00Z"
        record["phase_transition"]["events"][1]["recorded_at"] = "2026-08-22T12:00:00Z"
        self.assert_semantically_invalid(record)

    def test_premature_mutation_forces_blocked_state(self):
        record = authorized_record()
        record["premature_mutation"] = {
            "detected_at": "2026-08-22T12:02:00Z",
            "changed_paths": ["src/a.ts"],
            "mutation_source": "formatter",
            "worktree_status": " M src/a.ts\n",
            "worktree_status_sha256": terminal_assignment.content_digest(" M src/a.ts\n"),
            "diff_evidence": [{
                "path": "src/a.ts",
                "capture": "+changed\n",
                "capture_sha256": terminal_assignment.content_digest("+changed\n"),
            }],
            "preserved_in_place": True,
        }
        self.assert_semantically_invalid(record)

    def test_rejects_incomplete_incident_path_evidence(self):
        record = copy.deepcopy(EXAMPLE)
        record["phase"] = "BLOCKED_PREMATURE_MUTATION"
        record["mutation_posture"] = "NO_FURTHER_MUTATION"
        capture = "+changed\n"
        status = " M src/a.ts\n M src/b.ts\n"
        record["premature_mutation"] = {
            "detected_at": "2026-08-22T12:02:00Z",
            "changed_paths": ["src/a.ts", "src/b.ts"],
            "mutation_source": "formatter",
            "worktree_status": status,
            "worktree_status_sha256": terminal_assignment.content_digest(status),
            "diff_evidence": [{
                "path": "src/a.ts",
                "capture": capture,
                "capture_sha256": terminal_assignment.content_digest(capture),
            }],
            "preserved_in_place": True,
        }
        self.assert_semantically_invalid(record)


if __name__ == "__main__":
    unittest.main()
