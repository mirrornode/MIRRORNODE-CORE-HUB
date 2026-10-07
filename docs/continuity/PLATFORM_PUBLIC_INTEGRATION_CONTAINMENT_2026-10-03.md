# Platform public integration containment — proposed governance evidence

**Status:** PROPOSED / in review; no canon promotion or release authority
**Observed:** 2026-10-06; exact-head npm receipt retained 2026-10-07
**Execution repository:** [mirrornode-platform PR #57](https://github.com/mirrornode/mirrornode-platform/pull/57)
**Current source head:** `3fec902883ab90acc0a8d47bc080735e01aa75a6`
**Predecessor source head:** `2f09c65638f4b75137fc1a4483fbbedfd76b4fcc`
**Prior verified CI head:** `be385f7221e9b4fbeefb8b0dbe9a4dd89815ee09`

## Predecessor evidence retained from October 3

The following source and CI observations belong to the predecessor heads named below. Current-head evidence and proposed disposition follow in the October 6 section.

## Boundary change under review

The platform's public `POST /api/agent` and `POST /api/event` routes previously accepted caller payloads without a defined caller authorization contract. PR #57 changes both handlers to bounded HTTP 503 responses without accepting a request parameter or forwarding the body. The public Osiris page removes the Sync event submission control. The change is a **capability restriction in proposed source**, not an expansion or a currently verified production deployment.

The candidate's [security record](https://github.com/mirrornode/mirrornode-platform/blob/2f09c65638f4b75137fc1a4483fbbedfd76b4fcc/docs/security/PUBLIC_EXPOSURE_CONTAINMENT.md) and route tests describe and test non-consumption, non-forwarding, and bounded responses. At the earlier `be385f7...` head, GitHub CI #200 and Canon Gate #126 passed. At current head `2f09c65...`, [CI #202](https://github.com/mirrornode/mirrornode-platform/actions/runs/37153121855) and [Canon Gate #128](https://github.com/mirrornode/mirrornode-platform/actions/runs/37153121801) also completed successfully: eight Python tests, 52 application tests, lint and build. npm again reported five high-severity vulnerabilities. No eligible approving review was observed; review and release disposition remain separate. No deployment, provider installer, upstream consumer, or credential-revocation conclusion follows from source and CI.

## Governance relationship

This record reflects the platform `AGENTS.md` rule that changes to agent capability boundaries must be reflected in CORE-HUB. It also preserves CORE-HUB `AGENTS.md`'s requirement for governance/registry evidence before release. This is a draft cross-repository reconciliation; it does not edit a ratified capability contract or claim a current complete registry. The CORE-HUB search found no explicit `POST /api/agent` or `POST /api/event` contract to revise in place; the absence of a search result does not establish that every downstream consumer has been inventoried.

Before either route is re-enabled, a separately reviewed contract must identify caller identity, permitted operations, server-side authorization, upstream authentication, negative tests, and response/logging limits, then reconcile the applicable CORE-HUB record. A Supabase session alone is not an authorization grant. The current candidate grants no invocation capability.

## Holds and disposition

- **OBSERVED:** PR #57 contains the source-level restriction and local/remote checks at the prior head. Fresh checks at its current head passed; eligible independent approval remains open.
- **UNKNOWN:** deployed route behavior, actual integration consumers, provider dependency tree, historical credential revocation, and the detailed identities and reachability of five high-severity findings reported by npm in CI #200.
- **PROPOSED:** retain PR #57 at review/release hold while this evidence is reviewed; determine whether this staged record or another governance/registry artifact is the correct lasting location. Resolve any conflict through the normal CORE-HUB review and Operator ratification process.

No agent promotion, canon authority, merge, deployment, credential change, public release, or capability reactivation is conferred by this document.

## Current-head reconciliation — October 6, 2026

The platform source at `3fec902883ab90acc0a8d47bc080735e01aa75a6` retains both non-forwarding HTTP 503 handlers and removal of the public Sync submission control. The latest incremental correction raises the Node 20 engine floor to 20.19.0; it adds no invocation capability. Ten GitHub checks pass at this head. Copilot returned COMMENTED, preserving capability and dependency concerns; no approving review is claimed.

A retained [exact-head npm audit receipt](./receipts/PR57_EXACT_HEAD_NPM_AUDIT_2026-10-07.md) now records the isolated installation and audit performed from platform head `3fec902883ab90acc0a8d47bc080735e01aa75a6`: Node `v20.20.2`, npm `10.8.2`, manifest and lockfile SHA-256 identities, `npm ci --ignore-scripts --audit=false` exit 0, full-audit exit 1 with six high findings, production-scope audit exit 1 with one high finding, observed dependency paths, and hashes for the Operator-local raw receipt artifacts. Five findings are on the dev-only eslint-config-next → @next/eslint-plugin-next → fast-glob → micromatch → braces 3.0.3 chain; source-map-js 1.2.1 remains in the production tree through Next.js → PostCSS. These are two underlying advisories, not six distinct exploits: [braces](https://github.com/advisories/GHSA-vfj7-8cjw-p6xm) and [source-map-js](https://github.com/advisories/GHSA-68fv-2mgg-jv7q). Deployment reachability is unknown. No vulnerable dependency was changed or risk waived.

### Concrete governance proposal

Retain this continuity document as the cross-repository evidence record for the **proposed temporary restriction** at the exact current platform head. Accept its location for this bounded reconciliation, while preserving the org agent-role registry unchanged: the platform is an integration surface and this proposal does not retire or change an agent's registered runtime role. This is a proposed disposition, not a claim that the authoritative registry is complete or that approval has already occurred.

The Operator's explicit disposition must choose: accept this evidence-record location for the proposed restriction, require an identified registry/contract amendment, or stop/park the change. A reviewer may assess accuracy and sufficiency but cannot substitute technical review for human governance authorization. If another governing contract is identified, reconcile it before release. Record the human decision against this CORE-HUB proposal commit and platform `3fec902883ab90acc0a8d47bc080735e01aa75a6` before disposing the platform capability thread.

Acceptance closes only the record-location question. PR review/merge, dependency remediation or explicit scoped risk disposition, deployed containment, consumer compatibility, historical credential revocation and release authorization remain open. Route reactivation still requires a separately reviewed authorization contract. No canon promotion, agent authority expansion or release permission follows.

Earlier paragraphs are dated predecessor evidence; their five-high count does not describe the current audited tree. Current source reference: [security record](https://github.com/mirrornode/mirrornode-platform/blob/3fec902883ab90acc0a8d47bc080735e01aa75a6/docs/security/PUBLIC_EXPOSURE_CONTAINMENT.md).
