# CG-0029 Operator Decision Packet — Draft

**Matter:** Continuity Console v0.1 Definition  
**Workflow state:** Assembled  
**Disposition:** Pending  
**Decision authority:** Operator  
**Packet status:** Incomplete — awaiting Ptah and Osiris positions

## 1. Decision required

Choose whether MIRRORNODE should proceed toward implementation of a public, read-only Continuity Console at `/continuity` in `mirrornode-platform`.

The proposed surface would reuse the existing System Integrity Scorecard as a design and adapter reference, render a build-generated allowlisted snapshot, and leave all execution and approval controls inside private MOPCON.

## 2. Proposed decision statement

> Approve Continuity Console v0.1 for implementation in `mirrornode-platform` as a static, read-only `/continuity` route using a typed, build-generated, allowlisted snapshot. The route may present source-labeled system orientation, active work, Council Grounds matters, and recent continuity records. It may not execute actions, mutate repositories, expose private MOPCON routes or data, ingest personal integrations, synthesize an overall health score, or present mock or stale data as current truth.

This wording remains provisional until all required reviews are received.

## 3. Evidence currently assembled

| Evidence | Finding | Decision relevance |
|---|---|---|
| Existing scorecard app | Real React/Vite surface with source badges, sync time, system cards, incident list, and live/mock adapter | Confirms reuse opportunity; also exposes silent fallback and unsupported-state risks |
| Platform home metadata | Platform is intentionally a static public orientation surface without unsupported live-state claims | Supports `/continuity` placement if the route remains read-only and source-labeled |
| MOPCON PR #3 | Contains runtime health, planning, approval/rejection, execution, and trace controls | Establishes the private action boundary that Continuity must not duplicate |
| Council Grounds | Separates workflow state, attributed positions, synthesis, and Operator disposition | Gives Continuity a safe source for matter summaries without granting decision authority |
| Theia position POS-0001 | Supports with conditions: static surface state, build snapshot, no direct MOPCON route, no synthetic health score | Conditions incorporated into the current definition |

## 4. Current areas of agreement

The assembled evidence currently supports these points:

1. Continuity and MOPCON are distinct surfaces.
2. Continuity is orientation, not control.
3. The scorecard should be reused conceptually rather than deployed as a separate product.
4. Public data must be allowlisted before snapshot generation.
5. Every status requires source and timestamp metadata.
6. Missing information renders as unavailable, not healthy.
7. Workflow state and Operator disposition remain separate.
8. Email, calendar, finances, customer data, and private traces are outside v0.1.
9. The public route must not call private systems or hold GitHub credentials at request time.
10. The page must not create an overall system-health score from incomplete evidence.

## 5. Required positions

### Theia — received

**Stance:** Support with conditions.  
**Status:** Conditions incorporated.

### Ptah — pending

Must determine:

- implementation feasibility in current Platform,
- minimal typed snapshot contract,
- generation script and artifact location,
- stale/failure behavior,
- reuse versus rewrite,
- required tests and blockers.

### Osiris — pending

Must determine:

- privacy and inference risks,
- freshness and authority-overstatement risks,
- prohibited fields,
- partial/failure behavior,
- public-history risks,
- deployment conditions.

## 6. Unresolved questions

1. What freshness windows apply to GitHub, Council, deployment, runtime, and MOPCON records?
2. Does the generated snapshot require a signed manifest in v0.1?
3. Where does Continuity appear in Platform navigation?
4. What is the final canonical Mirror Mirror route?
5. Should snapshot generation run manually, during CI, or during deployment build?
6. What public continuity-history retention window is appropriate?
7. How are source disagreement and disputed records represented?

## 7. Non-negotiable implementation boundary

An approval must not authorize:

- runtime execution,
- PR creation, merging, closing, or labeling,
- Council state transitions,
- autonomous health conclusions,
- private MOPCON linking without authentication,
- private trace or Operator-note exposure,
- email, calendar, finance, or customer-data ingestion,
- hidden request-time calls to GitHub or private infrastructure,
- replacement of stale data with unlabeled mock data.

## 8. Decision options

### Option A — Approve implementation

Use only after Ptah and Osiris reviews confirm the boundary is feasible and safe.

Effect:

- PR #29 may be finalized and merged as the governing definition.
- A separate implementation branch may be opened in `mirrornode-platform`.
- Implementation remains subject to build, accessibility, source-label, and privacy verification.

### Option B — Revision required

Use when the direction is correct but required reviews identify unresolved design, security, or truth-model defects.

Effect:

- PR #29 remains draft.
- CG-0029 returns to framing or assembled after revision.
- No Platform implementation begins.

### Option C — Park

Use when the concept remains valid but current runtime, Platform, business, or competition priorities make implementation premature.

Effect:

- Definition and positions remain preserved.
- No implementation authority is granted.

### Option D — Reject

Use when the public Continuity concept creates more confusion, exposure, or maintenance burden than value.

Effect:

- The scorecard remains detached or private.
- CG-0029 closes with a rejection rationale.

## 9. Current recommendation

**Provisional recommendation: proceed toward Option A, but do not approve yet.**

The concept is coherent and the first review corrections materially improved it. The packet lacks the required implementation-feasibility and boundary-risk positions. Approval before those positions would defeat the Council Grounds protocol this matter is intended to exercise.

## 10. Operator disposition block

Complete only after synthesis-ready state.

```yaml
matterId: CG-0029
status: ratified | revision-required | parked | rejected
authority: operator
decidedAt: <timestamp>
selectedOption: A | B | C | D
rationale: >-
  <Operator rationale>
approvedScope:
  - <exact scope>
prohibitedScope:
  - <exact exclusions>
nextAction: >-
  <single next action>
canonAction: separate-explicit-action | none
```

## 11. Immediate next step

Obtain and register exact attributed positions from Ptah and Osiris. Then prepare a conflict-aware synthesis and replace this draft's provisional recommendation with a final recommendation for Operator disposition.
