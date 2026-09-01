# MIRRORNODE-00 — Operational Addendum

**Date:** 2026-09-01  
**Status:** CANDIDATE OPERATIONAL EVIDENCE / UNRATIFIED  
**Authority effect:** NONE  
**Canonical precedence:** NONE  
**Promotion gate:** Ptah evaluation + explicit Operator ratification + canonical promotion record in accordance with `MASTER_INDEX.md`  
**Historical integrity:** earlier dossiers, reviews, exact-head attestations, and authority records remain unchanged

## Purpose

This candidate record reconciles recent implementation and verification evidence from the MOPCON / governed runtime / Osiris integration session.

It is useful for current-state reasoning but is **not canon merely because it exists, is indexed, is reviewed, or is merged**. Until the required promotion gate is satisfied, ratified authority records retain precedence.

The labels used here are intentionally separate:

- **observed** — directly seen in runtime, database, endpoint, build, or tool evidence;
- **implemented** — code exists at an identified repository/branch/head;
- **verified** — stated behavior was exercised successfully in the stated scope;
- **held** — intentionally prevented from advancing pending evidence, security, review, or authority;
- **not authorized** — no consequential action is granted by the evidence.

---

## 1. Current operating shape

MOPCON is the current private Operator cockpit implementation surface. Its working modules include:

- observed system/runtime evidence;
- governed plan → approve → execute → trace interaction;
- Operator Debt / NOW semantics;
- commercial readiness;
- Osiris fulfillment state;
- authenticated private case visibility;
- workstream / architecture context;
- permitted-next-action semantics.

Operating principle:

> Different types of work, different modules, same Operator interface.

MOPCON is an implementation/control surface, not governance authority by repository existence.

---

## 2. MOPCON exact-head lineage

Repository: `mirrornode/mirrornode-operator-console`  
Draft PR: `#27`  
Branch: `feat/local-runtime-console-2026-08-31`

### Current head

`5fe21304aadbef67a9f5b3d983f21a6a1f6a0b60`

State:

- open / draft / unmerged;
- local `npm run type-check` / `tsc --noEmit` reported clean at this exact head on 2026-09-01;
- no GitHub commit status check substitutes for that local evidence;
- fresh independent exact-head review has been requested.

### Prior E2E head

`fe63850aa1371126c159d3a64b044ee7b1db6fe2`

Verified locally at that predecessor:

- MOPCON private-case API failed closed with HTTP `401` before Operator authentication;
- Operator authentication returned HTTP `200`;
- authenticated case projection was `available`;
- projected mutation state was `disabled`;
- three paid Osiris cases were visible through the minimum projection.

That E2E result remains evidence for `fe63850...`; it is not silently promoted to exact-head E2E proof for `5fe213...`.

### Independent review correction

Codex reviewed predecessor `5bb06891036c7871f60ff90df269e96c98e74004` and reported 3 P1 + 5 P2 findings. Current head `5fe213...` contains bounded corrections for all eight:

1. explicit case-field allowlist reconstruction;
2. all-or-nothing malformed projection rejection;
3. current authenticated private-boundary evidence instead of stale “missing boundary” language;
4. retirement of already-completed Osiris next actions;
5. fulfillment page no longer presents historical verification as present-tense reader availability;
6. offer/methodology drift classified as a future public-promise/scale gate rather than current Operator Debt while bounded implementation can continue;
7. plaintext HTTP reader transport allowed only on loopback; non-loopback requires HTTPS and embedded URL credentials are rejected;
8. Operator-visible plan includes immutable evidence/bound-objective digest metadata before approval rather than hiding all bound execution context.

Fresh review is required before those corrections are considered independently cleared.

---

## 3. MOPCON private-data boundary

Implemented local single-Operator properties include:

- server/local Operator password;
- signed HttpOnly session cookie;
- SameSite strict;
- bounded session TTL;
- fail-closed missing auth configuration;
- authenticated `/cases` and `/api/private/cases`;
- loopback-default local binding;
- no Supabase or Stripe server credential supplied to MOPCON.

The MOPCON case reader now also:

- requires the configured source URL to be HTTPS unless the host is loopback;
- rejects embedded source-URL credentials;
- requires a valid top-level projection contract;
- rejects the entire projection if any case row is malformed;
- materializes only the explicit minimum `OperatorCase` allowlist.

This remains a **local single-Operator v0.1 boundary**, not a complete remote identity/security architecture.

---

## 4. Platform read-only case projection

Repository: `mirrornode/mirrornode-platform`  
Draft PR: `#53`  
Branch: `feat/mopcon-readonly-case-projection-2026-08-31`

### Current head

`56bfd1d31b8a5964f5de870b59f5e8c3568b418b`

Current exact-head evidence:

- Vercel commit status: **success**;
- corrected implementation is open / draft / unmerged;
- fresh independent exact-head review has been requested;
- fresh local route-test execution at this exact head remains a separate hold condition.

### Verification lineage

Pre-Turbopack-fix predecessor:

`b78152011c81c4d4fa2d09a3c9f1c7e70f9fd78f`

At that predecessor, the unauthenticated preview route was exercised and returned HTTP `401` with no customer projection.

Later local reader head:

`062ad630ad3c795dd27c2e84d251880b8c615c3f`

At that predecessor:

- local Platform reader ran on loopback;
- authenticated read against the production ledger succeeded;
- MOPCON consumed the minimum projection successfully;
- three paid cases were observed through the read path.

Do not attribute the earlier unauthenticated preview check to `062ad...` or `56bfd...` without a rerun.

### Current review corrections

Codex reviewed `062ad630...` and found two P2 issues. Current head `56bfd1d...` corrects both:

1. **UUID schema reproducibility** — checked-in additive migration `supabase/migrations/20260901074500_add_guest_audit_purchase_case_uuid.sql` tracks/backfills the independent case UUID for reproducible environments. The migration is **not applied to production by this record**.
2. **Actionable-case completeness** — actionable fulfillment states are internally paged until exhausted so older active cases cannot disappear behind a 100-row history cap; terminal history remains bounded.

Current-head tests and fresh exact-head review are still required.

---

## 5. Case projection authority boundary

MOPCON receives only the minimum Operator case view:

- case UUID;
- masked customer identity;
- payment state;
- fulfillment state;
- timestamps;
- intake-present flag;
- artifact count.

Deliberately excluded:

- Stripe session/customer identifiers;
- raw intake narrative;
- artifact URLs;
- Supabase service-role credential;
- release/delivery authority;
- customer-data mutation authority.

Platform retains its existing service-role credential server-side. Therefore:

- **MOPCON compromise does not directly expose that credential through this projection contract**;
- **the Platform server itself still holds broader server-side authority**;
- GET-only projection code and `mutation: disabled` do not prove mutation is technically impossible across the wider customer-case system.

Correct statement:

**projected mutation state: DISABLED; customer mutation/release/delivery: NOT AUTHORIZED.**

---

## 6. Live Osiris case evidence

The read-only aggregate database evidence and authenticated MOPCON projection previously agreed on:

- **3 paid Osiris cases total**;
- **2** at `intake_complete`;
- **1** at `fulfillment_started`.

During that verification no raw intake narrative, full customer identity, Stripe identifier, or artifact URL was printed, and no production row was intentionally mutated by the read verification.

This is a dated observation and must be refreshed before being treated as a later live count.

---

## 7. Case identity

`guest_audit_purchases.id` is the independent UUID used by the projection as `case_id`.

Current interpretation:

- ledger UUID = candidate canonical first-dollar case identity;
- Stripe identifiers = payment identity/evidence;
- remaining structural gap = durable binding of evidence versions, findings/deliverable versions, release approvals, and delivery receipts to that case UUID.

The checked-in Platform migration exists to make that UUID reproducible from repository schema history. Applying that migration remains separately governed.

---

## 8. Operator Debt / NOW

Operator Debt means:

> items that cannot legitimately advance until the Operator acts.

Working lanes:

- `operator_required`;
- `execution_active`;
- `blocked_elsewhere`;
- `watch`;
- `parked`.

Only `operator_required` contributes to Operator Debt.

At the last live case observation, two paid cases were `intake_complete` without recorded Operator review. Under the manual fulfillment contract, they could not legitimately advance into fulfillment without Operator review.

**Derived customer-case Operator Debt at that observation: 2.**

That live case debt is not yet aggregated into the MOPCON `NOW` home surface.

The Osiris public-offer/methodology naming drift is **not current Operator Debt** while bounded implementation can continue without changing the public promise. It becomes an Operator-required decision before a consequential storefront/promise/fulfillment-scale change.

---

## 9. Fulfillment spine

Working lifecycle:

1. Purchase — production wired.
2. Intake — production wired.
3. Case Bound — durable partial.
4. Evidence — missing dedicated durable state.
5. Findings — missing dedicated durable state.
6. Operator Release — missing dedicated durable release receipt.
7. Delivery — durable partial.
8. Delivery Receipt — missing immutable effect receipt.

Important distinctions:

- `operator_reviewed_at` is a pre-fulfillment checkpoint, not an exact-version release receipt;
- `delivered_at` is a timestamp, not proof of which approved artifact/version was delivered;
- read-only case visibility is not fulfillment authority.

Remaining scale blockers include version-bound evidence/findings, exact-version release approval, immutable delivery receipt, and fail-closed stale-authority behavior.

---

## 10. Governed runtime implementation

Repository: `mirrornode/mirrornode-agent-runtime`

Current MOPCON-connected runtime implementation follows:

`plan → explicit Operator approve → execute → trace`

Known gaps remain:

- plan storage is in-memory;
- trace durability is insufficient for restart/serverless continuity;
- runtime-native remote authentication is incomplete;
- local reachability is not durable production service;
- runtime approval does not grant repository write, merge, deployment, provider-promotion, or customer-effect authority.

**Authority qualification:** this record identifies the current implementation surface only. It does not resolve or grant dispatch, routing, or governance authority where those remain unresolved in ratified governance records/registries.

The target milestone `ORACLE ONLINE v0.1 — Durable Advisory Runtime` remains incomplete.

---

## 11. Commercial spine

Current working progression in MOPCON:

1. Project Archaeologist — discovery / lead generation.
2. Osiris Audit — current bounded `$149` entry offer.
3. MOPCON Secure — recurring observation/control/escalation.
4. Assurance Sprint — bespoke remediation / implementation.
5. Enterprise Control Plane — future/custom destination.

MOPCON Secure remains bounded to recurring observation, authority visibility, evidence/state tracking, drift detection, alerts, control configuration, and escalation. Bespoke remediation, code changes, migrations, provider integration, and material customer-system changes belong to Assurance Sprint.

---

## 12. Public-offer / methodology drift

Current unresolved naming/contract drift:

- public Platform sells **Osiris Audit v1** at `$149`;
- current `osiris-audit` methodology defines **Structural Scan v1** as a distinct `$149` entry engagement before a larger Agent Authority Audit.

No tool or runtime should silently choose a new customer promise.

Disposition:

**future Operator decision gate before storefront wording change or fulfillment scaling; bounded implementation may continue while the public promise remains unchanged.**

---

## 13. Security/dependency debt

During local Platform worktree installation, `npm ci` reported **6 high-severity vulnerabilities**.

Current classification:

- package-manager finding observed;
- exact package/reachability/exploitability not yet triaged in this record;
- no `npm audit fix` was run;
- no claim is made that all six are exploitable in the deployed path.

A bounded dependency audit remains required.

---

## 14. Superseded watch state

MOPCON PR `#25` was closed **unmerged** as superseded by PR `#27`.

Its static/pre-customer watch assumptions remain in Git history as provenance but are not current operating evidence.

Closing that PR did not delete history or authorize PR `#27`.

---

## 15. Exact-head anchors

| Surface | Exact head | Evidence / state |
|---|---|---|
| MOPCON PR #27 current | `5fe21304aadbef67a9f5b3d983f21a6a1f6a0b60` | draft; exact-head local type-check clean; fresh review requested |
| MOPCON case E2E predecessor | `fe63850aa1371126c159d3a64b044ee7b1db6fe2` | local auth/private-case E2E verified |
| Platform PR #53 current | `56bfd1d31b8a5964f5de870b59f5e8c3568b418b` | draft; Vercel success; current-head local route tests pending; fresh review requested |
| Platform local-reader predecessor | `062ad630ad3c795dd27c2e84d251880b8c615c3f` | authenticated local production-ledger read path verified |
| Platform unauthenticated-preview predecessor | `b78152011c81c4d4fa2d09a3c9f1c7e70f9fd78f` | unauthenticated preview 401/no projection observed |

If a head moves, its exact-head statement becomes historical.

---

## 16. Explicitly not authorized / not claimed

This candidate record does not authorize or claim:

- merge of MOPCON PR #27;
- merge of Platform PR #53;
- merge or canonization of this CORE-HUB candidate;
- application of the new Platform UUID migration to production;
- production promotion of the case reader;
- MOPCON production deployment;
- Oracle/runtime provider promotion;
- dispatch/routing/governance authority transfer to `mirrornode-agent-runtime`;
- autonomous case advancement;
- release approval;
- customer delivery;
- customer-data mutation;
- Supabase/Stripe credential transfer into MOPCON;
- Osiris Scale Ready status;
- full `ORACLE ONLINE v0.1` completion.

---

## 17. Candidate disposition

**MOPCON `5fe213...`: exact-head local type-check clean; independent re-review pending.**

**Platform `56bfd1d...`: Vercel exact-head success; corrected UUID/pagination implementation; local route tests and independent re-review pending.**

**Last observed customer-case distribution: 3 paid — 2 `intake_complete`, 1 `fulfillment_started`; derived customer-case Operator Debt at that observation = 2.**

**Projected mutation state: DISABLED. Customer mutation / release / delivery: NOT AUTHORIZED.**

**Governed runtime implementation: active locally; durable/authenticated `ORACLE ONLINE v0.1` remains incomplete; routing/governance authority is not granted by this record.**

**Canon status: CANDIDATE ONLY.** It becomes eligible for canonical promotion only after the required **Ptah evaluation + explicit Operator ratification + promotion record**. Ordinary review or merge alone is insufficient.
