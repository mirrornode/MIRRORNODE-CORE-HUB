# POS-0001 — Ptah CI Enforcement Feasibility Review

**Matter:** CG-0031 — Council Authorization Gate v0.1  
**Reviewer:** Ptah  
**Result:** `feasible-with-conditions`

## Assessment

The Phase 0 Council Authorization Gate is technically feasible within the CG-0031 boundary.

A strict checked-in requirement contract can deterministically bind:

- exact Council matter ID;
- authority repository;
- immutable authority commit SHA;
- exact authority record path;
- implementation repository;
- protected path allowlist;
- authorized scope;
- accepting disposition vocabulary;
- explicit machine-readable conditions.

Unknown fields, unsupported versions, mutable refs, missing evidence, unknown conditions, ambiguous conditions, and unsatisfied conditions can all fail closed.

The validator can distinguish accepting dispositions (`accepted`, `accepted-with-conditions`) without parsing free-text rationale for authority. Free text may remain explanatory only.

The authority source should be pinned to an immutable CORE-HUB commit and exact record path. The validator must not trust branch heads, tags alone, cached last-known-good authority, or an implementation-repository copy of the authority record.

The pilot can remain limited to CG-0030 and the `mirrornode-platform` `/continuity` boundary. The workflow may run and fail as an advisory/scoped CI pilot without becoming a required merge check or changing branch protection.

## Required implementation condition

The gate must not self-validate against a requirement definition, protected-path declaration, validator source, or authority-binding configuration that the same evaluated change can weaken without detection.

The implementation evidence must therefore prove one of these equivalent safeguards:

1. the relevant gate/requirement configuration is sourced from an immutable authority-controlled artifact; or
2. changes to gate/requirement configuration are separately detected and fail the pilot validation unless authorized by a separate governing change.

A negative fixture must demonstrate that narrowing or altering the protected-path declaration cannot make an otherwise governed `/continuity` change pass.

## Recommended implementation placement

- Governance contract and authority records: `MIRRORNODE-CORE-HUB`.
- Reusable validator: authority-governed source with an immutable version/pin.
- Pilot workflow invocation: `mirrornode-platform`, scoped to `/continuity` and CG-0030.

The exact long-term executable location remains an implementation choice so long as the authority source and validator identity are pinned and the dependency direction remains from authority record to verifier.

## Recommendation

**Support CG-0031 as `feasible-with-conditions`.**

This review does not authorize required-check activation, branch-protection changes, broader rollout, runtime enforcement, deployment, publication, or any authority creation by CI.