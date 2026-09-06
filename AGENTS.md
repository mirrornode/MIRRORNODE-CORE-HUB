# Agents — MIRRORNODE-CORE-HUB

> **Current candidate reconciliation — 2026-09-06**
>
> PR #63 introduces a role/authority registry at `estate/roles.v1.json`.
> Until reviewed and promoted, it is a candidate current operating model. It supersedes the historical Lucian-centered registry **for current work routing only**, without deleting that historical evidence.
>
> Current principle: **the seat defines authority, not the model/vendor identity**.

## Current candidate operating seats

| Seat | Core function | May edit? | May authorize consequential action? |
|---|---|---:|---:|
| Operator | Business/governance/consequential disposition | Through approved executor | Yes |
| Builder | Bounded implementation | Bounded branch/worktree | No |
| Reviewer | Semantic/adversarial inspection | No | No |
| Arbitrator | Resolve conflicting findings/evidence | No | No |
| Final Review Seat | Fresh read-only exact-head final disposition | No | No |
| Projector | Normalize/display governed state | No | Never |
| Executor | Perform one explicitly approved bounded operation | Only within approved command | No |

Current examples are recorded in `estate/roles.v1.json`.

## Routing rule

There is no general-purpose canonical dispatcher inferred from historical runtime code.

Current work routes by:
1. domain;
2. owner seat;
3. exact subject;
4. next evidence-producing action.

See `estate/workstreams.v1.json`.

No ACTIVE work exists without those four fields.

## Resident Runtime

No agent runtime is hosted in this repository.

## Historical Org-Wide Runtime Registry Snapshot

The table below is retained as **historical evidence only**.

| Agent | Port | Historical role | Source |
|---|---:|---|---|
| LUCIAN | 7700 | Orchestration & Manifest | `lucian/runtime.py` |
| OSIRIS | 7701 | Payment & Commerce (Stripe) | `osiris/runtime.py` |
| HERMES | 7702 | Messaging & Protocol | Lucian registry |
| THOTH | 7703 | Services & Health | Lucian registry |
| THEIA | 7704 | Witness & Observation | Lucian registry |
| PTAH | 7705 | Creation & Bridge | Lucian registry |
| EVE | 7706 | Embodiment & Physical Manifest | Lucian registry |

Historical canonical port range for that runtime generation: 7700–7706.

Presence in this table does not prove current activation, runtime eligibility, routing authority, or governance authority.

See:
- `docs/continuity/LUCIAN_AND_RUNTIME_RECONCILIATION_2026-08-13.md`
- `docs/continuity/AGENT_REGISTRY_EVIDENCE_SNAPSHOT_2026-08-13.md`

## Governance rules

- No agent may expand its own authority.
- Runtime location, implementation presence, conceptual role, and governance authority are distinct facts.
- Exact-head review does not authorize merge.
- Merge does not authorize deployment, migration, or live-case mutation.
- Historical role names do not override the current seat/authority registry.
- UNKNOWN remains UNKNOWN when current evidence is incomplete.

## Coding Agent Instructions

See `.github/copilot-instructions.md` and the candidate `estate/MIRRORNODE_ENGINEERING_DOCTRINE_V1.md`.
