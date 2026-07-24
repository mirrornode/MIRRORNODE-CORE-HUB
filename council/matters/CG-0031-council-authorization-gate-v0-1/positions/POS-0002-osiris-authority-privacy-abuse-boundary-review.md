# POS-0002 — Osiris Authority, Privacy, and Abuse Boundary Review

**Matter:** CG-0031 — Council Authorization Gate v0.1  
**Reviewer:** Osiris  
**Result:** `safe-with-conditions`

## Assessment

The Phase 0 gate can operate without becoming an authority source if the verifier-only boundary in CG-0031 is enforced exactly.

Authority must remain exclusively attributable to a previously recorded Operator disposition in the pinned Council record. The gate may verify that authority but may not create, infer, amend, revoke, extend, or publish it.

The following must remain prohibited as authority sources:

- merged pull requests;
- review approval;
- CI success;
- Continuity Ledger status;
- source-check labels;
- free-text rationale;
- mutable branch or tag state;
- cached last-known-good authority.

`accepted-with-conditions` is safe only when every applicable condition is explicit, machine-readable, supported, and satisfied. Unknown, ambiguous, missing, or unsatisfied conditions must fail closed.

Superseded, revoked, conflicting, malformed, unpinned, or mismatched authority records must fail closed. The validator may not select a convenient record or silently fall back.

CI diagnostics must remain disclosure-minimized to the bounded fields already described by CG-0031: matter ID, validation stage, pass/fail, stable reason code, and safe remediation summary. Private deliberation, private Operator rationale, credentials, customer data, internal topology, and unrelated governance records must not be emitted.

## Required anti-bypass condition

The evaluated change must not be able to weaken the gate definition, authority binding, or protected-path declaration and then use that weakened definition to validate itself.

The implementation must either consume an immutable authority-controlled gate configuration or detect and fail self-modifying/narrowing changes unless they are separately authorized. A negative fixture must prove that a contributor cannot evade the `/continuity` pilot by narrowing or altering the protected-path declaration.

This condition is compatible with Ptah POS-0001 and does not create a new authority source.

## Separation of responsibilities

- Council Grounds remains the authority record.
- The Operator remains final authority.
- The Continuity Ledger remains non-operative.
- CI remains a deterministic verifier and failure surface only.
- Runtime and MOPCON receive no new authority from this matter.

## Recommendation

**Support CG-0031 as `safe-with-conditions`.**

The Phase 0 pilot can operate without becoming an authority source provided the anti-self-modification condition above is included in the implementation evidence and tests. Required-check activation, branch-protection changes, broader rollout, runtime enforcement, deployment, and publication remain separate future decisions.