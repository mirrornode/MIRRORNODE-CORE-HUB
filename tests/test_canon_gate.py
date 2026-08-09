import importlib.util
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "canon_gate.py"
SPEC = importlib.util.spec_from_file_location("canon_gate", MODULE_PATH)
canon_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(canon_gate)


class CanonGatePhantomRouteTests(unittest.TestCase):
    def test_negation_after_route_is_not_flagged(self):
        diff = "+ - /system/execute is not a real route\n"
        self.assertEqual(canon_gate.check_phantom_routes(diff), [])

    def test_negation_before_route_is_not_flagged(self):
        diff = "+ Never reference /system/replay from runtime code\n"
        self.assertEqual(canon_gate.check_phantom_routes(diff), [])

    def test_bare_phantom_route_is_flagged(self):
        route = "/execute" + "-task"
        diff = f"+ POST {route}\n"
        violations = canon_gate.check_phantom_routes(diff)
        self.assertEqual(len(violations), 1)
        self.assertIn(route, violations[0])

    def test_diff_metadata_is_ignored(self):
        diff = "+++ b/docs/routes.md\n"
        self.assertEqual(canon_gate.check_phantom_routes(diff), [])


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
