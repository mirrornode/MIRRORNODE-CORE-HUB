# MIRRORNODE-00 — Operational Addendum

**Date:** 2026-09-01  
**Status:** DRAFT CURRENT-STATE RECORD  
**Authority effect:** NONE  
**Supersedes for current-state questions:** `canon/dossiers/2026-08/MIRRORNODE-00-CLOSEOUT-2026-08-22.md`  
**Does not rewrite:** any earlier dossier, review, Council disposition, or exact-head attestation

## Purpose

This addendum records the current operational state reached during the MOPCON / Oracle / Osiris integration session spanning 2026-08-31 through 2026-09-01.

It exists to prevent current implementation truth from drifting away from MIRRORNODE's governance record while preserving strict distinctions between:

- **observed** — directly seen in runtime, database, build, or local endpoint evidence;
- **implemented** — code exists on an identified branch/head;
- **verified** — the stated behavior was exercised successfully in the stated scope;
- **held** — intentionally prevented from advancing pending an authority, evidence, security, or review condition;
- **not authorized** — no merge, deployment, provider promotion, customer mutation, release, or delivery authority is implied by this record.

This document is a current-state record, not a ratification instrument.

---

## 1. Current operating shape

MIRRORNODE is currently converging on one private Operator cockpit with bounded modules rather than separate ad hoc interfaces.

### Private Operator surface

**MOPCON** — `mirrornode/mirrornode-operator-console`

Current functional modules on the active feature branch include:

- system/runtime evidence;
- governed Oracle/runtime plan flow;
- Operator Debt model;
- commercial readiness;
- Osiris fulfillment state;
- authenticated private case projection;
- architecture and workstream state;
- permitted-next-action / action-rail semantics.

The intended operating principle is:

> Different types of work, different modules, same Operator interface.

The intended MOPCON shell remains:

- top: current lane / target / runtime state / Operator Debt;
- left: architecture / docs / evidence / context;
- center: active task module;
- right: runtime / logs / plans / approvals / blockers;
- bottom: permitted next actions.

This shell is partially implemented. Layout polish is explicitly lower priority than functional integration and authority correctness.

---

## 2. MOPCON implementation state

### Active draft PR

Repository: `mirrornode/mirrornode-operator-console`  
PR: `#27` — `feat: assemble local Operator cockpit and read-only Osiris cases`  
Branch: `feat/local-runtime-console-2026-08-31`  
Exact head recorded for this addendum: `fe63850aa1371126c159d3a64b044ee7b1db6fe2`  
PR state at capture: **open / draft / mergeable**

The PR remains intentionally unmerged.

### Local validation at exact head

Observed locally at `fe63850aa1371126c159d3a64b044ee7b1db6fe2`:

- `npm run type-check` / `tsc --noEmit` passed;
- MOPCON was listening on `127.0.0.1:3000`;
- the authenticated `/cases` surface rendered the live read-only case projection;
- unauthenticated `/api/private/cases` returned HTTP `401`;
- authenticated Operator session returned HTTP `200`;
- private case projection reported `available`;
- projected mutation authority reported `disabled`.

No repository merge, production deployment, customer mutation, release, or delivery was performed.

---

## 3. MOPCON Operator authentication boundary

MOPCON now has a local single-Operator authentication shell.

Implemented properties:

- `MOPCON_OPERATOR_PASSWORD` is local/server-side only;
- `MOPCON_SESSION_SECRET` signs the Operator session;
- session cookie is HttpOnly;
- SameSite is strict;
- production cookie mode is Secure;
- session TTL is bounded;
- missing auth configuration fails closed;
- password verification uses SHA-256 plus timing-safe comparison;
- private `/cases` and `/api/private/cases` require a valid Operator session;
- secrets are ignored by Git and are not returned by API responses.

Current scope caveat:

This is acceptable as a **local single-Operator v0.1 boundary**. It is not a complete remote identity system. Before network exposure or higher-authority write operations, additional hardening remains required, including stronger identity/revocation, rate limiting, explicit CSRF/re-auth controls for state-changing actions, and remote transport protections.

---

## 4. Local network boundary

Current local intended bindings:

| Surface | Binding | Role |
|---|---|---|
| MOPCON | `127.0.0.1:3000` | private Operator cockpit |
| Platform read projection | `127.0.0.1:3002` | local server-side read bridge to production ledger |
| Agent runtime / Oracle | `127.0.0.1:8000` | governed reasoning/runtime |

MOPCON `dev` and `start` scripts were changed to bind loopback by default rather than all interfaces.

MOPCON `allowedDevOrigins` was narrowed for loopback development.

The Platform read-projection worktree is also started explicitly with `--hostname 127.0.0.1 --port 3002`.

These bindings reduce accidental LAN exposure. They do not by themselves constitute a complete remote security architecture.

---

## 5. Read-only Osiris case projection

### Platform draft PR

Repository: `mirrornode/mirrornode-platform`  
PR: `#53` — `feat: add MOPCON read-only Osiris case projection`  
Branch: `feat/mopcon-readonly-case-projection-2026-08-31`  
Exact head recorded for this addendum: `062ad630ad3c795dd27c2e84d251880b8c615c3f`  
Base: `main` at `f47b237cce4fcf0edf495c2f64b2d371d3b08103`  
PR state at capture: **open / draft / mergeable**  
Exact-head Vercel status at capture: **success**

### Projection architecture

MOPCON does **not** receive a Supabase service-role credential.

The Platform server retains the existing Supabase service-role authority and exposes a separate GET-only endpoint:

`/api/internal/mopcon/cases`

The endpoint requires a high-entropy bearer read secret and returns only a minimum Operator projection.

Projected fields:

- independent case UUID;
- masked customer identity;
- payment state;
- fulfillment state;
- created/updated timestamps;
- intake-present state;
- intake-submitted timestamp;
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
- mutation/release/delivery authority.

Response caching is disabled with `cache-control: no-store`.

### Fail-closed evidence

Preview behavior was directly exercised before the final config-only Turbopack-root correction and returned:

- HTTP `401 Unauthorized` without the read secret;
- `cache-control: no-store`;
- no customer data.

The current exact Platform head also passed its Vercel build after the Turbopack-root correction.

The current exact implementation was then exercised locally against the production ledger through the loopback bridge.

---

## 6. Live Osiris case evidence

A read-only aggregate database query and the authenticated MOPCON projection both established the same current case distribution:

- **3 paid Osiris cases total**;
- **2** at `intake_complete`;
- **1** at `fulfillment_started`.

The MOPCON case screen rendered those three records with masked customer identity and minimum lifecycle metadata.

No raw intake narrative, full customer identity, Stripe identifiers, or artifact URLs were printed during verification.

No production row was mutated by this verification flow.

### Current projection state

`AVAILABLE`

### Current mutation state

`DISABLED`

---

## 7. Case identity correction

A previous MOPCON fulfillment description incorrectly treated the Stripe session as effectively doubling as case identity.

That is stale.

`guest_audit_purchases` already contains an independent UUID `id`, and the current projection exposes that value as `case_id`.

Current interpretation:

- case UUID = candidate canonical case identity;
- Stripe session/customer identifiers = payment identity/evidence only;
- the remaining structural gap is not creation of a case identifier;
- the remaining gap is **formal binding of evidence, findings/deliverable versions, release approval, and delivery receipt to the case UUID**.

MOPCON fulfillment source data was corrected accordingly on head `fe63850aa1371126c159d3a64b044ee7b1db6fe2`.

---

## 8. Operator Debt

Operator Debt is a first-class MOPCON concept defined as:

> the count of items that cannot legitimately advance until the Operator acts.

Canonical working states:

- `operator_required`;
- `execution_active`;
- `blocked_elsewhere`;
- `watch`;
- `parked`.

Only `operator_required` contributes to Operator Debt.

### Current derived case debt

The live case projection currently shows:

- 2 paid cases at `intake_complete` without recorded Operator review;
- 1 case already at `fulfillment_started` with an Operator review timestamp.

Under the current manual Osiris fulfillment boundary, the two `intake_complete` cases cannot legitimately enter fulfillment until Operator review.

Therefore:

**Derived live customer-case Operator Debt = 2.**

Important distinction:

This count is currently a **derived operational truth from the live case state and fulfillment contract**. It is not yet fully wired into the MOPCON `NOW` aggregate/home surface at the time of this addendum.

### Intended NOW sources

The Operator Debt / NOW surface should eventually aggregate only genuinely Operator-blocked items from:

- customer case review;
- release approval;
- runtime approval;
- exact-head PR/review disposition;
- security disposition;
- commercial/public-promise decisions;
- incidents or degraded authority requiring explicit disposition.

Each NOW item should answer:

- WHAT needs the Operator;
- WHY it cannot advance;
- AGE;
- IMPACT;
- EVIDENCE;
- smallest legitimate ACTION.

---

## 9. Oracle / governed runtime state

Current runtime model remains the governed:

`plan -> explicit Operator approve -> execute -> trace`

The reviewed repo-steward stack remains bounded to runtime eligibility and does not create GitHub mutation, merge, deploy, or repository-write authority.

The current local Oracle/runtime chain has previously been verified end-to-end as:

browser -> MOPCON -> runtime proxy -> governed runtime -> model -> trace -> MOPCON.

MOPCON adds server-side evidence context rather than asking the Oracle to invent host/system state.

### Oracle Online status

The target milestone remains:

`ORACLE ONLINE v0.1 — Durable Advisory Runtime`

Current status is **not fully achieved**.

Known remaining gaps:

- plan storage remains in-memory;
- trace durability is not yet sufficient for serverless/restart continuity despite local trace logs;
- runtime-native explicit remote authentication is incomplete;
- current local reachability is not equivalent to durable authenticated production service;
- legacy Vercel `oracle` projects are not the authority for the current governed Oracle runtime.

No provider promotion is implied by this addendum.

---

## 10. Evidence architecture

MOPCON now distinguishes at least:

- observed;
- unreachable;
- unknown;
- registered;
- declared.

The system evidence adapter is server-side and avoids secrets.

The runtime proxy appends a bounded MOPCON evidence envelope to Oracle objectives and strips that envelope from the user-facing returned objective while preserving the evidence-bound runtime/trace record.

Current evidence includes runtime/system state plus declared commercial and fulfillment spine state.

This is evidence projection, not canonical-state invention.

---

## 11. Commercial spine

Current commercial progression recorded in MOPCON:

1. **Project Archaeologist** — discovery / lead generation; planned `$5–$29`.
2. **Osiris Audit** — current bounded `$149` entry offer.
3. **MOPCON Secure** — recurring control / observation / authority visibility; price not yet locked.
4. **Assurance Sprint** — material remediation / implementation; planned `$3.5k+`.
5. **Enterprise Control Plane** — custom / parked.

### MOPCON Secure boundary

Approved working boundary:

**IN:** recurring observation, authority visibility, evidence/state tracking, drift detection, alerts, policy/control configuration, Operator escalation.

**OUT:** bespoke remediation, architecture redesign, code changes, migrations, provider integration, material customer-system changes, open-ended consulting.

OUT work belongs to Assurance Sprint.

MOPCON Secure must not silently absorb Lane 4 consulting.

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

The existing ledger states remain:

- `intake_pending`;
- `intake_complete`;
- `fulfillment_started`;
- `delivered`;
- `paused`;
- `refunded`.

`operator_reviewed_at` is a pre-fulfillment checkpoint, not a release approval receipt.

`delivered_at` records delivery timing but does not prove which exact approved artifact/version was delivered.

### Remaining scale blockers

- bind evidence bundles to case UUID and immutable source/version identity;
- bind findings/deliverable versions to case/evidence versions;
- create explicit exact-version Operator release approval;
- create immutable delivery receipt binding case, exact artifact/version/hash, approval, destination, timestamp/effect;
- preserve fail-closed behavior on stale or incomplete authority/evidence.

---

## 13. Public-offer / methodology drift

An unresolved commercial-contract drift remains recorded:

- the public Platform sells **Osiris Audit v1** at `$149`;
- the current `osiris-audit` methodology repo defines **Structural Scan v1** as a distinct `$149` entry engagement before the larger Agent Authority Audit.

MOPCON must not silently choose a new customer promise.

Current disposition:

**OPERATOR REVIEW REQUIRED before storefront copy change or fulfillment scaling.**

This drift does not prevent bounded implementation work that does not alter the public promise.

---

## 14. Security and dependency debt discovered in this session

During local Platform worktree installation:

`npm ci` reported **6 high-severity vulnerabilities**.

Current classification:

- observed package-manager finding;
- details not yet triaged in this addendum;
- no claim is made that the findings are exploitable in the deployed path;
- no `npm audit fix` was run;
- blind dependency mutation was intentionally avoided during the authority-boundary verification.

Required next action:

Run a bounded dependency audit, classify exact packages/paths/reachability, then remediate on a dedicated branch with regression testing rather than accepting automatic broad upgrades.

---

## 15. Explicitly not authorized / not claimed

Nothing in this session or addendum authorizes or claims:

- merge of MOPCON PR #27;
- merge of Platform PR #53;
- production promotion of the MOPCON case projection;
- production deployment of MOPCON;
- Oracle/runtime provider promotion;
- autonomous case advancement;
- autonomous fulfillment start;
- release approval;
- customer delivery;
- customer-data mutation;
- Supabase credential transfer into MOPCON;
- Stripe credential transfer into MOPCON;
- raw customer intake display in the default case table;
- Scale Ready status for Osiris;
- full `ORACLE ONLINE v0.1` completion;
- independent exact-head review of the current MOPCON accumulated feature head.

---

## 16. Current exact-head anchors

| Surface | Exact head | State |
|---|---|---|
| MOPCON PR #27 | `fe63850aa1371126c159d3a64b044ee7b1db6fe2` | draft; local type-check + auth/case E2E verified |
| Platform PR #53 | `062ad630ad3c795dd27c2e84d251880b8c615c3f` | draft; Vercel exact-head build success; local case reader operational |
| Platform base | `f47b237cce4fcf0edf495c2f64b2d371d3b08103` | current PR base recorded at capture |

If either head moves, any exact-head statement in this addendum becomes historical and must not be silently carried forward.

---

## 17. Current operational summary

### Verified now

- local MOPCON private Operator gate works;
- unauthenticated private case access fails closed;
- MOPCON is loopback-bound in the verified local configuration;
- local Platform case bridge is loopback-bound;
- Platform keeps the Supabase service-role credential server-side;
- MOPCON receives a minimum read-only case projection;
- three real paid Osiris cases are visible through the authenticated cockpit;
- projected mutation remains disabled;
- current case-state distribution is 2 `intake_complete`, 1 `fulfillment_started`;
- derived customer-case Operator Debt is 2;
- case identity is an independent UUID, not Stripe identity;
- MOPCON exact head passes local TypeScript type-check;
- Platform exact head passes Vercel build.

### Implemented but not yet promoted

- accumulated MOPCON cockpit modules on PR #27;
- Platform read-only MOPCON case endpoint on PR #53;
- current commercial and fulfillment registry refinements;
- case projection UI;
- Operator auth shell;
- loopback default MOPCON dev/start behavior.

### Held / next

- aggregate live Operator Debt into MOPCON `NOW`;
- inspect the two pending Osiris case reviews through a deliberate case-detail workflow;
- preserve read-only boundary until a separate governed mutation design exists;
- perform fresh exact-head review before merge eligibility;
- triage the 6 high npm findings;
- reconcile Osiris `$149` public-offer/methodology naming drift;
- add durable evidence/findings/release/delivery-receipt records;
- complete Oracle durability/authentication work before claiming `ORACLE ONLINE v0.1`.

---

## 18. Disposition

**CURRENT LOCAL OPERATOR COCKPIT: OPERATIONALLY VERIFIED FOR READ-ONLY CASE VISIBILITY IN THE STATED LOCAL SCOPE.**

**CURRENT MOPCON / PLATFORM CHANGES: REVIEW-HELD DRAFT IMPLEMENTATIONS.**

**CUSTOMER CASE MUTATION / RELEASE / DELIVERY: NOT AUTHORIZED.**

**ORACLE ONLINE v0.1: INCOMPLETE — DURABILITY/AUTHENTICATION GAPS REMAIN.**

**LIVE CUSTOMER-CASE OPERATOR DEBT: 2 (DERIVED; NOT YET AGGREGATED INTO `NOW`).**

This is the source-of-truth candidate for current operational state until superseded by a later dated record. It becomes mainline source-of-truth only if separately reviewed and merged under the repository's normal authority process.
