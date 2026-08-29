"""CI coverage for scripts/path_denotation.py.

Regression tests for probe families 1-6 of canon/verification/adversarial-probe-corpus-v0.1.md.
Every path in `ESCAPED_AT_ORIGIN` was accepted at PR #53 head
05d83494527a7318139d5255dd75fb4ff740600c and must stay refused forever.

Run: python3 -m unittest tests.test_path_denotation
"""

import os
import sys
import unittest

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts")
)

from path_denotation import (
    PathDenotationError,
    check_repo_path,
    check_unique_identities,
    normalize_repo_path,
)

# Accepted at the origin head. Family 1-5.
ESCAPED_AT_ORIGIN = [
    "../../other-repo/secret.ts",
    "a/../../../etc/passwd",
    "src/../../escape.ts",
    ".git/config",
    ".github/workflows/audit.yml",
    "src/x\ny.ts",
    "src/dir/",
]

MUST_REFUSE = ESCAPED_AT_ORIGIN + [
    "/etc/passwd",
    "~/secrets",
    "C:/Windows/System32",
    "src//a.ts",
    "./src/a.ts",
    "src/./a.ts",
    "src/b/../a.ts",
    "src/ a.ts/x",
    "src/a\x00.ts",
    "",
    "x" * 2000,
    ".git/hooks/pre-commit",
    ".github/workflows/release.yml",
    "src\\a.ts",
]

MUST_ACCEPT = [
    "src/a.ts",
    "docs/orchestration/terminal-agent-assignment.schema.json",
    "a/b/c/d/e.txt",
    "file-with.many.dots.ts",
    "scripts/path_denotation.py",
]


class TestRefusal(unittest.TestCase):
    def test_origin_escapes_stay_refused(self):
        """Family 1-5: every path that escaped at 05d8349."""
        for raw in ESCAPED_AT_ORIGIN:
            with self.subTest(path=raw), self.assertRaises(PathDenotationError):
                check_repo_path(raw)

    def test_all_refused(self):
        for raw in MUST_REFUSE:
            with self.subTest(path=raw), self.assertRaises(PathDenotationError):
                check_repo_path(raw)

    def test_non_string_refused(self):
        for raw in (None, 42, ["src/a.ts"], {"path": "src/a.ts"}):
            with self.subTest(value=raw), self.assertRaises(PathDenotationError):
                check_repo_path(raw)


class TestAcceptance(unittest.TestCase):
    def test_legitimate_paths_accepted(self):
        """A validator that refuses everything is broken, not secure."""
        for raw in MUST_ACCEPT:
            with self.subTest(path=raw):
                self.assertEqual(check_repo_path(raw), raw)

    def test_normalize_is_identity_for_canonical(self):
        for raw in MUST_ACCEPT:
            with self.subTest(path=raw):
                self.assertEqual(normalize_repo_path(raw), raw)


class TestProtectedSurfaces(unittest.TestCase):
    """Family 3-5: the gate must not be writable by what it gates."""

    def test_protected_refused_by_default(self):
        for raw in (".git/config", ".github/workflows/audit.yml"):
            with self.subTest(path=raw), self.assertRaises(PathDenotationError):
                check_repo_path(raw)

    def test_protected_requires_explicit_optin(self):
        self.assertEqual(
            check_repo_path(".github/workflows/audit.yml", allow_protected=True),
            ".github/workflows/audit.yml",
        )

    def test_optin_does_not_defeat_traversal(self):
        """allow_protected relaxes one rule only; it is not a bypass."""
        for raw in ("../../escape.ts", "/etc/passwd", "src/dir/"):
            with self.subTest(path=raw), self.assertRaises(PathDenotationError):
                check_repo_path(raw, allow_protected=True)

    def test_protected_lookalike_is_not_protected(self):
        """.gitignore and .githubby are ordinary files, not protected surfaces."""
        for raw in (".gitignore", ".githubby/notes.md"):
            with self.subTest(path=raw):
                self.assertEqual(check_repo_path(raw), raw)


class TestPositiveContainment(unittest.TestCase):
    """Family 6: the founding regression. Containment, never mere exclusion."""

    def test_inside_root_accepted(self):
        for raw in ("build/out.log", "build/nested/deep/out.log", "build"):
            with self.subTest(path=raw):
                self.assertEqual(check_repo_path(raw, root="build"), raw)

    def test_outside_root_refused(self):
        for raw in ("src/a.ts", "../outside.log", "out.log"):
            with self.subTest(path=raw), self.assertRaises(PathDenotationError):
                check_repo_path(raw, root="build")

    def test_prefix_without_segment_boundary_refused(self):
        """buildother/ is not inside build/. Naive prefix matching would allow it."""
        for raw in ("buildother/x.log", "build-other/x.log", "builds/x.log"):
            with self.subTest(path=raw), self.assertRaises(PathDenotationError):
                check_repo_path(raw, root="build")

    def test_root_cannot_be_escaped_by_traversal(self):
        with self.assertRaises(PathDenotationError):
            check_repo_path("build/../src/a.ts", root="build")

    def test_nested_root(self):
        self.assertEqual(
            check_repo_path("var/artifacts/run/report.json", root="var/artifacts"),
            "var/artifacts/run/report.json",
        )
        with self.assertRaises(PathDenotationError):
            check_repo_path("var/other/report.json", root="var/artifacts")


class TestUniqueIdentities(unittest.TestCase):
    """Family 2, 7, 8: uniqueness on normalized identity, destinations included."""

    def test_distinct_accepted(self):
        self.assertEqual(
            check_unique_identities(["src/a.ts", "src/b.ts"]), ["src/a.ts", "src/b.ts"]
        )

    def test_exact_duplicate_refused(self):
        with self.assertRaises(PathDenotationError):
            check_unique_identities(["src/a.ts", "src/a.ts"])

    def test_aliased_pair_refused(self):
        for pair in (
            ["src/a.ts", "./src/a.ts"],
            ["src/a.ts", "src/b/../a.ts"],
            ["src/a.ts", "src//a.ts"],
        ):
            with self.subTest(pair=pair), self.assertRaises(PathDenotationError):
                check_unique_identities(pair)

    def test_move_destination_collision_refused(self):
        """Two MOVEs onto one destination, passed as the full target list."""
        with self.assertRaises(PathDenotationError):
            check_unique_identities(["src/a.ts", "src/z.ts", "src/c.ts", "src/z.ts"])

    def test_empty_list_accepted(self):
        self.assertEqual(check_unique_identities([]), [])


class TestErrorQuality(unittest.TestCase):
    def test_refusals_are_specific_type(self):
        """A bare Exception catch lets probe typos masquerade as security refusals."""
        try:
            check_repo_path("../escape.ts")
        except PathDenotationError as exc:
            self.assertTrue(str(exc), "refusal must carry a reason")
        else:
            self.fail("expected refusal")


if __name__ == "__main__":
    unittest.main(verbosity=2)
