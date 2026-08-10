import importlib.util
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "canon_gate.py"
SPEC = importlib.util.spec_from_file_location("canon_gate", MODULE_PATH)
canon_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(canon_gate)


def raw_diff(*added_lines: str) -> str:
    body = "\n".join(f"+{line}" for line in added_lines)
    return (
        "diff --git a/example.txt b/example.txt\n"
        "index 1111111..2222222 100644\n"
        "--- a/example.txt\n"
        "+++ b/example.txt\n"
        "@@ -0,0 +1,1 @@\n"
        f"{body}\n"
    )


class CanonGatePhantomRouteTests(unittest.TestCase):
    def test_negation_after_route_is_not_flagged(self):
        diff = raw_diff("- /system/execute is not a real route")
        self.assertEqual(canon_gate.check_phantom_routes(diff), [])

    def test_negation_before_route_is_not_flagged(self):
        diff = raw_diff("Never reference /system/replay")
        self.assertEqual(canon_gate.check_phantom_routes(diff), [])

    def test_article_before_route_is_not_flagged(self):
        diff = raw_diff("Do not expose the /system/execute route")
        self.assertEqual(canon_gate.check_phantom_routes(diff), [])

    def test_route_noun_after_route_is_not_flagged(self):
        diff = raw_diff("The /system/replay route is prohibited")
        self.assertEqual(canon_gate.check_phantom_routes(diff), [])

    def test_unrelated_negation_does_not_exempt_route(self):
        route = "/system/" + "execute"
        diff = raw_diff(f'app.post("{route}", handler)  # do not cache')
        violations = canon_gate.check_phantom_routes(diff)
        self.assertEqual(len(violations), 1)
        self.assertIn(route, violations[0])

    def test_leading_negation_for_other_object_does_not_exempt_route(self):
        route = "/system/" + "execute"
        diff = raw_diff(f'Do not expose metrics, but app.post("{route}", handler)')
        violations = canon_gate.check_phantom_routes(diff)
        self.assertEqual(len(violations), 1)
        self.assertIn(route, violations[0])

    def test_documentary_first_occurrence_does_not_exempt_active_second_occurrence(self):
        route = "/system/" + "execute"
        diff = raw_diff(
            f'/* {route} is prohibited */ app.post("{route}", handler)'
        )
        violations = canon_gate.check_phantom_routes(diff)
        self.assertEqual(len(violations), 1)
        self.assertIn(route, violations[0])

    def test_two_documentary_occurrences_are_allowed(self):
        route = "/system/" + "execute"
        diff = raw_diff(
            f'{route} is prohibited; do not reference {route}'
        )
        self.assertEqual(canon_gate.check_phantom_routes(diff), [])

    def test_unrelated_word_does_not_exempt_route(self):
        route = "/system/" + "replay"
        diff = raw_diff(f'app.post("{route}", donut_handler)')
        violations = canon_gate.check_phantom_routes(diff)
        self.assertEqual(len(violations), 1)
        self.assertIn(route, violations[0])

    def test_bare_phantom_route_is_flagged(self):
        route = "/execute" + "-task"
        diff = raw_diff(f"POST {route}")
        violations = canon_gate.check_phantom_routes(diff)
        self.assertEqual(len(violations), 1)
        self.assertIn(route, violations[0])

    def test_file_header_is_not_treated_as_added_source(self):
        diff = (
            "diff --git a/docs/routes.md b/docs/routes.md\n"
            "--- a/docs/routes.md\n"
            "+++ b/docs/routes.md\n"
        )
        self.assertEqual(list(canon_gate._added_diff_lines(diff)), [])

    def test_added_source_starting_with_two_pluses_is_scanned(self):
        route = "/system/" + "execute"
        diff = raw_diff(f'++ counter; // {route}')
        violations = canon_gate.check_phantom_routes(diff)
        self.assertEqual(len(violations), 1)
        self.assertIn(route, violations[0])

    def test_new_file_header_then_hunk_is_parsed(self):
        route = "/system/" + "replay"
        diff = (
            "diff --git a/new.js b/new.js\n"
            "new file mode 100644\n"
            "--- /dev/null\n"
            "+++ b/new.js\n"
            "@@ -0,0 +1 @@\n"
            f'+fetch("{route}")\n'
        )
        violations = canon_gate.check_phantom_routes(diff)
        self.assertEqual(len(violations), 1)


class CanonGateRepoMapTests(unittest.TestCase):
    @patch.object(canon_gate.subprocess, "run")
    def test_repo_map_base_presence_uses_git_show(self, run):
        run.return_value = SimpleNamespace(returncode=0)
        self.assertTrue(canon_gate._repo_map_was_present())
        command = run.call_args.args[0]
        self.assertEqual(command[:2], ["git", "show"])
        self.assertTrue(command[2].endswith(":REPO_MAP.md"))

    @patch.object(canon_gate.subprocess, "run")
    def test_repo_map_absent_on_base_is_false(self, run):
        run.return_value = SimpleNamespace(returncode=128)
        self.assertFalse(canon_gate._repo_map_was_present())


if __name__ == "__main__":
    unittest.main()
