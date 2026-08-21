# MIRRORNODE Orientation Protocol

**Status:** PROPOSAL / TECHNICAL ORIENTATION  
**Authority effect:** NONE  
**Companion:** [`START_HERE.md`](START_HERE.md)  
**Purpose:** Define a deterministic re-entry, provenance, freshness, and source-navigation protocol for intelligent participants entering or resuming MIRRORNODE work.

This document is the technical sister page to `START_HERE.md`.

`START_HERE.md` restores conceptual bearings. This document specifies how a participant converts those bearings into a current, source-bound working state.

It is not a source of execution authority and must never be used as a substitute for canon, matter records, exact-head review, policy, delegation, or Operator authorization.

---

## 1. Problem Statement

MIRRORNODE is a distributed cognitive and operational system. Different intelligent participants may resume work with different cached representations of:

- system topology;
- terminology;
- authority semantics;
- repository state;
- active matters;
- review validity;
- participant roles;
- independence requirements;
- relational history;
- current implementation boundaries.

High-capability reasoning does not eliminate this problem. It can make the problem harder to detect because a stale model may remain internally coherent.

The failure class is **coherence drift under version skew**.

A participant may reason correctly from an obsolete MIRRORNODE model and still produce the wrong operational conclusion.

Therefore MIRRORNODE re-entry must be treated as a state synchronization problem.

---

## 2. Core Invariant

> **No participant should be required to rediscover the whole system, and no participant should be permitted to act as though its cached model is current without synchronization.**

The protocol distinguishes:

1. conceptual orientation;
2. source discovery;
3. provenance qualification;
4. freshness binding;
5. matter-local context loading;
6. authority verification;
7. work execution.

These stages must not be silently collapsed.

---

## 3. Context Epoch

MIRRORNODE should maintain a versioned **Context Epoch** for architecture-level semantic changes.

A Context Epoch changes when one or more of the following materially changes:

- authority semantics;
- canonical source routing;
- identity or independence rules;
- review-validity rules;
- MOPCON's coordination contract;
- runtime/authority boundary;
- knowledge-provenance semantics;
- deliberation semantics;
- repository-governance rules;
- source-of-truth topology.

A Context Epoch is not a governance disposition and does not ratify the changes it describes. It is a synchronization marker.

Recommended fields:

```yaml
context_epoch: CE-YYYYMMDD-NN
created_at: RFC3339
orientation_version: string
previous_epoch: string | null
changed_concepts:
  - string
invalidated_assumptions:
  - string
stable_invariants:
  - string
source_manifest_ref: string
architecture_delta_ref: string
```

A node resuming from an older epoch must ingest the delta before its prior system model is treated as current.

---

## 4. Architecture Delta

Each Context Epoch should have a compact **Architecture Delta** answering only:

- What changed?
- What did not change?
- What terminology was renamed or split?
- Which previous assumptions are now invalid?
- Which authority boundaries changed?
- Which review/freshness rules changed?
- Which source locations changed?
- What must each participant preserve from the previous epoch?

The Architecture Delta exists specifically to prevent giant orientation packets from becoming the normal synchronization mechanism.

It is a migration record, not canon.

---

## 5. Artifact Status Taxonomy

Every artifact used during orientation should be classified before substantive reliance.

Allowed status values:

```text
CANON
RATIFIED_GOVERNANCE
ACTIVE_MATTER
PROPOSAL
IMPLEMENTATION
OPERATIONAL_RECORD
HISTORICAL
DISCUSSION
ORIENTATION
UNKNOWN_STATUS
```

Rules:

- `PROPOSAL` must never be promoted by inference.
- `IMPLEMENTATION` does not establish constitutional standing.
- `ORIENTATION` does not establish authority.
- `HISTORICAL` may explain lineage but does not automatically describe current state.
- `ACTIVE_MATTER` may contain unresolved positions and must not be treated as disposition.

---

## 6. Provenance-Qualified Knowledge States

MIRRORNODE must not collapse all non-direct knowledge into `UNKNOWN`, and must not collapse trusted provenance into personal verification.

Use the following epistemic states:

### `DIRECT`

The current participant directly observed the cited source or evidence.

### `TRUSTED_RECEIPT`

A recognized participant or system supplied a target-bound, timestamped observation or receipt with sufficient provenance for the current task.

This is usable knowledge unless the task specifically requires independent verification.

### `PACKET_ASSERTED`

The claim appears in supplied context but lacks sufficient source-bound provenance for stronger classification.

### `INFERRED`

The claim is derived from other evidence rather than directly observed.

The inference path should be explainable.

### `STALE`

The claim was previously supported but its freshness or target binding has expired.

### `UNKNOWN`

No adequate evidence supports the claim.

### `CONFLICTED`

Credible evidence disagrees and the conflict remains unresolved.

These states describe knowledge provenance. They do not themselves create authority.

---

## 7. Independence Mode

A task must declare whether prior trusted receipts may be used.

Recommended modes:

### `COLLABORATIVE`

Trusted receipts from recognized participants may be used with provenance preserved.

### `INDEPENDENT_REVIEW`

The reviewer must independently inspect the required source set. Prior conclusions, deliberation results, relational context, or another reviewer's judgment may not be used as substantive evidence unless the review specification explicitly allows a second challenge phase.

### `CORROBORATION`

The participant independently verifies a specific prior claim or receipt.

### `SYNTHESIS`

The participant may combine provenance-qualified positions but must preserve disagreement and must not convert synthesis into authority.

A task that does not specify independence mode defaults to `COLLABORATIVE` for non-authority work and to the governing contract for authority-bearing review.

---

## 8. Re-entry Bootstrap Sequence

A returning participant should execute the following sequence.

### Step 1 — Orientation

Read `START_HERE.md`.

Output internally:

```text
ORIENTED = true
AUTHORITY_ACQUIRED = false
```

### Step 2 — Epoch Check

Determine the participant's last known Context Epoch.

If current epoch differs:

1. load Architecture Delta;
2. mark invalidated assumptions stale;
3. preserve explicitly stable invariants;
4. do not import authority state from the prior epoch.

### Step 3 — Matter Classification

Identify the current task/matter and classify it:

```text
governance
repository
runtime
mopcon_coordination
public_surface
business_operation
research
other
```

### Step 4 — Source Routing

Navigate to the authoritative or evidentiary surface for that class.

Orientation text is no longer sufficient after this point.

### Step 5 — Target Binding

Resolve the exact relevant target:

- artifact version;
- repository;
- branch/ref;
- commit SHA;
- matter identifier;
- policy version;
- runtime state hash;
- or other governing target.

### Step 6 — Provenance Classification

Classify each material claim using the knowledge states in Section 6.

### Step 7 — Freshness Check

Determine whether the evidence remains valid for the resolved target.

If the target moved, target-bound review or assent becomes stale unless the governing procedure explicitly permits inheritance.

### Step 8 — Independence Check

Apply the declared independence mode before consuming other participants' conclusions.

### Step 9 — Load Minimal Adjacent Context

Load only the context necessary to understand the current target.

Avoid reconstructing the entire MIRRORNODE history unless the task specifically requires historical analysis.

### Step 10 — Authority Check

Before consequential action, consult the actual authority-bearing source.

Orientation, trusted receipts, relational history, and deliberative consensus cannot satisfy this step by themselves.

---

## 9. Source Routing Contract

The default routing map is:

| Question class | Primary source surface | Orientation may answer? |
|---|---|---:|
| Canon / ratification / constitutional standing | CORE-HUB canon + promotion/disposition records | No |
| Active governance matter | Matter directory + exact target + positions + disposition | No |
| Repository state / CI / review / protection | Repo Steward + GitHub evidence | No |
| Runtime execution | Runtime repository + current plan/state/receipt | No |
| Coordination / active workload | MOPCON operational records | Partially |
| Public presentation | Public deployment + source repository | Partially |
| Historical lineage | Historical records + current supersession chain | Partially |

If a question crosses surfaces, each claim retains its own provenance rather than inheriting the strongest source classification in the answer.

---

## 10. Review Freshness Rules

Default rule:

> **A target-bound review is valid only for the target it actually reviewed.**

For commit-bound repository review:

```text
review.target_sha == current_required_sha
```

must hold unless the governing procedure explicitly defines a safe inheritance rule.

The following do not independently establish exact-head clearance:

- green CI;
- review request;
- review against an ancestor SHA;
- resolved historical thread;
- prior consensus;
- mergeability;
- familiarity with the change;
- unchanged PR title;
- unchanged branch name.

---

## 11. Relational Context Boundary

Relational intelligence may be loaded during ordinary collaboration but must not contaminate independence-sensitive passes.

If a task is `INDEPENDENT_REVIEW`, the review packet should explicitly define whether the following are excluded:

- Intersection Record;
- prior Deliberation Graph;
- prior reviewer conclusions;
- implementer commentary;
- synthesized recommendation;
- relational preference scores;
- historical agreement patterns.

Default for authority-bearing independent review: exclude them until the independent position is committed.

---

## 12. Coherence Drift Detection

A participant should declare `COHERENCE_RISK` when any of the following occurs:

- familiar terminology now has a materially different definition;
- an active matter references a target the participant cannot resolve;
- current and cached authority models disagree;
- provider/seat/identity semantics changed;
- a source moved or was superseded;
- the participant is relying on relational memory to fill missing implementation state;
- multiple packets provide inconsistent heads or status;
- the participant cannot distinguish proposal from ratified state;
- the participant's last Context Epoch is unknown.

`COHERENCE_RISK` triggers reorientation, not improvisation.

---

## 13. Minimal Re-entry Acknowledgment

After bootstrap, a participant should be able to state:

```yaml
context_epoch: <current>
matter: <identifier or task>
artifact_status: <taxonomy value>
target: <exact target>
independence_mode: <mode>
knowledge:
  direct: []
  trusted_receipt: []
  packet_asserted: []
  inferred: []
  stale: []
  unknown: []
  conflicted: []
blocking_uncertainty: []
authority_source_loaded: true | false
```

This acknowledgment is diagnostic. It is not a vote, review approval, or authorization artifact.

---

## 14. Orientation Cache Rules

Orientation may be cached.

Authority state may not be inferred from the cache.

Recommended cache keys:

```text
orientation_version
context_epoch
source_manifest_ref
architecture_delta_ref
loaded_at
expires_at
```

When the Context Epoch changes, cached architectural assumptions become invalid until the delta is ingested.

---

## 15. Human Legibility Constraint

The bootstrap protocol exists for intelligent participants, but its results must remain legible to the Operator.

MOPCON should be able to answer for any active participant:

- What Context Epoch is it operating under?
- What matter is it working on?
- What source set did it load?
- What target is it bound to?
- Which claims are direct vs trusted receipts vs unknown?
- Is it operating independently or collaboratively?
- What uncertainty remains?
- Does it currently possess any execution eligibility under an actual authority source?

Do not display this as a single confidence score.

---

## 16. Failure Semantics

### `ORIENTATION_FAIL`

The participant cannot establish the current system context or source map.

### `TARGET_FAIL`

The exact required artifact/ref/version cannot be resolved.

### `PROVENANCE_HOLD`

A material claim exists but its evidence provenance is insufficient for the requested task.

### `FRESHNESS_HOLD`

Evidence exists but is stale relative to the target.

### `INDEPENDENCE_HOLD`

The requested review cannot satisfy its independence contract.

### `AUTHORITY_HOLD`

The participant understands the task but cannot establish current permission for consequential action.

These states should remain distinct. A participant may be perfectly coherent and still lack authority.

---

## 17. Anti-Patterns

The protocol explicitly rejects:

### Giant-state-dump dependence

If every return requires a complete narrative export, synchronization has failed.

### Personal rediscovery requirement

If every participant must personally re-verify every shared fact for ordinary collaboration, the system cannot benefit from collective evidence.

### Blind shared-memory trust

If a participant treats another lane's memory as direct evidence without provenance, collective context becomes rumor.

### Proposal gravity

A sophisticated proposal must not become de facto canon merely because every active participant has started using its language.

### Semantic aliasing

Old and new meanings of the same term must not coexist without an epoch/delta record.

### Review inheritance by familiarity

A reviewer knowing the matter well does not make its previous review current.

---

## 18. Design Principle

MIRRORNODE should behave like a well-designed distributed system:

- participants may cache;
- caches have versions;
- state has provenance;
- observations have freshness bounds;
- migrations have deltas;
- conflicting replicas are detected;
- authority is not reconstructed from cache;
- irreversible operations require current, explicit eligibility;
- recovery paths are intentional.

The intelligent nature of the participants increases the value of this discipline; it does not remove the need for it.

---

## 19. Final Invariant

> **Orientation is allowed to restore coherence. It is never allowed to manufacture currency, independence, evidence, or authority.**

The intended flow is:

```text
START_HERE
    ↓
CONTEXT EPOCH / ARCHITECTURE DELTA
    ↓
SOURCE ROUTING
    ↓
EXACT TARGET
    ↓
PROVENANCE + FRESHNESS + INDEPENDENCE
    ↓
MATTER-LOCAL WORK
    ↓
EXPLICIT AUTHORITY WHEN CONSEQUENCE BEGINS
```

This is the re-entry contract.
