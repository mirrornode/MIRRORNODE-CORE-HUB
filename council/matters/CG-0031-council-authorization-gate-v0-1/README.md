# CG-0031 — Council Authorization Gate v0.1

## Purpose

CG-0031 is a **proposed** governance matter. It does not grant authority by itself and does not implement or activate a CI gate.

Its purpose is to decide whether MIRRORNODE should authorize a bounded Phase 0 implementation of a **Council Authorization Gate**: a deterministic repository check that verifies an accepting Operator disposition already exists before scoped implementation work may pass CI.

The gate does not create authority. It verifies previously recorded authority.

## Derived Architectural Consequence

This matter follows from the separation already established across MIRRORNODE:

- **Council Grounds** records matters, reviews, and Operator dispositions.
- **The Operator** alone grants or withholds authority through recorded disposition.
- **The Operator Continuity Ledger** preserves continuity and authority state but remains non-operative.
- **CI** may enforce a recorded boundary without deciding it.
- **Runtime** executes only after authorized implementation exists.

The missing transition is therefore explicit: implementation-facing repositories need a deterministic way to reject work whose required authority has not yet become effective.

CG-0031 records that consequence for review. Logical necessity does not itself constitute implementation authority.

## Phase 0 Question

Should MIRRORNODE authorize implementation and local validation of a reusable Council Authorization Gate, with an initial scoped CI pilot for the `mirrornode-platform` `/continuity` boundary and CG-0030?

The pilot would verify a pinned Council record and fail when the required accepting Operator disposition is absent, malformed, mismatched, superseded, revoked, or conditionally unsatisfied.

## Authority Model

The authority chain must remain:

```text
Operator disposition in Council Grounds
        ↓
Pinned, merged authority record
        ↓
Deterministic CI validation
        ↓
Scoped implementation check passes or fails
```

The gate may answer only:

> Does the referenced governance record already authorize this exact repository, surface, and implementation scope?

It may not answer whether authority ought to be granted.

## Phase 0 Scope Requested

If CG-0031 is accepted, Phase 0 may implement:

- A strict, machine-readable authorization-requirement contract.
- A reusable validator with deterministic pass/fail behavior and stable reason codes.
- Validation of an exact Council matter ID, repository, path scope, authority source commit, record path, Operator disposition, accepting state, and applicable conditions.
- An allowlist of accepting dispositions, initially limited to `accepted` and `accepted-with-conditions`.
- Machine-readable condition checking; unknown or unsatisfied conditions fail closed.
- Exact source pinning to a repository, immutable commit SHA, and record path. Mutable branch references may not establish authority.
- Exact target matching for repository and protected path scope.
- Failure-closed behavior for missing, malformed, conflicting, stale, superseded, revoked, unpinned, or unsupported records.
- Fixture-based passing and failing test cases.
- A scoped CI pilot in `mirrornode-platform` for changes within the `/continuity` implementation boundary that reference CG-0030.
- An implementation evidence packet containing contract, validator, tests, CI results, boundary confirmation, and failure cases.

## Not Authorized

CG-0031 does **not** authorize:

- Granting, inferring, amending, revoking, or recording authority through CI.
- Treating a merged PR, approved review, successful check, Ledger entry, or source-checked artifact as an Operator disposition.
- Parsing free-text rationale to infer authorization or satisfy conditions.
- Reading authority from mutable branch heads or unpinned remote artifacts.
- Writing to Council Grounds, the Operator Continuity Ledger, implementation repositories, or runtime state.
- A bypass, override, emergency approval, or self-authorization mechanism.
- Organization-wide or all-repository rollout.
- Branch-protection changes or making the pilot check a required merge check.
- Blocking unrelated files, repositories, surfaces, or workstreams.
- Runtime, MOPCON, deployment, publication, or production-data changes.
- Exposure of private deliberation, private rationale, or sensitive operational data in CI logs.

## Initial Pilot Boundary

Phase 0 is intentionally narrow:

- **Authority record:** CG-0030.
- **Authority repository:** `mirrornode/MIRRORNODE-CORE-HUB`.
- **Implementation repository:** `mirrornode/mirrornode-platform`.
- **Protected surface:** the `/continuity` implementation boundary.
- **Gate effect:** the CI job passes or fails; required branch-protection activation remains unauthorized.

The validator may be reusable by design, but no other repository or path becomes governed by CG-0031.

## Conditions and Failure Behavior

An `accepted-with-conditions` disposition is effective only when every applicable condition is represented in a supported machine-readable form and is satisfied by reviewable evidence.

The gate must fail closed when:

- the authority record is missing or malformed;
- the matter ID, repository, path, or requested scope does not match;
- the record is not pinned to an immutable commit;
- disposition authority is not the Operator;
- disposition state is non-accepting or unknown;
- required timestamps or rationale are absent;
- a condition is unknown, ambiguous, or unsatisfied;
- the record has been superseded or revoked;
- authoritative records conflict.

No last-known-good authority fallback is permitted. Authority is not a cached data product.

## Privacy and Disclosure Boundary

CI output should expose only the minimum information required to diagnose a failure, such as matter ID, validation stage, and stable reason code.

The gate must not print private Council deliberation, private Operator rationale, credentials, customer data, internal topology, or unrelated governance records.

## Reviews

CG-0031 requests:

- **Ptah** — implementation feasibility review limited to the authority input contract, immutable source pinning, repository and path matching, condition representation, deterministic failure behavior, testability, and initial pilot topology.
- **Osiris** — authority, privacy, and abuse-boundary review limited to non-inference, non-creation of authority, supersession and revocation behavior, disclosure-safe diagnostics, bypass resistance, and separation from runtime authority.

Both reviews are advisory. Neither review changes `authorityEffect` or grants implementation authority.

## Operator Disposition

While CG-0031 remains under review:

- `workflowState: proposed`
- `authorityEffect: none-until-operator-disposition`

must remain unchanged.

Only a recorded accepting Operator disposition may authorize Phase 0 implementation. Activation as a required merge check, broader rollout, or additional protected scopes requires a later Council matter.

## Constitutional Boundary

CG-0031 does not move governance into CI.

Council Grounds remains the authority record. The Operator remains final authority. The Ledger remains non-operative. CI is limited to deterministic verification and scoped failure. Runtime receives no new authority from this matter.
