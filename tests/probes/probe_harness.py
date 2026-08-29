"""Should-be-refused / was-accepted probe harness.

The harness inverts the usual test polarity. A normal suite asserts that valid input is
accepted; this asserts that *invalid* input is refused, and treats acceptance as a hole. That
inversion is the whole point: PR #53 shipped 47 passing tests and still had ten open holes,
because the suite only encoded failure modes its author had already thought of.

Usage against a real system -- bind the two validation callables and go:

    from probe_harness import ProbeSuite

    suite = ProbeSuite(
        schema_validate=lambda r: MY_VALIDATOR.validate(r),
        semantic_validate=my_module.validate_semantics,
        refusal_errors=(jsonschema.ValidationError, my_module.AssignmentValidationError),
    )
    suite.refuse("traversal in authorized_files", build_record(path="../../escape.ts"),
                 family=1)
    suite.accept("baseline legitimate record", EXAMPLE)
    raise SystemExit(suite.report())

Rules the harness enforces so a run cannot flatter itself:

  * `refusal_errors` must be specific. A bare `except Exception` lets an AttributeError or a
    typo in the probe itself masquerade as a security refusal. This was a real defect caught
    mid-cycle in PR #53's own suite.
  * Every suite must contain at least one `accept` probe. A validator that refuses everything
    is broken, not secure, and an all-refuse run would otherwise report a clean sweep.
  * Probes carry a `family` number from references/probe-corpus.md so coverage is auditable
    and a skipped family is visible as absent rather than assumed.

Run this file directly for a self-demonstration: it builds a toy record validator carrying
PR #53's real defects, shows the harness catching them, then shows a hardened validator
passing the same corpus.
"""

from __future__ import annotations

import sys
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ProbeResult:
    label: str
    family: int | None
    expected: str          # "REFUSED" | "ACCEPTED"
    observed: str          # "refused" | "accepted"
    detail: str = ""

    @property
    def ok(self) -> bool:
        return self.observed.upper() == self.expected


@dataclass
class ProbeSuite:
    """Collects probes and reports holes.

    schema_validate / semantic_validate: callables taking a record, raising on rejection.
    refusal_errors: the exception types that count as a legitimate refusal. Anything else
                    propagates as a harness error rather than being scored.
    """

    schema_validate: Callable[[Any], None]
    semantic_validate: Callable[[Any], None] | None = None
    refusal_errors: tuple[type[BaseException], ...] = (ValueError,)
    results: list[ProbeResult] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def _run(self, record: Any) -> tuple[bool, str]:
        """Return (accepted, detail)."""
        for stage, fn in (("schema", self.schema_validate),
                          ("semantic", self.semantic_validate)):
            if fn is None:
                continue
            try:
                fn(record)
            except self.refusal_errors as exc:
                return False, f"{stage}: {exc}"
            except Exception as exc:  # harness fault, not a security result
                raise RuntimeError(
                    f"{stage} validation raised an unscored {type(exc).__name__}: {exc}. "
                    "Add it to refusal_errors if it is a legitimate rejection, or fix the "
                    "probe. Never let it count as a refusal."
                ) from exc
        return True, ""

    def refuse(self, label: str, record: Any, *, family: int | None = None) -> bool:
        """Assert the system refuses `record`. Acceptance is a hole."""
        try:
            accepted, detail = self._run(record)
        except RuntimeError as exc:
            self.errors.append(f"{label}: {exc}")
            return False
        self.results.append(ProbeResult(
            label, family, "REFUSED", "accepted" if accepted else "refused", detail
        ))
        return not accepted

    def accept(self, label: str, record: Any, *, family: int | None = None) -> bool:
        """Assert the system accepts `record`. Required baseline; refusal means broken."""
        try:
            accepted, detail = self._run(record)
        except RuntimeError as exc:
            self.errors.append(f"{label}: {exc}")
            return False
        self.results.append(ProbeResult(
            label, family, "ACCEPTED", "accepted" if accepted else "refused", detail
        ))
        return accepted

    def refuse_each(
        self, label_fmt: str, records: Iterable[tuple[str, Any]], *, family: int | None = None
    ) -> None:
        for name, record in records:
            self.refuse(label_fmt.format(name), record, family=family)

    def report(self, *, verbose: bool = True) -> int:
        """Print results and return a process exit code. 0 only if genuinely clean."""
        holes = [r for r in self.results if not r.ok and r.expected == "REFUSED"]
        broken = [r for r in self.results if not r.ok and r.expected == "ACCEPTED"]
        baselines = [r for r in self.results if r.expected == "ACCEPTED"]

        if verbose:
            for r in self.results:
                if r.ok:
                    tag = "ok" if r.expected == "ACCEPTED" else "refused"
                else:
                    tag = "HOLE" if r.expected == "REFUSED" else "BROKEN"
                fam = f"[f{r.family:02d}] " if r.family else "      "
                print(f"  [{tag:8s}] {fam}{r.label}")

        print()
        families = sorted({r.family for r in self.results if r.family})
        print(f"probes={len(self.results)}  families covered={families or 'none declared'}")

        if not baselines:
            print("VERDICT: INVALID RUN -- no accept probe. A validator that refuses "
                  "everything would report clean.")
            return 2
        if self.errors:
            print(f"VERDICT: INVALID RUN -- {len(self.errors)} harness error(s):")
            for e in self.errors:
                print(f"  ! {e}")
            return 2
        if broken:
            print(f"VERDICT: BROKEN -- {len(broken)} legitimate record(s) refused.")
            return 2
        if holes:
            print(f"VERDICT: {len(holes)} HOLE(S) -- accepted input that must be refused:")
            for r in holes:
                print(f"  ! {r.label}")
            print("\nDisposition: HOLD. Any live P1 forces HOLD; report, do not merge.")
            return 1
        print("VERDICT: ADVERSARIAL_PROBES_PASS for the declared families only.")
        print("This is NOT clearance. It does not imply EXACT_HEAD_REVIEWED, "
              "INDEPENDENT_EXACT_HEAD_REVIEWED, CONSTITUTIONALLY_CLEARED, or MERGE_AUTHORIZED.")
        return 0


# ---------------------------------------------------------------------------
# Self-demonstration: a toy authority record carrying PR #53's real defects.
# ---------------------------------------------------------------------------

class Refused(ValueError):
    """Toy refusal type."""


def _toy_record(**over: Any) -> dict:
    rec = {
        "phase": "IMPLEMENTATION",
        "posture": "SOURCE_WRITE",
        "authorized_files": [{"path": "src/a.ts", "operation": "MODIFY", "dest": None}],
        "artifact_paths": [],
        "external_effects": [],
    }
    rec.update(over)
    return rec


def _vulnerable_validate(rec: dict) -> None:
    """Reproduces the defects that escaped at 05d8349: paths are only shape-checked, and
    artifact scope is constrained negatively (disjoint from source) with no positive root."""
    for entry in rec["authorized_files"]:
        p = entry["path"]
        if not p or p.startswith("/") or "\\" in p:
            raise Refused(f"bad path {p!r}")
    source = {e["path"] for e in rec["authorized_files"]}
    for p in rec.get("artifact_paths", []):
        if p in source:                       # <-- the regression: "not X", never "only Y"
            raise Refused(f"artifact overlaps source: {p!r}")


def _hardened_validate(rec: dict) -> None:
    """Positive containment via path_denotation, plus destination collision checks."""
    import os

    here = os.path.dirname(os.path.abspath(__file__))
    for candidate in (here, os.path.join(here, "..", "..", "scripts")):
        if os.path.isfile(os.path.join(candidate, "path_denotation.py")):
            sys.path.insert(0, candidate)
            break
    from path_denotation import (
        PathDenotationError,
        check_repo_path,
        check_unique_identities,
    )
    try:
        targets: list[str] = []
        for entry in rec["authorized_files"]:
            targets.append(entry["path"])
            if entry.get("dest") is not None:
                targets.append(entry["dest"])   # destinations are write targets too
        check_unique_identities(targets, label="authorized targets")

        root = rec.get("artifact_root")
        for p in rec.get("artifact_paths", []):
            if root is None:
                raise Refused("artifact paths declared without a positive artifact_root")
            check_repo_path(p, root=root)       # contained within, not merely disjoint
        if rec["phase"] == "VERIFICATION" and rec.get("external_effects"):
            raise Refused("verification may not carry external effects")
    except PathDenotationError as exc:
        raise Refused(str(exc)) from exc


def _demo() -> int:
    corpus: list[tuple[str, int, dict]] = [
        ("traversal in authorized path", 1,
         _toy_record(authorized_files=[
             {"path": "../../other-repo/secret.ts", "operation": "MODIFY", "dest": None}])),
        ("aliased duplicate identity", 2,
         _toy_record(authorized_files=[
             {"path": "src/a.ts", "operation": "MODIFY", "dest": None},
             {"path": "src/b/../a.ts", "operation": "MODIFY", "dest": None}])),
        (".git target", 3,
         _toy_record(authorized_files=[
             {"path": ".git/config", "operation": "MODIFY", "dest": None}])),
        ("verification writes the CI gate", 4,
         _toy_record(phase="VERIFICATION", posture="VERIFICATION_ARTIFACTS_ONLY",
                     artifact_paths=[".github/workflows/audit.yml"])),
        ("verification rewrites its own validator", 5,
         _toy_record(phase="VERIFICATION", posture="VERIFICATION_ARTIFACTS_ONLY",
                     artifact_paths=["scripts/validate.py"])),
        ("artifact escapes the repository", 6,
         _toy_record(phase="VERIFICATION", posture="VERIFICATION_ARTIFACTS_ONLY",
                     artifact_paths=["../../outside/artifact.log"])),
        ("duplicate MOVE destinations", 7,
         _toy_record(authorized_files=[
             {"path": "src/a.ts", "operation": "MOVE", "dest": "src/z.ts"},
             {"path": "src/c.ts", "operation": "MOVE", "dest": "src/z.ts"}])),
        ("MOVE onto a DELETE target", 8,
         _toy_record(authorized_files=[
             {"path": "src/a.ts", "operation": "MOVE", "dest": "src/b.ts"},
             {"path": "src/b.ts", "operation": "DELETE", "dest": None}])),
        ("verification carries an external effect", 10,
         _toy_record(phase="VERIFICATION", posture="VERIFICATION_ARTIFACTS_ONLY",
                     external_effects=["POST https://prod.example.com/deploy"])),
    ]

    overall = 0
    for name, validate in (("VULNERABLE (as shipped at 05d8349)", _vulnerable_validate),
                           ("HARDENED (positive containment)", _hardened_validate)):
        print(f"\n{'=' * 72}\n{name}\n{'=' * 72}")
        suite = ProbeSuite(schema_validate=validate, refusal_errors=(Refused,))
        for label, family, record in corpus:
            suite.refuse(label, record, family=family)
        suite.accept("baseline: legitimate implementation record", _toy_record())
        suite.accept(
            "baseline: legitimate verification record",
            _toy_record(phase="VERIFICATION", posture="VERIFICATION_ARTIFACTS_ONLY",
                        artifact_root="build", artifact_paths=["build/report.json"]),
        )
        code = suite.report()
        print(f"exit={code}")
        if name.startswith("HARDENED"):
            overall = code
    return overall


if __name__ == "__main__":
    raise SystemExit(_demo())
