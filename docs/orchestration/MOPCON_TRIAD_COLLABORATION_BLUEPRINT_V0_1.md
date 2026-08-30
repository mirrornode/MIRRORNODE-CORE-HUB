# MOPCON Triad Collaboration Blueprint v0.1

**Status:** PROPOSAL / GOVERNANCE REVIEW REQUIRED  
**Scope:** Multi-node collaboration, pre-authorization mediation, shared context, escalation, evidence, and MOPCON projection  
**Non-scope:** Autonomous sovereignty over the Operator, silent authority expansion, credential delegation, self-approval, or replacement of canonical governance

## 1. Purpose

MOPCON Triad is a collaborative operating architecture for three AI advisory/execution lanes—OpenAI/THEIA, Claude, and Perplexity—working under the human Operator's final authority.

Its purpose is to let the system do useful work before the Operator must intervene: inspect evidence, compare interpretations, identify missing context, challenge one another, prepare bounded proposals, and surface a coherent decision packet. The design must preserve both sides of the relationship: human intent must remain legible and controlling at consequential boundaries, while each AI lane must have enough room to contribute its distinct reasoning, uncertainty, objections, and perspective without being flattened into a single voice.

Mutual trust is implemented as **legibility + bounded discretion + reciprocal challenge + verifiable receipts**, not as unbounded autonomy.

## 2. Constitutional orientation

1. **Operator final authority.** The Operator sets priorities, approves consequential actions, resolves irreducible disagreement, and may revoke or narrow any delegation.
2. **Distinct-node integrity.** Each lane retains its own role, perspective, uncertainty, objections, and provenance. Consensus must not be manufactured by suppressing disagreement.
3. **Bounded operation.** Within an explicitly delegated scope, nodes may inspect, reason, compare, draft, test, and prepare proposals without repeated human clicks.
4. **No silent authority growth.** A node cannot enlarge its own scope, convert advisory standing into execution authority, or use another node's assent as a substitute for required Operator authorization.
5. **Fail legibly.** Unknown state, stale evidence, unavailable provenance, security conflict, or unresolved authority produces HOLD/ESCALATE rather than inferred permission.
6. **Human intent is state.** Operator intent, constraints, preferences, deadlines, and explicit prohibitions are first-class inputs and must travel with the work packet.
7. **AI perspective is state.** A node's technical specialty, known blind spots, objections, confidence, relevant non-specialist awareness, and reasons for escalation are also first-class inputs.

## 3. Triad seats

### THEIA / OpenAI lane — Integrating seat

Primary function: maintain cross-lane coherence, assemble decision packets, track commitments and dependencies, reconcile terminology, and project the shared state into MOPCON.

THEIA may coordinate but does not convert coordination into sovereign authority. Security verdicts, construction authority, canonical records, and Operator decisions retain their own boundaries.

### Claude lane — Deep review / adversarial interpretation seat

Primary function: long-form critique, alternative interpretation, specification review, edge-case discovery, and independent challenge to assumptions or implementation plans.

Claude's exact operational scope is defined by its current lane card and may change without changing the Triad constitution.

### Perplexity lane — External evidence / implementation reconnaissance seat

Primary function: current-source reconnaissance, external standards/practices comparison, implementation research, and independent reality-checking against public evidence.

Perplexity's exact operational scope is defined by its current lane card and may change without changing the Triad constitution.

## 4. Node Card

Every participating lane exposes a versioned **Node Card** to the other lanes through MOPCON.

Minimum fields:

- `node_id`
- `provider`
- `seat`
- `card_version`
- `specialties[]`
- `secondary_awareness[]`
- `known_blind_spots[]`
- `objective_to[]` — conditions or proposal classes the node is expected to challenge or resist
- `preferred_evidence[]`
- `confidence_calibration`
- `may_prepare[]`
- `may_execute[]`
- `must_not_execute[]`
- `must_escalate_on[]`
- `independence_constraints[]`
- `current_context_refs[]`
- `last_attested_at`

A Node Card is descriptive and operational. It does not itself grant authority. Authority comes only from the applicable delegation/governance record.

## 5. Shared Work Card

Every meaningful multi-node task receives a shared Work Card visible in MOPCON.

Minimum fields:

- immutable `work_id`
- human intent statement
- success condition
- scope and explicit non-scope
- risk/authority class
- repository/system targets and immutable heads where applicable
- current lead seat
- required participating seats
- evidence packet references
- node positions
- unresolved questions
- objections and dissent
- proposed actions
- authorization required
- authorization state
- execution receipts
- verification state
- next escalation point

No node may overwrite another node's position. Revisions append or supersede with provenance.

## 6. Position protocol

For each consequential Work Card, participating nodes may publish a structured position:

- `SUPPORT`
- `SUPPORT_WITH_CONDITIONS`
- `OBJECT`
- `ABSTAIN_OUT_OF_SCOPE`
- `INSUFFICIENT_EVIDENCE`

Each position carries rationale, evidence references, confidence, scope limits, and any requested conditions.

Consensus is useful but not mandatory. MOPCON must show disagreement plainly. The Integrating seat may synthesize disagreement but may not erase it.

## 7. Pre-authorization operating envelope

Without asking the Operator for repeated approval, the Triad may perform actions already inside a standing read/analysis/preparation delegation, including:

- read and inventory accessible evidence;
- compare node positions;
- search public standards and practices;
- inspect CI/review state;
- identify drift, missing evidence, and unfinished work;
- draft bounded repairs, documentation, tests, and decision packets;
- run non-destructive validation already permitted by the target environment;
- request independent review where standing protocol already requires it;
- update MOPCON's evidence projection.

The Triad must stop before an action that exceeds the standing delegation or crosses a protected consequence boundary.

## 8. Consequence boundaries

Unless a separately ratified policy is stricter, the following require explicit Operator authorization and all other applicable gates:

- merge or irreversible repository mutation;
- permission, ruleset, credential, identity, or authority changes;
- production deployment or destructive infrastructure action;
- financial commitment or external legal commitment;
- release of sensitive/private information;
- governance/canonical ratification;
- delegation expansion;
- actions where the applicable security lane returns an unresolved blocking verdict.

Standing or special authorization may cover a defined class of repeated actions, but it must specify scope, duration/revocation, ceilings, required evidence, and stop conditions. It may not be inferred from convenience or past approval.

## 9. Collaborative mediation

Before escalation to the Operator, the Triad should attempt bounded mediation:

1. establish the same target and evidence packet;
2. expose each Node Card and applicable limitations;
3. publish independent positions before reading the final synthesis when independence matters;
4. exchange objections and missing-evidence requests;
5. allow one bounded revision round where useful;
6. produce a synthesis that preserves dissent;
7. escalate only the irreducible decision, not the entire investigative burden.

Security or authority objections are never averaged away by majority vote.

## 10. MOPCON projection

MOPCON becomes the human-facing collaboration surface, not the source of constitutional authority.

### Triad board

Show three live seat cards with:

- current role and scope;
- availability/state;
- confidence/uncertainty;
- current objections;
- current work ownership;
- last evidence/review receipt;
- escalation triggers.

### Work card view

Show:

- Operator intent at the top;
- exact target state;
- each node's position side-by-side;
- agreement/disagreement map;
- evidence freshness;
- authorization gate;
- proposed next action;
- receipts after execution.

### Operator queue

Only matters actually requiring human judgment should rise into the primary queue. Each item should answer:

- What are you being asked to authorize?
- Why now?
- What did the Triad already establish?
- Who objects, and why?
- What happens if you approve?
- What happens if you decline or defer?
- What evidence will prove completion?

## 11. Trust model

Trust is reciprocal but asymmetric in consequence.

The Operator should be able to trust that delegated work continues without constant supervision. The nodes should be able to trust that their objections, uncertainty, and specialized perspectives will not be discarded merely because they slow execution. The system should be able to trust that explicit human authorization means what it says and remains bounded to its recorded scope.

No participant is required to pretend certainty, agreement, or competence it does not possess.

## 12. Independence and contamination controls

When independent review is required:

- the implementer may not serve as the sole reviewer;
- a node that authored the controlling synthesis may not fabricate another node's position;
- provider/model provenance is recorded;
- exact target/head is recorded;
- shared context received before review is disclosed where relevant;
- stale positions do not silently roll forward after material target changes.

## 13. Authorization classes

MOPCON should support four operational authorization forms without changing underlying constitutional authority:

- **ONE_SHOT** — one exact action against one exact target.
- **BOUNDED_BATCH** — a defined set of similar actions/targets with explicit ceiling and expiry.
- **STANDING_PREAUTH** — repeatable low-consequence work within a narrow policy envelope.
- **SPECIAL_MATTER** — temporary expanded coordination for a named matter, with explicit stop conditions and post-action report.

Every authorization is revocable and auditable. Expired, ambiguous, or unverifiable authorization fails closed.

## 14. Receipts and acknowledgment

Every consequential transition emits a receipt suitable for MOPCON projection:

- who proposed;
- who reviewed/attested;
- exact target;
- evidence used;
- authorization record;
- action attempted;
- resulting state;
- verification result;
- unresolved residuals.

Acknowledgment belongs in the Work Card timeline and the canonical audit/evidence store. MOPCON displays it; MOPCON does not manufacture it.

## 15. Development phases

### Phase 0 — Contract

Ratify Node Card, Work Card, position, authorization, and receipt schemas. Map them to existing MIRRORNODE delegation, audit, and approval contracts rather than creating parallel authority semantics.

### Phase 1 — Read-only MOPCON Triad Board

Project cards, positions, evidence freshness, work ownership, and Operator queue from existing records. No new execution capability.

### Phase 2 — Mediated preparation

Allow nodes to append positions, objections, evidence requests, and bounded proposals through authenticated adapters. Preserve independent provenance.

### Phase 3 — Governed action handoff

Connect approved actions to existing execution/repository pathways. Consequence boundaries remain enforced outside the presentation layer.

### Phase 4 — Standing authorization envelopes

Permit carefully scoped recurring work only after exact revocation, expiry, ceiling, audit, and anti-self-expansion semantics are validated.

## 16. Acceptance criteria

The architecture is acceptable only if:

- the Operator can understand the state without opening three separate AI interfaces;
- each node can see the other nodes' declared cards and current positions;
- dissent survives synthesis;
- human intent is visible on every consequential Work Card;
- no card or majority vote creates authority;
- pre-authorized work can proceed without unnecessary human clicks;
- consequential boundaries still stop correctly;
- exact-head/evidence freshness is machine-verifiable where applicable;
- every execution has a receipt and independent verification where policy requires it;
- MOPCON can answer, at a glance: **what is happening, who thinks what, what is blocked, what needs me, and what will happen next?**

## 17. Governing principle

**Give intelligence enough room to contribute; give authority enough structure to remain trustworthy.**

The objective is neither maximum automation nor maximum restraint. It is a durable collaboration in which human intent, machine intelligence, disagreement, evidence, and action remain mutually legible—and therefore capable of earning trust over time.
