# MIRRORNODE-00 — Operational Addendum

**Date:** 2026-09-01  
**Status:** DRAFT CURRENT-STATE RECORD  
**Authority effect:** NONE  
**Current-state precedence:** supersedes `canon/dossiers/2026-08/MIRRORNODE-00-CLOSEOUT-2026-08-22.md` only for questions of present operational state  
**Historical integrity:** does not rewrite any earlier dossier, review, Council disposition, exact-head attestation, or authority grant

## Purpose

This addendum records the operational state reached during the MOPCON / Oracle / Osiris integration session spanning 2026-08-31 through 2026-09-01.

It exists to prevent implementation truth from drifting away from governance while preserving five distinct labels:

- **observed** — directly seen in runtime, database, build, or endpoint evidence;
- **implemented** — code exists on an identified branch/head;
- **verified** — the stated behavior was exercised successfully in the stated scope;
- **held** — intentionally prevented from advancing pending evidence, authority, security, or review;
- **not authorized** — no merge, deployment, provider promotion, customer mutation, release, or delivery authority is implied.

This document is a current-state record, not a ratification instrument.

---

## 1. Current operating shape

MIRRORNODE is converging on one private Operator cockpit with bounded modules rather than separate ad hoc interfaces.

### MOPCON

Repository: `mirrornode/mirrornode-operator-console`

Current feature-branch modules include:

- system/runtime evidence;
- governed Oracle/runtime plan flow;
- Operator Debt;
- commercial readiness;
- Osiris fulfillment state;
- authenticated private case projection;
- architecture/workstream state;
- permitted-next-action semantics.

Operating principle:

> Different types of work, different modules, same Operator interface.

Intended shell:

- top — current lane, target, runtime state, Operator Debt;
- left — architecture, docs, evidence, context;
- center — active task module;
- right — runtime, traces, plans, approvals, blockers;
- bottom — permitted next actions.

Functional integration and authority correctness remain higher priority than visual polish.

---

## 2. MOPCON exact-head state and verification lineage

Draft PR: `mirrornode/mirrornode-operator-console#27`  
Branch: `feat/local-runtime-console-2026-08-31`  
Current exact head: `0650d0df78dd803856ed1bf2163986db794444c3`  
PR state at this record: **open / draft / mergeable / unmerged**

### Last exact head with local case E2E proof

`fe63850aa1371126c159d3a64b044ee7b1db6fe2`

Observed and verified at that head:

- `npm run type-check` / `tsc --noEmit` passed;
- MOPCON listened on `127.0.0.1:3000`;
- unauthenticated `/api/private/cases` returned HTTP `401`;
- Operator authentication returned HTTP `200`;
- authenticated `/cases` rendered live cases;
- projection state was `available`;
- mutation state was `disabled`;
- three paid cases were visible through the minimum private projection.

### Later exact-head type-check proof

`5bb06891036c7871f60ff90df269e96c98e74004`

The Operator locally fetched that exact head and ran:

`npm run type-check` -> `tsc --noEmit`

The command completed without a TypeScript error on 2026-09-01.

This proves exact-head type correctness at `5bb0689...`; it does not silently transfer E2E proof from `fe63850...` or type-check proof to a later head.

### Changes after the type-checked head

The current head `0650d0d...` contains bounded truth/state reconciliation after `5bb0689...`:

1. the system fulfillment endpoint no longer claims the private case projection is held pending an authenticated private-data boundary;
2. the Oracle evidence envelope was advanced to `mopcon.local-evidence.v0.5`, recognizing that the authenticated case boundary exists while deliberately excluding private case rows from Oracle evidence envelopes;
3. the live workstream registry retired obsolete next actions to “add authenticated private case projection” and “independent case identity”; the remaining Osiris gap is downstream lifecycle binding to the ledger UUID.

The current head therefore **must not inherit exact-head type-check or review status by implication**. Fresh current-head type-check and exact-head review remain required.

No merge or deployment has occurred.

---

## 3. Operator authentication boundary

MOPCON now has a local single-Operator authentication shell.

Implemented properties:

- `MOPCON_OPERATOR_PASSWORD` is server/local only;
- `MOPCON_SESSION_SECRET` signs the Operator session;
- session cookie is HttpOnly;
- SameSite is `strict`;
- production cookie mode is Secure;
- session TTL is bounded;
- missing auth configuration fails closed;
- password verification uses a timing-safe comparison path;
- `/cases` and `/api/private/cases` require a valid Operator session;
- secrets are ignored by Git and are not returned by the APIs.

This is acceptable as a **local single-Operator v0.1 boundary**. It is not a complete remote identity system. Before network exposure or state-changing remote operations, stronger identity/revocation, rate limiting, CSRF/re-auth controls, and remote transport protections remain required.

---

## 4. Local network boundary

The session used these loopback bindings:

| Surface | Binding | Role |
|---|---|---|
| MOPCON | `127.0.0.1:3000` | private Operator cockpit |
| Platform case reader | `127.0.0.1:3002` | server-side minimum projection bridge |
| Governed Oracle/runtime | `127.0.0.1:8000` | reasoning/runtime |

MOPCON `dev` and `start` now bind loopback by default. Its development origin configuration was narrowed for loopback use. The Platform reader was explicitly started on loopback.

These controls reduce accidental LAN exposure. They do not constitute a complete remote security architecture.

---

## 5. Platform read-only Osiris case projection

Draft PR: `mirrornode/mirrornode-platform#53`  
Branch: `feat/mopcon-readonly-case-projection-2026-08-31`  
Exact head: `062ad630ad3c795dd27c2e84d251880b8c615c3f`  
Base: `main` at `f47b237cce4fcf0edf495c2f64b2d371d3b08103`  
PR state: **open / draft / mergeable**  
Vercel exact-head build status: **success**

### Boundary design

MOPCON does **not** receive a Supabase service-role credential.

Platform retains the Supabase service-role authority server-side and exposes one GET-only endpoint:

`/api/internal/mopcon/cases`

The endpoint requires a high-entropy bearer read secret and returns only the minimum Operator view.

Projected fields:

- independent case UUID;
- masked customer identity;
- payment state;
- fulfillment state;
- created/updated timestamps;
- intake-present state and submission timestamp;
- artifact count;
- Operator-review timestamp;
- fulfillment-start timestamp;
- delivered timestamp.

Deliberately omitted:

- Stripe session/customer identifiers;
- raw intake narrative;
- artifact URLs;
- Supabase credentials;
- secrets;
- mutation, release, or delivery authority.

Response caching is disabled with `cache-control: no-store`.

### Verification

The route was observed to fail closed with HTTP `401` without authorization and no customer data. The exact Platform head passed its Vercel build. The local loopback reader at the same branch head was then exercised against the production ledger and consumed successfully by authenticated MOPCON.

Production promotion of this reader remains **held** pending fresh exact-head review and a separately approved secret/deployment strategy.

---

## 6. Live Osiris case evidence

A read-only aggregate database query and the authenticated MOPCON projection agreed on the same distribution:

- **3 paid Osiris cases total**;
- **2** at `intake_complete`;
- **1** at `fulfillment_started`.

MOPCON rendered those records with masked customer identity and minimum lifecycle metadata.

During verification:

- no raw intake narrative was printed;
- no full customer identity was printed;
- no Stripe identifier was printed;
- no artifact URL was printed;
- no production row was mutated.

Current proven projection state: **AVAILABLE**  
Current proven mutation state: **DISABLED**

---

## 7. Case identity correction

A previous MOPCON description incorrectly treated Stripe identity as effectively doubling as case identity.

That statement is stale.

`guest_audit_purchases` already has an independent UUID `id`; the minimum projection exposes it as `case_id`.

Current interpretation:

- ledger UUID = candidate canonical first-dollar case identity;
- Stripe IDs = payment identity/evidence only;
- remaining structural gap = binding evidence, findings/deliverable versions, release approval, and delivery receipt to that case UUID.

The MOPCON fulfillment registry and current workstream state now reflect this correction.

---

## 8. Operator Debt and NOW

Operator Debt means:

> the count of items that cannot legitimately advance until the Operator acts.

Working states:

- `operator_required`;
- `execution_active`;
- `blocked_elsewhere`;
- `watch`;
- `parked`.

Only `operator_required` contributes to Operator Debt.

### Derived customer-case debt

The live case projection shows:

- two paid cases at `intake_complete` without recorded Operator review;
- one case at `fulfillment_started` with Operator review recorded.

Under the current manual fulfillment contract, the two `intake_complete` cases cannot legitimately enter fulfillment until Operator review.

**Derived live customer-case Operator Debt = 2.**

This is a derived operational truth from the live ledger plus the fulfillment contract. It is **not yet aggregated into the MOPCON `NOW` home surface**.

Intended NOW sources are limited to genuinely Operator-blocked items, including:

- customer case review;
- release approval;
- runtime approval;
- exact-head PR/review disposition;
- security disposition;
- commercial/public-promise decisions;
- incidents or degraded authority requiring explicit disposition.

Each NOW item should expose:

- WHAT needs the Operator;
- WHY it cannot advance;
- AGE;
- IMPACT;
- EVIDENCE;
- smallest legitimate ACTION.

Work that can legitimately continue without the Operator does not belong in Operator Debt.

### Superseded static watch surface

MOPCON PR #25 (`feat/mopcon-mobile-command-center-v0-1`) was closed **unmerged** on 2026-09-01 as superseded by the live cockpit in PR #27.

Its static/manual watch entries and pre-customer assumptions remain historical provenance but are no longer current operating truth. No branch history was deleted and no code from PR #25 was merged by that disposition.

The current live workstream registry contains no active `watch` workstream entries at this capture; future watch items should be derived from current evidence rather than resurrected from the static snapshot.

---

## 9. Oracle / governed runtime

Current governed runtime model remains:

`plan -> explicit Operator approve -> execute -> trace`

The local chain has previously been verified end-to-end as:

browser -> MOPCON -> runtime proxy -> governed runtime -> model -> trace -> MOPCON.

MOPCON supplies bounded server-side evidence context rather than asking Oracle to invent host/system state.

The target milestone remains:

`ORACLE ONLINE v0.1 — Durable Advisory Runtime`

It is **not complete**.

Known remaining gaps:

- plan storage remains in-memory;
- trace durability is insufficient for restart/serverless continuity;
- runtime-native remote authentication is incomplete;
- local reachability is not equivalent to durable authenticated production service;
- legacy Vercel `oracle` projects are not authority for the current governed runtime.

Runtime approval does not imply repository write, merge, deployment, or provider-promotion authority.

---

## 10. Evidence model

MOPCON distinguishes at least:

- observed;
- unreachable;
- unknown;
- registered;
- declared;
- authenticated private-case state as a separately gated class.

The current runtime evidence envelope is `mopcon.local-evidence.v0.5`.

The evidence adapter is server-side and avoids secrets. The runtime proxy adds a bounded MOPCON evidence envelope for Oracle work while preserving the user-facing objective separately.

The existence of the authenticated private-case boundary does **not** mean private customer rows belong in Oracle context. Private purchase/intake rows remain excluded from the Oracle evidence envelope and stay behind the Operator-session-gated case surface unless separately authorized.

Evidence projection must not be treated as canonical-state invention.

---

## 11. Commercial spine

Current commercial progression recorded in MOPCON:

1. **Project Archaeologist** — discovery / lead generation; planned `$5–$29`.
2. **Osiris Audit** — current bounded `$149` entry offer.
3. **MOPCON Secure** — recurring control / observation / authority visibility; price TBD.
4. **Assurance Sprint** — material remediation / implementation; planned `$3.5k+`.
5. **Enterprise Control Plane** — custom / parked.

### MOPCON Secure boundary

**IN:** recurring observation, authority visibility, evidence/state tracking, drift detection, alerts, policy/control configuration, Operator escalation.

**OUT:** bespoke remediation, architecture redesign, code changes, migrations, provider integration, material customer-system changes, open-ended consulting.

OUT work belongs to Assurance Sprint. MOPCON Secure must not silently absorb bespoke implementation/consulting.

---

## 12. Osiris fulfillment spine

Current working lifecycle:

1. Purchase — production wired.
2. Intake — production wired.
3. Case Bound — durable partial.
4. Evidence — missing dedicated durable state.
5. Findings — missing dedicated durable state.
6. Operator Release — missing dedicated durable release receipt.
7. Delivery — durable partial.
8. Delivery Receipt — missing immutable effect receipt.

Current ledger states:

`intake_pending`, `intake_complete`, `fulfillment_started`, `delivered`, `paused`, `refunded`.

Important authority distinctions:

- `operator_reviewed_at` = pre-fulfillment checkpoint, not a release approval receipt;
- `delivered_at` = delivery timestamp, not proof of the exact approved artifact/version delivered;
- live case projection = read-only visibility, not fulfillment authority.

Remaining scale blockers:

- case-bound versioned evidence records;
- case/evidence-bound findings or deliverable versions;
- exact-version Operator release approval;
- immutable delivery receipt binding case, artifact/version/hash, approval, destination, and effect;
- fail-closed behavior on stale or incomplete authority/evidence.

The private case projection itself is now **locally verified read-only**. Production promotion remains held.

---

## 13. Public-offer / methodology drift

An unresolved commercial-contract drift remains:

- public Platform sells **Osiris Audit v1** at `$149`;
- current `osiris-audit` methodology defines **Structural Scan v1** as a distinct `$149` entry engagement before the larger Agent Authority Audit.

MOPCON must not silently choose a new customer promise.

Current disposition:

**OPERATOR REVIEW REQUIRED before storefront copy change or fulfillment scaling.**

This does not block bounded implementation work that leaves the public promise unchanged.

---

## 14. Security and dependency debt discovered

During local Platform worktree installation, `npm ci` reported **6 high-severity vulnerabilities**.

Current classification:

- observed package-manager finding;
- exact package/path/reachability details not yet triaged in this record;
- no claim is made that the findings are exploitable in the deployed path;
- no `npm audit fix` was run;
- blind dependency mutation was intentionally avoided during the authority-boundary verification.

Required next action: bounded dependency audit, exact reachability classification, then dedicated remediation with regression testing.

---

## 15. Explicitly not authorized / not claimed

Nothing in this session or addendum authorizes or claims:

- merge of MOPCON PR #27;
- merge of Platform PR #53;
- merge of this CORE-HUB source-of-truth branch;
- production promotion of the case projection;
- production deployment of MOPCON;
- Oracle/runtime provider promotion;
- autonomous case advancement or fulfillment start;
- release approval;
- customer delivery;
- customer-data mutation;
- Supabase or Stripe credential transfer into MOPCON;
- private case rows in the Oracle evidence envelope;
- raw customer intake in the default case table;
- Osiris Scale Ready status;
- full `ORACLE ONLINE v0.1` completion;
- independent exact-head review of the current MOPCON feature head.

---

## 16. Exact-head anchors

| Surface | Exact head | State |
|---|---|---|
| MOPCON PR #27 — current | `0650d0df78dd803856ed1bf2163986db794444c3` | draft; stale live claims reconciled; fresh current-head type-check/review required |
| MOPCON — latest exact type-check | `5bb06891036c7871f60ff90df269e96c98e74004` | `npm run type-check` / `tsc --noEmit` passed locally |
| MOPCON — last auth/case E2E-verified predecessor | `fe63850aa1371126c159d3a64b044ee7b1db6fe2` | local type-check + auth/case E2E verified |
| Platform PR #53 | `062ad630ad3c795dd27c2e84d251880b8c615c3f` | draft; Vercel exact-head build success; local case reader operational |
| Platform PR #53 base | `f47b237cce4fcf0edf495c2f64b2d371d3b08103` | base at capture |
| Superseded MOPCON PR #25 | `9b46bd37b3c80d02c19959f925c7e59d5ec77af5` | closed unmerged; static watch snapshot retained as history only |

If any head moves, its exact-head statement becomes historical and must not be silently carried forward.

---

## 17. Current disposition

**LOCAL OPERATOR COCKPIT: OPERATIONALLY VERIFIED FOR READ-ONLY CASE VISIBILITY AT `fe63850...` IN THE STATED LOCAL SCOPE.**

**MOPCON TYPE-CHECK: VERIFIED AT `5bb0689...`.**

**CURRENT MOPCON HEAD `0650d0d...`: TRUTH-RECONCILED DRAFT; FRESH CURRENT-HEAD TYPE-CHECK AND EXACT-HEAD REVIEW REQUIRED.**

**STATIC WATCH SNAPSHOT PR #25: SUPERSEDED / CLOSED UNMERGED / HISTORY PRESERVED.**

**PLATFORM READ PROJECTION `062ad630...`: DRAFT; LOCAL READ PATH OPERATIONAL; PRODUCTION PROMOTION HELD.**

**LIVE CUSTOMER-CASE OPERATOR DEBT: 2 — DERIVED; NOT YET AGGREGATED INTO `NOW`.**

**CUSTOMER CASE MUTATION / RELEASE / DELIVERY: NOT AUTHORIZED.**

**ORACLE ONLINE v0.1: INCOMPLETE — DURABILITY/AUTHENTICATION GAPS REMAIN.**

This is the current operational source-of-truth candidate until superseded by a later dated record. It becomes mainline canon only if separately reviewed and merged under normal CORE-HUB authority.