# MIRRORNODE Consolidation Spine — 2026-09-06

Status: DRAFT CANDIDATE — current cleanup and continuity register. This file is a dated control surface, not self-promoted canon.

## Objective

Collapse the current estate into a small, legible operating model that preserves successful engineering work while stopping stale context, duplicate surfaces, unresolved roles, and non-revenue expansion from consuming attention.

Priority order:

```text
1. truthful source of truth
2. revenue-capable Osiris loop
3. reproducible proof
4. business operating readiness
5. GitHub Developer Program / credibility leverage
6. productized consulting
7. passive/recurring product experiments
8. deferred architecture
```

## Classification model

Every repo, PR, cloud project, database, surface, and workflow should receive one current disposition:

- ACTIVE — required for the present operating/revenue loop.
- SUPPORT — required evidence, governance, infra, or continuity dependency.
- VERIFY — current role/state must be re-observed before disposition.
- PARK — valid work intentionally held with explicit restart condition.
- SUPERSEDE — preserved history replaced by a newer artifact.
- RETIRE — no longer part of the intended estate.
- EXPERIMENTAL — isolated work with no implied production/runtime authority.

Every current-state record must distinguish implementation, verification, merge, deployment, activation, authorization, and canon status.

### Inventory vs disposition

Inventory and disposition are separate artifacts.

Inventory answers:

```text
what exists
where it exists
what it connects to
known / unknown
```

Disposition answers:

```text
what happens next
who owns the decision
restart/retirement condition
```

Do not mutate, delete, pause, or "clean up" a surface merely because inventory evidence looks stale, duplicated, insecure, or surprising. Discovery is evidence collection; disposition is a deliberate lifecycle decision.

### No hidden work

No ACTIVE work may exist without:

```text
domain
owner_seat
exact_subject
next_evidence_producing_action
```

Everything else is PARK, VERIFY, SUPERSEDE, RETIRE, SUPPORT, or EXPERIMENTAL with a recorded reason and restart condition.

## A. Source-of-truth cleanup

### CORE-HUB pre-consolidation observations (superseded by this PR where noted)

- `MASTER_INDEX.md` is append-only but materially behind the current estate. It contains only the older promotion record and should not be treated as a complete current operational registry.
- Pre-change: `CANONICAL_SOURCES.md` omitted several current surfaces. Resulting tree: it now routes current-state questions through the Estate Worktree and names the major current owning sources.
- Pre-change: `AGENTS.md` recorded unresolved routing from 2026-08-13. Resulting tree: current candidate routing is seat-based and the Lucian-centered registry is explicitly historical.
- Pre-change: `AGENTS_TODO.md` called for a reconciled registry. Resulting tree: the seat/authority and workstream registries satisfy that candidate reconciliation, pending review/promotion.
- PR #62 is a valuable 2026-09-01 candidate operational record but is already temporally superseded by later Osiris/GitHub-Ops/estate-worktree evidence. Preserve it as dated evidence; do not silently treat it as current truth.
- PR #63 / Estate Worktree is the current candidate continuity/control surface and should absorb the exact-subject, node-checkin, engineering-doctrine, and consolidation-register model before promotion.

### Target documentation hierarchy

```text
MASTER_INDEX.md
  -> promoted canonical decisions only

CANONICAL_SOURCES.md
  -> current owning sources and provider boundaries

estate/
  -> current machine/human operating register
  -> repo census
  -> active exact-head subjects
  -> state/disposition
  -> current connections/surfaces
  -> revenue register
  -> engineering doctrine

docs/continuity/
  -> dated historical handoffs and superseded snapshots
```

Do not erase historical documents to make current documentation look clean. Mark them historical/superseded and route current-state questions to the current register.

## B. Current live estate observations — 2026-09-06

### GitHub

Observed accessible repository census: 43 repositories.

Current key work:

| Subject | Current state | Disposition |
|---|---|---|
| `mirrornode-platform#54@f9365b8...` | MERGED via squash to `main@f68111b...`; hosted rollout remains separately unauthorized | ACTIVE revenue implementation / rollout HOLD |
| `CORE-HUB#63@<live GitHub PR head>` | open, non-draft, mergeable; self-head resolved from live PR metadata to avoid self-referential drift | ACTIVE / continuity control surface |
| `CORE-HUB#62@b7f593c...` | open, non-draft, dated 2026-09-01 operational truth candidate | SUPERSEDE as current; preserve history |
| `operator-console#29@4d4418b...` | draft, open | PARK unless required for first-dollar visibility |
| `MIRRORNODE-INFRA#7` | merged | SUPPORT / successful fail-closed hardening history |
| `MIRRORNODE-INFRA#8` | merged | SUPPORT / execution-entrypoint invariant |
| `MIRRORNODE-INFRA#6@22cbbeb...` | draft, open | VERIFY for supersession/closeout against #7/#8/current main |
| `mirrornode-github-ops#1@bd9479a...` | draft, open | SUPPORT / GitHub Developer Program + proof-audit foundation |
| `agent-runtime#6@c060546...` | open | PARK — Protected Relay not revenue-critical |
| `workspace#4@f1a1ab9...` | open | PARK — doctrine/research lane |

No PR number is valid as a subject without repository + exact head.

### Vercel

Live team observed:

```text
team: Mirrornode
slug: inphase
plan: hobby
projects observed: 25
```

The project list contains several likely duplicate, historical, or experimental surfaces, including multiple Oracle, Osiris UI, Rotan, and older hub/homepage variants.

Disposition required:

1. identify current production/public surfaces;
2. identify preview-only/support surfaces;
3. mark duplicates/historical projects;
4. confirm Git linkage and deployment authority;
5. retire or archive stale surfaces only after evidence capture.

Do not infer production from project existence.

Known high-value surfaces to verify first:

- `mirrornode-platform`
- `public` -> `mirrornode-parallax`
- `theia-core`
- `osiris`
- `osiris-ui` variants
- `mirrornode`
- `mirrornode-hub`
- Oracle variants

### Supabase

Two active healthy projects were observed:

#### 1. Mirrornode OS

- region: us-west-1
- PostgreSQL 17
- active/healthy
- 9 recorded migrations
- public tables observed:
  - subscriptions
  - guest_audit_purchases
  - khepri_arc_registry
  - khepri_witness_snapshots
  - khepri_ingestion_log
  - khepri_threshold_registry
- RLS enabled on all observed public tables.
- Current hosted database does not yet contain the pending PR #54 controlled-start migration by design.

Disposition: ACTIVE production data plane. All DDL changes require separate target authorization and verification.

#### 2. mirrornode-schema-reconciliation-replay

- active/healthy
- PostgreSQL 17
- 7 replay/test migrations
- one public `guest_audit_purchases` table
- observed rows: 0
- RLS is currently disabled on that table.

Disposition: VERIFY / likely test-only standby.

Security note: Supabase reports the disabled-RLS table as a critical advisory because anon/authenticated roles may have unrestricted table access if the project is reachable with a client key. Do not auto-enable RLS without deciding the intended test-access model; enabling RLS without policies can break the replay fixture. Preferred near-term disposition is to confirm whether the replay project is still needed, then pause/retire it or explicitly harden/isolate it.

## C. Local machine estate — census required

The cloud/repository estate is more current than the local-machine register.

Create one reproducible local census artifact that records, without secrets:

- repository path;
- remote URL;
- current branch;
- HEAD;
- dirty/clean state;
- ahead/behind state;
- active worktree list;
- Node/Python/Docker/Supabase/Vercel/gh versions;
- Docker engine availability;
- local Supabase stack state;
- Vercel project bindings;
- untracked build/test artifacts;
- stale worktrees;
- local-only branches not pushed;
- local environment variable names by presence only, never values.

Destination should be MIRRORNODE-INFRA or the Estate Worktree as a machine-generated dated receipt. The inventory mechanism should be retained; generated machine-specific output should remain dated evidence.

## D. Roles and authority

Current operating seats should be made explicit:

- Operator — final business/governance/merge/deploy/migration/live-mutation authority.
- Builder — bounded code edits only.
- Reviewer — independent semantic/adversarial inspection; no edits.
- Arbitrator — resolves disputed findings; no edits.
- Final Review Seat — read-only exact-head final review; no push/merge/deploy authority.
- Projector services — read-only normalized evidence.
- Executor services — narrowly authorized commands with receipts.

Retire the assumption that independent assurance necessarily means a second unrelated human GitHub identity. Preserve separation of functions while expressing platform controls in a way the actual single-Operator organization can satisfy honestly.

## E. Revenue operating spine

### Primary lane — Osiris Audit v1

State: ACTIVE.

Current intended flow:

```text
visitor
-> offer
-> checkout
-> verified payment
-> case
-> intake
-> explicit authorization
-> Operator accept/start
-> evidence
-> findings
-> remediation
-> human review
-> delivery
-> receipt
```

PR #54 is now merged at the exact cleared head. The single-Operator ruleset correction was applied and preserved controls were re-verified. Do not start another Osiris architecture cycle. Hosted migration, deployment, runtime verification, and live-case progression remain separate future operations requiring explicit authorization.

### Proof product

Use the GitHub Ops assessment as the first narrow proof audit.

The proof should produce a customer-legible sample report showing:

- repository/workflow/protection state;
- evidence provenance;
- false-PASS resistance;
- dependency/security visibility;
- Operator Debt;
- prioritized remediation;
- Permanent Control vs Accepted Debt;
- exact-head/config evidence.

### Productized consulting

Near-term consulting offers should reuse proven MIRRORNODE mechanisms rather than invent new services:

1. Osiris Audit v1 — bounded structural/evidence-chain audit.
2. GitHub AI/DevOps Assurance Review — repository/workflow/protection/provenance assessment.
3. Assurance Sprint — higher-touch remediation/implementation engagement.
4. Repository archaeology / project recovery — reconstruct current truth from drifted AI-assisted projects.
5. Controlled delivery / release-boundary review — payment-to-fulfillment, deploy, migration, and authority boundaries.

Every consulting offer should reuse one intake spine, one evidence model, and one report skeleton.

### Passive / low-touch income experiments

These are secondary to direct paid work and should be built only from already-proven internal assets:

- exact-head PR review checklist/template;
- GitHub ruleset starter pack for solo technical operators;
- AI-assisted repository evidence-chain workbook;
- project archaeology template;
- Operator Debt register/template;
- audit-report template pack;
- reusable local estate census/verification toolkit;
- future read-only GitHub check/app subscription when GitHub Ops is proven.

Do not build a marketplace/catalog before at least one artifact is proven useful in paid or design-partner work.

### Distribution

Near-term distribution should favor direct evidence-led outreach over broad speculative marketing.

Initial proof target:

- 5–10 design-partner/customer conversations;
- 2–3 completed paid or explicitly negotiated audits/assurance engagements;
- one polished sample GitHub Ops report;
- one credible before/after case story without exposing private customer data.

Broad Discord/Reddit/tech-news distribution becomes more efficient after the proof artifact and fulfillment loop are complete.

## F. GitHub Developer Program

Official current eligibility requires an integration in production or development using the GitHub API and a support email address.

MIRRORNODE already has a GitHub API integration in development through `mirrornode-github-ops`, so this should be treated as an ACTIVE credibility/application lane rather than a speculative future project.

Application-readiness checklist:

- GitHub API integration clearly documented;
- support email designated;
- public-safe product/integration description;
- minimal screenshots or sample report;
- explicit permissions/read-only boundary;
- support/privacy contact path;
- no claim that Developer Program membership implies security certification.

A GitHub App is a sensible product architecture because GitHub recommends Apps over OAuth apps for fine-grained permissions and short-lived tokens, but Developer Program eligibility itself should not be blocked on unnecessary app generalization if the current integration already satisfies the API-in-development requirement.

## G. Business operating readiness

Keep business systems out of technical canon except for non-secret state and ownership.

Maintain a separate private business-readiness register covering:

- business checking / reserve / tax compartments;
- Stripe live account and reconciliation;
- support/business email;
- bookkeeping cadence;
- customer terms/refund/privacy/data-retention language;
- invoice/receipt flow;
- customer contact/support workflow;
- tax/document storage;
- insurance and contract status where applicable;
- runway and recurring infrastructure costs.

No credentials, account numbers, or secret values belong in repository documentation.

## H. Standby register

Parked work is not abandoned. Every parked item gets a restart condition.

Recommended PARK now:

- broad MOPCON expansion beyond minimum first-dollar visibility;
- Protected Relay implementation;
- generalized Oracle multi-provider automation;
- generalized Repo Steward mutation authority;
- autonomous remediation/release;
- broad subscription monitoring;
- speculative multi-platform orchestration;
- nonessential visual/UI rebuilds;
- experimental games/art surfaces not tied to immediate revenue.

Restart only when a named customer, revenue proof, safety requirement, or blocking dependency earns the work.

## I. Weekly operating outputs

| Domain | Weekly output |
|---|---|
| Source of truth | One dated state snapshot with changed facts and unresolved unknowns |
| Revenue | Qualified conversations, offers sent, paid/negotiated engagements, and next decision dates |
| Business operations | One closed readiness item |
| Estate hygiene | One classified inventory increment |
| Continuity | Exact-head handoff records for all active subjects |
| Credibility | One public-safe proof or application artifact |
| Productization | Capture repetition; no speculative asset build |
| Research/architecture | New work enters only as PARK with restart condition |

Default calendar allocation for the next few weeks:

```text
50–60%  revenue / sample audits / proposals / conversations / fulfillment readiness
20–25%  business readiness + minimum delivery-protecting cleanup
10–15%  credibility / GitHub Developer Program / public-safe proof
<=10%   continuity + architecture preservation
```

Revenue is the scheduling authority. If work does not produce revenue, protect fulfillment, establish current truth, or create credible proof, it waits.

## J. Concurrent cleanup work

The consolidation sprint should run in parallel tracks with explicit ownership:

### Track 1 — Canon/continuity
- promote the Estate Worktree model after review;
- update CANONICAL_SOURCES;
- replace unresolved AGENTS registry with the seat/authority model;
- supersede stale operational snapshots;
- create one current-state routing page.

### Track 2 — Revenue
- resolve PR #54 ruleset mismatch;
- merge only the exact cleared head;
- separately verify/apply hosted DB migration with Operator authorization;
- smoke-test the paid-to-intake-to-Operator-start path;
- produce first GitHub Ops proof audit and sample report;
- begin direct design-partner outreach.

### Track 3 — Estate hygiene
- local machine census;
- Vercel 25-project classification;
- Supabase replay-project disposition;
- open-PR supersession/closeout sweep;
- remove stale worktrees/branches only after evidence capture.

### Track 4 — Credibility
- GitHub Developer Program packet;
- support email;
- public GitHub Ops integration description;
- sample report;
- developer-facing README.

### Track 5 — Productization
- one reusable intake;
- one evidence schema;
- one report schema;
- one delivery checklist;
- derive consulting and low-touch products from the same spine.

## K. PR #63 acceptance condition

PR #63 should remain a bounded continuity spine, not become an encyclopedic database.

Acceptance requires only:

1. every ACTIVE work item has repo/PR or branch, source branch, execution worktree branch when relevant, and exact immutable head;
2. every repository in the initial census has one lifecycle disposition;
3. every known production-capable or data-bearing surface has an owner seat and verification status;
4. revenue-critical work is visibly separated from research, experiments, and parked architecture;
5. historical documents are labeled historical/superseded rather than silently treated as current control sources;
6. the Engineering Doctrine remains explicitly candidate guidance until reviewed and promoted.

## L. Revenue-first estate sweep

Sweep from revenue impact outward:

| Order | Sweep | Required outcome |
|---:|---|---|
| 1 | PR #54 + production-adjacent platform surfaces | Exact merge/release/migration/case-start boundaries and current state |
| 2 | CORE-HUB PR #63 | Candidate continuity spine ready for disposition |
| 3 | GitHub repository census | Every repository assigned a lifecycle class |
| 4 | Vercel project census | Repo ownership, purpose, deployment policy, keep/freeze/retire decision |
| 5 | Supabase classification | Production data plane separated from replay/test surfaces |
| 6 | Local-machine census | Reproducible secrets-free census script plus dated output |

## M. Exit criteria for the consolidation sprint

The sprint is complete when:

1. one current source tells a node where to look for current truth;
2. every active repo/work item has an explicit disposition;
3. stale current-state docs are superseded, not silently left ambiguous;
4. local/cloud/provider/database inventories are dated and reproducible;
5. roles/authority are explicit and platform controls match the single-Operator model;
6. Osiris has a verified first-dollar path through delivery readiness;
7. the GitHub Ops proof report exists;
8. GitHub Developer Program application materials are ready;
9. parked work has restart conditions;
10. the next 30 days of work are dominated by revenue, customer proof, and business readiness rather than new architecture.

## N. Immediate order

1. Correct the solo-Operator GitHub protection policy without weakening unrelated protections.
2. Merge the exact-cleared Osiris PR #54 only after the policy is truthful and re-verified.
3. Finish PR #63 to the narrow acceptance condition above.
4. Generate the first polished GitHub Ops sample audit.
5. Begin direct outreach and paid/design-partner conversations immediately using truthful current-state claims.
6. Keep hosted migration/deploy/live-case start separately gated and authorize them only when they are actually needed for fulfillment.
7. Run the GitHub/Vercel/Supabase/local cleanup sweep from revenue impact outward.
8. Prepare the GitHub Developer Program application/support surface.
9. Convert repeated paid delivery work into productized/passive assets.
10. Reopen parked architecture only when a customer, proof need, safety requirement, or blocking dependency earns it.
