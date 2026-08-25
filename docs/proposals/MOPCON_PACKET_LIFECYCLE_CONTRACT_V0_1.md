# MOPCON Packet Lifecycle Contract v0.1

**Status:** PROPOSAL — READY FOR IMPLEMENTATION REVIEW  
**Scope:** GitHub exact-head packet lifecycle semantics for MOPCON and Packet Forge  
**Authority note:** This document records a proposed mechanically testable contract. It does not itself promote canon, authorize implementation, or manufacture clearance.

## Contract

The governed subject of every transition, review, approval, and publication event is `packetVersionId`, not `packetId`. Transition evaluation is fail-closed: an unknown state, missing guard input, unresolved authority, stale hash, or unrecognized policy version produces rejection and no best-effort advancement.

This version is narrow by design:

- GitHub exact-head source bundles only.
- One release-review policy.
- One deterministic rendered artifact per `packetVersionId`.
- No collaborative editing.
- No autonomous release.
- No generalized document platform behavior.

The acceptance bar is simple: it must be impossible, through the schema and transition function, to publish a packet that was not bound, rendered, reviewed, and approved against the exact immutable subject being released.

## 1. Identity model

```ts
export type PacketId = string
export type PacketVersionId = string

export type PacketIdentity = {
  packetId: PacketId
  packetVersionId: PacketVersionId
}
```

Rules:

- `packetId` identifies the logical packet lineage.
- `packetVersionId` identifies the immutable governed version instance.
- All transitions, reviews, approvals, publications, and audit events bind to `packetVersionId`.
- A substantive change to render subject or release basis requires a new `packetVersionId`.
- Creating a successor packet version must not rewrite the lifecycle history of its predecessor.

A new `packetVersionId` is required when any of the following changes:

- `sourceBundleHash`
- `templateId`
- `templateVersion`
- `renderProfileHash`
- `reviewPolicyVersion`
- finding version set
- evidence binding set
- scope
- audience-affecting substantive content

## 2. State enum

```ts
export enum PacketLifecycleState {
  REQUESTED = "REQUESTED",
  BOUND = "BOUND",
  VALIDATED = "VALIDATED",
  RENDERED_DRAFT = "RENDERED_DRAFT",
  IN_REVIEW = "IN_REVIEW",
  CHANGES_REQUIRED = "CHANGES_REQUIRED",
  APPROVED_FOR_RELEASE = "APPROVED_FOR_RELEASE",
  PUBLISHED = "PUBLISHED",
  WITHHELD = "WITHHELD",
  CANCELLED = "CANCELLED",
  SUPERSEDED = "SUPERSEDED",
  RETIRED = "RETIRED",
}
```

State classification:

- **Blocking state:** `WITHHELD`
- **Publication state:** `PUBLISHED`
- **Terminal states:** `CANCELLED`, `SUPERSEDED`, `RETIRED`

Rules:

- Every `packetVersionId` has exactly one current lifecycle state.
- Every released packet version has exactly one immutable publication event.
- A published packet version may later become `SUPERSEDED` or `RETIRED`, but its publication event and published bytes remain immutable.

## 3. Governing records

### Packet subject

```ts
export type PacketSubject = {
  packetId: PacketId
  packetVersionId: PacketVersionId
  packetFamily: "repository_reality_summary" | "control_verification_report" | "meeting_brief"
  caseId: string
  state: PacketLifecycleState

  templateId: string
  templateVersion: string
  renderProfileHash: string
  reviewPolicyVersion: "release_review_v1"

  sourceBundleId?: string
  sourceBundleHash?: string
  artifactHash?: string
  renderReceiptId?: string

  createdAt: string
  updatedAt: string
  publishedAt?: string
  supersedesPacketVersionId?: PacketVersionId
  supersededByPacketVersionId?: PacketVersionId
  withheldReason?: string
  cancelledReason?: string
  retiredReason?: string
}
```

### GitHub exact-head source bundle

```ts
export type GitHubSourceBundle = {
  sourceBundleId: string
  caseId: string
  repository: string
  commitSha: string
  treeHash: string
  snapshotIds: string[]
  findingVersionRefs: Array<{ findingId: string; version: string }>
  evidenceHashRefs: Array<{ evidenceId: string; hash: string }>
  scopeHash: string
  createdAt: string
  hash: string
}
```

### Render receipt

```ts
export type PacketRenderReceipt = {
  renderReceiptId: string
  packetVersionId: PacketVersionId
  sourceBundleHash: string
  templateId: string
  templateVersion: string
  renderProfileHash: string
  rendererId: string
  rendererVersion: string
  renderInputHash: string
  artifactHash: string
  renderedAt: string
}
```

### Release approval

```ts
export type PacketReleaseApproval = {
  approvalId: string
  packetVersionId: PacketVersionId
  artifactHash: string
  sourceBundleHash: string
  templateId: string
  templateVersion: string
  renderProfileHash: string
  reviewPolicyVersion: "release_review_v1"
  reviewer: string
  reviewerRole: string
  decision: "APPROVE"
  decidedAt: string
}
```

## 4. Generated Artifact Non-Authority Invariant

Generated packets are projections of authoritative records. They may describe case state, present findings, cite evidence, translate findings, and preserve provenance. They must not originate or alter findings, establish evidence validity, authorize operations, change case state, manufacture a reviewer decision, or become canonical merely through publication.

## 5. Lifecycle transitions only

Every legal transition must be explicit. All unspecified transitions are invalid and rejected.

| From | Event | Guard set | To |
|---|---|---|---|
| `REQUESTED` | `PacketSourcesBound` | G1, G2, G3 | `BOUND` |
| `REQUESTED` | `PacketWithheld` | G13 | `WITHHELD` |
| `REQUESTED` | `PacketCancelled` | G14 | `CANCELLED` |
| `BOUND` | `PacketValidated` | G4, G5 | `VALIDATED` |
| `BOUND` | `PacketWithheld` | G13 | `WITHHELD` |
| `BOUND` | `PacketCancelled` | G14 | `CANCELLED` |
| `VALIDATED` | `PacketRendered` | G6, G7, G8 | `RENDERED_DRAFT` |
| `VALIDATED` | `PacketWithheld` | G13 | `WITHHELD` |
| `RENDERED_DRAFT` | `PacketReviewStarted` | G9 | `IN_REVIEW` |
| `RENDERED_DRAFT` | `PacketWithheld` | G13 | `WITHHELD` |
| `RENDERED_DRAFT` | `PacketCancelled` | G14 | `CANCELLED` |
| `IN_REVIEW` | `PacketReviewChangesRequired` | G10 | `CHANGES_REQUIRED` |
| `IN_REVIEW` | `PacketReleaseApproved` | G11 | `APPROVED_FOR_RELEASE` |
| `IN_REVIEW` | `PacketWithheld` | G13 | `WITHHELD` |
| `CHANGES_REQUIRED` | `PacketCancelled` | G14 | `CANCELLED` |
| `CHANGES_REQUIRED` | `PacketWithheld` | G13 | `WITHHELD` |
| `APPROVED_FOR_RELEASE` | `PacketPublished` | G12 | `PUBLISHED` |
| `APPROVED_FOR_RELEASE` | `PacketWithheld` | G13 | `WITHHELD` |
| `PUBLISHED` | `PacketSuperseded` | G15 | `SUPERSEDED` |
| `PUBLISHED` | `PacketRetired` | G16 | `RETIRED` |
| `WITHHELD` | `PacketCancelled` | G14 | `CANCELLED` |

Notes:

- `PacketVersionReissued` is not a lifecycle transition on the predecessor subject.
- No event that creates `vN+1` may mutate the current state of `vN` to `REQUESTED`.
- No terminal state has outgoing transitions.

## 6. Subject creation outside the reducer

Successor creation is a lineage operation, not a state transition on the predecessor subject.

```ts
export type PacketVersionReissueRequest = {
  predecessorPacketVersionId: PacketVersionId
  newPacketVersionId: PacketVersionId
  reason: string
  actor: string
  at: string
}

export type PacketVersionReissueOutcome =
  | {
      accepted: true
      predecessorState: "CHANGES_REQUIRED" | "WITHHELD"
      createdSubject: PacketSubject
    }
  | {
      accepted: false
      failure: GuardFailureCode
      detail: string
    }
```

Rules:

- Reissue may occur only from a predecessor in `CHANGES_REQUIRED` or `WITHHELD`.
- The predecessor remains immutable and historically complete in its current state.
- The created successor begins at `REQUESTED`.
- Reissue must preserve lineage via shared `packetId` and distinct `packetVersionId`.

## 7. Guard definitions

All guards are deterministic predicates over explicit inputs. Missing input means failure, not fallback.

```ts
export type GuardResult =
  | { ok: true }
  | { ok: false; code: GuardFailureCode; detail: string }

export type GuardFailureCode =
  | "UNKNOWN_STATE"
  | "UNKNOWN_EVENT"
  | "MISSING_INPUT"
  | "UNRESOLVED_AUTHORITY"
  | "STALE_HASH"
  | "POLICY_VERSION_UNRECOGNIZED"
  | "SUBJECT_MISMATCH"
  | "SOURCE_BUNDLE_INVALID"
  | "RENDER_NOT_DETERMINISTIC"
  | "REVIEW_RECORD_INVALID"
  | "APPROVAL_BINDING_INVALID"
  | "PUBLICATION_IMMUTABILITY_BROKEN"
  | "TERMINAL_STATE"
  | "LINEAGE_CONFLICT"
  | "SUPERSESSION_CYCLE"
```

Guard set:

- **G1:** `caseId`, `packetId`, and `packetVersionId` exist and resolve.
- **G2:** `sourceBundleId` resolves to a valid GitHub exact-head bundle.
- **G3:** `sourceBundleHash` is present and matches the stored source bundle hash.
- **G4:** template and render profile exist and are recognized.
- **G5:** `reviewPolicyVersion === "release_review_v1"` and is recognized.
- **G6:** render receipt exists for this exact `packetVersionId`.
- **G7:** render receipt binds the same `sourceBundleHash`, `templateId`, `templateVersion`, and `renderProfileHash` as the subject.
- **G8:** deterministic render condition holds; for immutable `renderInputHash + rendererVersion`, the accepted `artifactHash` is stable. A discrepancy yields `RENDER_NOT_DETERMINISTIC`.
- **G9:** rendered draft metadata block is complete; review has not yet started for a different artifact hash.
- **G10:** review rejection record exists for this exact `packetVersionId` and artifact.
- **G11:** approval record exists and exactly matches `packetVersionId`, `artifactHash`, `sourceBundleHash`, `templateId`, `templateVersion`, `renderProfileHash`, and `reviewPolicyVersion`.
- **G12:** publication request binds to the exact approved immutable subject; `artifactHash` and `sourceBundleHash` are unchanged since approval.
- **G13:** a valid withholding reason exists and the actor is authorized to withhold.
- **G14:** a valid cancellation reason exists and the packet is not already terminal.
- **G15:** successor exists; successor shares the same `packetId`; successor is already `PUBLISHED`; successor references this subject as predecessor; subject has no prior successor; successor is not subject; adding the edge introduces no cycle.
- **G16:** authorized retirement reason exists and packet is currently `PUBLISHED`.

## 8. Transition evaluation and atomic commit contract

The reducer evaluates transitions but does not itself perform persistence.

```ts
export type TransitionEvaluation =
  | {
      accepted: true
      nextState: PacketLifecycleState
      auditRecord: PacketLifecycleAuditEvent
    }
  | {
      accepted: false
      auditRecord: PacketLifecycleAuditEvent
      failure: GuardFailureCode
      detail: string
    }

export function evaluatePacketTransition(
  subject: PacketSubject,
  event: PacketLifecycleEvent,
  deps: GuardDependencies,
): TransitionEvaluation
```

The application layer must commit accepted state change and corresponding append-only audit record as one logical operation. If audit persistence fails, the state transition is not committed. Equivalent guarantees may be supplied by a transactional database write, transactional outbox, or another mechanism with the same atomicity property.

## 9. Event requirements

```ts
export type PacketLifecycleEvent =
  | { type: "PacketSourcesBound"; packetVersionId: PacketVersionId; sourceBundleId: string; sourceBundleHash: string; actor: string; at: string }
  | { type: "PacketValidated"; packetVersionId: PacketVersionId; actor: string; at: string }
  | { type: "PacketRendered"; packetVersionId: PacketVersionId; renderReceiptId: string; artifactHash: string; actor: string; at: string }
  | { type: "PacketReviewStarted"; packetVersionId: PacketVersionId; actor: string; at: string }
  | { type: "PacketReviewChangesRequired"; packetVersionId: PacketVersionId; actor: string; at: string; reason: string }
  | { type: "PacketReleaseApproved"; packetVersionId: PacketVersionId; approvalId: string; actor: string; at: string }
  | { type: "PacketPublished"; packetVersionId: PacketVersionId; actor: string; at: string }
  | { type: "PacketWithheld"; packetVersionId: PacketVersionId; actor: string; at: string; reason: string }
  | { type: "PacketCancelled"; packetVersionId: PacketVersionId; actor: string; at: string; reason: string }
  | { type: "PacketSuperseded"; packetVersionId: PacketVersionId; supersededByPacketVersionId: PacketVersionId; actor: string; at: string }
  | { type: "PacketRetired"; packetVersionId: PacketVersionId; actor: string; at: string; reason: string }
```

## 10. Audit record semantics

Rejected attempts must be recordable even when authoritative identities cannot be fully resolved.

```ts
export type PacketLifecycleAuditEvent = {
  eventId: string
  attemptedPacketVersionId?: PacketVersionId
  resolvedPacketVersionId?: PacketVersionId
  resolvedPacketId?: PacketId
  resolvedCaseId?: string
  previousState?: PacketLifecycleState
  attemptedEventType: string
  accepted: boolean
  nextState?: PacketLifecycleState
  failureCode?: GuardFailureCode
  failureDetail?: string
  actor: string
  at: string
  sourceBundleHash?: string
  artifactHash?: string
  templateId?: string
  templateVersion?: string
  renderProfileHash?: string
  reviewPolicyVersion?: string
}
```

Rules:

- If `accepted === true`, resolved identities, `previousState`, and `nextState` are required.
- If `accepted === false`, attempted identity is recorded exactly as supplied; resolved identity fields are present only if actually resolved.
- Rejected evaluations append only an audit record; they do not mutate subject state.
- Audit events are immutable.

## 11. Invalid-transition behavior

Invalid transitions do not move the state machine. They return rejection and emit a rejection audit event.

| Failure code | Meaning | Required behavior |
|---|---|---|
| `UNKNOWN_STATE` | Subject state not recognized by machine version | Reject, append audit event, no mutation |
| `UNKNOWN_EVENT` | Event not legal from current state | Reject, append audit event, no mutation |
| `MISSING_INPUT` | Required guard input absent | Reject, append audit event, no mutation |
| `UNRESOLVED_AUTHORITY` | Required source/approval/subject authority record missing | Reject, append audit event, no mutation |
| `STALE_HASH` | Bound hash no longer matches authoritative record | Reject, append audit event, no mutation |
| `POLICY_VERSION_UNRECOGNIZED` | Review policy version not known | Reject, append audit event, no mutation |
| `SUBJECT_MISMATCH` | Event references different `packetVersionId` or mismatched bindings | Reject, append audit event, no mutation |
| `SOURCE_BUNDLE_INVALID` | Source bundle violates v0.1 GitHub exact-head rules | Reject, append audit event, no mutation |
| `RENDER_NOT_DETERMINISTIC` | Artifact binding unstable for immutable render input | Reject, append audit event, no mutation |
| `REVIEW_RECORD_INVALID` | Review record missing or malformed | Reject, append audit event, no mutation |
| `APPROVAL_BINDING_INVALID` | Approval not bound to exact immutable subject | Reject, append audit event, no mutation |
| `PUBLICATION_IMMUTABILITY_BROKEN` | Artifact changed after approval or publish attempt conflicts with frozen subject | Reject, append audit event, no mutation |
| `TERMINAL_STATE` | Transition attempted from terminal state | Reject, append audit event, no mutation |
| `LINEAGE_CONFLICT` | Reissue or supersession violates lineage rules | Reject, append audit event, no mutation |
| `SUPERSESSION_CYCLE` | Proposed supersession edge introduces cycle | Reject, append audit event, no mutation |

## 12. Invariants

The following invariants must be mechanically testable.

1. **Governed Subject Invariant** — every transition, review, approval, and publication event binds to `packetVersionId`.
2. **Fail-Closed Invariant** — unknown state, missing input, unresolved authority, stale hash, or unrecognized policy version yields rejection only.
3. **Generated Artifact Non-Authority Invariant** — a generated packet never becomes authority for findings, evidence validity, authorization, or case state.
4. **Exact Subject Release Invariant** — a packet may be published only if the `packetVersionId`, `artifactHash`, `sourceBundleHash`, `templateId`, `templateVersion`, `renderProfileHash`, and `reviewPolicyVersion` exactly match the approval record.
5. **Immutable Publication Invariant** — once published, bytes and publication event for that `packetVersionId` are immutable.
6. **No In-Place Revision Invariant** — substantive changes require a new `packetVersionId`.
7. **Single Current State Invariant** — every `packetVersionId` has exactly one current lifecycle state.
8. **Single Publication Event Invariant** — every published `packetVersionId` has exactly one publication event.
9. **Terminal Closure Invariant** — `CANCELLED`, `SUPERSEDED`, and `RETIRED` have no outgoing transitions.
10. **No Silent Drift Invariant** — a changed source bundle hash or artifact hash invalidates approval for publication.
11. **State/Audit Atomicity Invariant** — an accepted transition becomes authoritative only if state change and append-only audit event are durably committed as one logical operation.
12. **Predecessor History Preservation Invariant** — creating a successor packet version cannot rewrite the predecessor lifecycle history.
13. **Supersession Lineage Invariant** — a packet version may supersede at most one predecessor; may be directly superseded by at most one successor; predecessor and successor share the same `packetId`; successor is already `PUBLISHED`; supersession is acyclic; a packet cannot supersede itself; and a `RETIRED` or `SUPERSEDED` packet cannot later acquire a different successor.
14. **Deterministic Render Invariant** — for immutable `renderInputHash + rendererVersion`, accepted render output must resolve to the same `artifactHash`; a discrepancy yields `RENDER_NOT_DETERMINISTIC`.

## 13. Minimal conformance tests

### Acceptance tests

- `REQUESTED -> BOUND` succeeds with valid exact-head GitHub bundle.
- `BOUND -> VALIDATED` succeeds with recognized template, render profile, and review policy.
- `VALIDATED -> RENDERED_DRAFT` succeeds only with a valid render receipt and deterministic artifact hash.
- `IN_REVIEW -> APPROVED_FOR_RELEASE` succeeds only with exact approval binding.
- `APPROVED_FOR_RELEASE -> PUBLISHED` succeeds only when hashes and policy bindings still match approval.
- `PUBLISHED -> SUPERSEDED` succeeds only when a later published packet version points back correctly and no cycle is introduced.
- Reissue from `CHANGES_REQUIRED` creates a new `packetVersionId` in `REQUESTED` while predecessor state remains unchanged.

### Rejection tests

- Publish without binding: reject.
- Publish without render: reject.
- Publish without review: reject.
- Publish without approval: reject.
- Publish with changed artifact hash after approval: reject.
- Publish with changed `sourceBundleHash` after approval: reject.
- Publish with unknown review policy version: reject.
- Transition from terminal state: reject.
- Reuse same `packetVersionId` after substantive change: reject.
- Approval referencing wrong `packetVersionId`: reject.
- Reissue that mutates predecessor state to `REQUESTED`: reject.
- Accepted state advance without durable audit append: reject/rollback.
- Supersession fork: reject.
- Supersession cycle: reject.
- Deterministic re-render mismatch for same render input: reject.

## 14. Reference flow

```text
subject creation
      |
      v
  REQUESTED
      |
  source bind
      v
    BOUND
      |
   validate
      v
  VALIDATED
      |
    render
      v
RENDERED_DRAFT
      |
 start review
      v
  IN_REVIEW
   /      \
  /        \
 v          v
CHANGES_   APPROVED_
REQUIRED   FOR_RELEASE
   |           |
   | reissue   | exact-binding check
   |           v
   |       PUBLISHED
   |        /      \
   v       v        v
new vN+1  SUPERSEDED RETIRED
REQUESTED
```

`WITHHELD` remains a recoverable blocking state. Recovery involving changed substantive inputs creates another governed version rather than laundering the old one back through `REQUESTED`.

## 15. Implementation readiness

This contract is ready for implementation review because it enforces three test-driving properties:

- It is impossible to publish a packet that was not bound, rendered, reviewed, and approved against the exact immutable subject being released.
- It is impossible for creating a successor packet version to rewrite the lifecycle history of its predecessor.
- It is impossible for authoritative state advancement to exist without its corresponding durable audit evidence.

### Implementation constraints

- `evaluatePacketTransition()` should remain pure.
- `PacketVersionReissueRequest` is a separate command/service boundary, not a lifecycle event.
- Persistence should enforce uniqueness for `packetVersionId`, publication events, and supersession successor relationships where possible.
- `renderInputHash` must be computed from a canonical serialization.
- Conformance tests must include malformed and partially resolvable inputs.
- Packet Forge rendering implementation follows lifecycle-contract conformance; it does not precede it.

### v0.1 proof target

> Attempt publication through every illegal path constructible by the test harness. MOPCON must refuse each path without authority manufacture, state drift, or loss of auditable evidence.
