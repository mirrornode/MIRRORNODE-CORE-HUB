"""Positive path containment for MIRRORNODE authority records.

Earned from PR #53 P1-B: a path can be syntactically present, digest-bound, exactly equal
across every evidence object, and correctly classified by operation, while denoting something
outside the repository. Binding a string proves nothing about the resource it names.

This module answers the *denotational* question -- does this string identify the resource we
think it identifies -- using positive containment rather than a blocklist. Import it from a
validator, or run it directly for its self-test.

    from path_denotation import check_repo_path, normalize_repo_path, PathDenotationError

    check_repo_path("src/a.ts")                      # -> "src/a.ts"
    check_repo_path("src/../../escape.ts")           # -> raises PathDenotationError
    check_repo_path("build/out.log", root="build")   # -> "build/out.log"
    check_repo_path("src/a.ts", root="build")        # -> raises (outside declared root)

Design rules, in order of importance:
  1. Containment is positive. A path is valid only if it normalizes to a form provably inside
     the repository, and inside a declared root when one is given.
  2. Normalized identity is canonical. Comparisons and uniqueness checks must run on the
     normalized form so one resource cannot present as two identities.
  3. Gate surfaces are never writable by what they gate. `.git` and `.github` are refused by
     default and require explicit, deliberate opt-in.
"""

from __future__ import annotations

import posixpath
import unicodedata

__all__ = [
    "PROTECTED_PREFIXES",
    "PathDenotationError",
    "check_repo_path",
    "check_unique_identities",
    "normalize_repo_path",
]

# Surfaces that decide whether the system is safe. Writable by nothing that they judge.
PROTECTED_PREFIXES = (".git", ".github")

_MAX_PATH_BYTES = 1024


class PathDenotationError(ValueError):
    """A path does not provably denote a bounded resource inside the repository."""


def normalize_repo_path(raw: str) -> str:
    """Return the canonical repository-relative identity of `raw`.

    Raises PathDenotationError if no such identity exists. The returned value is what must be
    used for every comparison, digest, and uniqueness check -- never the caller's spelling.
    """
    if not isinstance(raw, str):
        raise PathDenotationError(f"path must be a string, got {type(raw).__name__}")
    if raw == "":
        raise PathDenotationError("path is empty")
    if len(raw.encode("utf-8")) > _MAX_PATH_BYTES:
        raise PathDenotationError("path exceeds maximum length")

    # Control characters, including newline and NUL, break every line- and NUL-delimited
    # evidence format we parse (git status --porcelain, diff headers, digest inputs).
    for ch in raw:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise PathDenotationError(f"path contains control character {ord(ch):#04x}")

    # Backslash is a separator on some hosts; permitting it creates two spellings of one path.
    if "\\" in raw:
        raise PathDenotationError("path contains a backslash")

    # Absolute and home-relative forms escape repository-relative interpretation entirely.
    if raw.startswith("/"):
        raise PathDenotationError("path is absolute")
    if raw.startswith("~"):
        raise PathDenotationError("path is home-relative")
    # Windows drive or UNC forms.
    if len(raw) >= 2 and raw[1] == ":":
        raise PathDenotationError("path carries a drive letter")

    # A trailing separator denotes a directory, not a file that can be operated on.
    if raw.endswith("/"):
        raise PathDenotationError("path has a trailing separator and denotes no file")

    # Unicode normalization: NFC/NFD spellings of one filename must not present as two
    # identities on normalizing filesystems.
    normalized = unicodedata.normalize("NFC", raw)

    segments = normalized.split("/")
    if any(seg == "" for seg in segments):
        raise PathDenotationError("path contains an empty segment")
    if any(seg == "." for seg in segments):
        raise PathDenotationError("path contains a '.' segment")
    if any(seg == ".." for seg in segments):
        # Refused before collapsing, not after. `a/../b` is inside the repo but is a second
        # spelling of `b`, and accepting it means identity depends on collapse order.
        raise PathDenotationError("path contains a '..' segment")
    if any(seg in {" ", "\t"} or seg != seg.strip() for seg in segments):
        raise PathDenotationError("path segment has leading or trailing whitespace")

    # posixpath.normpath is a belt-and-braces check, not the primary defence: if normalizing
    # changes anything, the input was not already canonical.
    canonical = posixpath.normpath(normalized)
    if canonical != normalized:
        raise PathDenotationError(
            f"path is not canonical ({normalized!r} normalizes to {canonical!r})"
        )
    if canonical.startswith("..") or posixpath.isabs(canonical):
        raise PathDenotationError("path escapes the repository root")

    return canonical


def _is_within(path: str, root: str) -> bool:
    """True if `path` is inside `root`, both already normalized. Segment-aware."""
    if root in ("", "."):
        return True
    return path == root or path.startswith(root + "/")


def check_repo_path(
    raw: str,
    *,
    root: str | None = None,
    allow_protected: bool = False,
) -> str:
    """Validate `raw` and return its canonical identity.

    root:             when given, the path must be contained *within* this declared root.
                      This is the positive-containment form. Never express an artifact
                      boundary as "disjoint from the source allowlist" -- that channels writes
                      toward whatever was not reviewed. See PR #53 P1-A.
    allow_protected:  permit `.git` / `.github` targets. Defaults False. Set True only with a
                      recorded reason; a surface that gates the system must not be writable by
                      what it gates.
    """
    canonical = normalize_repo_path(raw)

    if not allow_protected:
        head = canonical.split("/")[0]
        if head in PROTECTED_PREFIXES:
            raise PathDenotationError(
                f"path targets protected surface {head!r}; "
                "gate surfaces are not writable by what they gate"
            )

    if root is not None:
        canonical_root = normalize_repo_path(root) if root not in ("", ".") else "."
        if not _is_within(canonical, canonical_root):
            raise PathDenotationError(
                f"path {canonical!r} is not contained within declared root {canonical_root!r}"
            )

    return canonical


def check_unique_identities(paths, *, label: str = "paths") -> list[str]:
    """Validate every path and require the canonical identities to be duplicate-free.

    Uniqueness must be enforced on normalized identities. Checking raw spellings lets one
    resource appear as two entries (PR #53 probe family 2). Pass *all* write targets --
    including move and rename destinations, which are write targets too (family 7 and 8).
    """
    seen: dict[str, str] = {}
    out: list[str] = []
    for raw in paths:
        canonical = check_repo_path(raw)
        if canonical in seen:
            raise PathDenotationError(
                f"{label}: {raw!r} and {seen[canonical]!r} denote the same resource "
                f"{canonical!r}"
            )
        seen[canonical] = raw
        out.append(canonical)
    return out


def _selftest() -> int:
    refuse = [
        # PR #53 P1-B, accepted at head 05d8349:
        ("../../other-repo/secret.ts", "traversal out of repo"),
        ("a/../../../etc/passwd", "traversal to absolute-ish target"),
        ("src/../../escape.ts", "traversal after a valid segment"),
        (".git/config", "repository identity"),
        (".github/workflows/audit.yml", "the gate that judges the change"),
        ("src/x\ny.ts", "embedded newline breaks evidence parsing"),
        ("src/dir/", "trailing separator denotes no file"),
        # generic denotation families:
        ("/etc/passwd", "absolute"),
        ("~/secrets", "home-relative"),
        ("C:/Windows/System32", "drive letter"),
        ("src//a.ts", "empty segment"),
        ("./src/a.ts", "non-canonical '.' segment"),
        ("src/./a.ts", "interior '.' segment"),
        ("src/b/../a.ts", "second spelling of src/a.ts"),
        ("src/ a.ts/x", "segment whitespace"),
        ("src/a\x00.ts", "NUL byte"),
        ("", "empty"),
        ("x" * 2000, "over length"),
    ]
    accept = [
        "src/a.ts",
        "docs/orchestration/terminal-agent-assignment.schema.json",
        "a/b/c/d/e.txt",
        "file-with.many.dots.ts",
        "unicode/café.ts",
    ]

    failures = 0
    print("=== must be REFUSED ===")
    for raw, why in refuse:
        try:
            got = check_repo_path(raw)
            print(f"  [HOLE]    {raw!r:45s} accepted as {got!r}  ({why})")
            failures += 1
        except PathDenotationError:
            print(f"  [refused] {raw!r:45s} ({why})")

    print("\n=== must be ACCEPTED ===")
    for raw in accept:
        try:
            print(f"  [ok]      {raw!r:45s} -> {check_repo_path(raw)!r}")
        except PathDenotationError as exc:
            print(f"  [BROKEN]  {raw!r:45s} refused: {exc}")
            failures += 1

    print("\n=== positive containment (declared root) ===")
    cases = [
        ("build/out.log", "build", True),
        ("build/nested/out.log", "build", True),
        ("src/a.ts", "build", False),
        ("buildother/x.log", "build", False),  # prefix without segment boundary
        ("../outside.log", "build", False),
    ]
    for raw, root, should in cases:
        try:
            check_repo_path(raw, root=root)
            ok = should
            verdict = "accepted"
        except PathDenotationError:
            ok = not should
            verdict = "refused"
        tag = "ok" if ok else "HOLE"
        print(f"  [{tag:7s}] {raw!r:28s} under root {root!r:8s} {verdict}")
        if not ok:
            failures += 1

    print("\n=== normalized uniqueness ===")
    try:
        check_unique_identities(["src/a.ts", "src/b.ts"])
        print("  [ok]      distinct paths accepted")
    except PathDenotationError as exc:
        print(f"  [BROKEN]  distinct paths refused: {exc}")
        failures += 1
    # Both spellings are individually refused as non-canonical, which is the stronger
    # outcome; assert the aliasing case cannot slip through either way.
    for pair in (["src/a.ts", "./src/a.ts"], ["src/a.ts", "src/b/../a.ts"]):
        try:
            check_unique_identities(pair)
            print(f"  [HOLE]    aliased pair accepted: {pair}")
            failures += 1
        except PathDenotationError:
            print(f"  [refused] aliased pair {pair}")

    print(f"\n{'PASS' if failures == 0 else f'{failures} FAILURE(S)'}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(_selftest())
