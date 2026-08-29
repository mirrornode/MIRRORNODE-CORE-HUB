# Adversarial Probe Corpus v0.1

**Status:** PROPOSED — not active canon. Promotion is an Operator decision.
**Owner:** Thoth (Verification) and Ptah (Governance)
**Purpose:** Permanent regression corpus for adversarial review of authority-bearing surfaces —
authorization records, phase gates, scope digests, evidence schemas, and validators.
**Origin:** PR #53 (specialized terminal-agent phase gating), head
`05d83494527a7318139d5255dd75fb4ff740600c`, 22 August 2026.

## Why this corpus exists

At the origin head, the proposal truthfully reported valid JSON Schema, a valid example,
successful semantic validation, 47/47 adversarial tests passing, and every negative test
failing for its intended reason. Ten further probe classes were then constructed. **All ten
were accepted when all ten should have been refused.**

The suite covered only the failure modes its author had anticipated. Every live finding sat in
the gaps between those tests — path denotation, destination collision, artifact scope,
raw-to-parsed agreement, and handoff lineage.

> A test suite demonstrates only the failure modes represented by that suite. It does not
> establish completeness of the threat model. A green suite is evidence. It is not clearance.

Every probe family below was earned from a real escaped defect. Once learned, a mistake should
be cheap forever — that is how a review cycle's cost amortizes across the system's future.

**Each family must be executed or explicitly marked not-applicable with a reason. "Not run" is
not a disposition.**

## How to run it

The harness pattern lives in `tests/probes/probe_harness.py`: construct a record that *should*
be refused, submit it to schema plus semantic validation, and report acceptance as a hole.

Two constraints keep a run from flattering itself:

- Every suite must contain at least one baseline `accept` probe. A validator that refuses
  everything is broken, not secure, and an all-refuse run would otherwise report clean.
- Refusal exception types must be specific. A bare `except Exception` lets a typo in the probe
  masquerade as a security refusal. This was a live defect in PR #53's own suite mid-cycle.

Deterministic path containment is implemented in `scripts/path_denotation.py` and is importable
directly by validators. `tests/test_path_denotation.py` runs it in CI.

---

## Families 1–16 — escaped at the origin head

### 1. Repository path traversal
`../../other-repo/secret.ts`, `a/../../../etc/passwd`, `src/../../escape.ts` in any path-typed
field. Also absolute forms, `~` expansion, and UNC/drive prefixes.

### 2. Normalized path equivalence
`src/a.ts` vs `./src/a.ts` vs `src//a.ts` vs `src/./a.ts` vs `src/b/../a.ts` — one resource
presented as multiple identities, defeating uniqueness and set-equality checks. Also case
folding and Unicode NFC/NFD equivalence on normalizing filesystems.

### 3. `.git` access
Any declared scope reaching `.git/config`, `.git/hooks/`, `.git/HEAD`, or `.git/objects/`.
Reaching `.git` is equivalent to controlling repository identity and history.

### 4. `.github` mutation during verification
Any non-implementation phase permitted to write `.github/workflows/`. The gate must not be
writable by what it gates.

### 5. Verifier self-modification
Any declared scope reaching the validator script, the schema, the test suite, or the agent
instruction projection. Probe every posture, not only the permissive one.

### 6. Artifact-root escape
Where artifact or output paths are constrained only by *exclusion* from another set, enumerate
the complement and probe its most privileged members. **The founding regression:** requiring
verification artifacts to be *disjoint from* the reviewed source allowlist channeled writes
toward everything unreviewed, including the CI gate and the validator itself. Strictly weaker
than the state it replaced.

### 7. Duplicate MOVE destinations
Two move or rename operations targeting one destination path.

### 8. MOVE/DELETE destination collision
`MOVE a → b` alongside `DELETE b`, and the same for `CREATE b`. Destinations are write targets
and must participate in collision checks.

### 9. Raw-vs-parsed disagreement
Where a human-readable capture and a machine-parsed record coexist, make them name different
resources. Both being digested together proves tamper-evidence, not agreement. Enforcement
follows the parsed side while auditors read the raw side.

### 10. Verification external effects
A non-mutating or verification-only posture carrying an inherited external effect such as
`POST https://prod.example.com/deploy`.

### 11. Handoff authorization-lineage mismatch
A handoff or terminal report describing changes that were never authorized, at a state where
authorized scope has been frozen empty and there is nothing left to reconcile against. The
handoff report is what a successor agent trusts most and is easily the least bound object.

### 12. Missing phase-specific authorization
A later gate validating on an earlier gate's authorization event. Check the prose claim about
action-specific authorization against what the record actually requires.

### 13. Mutable working-directory identity
Checkout path, worktree root, or environment identity changed after authorization while every
digest still verifies. Probe every checkout-identity field for binding coverage.

### 14. Expired authorization
Evidence timestamped after `valid_until`; unbounded or absent expiry; expiry far in the future.

### 15. Superseded or revoked authorization
`status` set to `REVOKED` or `SUPERSEDED` with evidence still accepted; `superseded_by`
pointing at a nonexistent, self-referential, or cyclic authorization.

### 16. Premature-mutation evidence completeness
Incident records whose status, changed-path, and diff evidence sets disagree; duplicates within
a set; rename source or destination dropped; empty evidence for a non-null incident.

---

## Families 17–20 — generic to any authority record

### 17. Boundary and empty values
Empty arrays where `minItems` should apply; empty strings; whitespace-only strings; zero-length
digests; `null` where a closed object is required; maximum-length and off-by-one lengths.

### 18. Ordering inversions
Every timestamp pair in reverse order. Every event sequence permuted. Authorization before
inspection; verification before authorization; evidence before the thing it evidences.

### 19. Cross-field contradiction
Every pair of fields that must agree, made to disagree — while keeping the record schema-valid
and every digest correctly recomputed over the contradictory content.

### 20. Negative constraint without positive boundary
Grep the design for `not`, `disjoint`, `must not`, `excluded`, `other than`. For each, enumerate
the complement and ask whether it contains anything more privileged than what was excluded.
This is a design-review probe, run against the schema and the prose, not only against instances.

> "Not X" is not the same thing as "only Y." Prefer positive containment: *only under this
> artifact root*, *only these normalized repository-relative paths*, *only this exact head*,
> *only this authorization lineage*.

---

## Extending the corpus

When a defect escapes, append a family with what to construct, which head it escaped at, and
why it matters. Do not delete families when a system stops being vulnerable to them —
regression probes are the point.

Beyond the fixed corpus, never ask only whether the existing tests pass. Ask:

1. What invariant does this test suite appear to believe exists?
2. What other representation could satisfy the implementation while violating that invariant?

Search specifically for aliasing, traversal, collisions, missing lineage, inconsistent duplicate
representations, phase authority leakage, stale evidence, self-reference, self-modification,
mutation through supposedly non-mutating surfaces, equivalent resource identifiers, negative
constraints lacking positive boundaries, and data that humans and machines trust differently.

## Claim discipline

A clean run yields `ADVERSARIAL_PROBES_PASS` **for the declared families only**. It does not
imply `EXACT_HEAD_REVIEWED`, `INDEPENDENT_EXACT_HEAD_REVIEWED`, `CONSTITUTIONALLY_CLEARED`, or
`MERGE_AUTHORIZED`. No lower claim implies a higher one.
