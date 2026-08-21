# Repo Steward Presence Reconciliation — 2026-08-21

## Status

**IMPLEMENTATION EVIDENCE RECORDED / GOVERNANCE REGISTRY STATUS UNRESOLVED**

Repo Steward v0.1 is being implemented in `MIRRORNODE-INFRA` as a repository-integrity control plane, with a corresponding proposed runtime prompt stack in `mirrornode-agent-runtime`.

This record exists to prevent implementation presence from being mistaken for ratified governance authority.

## Proposed stack

- REPO STEWARD — integrates repository health evidence and bounded administrative proposals.
- SURVEYOR — inventories repositories, stacks, workflows, configuration, and ownership evidence.
- SENTINEL — classifies code/check/CI integrity as PASS/HOLD/FAIL/UNKNOWN.
- NOTARY — binds review/check/evidence claims to exact repository identities and immutable heads.
- CUSTODIAN — prepares bounded repair proposals.
- WARDEN — reviews permissions, branch/ruleset posture, secret-risk, destructive paths, and self-expansion hazards.

## Observed implementation boundary

The INFRA implementation is designed with a GET-only checker and proposal-only administration engine. Its v0.1 write transport is absent.

Any future Repo Steward repository mutation is specified to require dual control:

1. explicit human Operator authorization bound to the target/action; and
2. at least one independent attestation from an approved OpenAI, Perplexity, or Claude advisory lane bound to the same target/action.

Neither side alone is sufficient inside the governed Repo Steward path. The advisory attestation is evidentiary/reviewing and does not create repository authority. Bot-only, service-account-only, coding-agent-only, advisory-model-only, and Operator-only Repo Steward mutation paths are non-conformant.

## Registry reconciliation rule

Neither implementation in INFRA nor presence in the generic runtime is sufficient to establish current governance-registry membership, dispatch authority, constitutional standing, merge authority, or repository permissions. Those questions remain subject to the existing registry/routing reconciliation boundary and any applicable Council/Operator process.

## Anti-self-certification rule

No Repo Steward component may certify its own repair as sufficient clearance. A changed head requires the owning repository's checks and applicable independent exact-head review before a merge decision.

## Platform-enforcement residual

The Repo Steward contract can close its own control plane, but GitHub account-level bypass resistance still depends on repository rulesets, branch protection, credentials, and account permissions. Until platform controls enforce the same dual-control rule, that gap must remain explicit rather than being treated as solved by documentation or application code.

## Current source lanes

- Implementation and policy: `MIRRORNODE-INFRA` branch/PR for Repo Steward v0.1.
- Proposed runtime prompt placement: `mirrornode-agent-runtime` branch/PR for Repo Steward stack v0.1.
- Governance/canonical interpretation: this CORE-HUB record and subsequent explicit disposition.

No source lane may silently substitute for another.
