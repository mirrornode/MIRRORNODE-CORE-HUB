#!/usr/bin/env python3
"""
Canon Gate - Pre-Audit Contract Enforcement
MIRRORNODE-CORE-HUB

Runs on every PR targeting main. Reads SYSTEM_CONTRACT.md, REPO_MAP.md,
and AGENTS_TODO.md as ground truth, then checks the incoming diff for
contract violations before any merge is allowed.

Exit 0 = contract checks passed.
Exit 1 = violation or validation failure found.

Expand PHANTOM_ROUTES and AUTHORITY_CONFLICTS as contracts evolve.
"""

import os
import re
import subprocess
import sys

CONTRACT_FILE = "SYSTEM_CONTRACT.md"
REPO_MAP_FILE = "REPO_MAP.md"
AGENTS_FILE = "AGENTS_TODO.md"

PHANTOM_ROUTES = [
    "/system/execute",
    "/system/replay",
    "/execute-task",
]

AUTHORITY_CONFLICTS = [
    r"osiris.*execution.*(engine|authority|core)",
    r"execution.*(engine|authority|core).*osiris",
    r"triaden?gine",
]

CANONICAL_PORTS = {"7700", "7701", "7702", "7703", "7704", "7705", "7706"}


def get_diff() -> str:
    base = os.environ.get("BASE_SHA", "HEAD~1")
    head = os.environ.get("HEAD_SHA", "HEAD")
    try:
        result = subprocess.run(
            ["git", "diff", base, head, "--unified=0"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as exc:
        print(f"[Canon Gate] ERROR: Could not get diff: {exc}")
        sys.exit(1)


def load_contract() -> str:
    try:
        with open(CONTRACT_FILE, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[Canon Gate] ERROR: {CONTRACT_FILE} not found. Cannot validate.")
        sys.exit(1)


def _repo_map_was_present() -> bool:
    base = os.environ.get("BASE_SHA", "HEAD~1")
    try:
        result = subprocess.run(
            ["git", "show", f"{base}:{REPO_MAP_FILE}"],
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except OSError:
        return False


def check_governance_files_present() -> list:
    violations = []

    for filename in [CONTRACT_FILE, AGENTS_FILE]:
        if not os.path.exists(filename):
            violations.append(
                f"CONTRACT DELETION: '{filename}' is missing. "
                "Governance files are protected and cannot be removed."
            )

    if _repo_map_was_present() and not os.path.exists(REPO_MAP_FILE):
        violations.append(
            f"CONTRACT DELETION: '{REPO_MAP_FILE}' is missing. "
            "Governance files are protected and cannot be removed."
        )

    return violations


def _added_diff_lines(diff: str):
    """Yield added source lines by parsing unified-diff hunk structure."""
    in_hunk = False

    for line in diff.splitlines():
        if line.startswith("diff --git "):
            in_hunk = False
            continue
        if line.startswith("@@"):
            in_hunk = True
            continue
        if not in_hunk:
            continue
        if line.startswith("+"):
            yield line


def _route_occurrence_is_negated(line: str, start: int, end: int) -> bool:
    """Return True when this exact route occurrence is explicitly documentary.

    The match is occurrence-local: another negated occurrence elsewhere on the
    same line cannot exempt an active use of the same route.
    """
    prefix = line[:start]
    suffix = line[end:]

    before_route = re.compile(
        r"(?:never\s+reference|do\s+not\s+(?:reference|use|call|expose)|"
        r"don't\s+(?:reference|use|call|expose)|"
        r"prohibited\s+route|forbidden\s+route|phantom\s+route)"
        r"\s+(?:the\s+)?[\s`'\"(:=\-]*$",
        re.IGNORECASE,
    )
    after_route = re.compile(
        r"^[\s`'\")\]:=\-]*(?:route|endpoint)?\s*(?:"
        r"is\s+(?:not\s+a\s+real\s+route|non-real|prohibited|forbidden|phantom|non-existent)|"
        r"must\s+not\s+be\s+(?:used|referenced|called|exposed)|"
        r"should\s+not\s+be\s+(?:used|referenced|called|exposed))\b",
        re.IGNORECASE,
    )

    return bool(before_route.search(prefix) or after_route.search(suffix))


def check_phantom_routes(diff: str) -> list:
    violations = []

    for line in _added_diff_lines(diff):
        for route in PHANTOM_ROUTES:
            occurrences = list(re.finditer(re.escape(route), line, re.IGNORECASE))
            if not occurrences:
                continue

            if any(
                not _route_occurrence_is_negated(line, match.start(), match.end())
                for match in occurrences
            ):
                violations.append(
                    f"PHANTOM ROUTE: '{route}' is declared non-real in "
                    f"{CONTRACT_FILE} but appears as an active or unqualified "
                    "addition in this PR."
                )

    return violations


def check_authority_conflicts(diff: str) -> list:
    violations = []
    for pattern_str in AUTHORITY_CONFLICTS:
        pattern = re.compile(
            r"^\+.*" + pattern_str,
            re.MULTILINE | re.IGNORECASE,
        )
        if pattern.search(diff):
            violations.append(
                f"AUTHORITY CONFLICT: Pattern '{pattern_str}' contradicts "
                f"LUCIAN as the declared execution authority in {CONTRACT_FILE}."
            )
    return violations


def check_unregistered_ports(diff: str) -> list:
    violations = []
    pattern = re.compile(
        r"^\+.*port[:\s]+([0-9]{4,5})",
        re.MULTILINE | re.IGNORECASE,
    )
    for match in pattern.finditer(diff):
        port = match.group(1)
        if port not in CANONICAL_PORTS:
            violations.append(
                f"UNREGISTERED PORT: Port {port} is not in the canonical "
                "agent registry (7700-7706). Update AGENTS_TODO.md first."
            )
    return violations


def main():
    print("[Canon Gate] " + "=" * 50)
    print("[Canon Gate] MIRRORNODE Contract Compliance Check")
    print("[Canon Gate] " + "=" * 50)

    print("[Canon Gate] Loading contract...")
    load_contract()

    print("[Canon Gate] Fetching PR diff...")
    diff = get_diff()

    if not diff:
        print("[Canon Gate] No diff detected. Contract check passed.")
        sys.exit(0)

    print("[Canon Gate] Running checks...\n")

    violations = (
        check_governance_files_present()
        + check_phantom_routes(diff)
        + check_authority_conflicts(diff)
        + check_unregistered_ports(diff)
    )

    if violations:
        print("[Canon Gate] RESULT: VIOLATIONS FOUND - merge blocked\n")
        for index, violation in enumerate(violations, 1):
            print(f"  {index}. {violation}")
        print(
            "\n[Canon Gate] Resolve all violations against "
            f"{CONTRACT_FILE} before this PR can merge."
        )
        print("[Canon Gate] " + "=" * 50)
        sys.exit(1)

    print("[Canon Gate] RESULT: All configured contract checks passed.")
    print(
        "[Canon Gate] Compliance verification only; merge remains subject "
        "to repository policy and Operator disposition."
    )
    print("[Canon Gate] " + "=" * 50)
    sys.exit(0)


if __name__ == "__main__":
    main()
