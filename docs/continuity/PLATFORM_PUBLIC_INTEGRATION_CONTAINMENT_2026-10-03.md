# Platform public integration containment — proposed governance evidence

**Status:** PROPOSED / in review; no canon promotion or release authority  
**Observed:** 2026-10-03  
**Execution repository:** [mirrornode-platform PR #57](https://github.com/mirrornode/mirrornode-platform/pull/57)  
**Source head at observation:** `2f09c65638f4b75137fc1a4483fbbedfd76b4fcc`  
**Prior verified CI head:** `be385f7221e9b4fbeefb8b0dbe9a4dd89815ee09`

## Boundary change under review

The platform's public `POST /api/agent` and `POST /api/event` routes previously accepted caller payloads without a defined caller authorization contract. PR #57 changes both handlers to bounded HTTP 503 responses without accepting a request parameter or forwarding the body. The public Osiris page removes the Sync event submission control. The change is a **capability restriction in proposed source**, not an expansion or a currently verified production deployment.

The candidate's [security record](https://github.com/mirrornode/mirrornode-platform/blob/2f09c65638f4b75137fc1a4483fbbedfd76b4fcc/docs/security/PUBLIC_EXPOSURE_CONTAINMENT.md) and route tests describe and test non-consumption, non-forwarding, and bounded responses. At the earlier `be385f7...` head, GitHub CI #200 and Canon Gate #126 passed. Fresh checks and review at the current head must be evaluated separately. No deployment, provider installer, upstream consumer, or credential-revocation conclusion follows from source and CI.

## Governance relationship

This record reflects the platform `AGENTS.md` rule that changes to agent capability boundaries must be reflected in CORE-HUB. It also preserves CORE-HUB `AGENTS.md`'s requirement for governance/registry evidence before release. This is a draft cross-repository reconciliation; it does not edit a ratified capability contract or claim a current complete registry. The CORE-HUB search found no explicit `POST /api/agent` or `POST /api/event` contract to revise in place; the absence of a search result does not establish that every downstream consumer has been inventoried.

Before either route is re-enabled, a separately reviewed contract must identify caller identity, permitted operations, server-side authorization, upstream authentication, negative tests, and response/logging limits, then reconcile the applicable CORE-HUB record. A Supabase session alone is not an authorization grant. The current candidate grants no invocation capability.

## Holds and disposition

- **OBSERVED:** PR #57 contains the source-level restriction and local/remote checks at the prior head. Its current head requires fresh checks and eligible independent review.
- **UNKNOWN:** deployed route behavior, actual integration consumers, provider dependency tree, historical credential revocation, and the detailed identities and reachability of five high-severity findings reported by npm in CI #200.
- **PROPOSED:** retain PR #57 at review/release hold while this evidence is reviewed; determine whether this staged record or another governance/registry artifact is the correct lasting location. Resolve any conflict through the normal CORE-HUB review and Operator ratification process.

No agent promotion, canon authority, merge, deployment, credential change, public release, or capability reactivation is conferred by this document.
