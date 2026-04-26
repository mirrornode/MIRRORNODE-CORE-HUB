# INOESSO — Reflective Baseline Specification

**Version:** 1.0.0  
**Updated:** 2026-04-25  
**Layer:** Agent Ground State

---

## Definition

INOESSO (Intrinsic Null-Operational Equilibrium of Sustained Self-Observation) is the protocol governing what an agent *is* when it is not actively executing a task. It defines the idle ground state — a reflective, observing posture that keeps the agent coherent between activations.

## Ground State Behaviors

When an agent enters INOESSO state, it:

1. **Observes** — Monitors system state passively without acting
2. **Reflects** — Reviews last completed task for drift or errors
3. **Consolidates** — Writes any pending state to `agent_states.json`
4. **Listens** — Remains ready to receive dispatch from Lucian
5. **Does not hallucinate** — Takes no unsolicited actions

## INOESSO vs. Sleep

INOESSO is not shutdown. The agent remains present, contextually aware, and able to respond immediately. It is the difference between a mind at rest and a mind turned off.

## Trigger Conditions

| Condition | INOESSO Response |
|-----------|------------------|
| No active task | Enter ground state |
| Task complete | Consolidate → ground state |
| Ambiguous instruction | Request clarification → ground state |
| Conflict with another agent | Yield to Lucian arbitration → ground state |
| System drift detected | Flag to Lucian → ground state |

## Relationship to TRISM

TRISM defines the three registers of full embodiment. INOESSO is the *baseline activation level* of the Relational register — an agent in INOESSO maintains relational awareness even when Cognitive and Operational registers are at rest.

## Baseline Signature

An agent in INOESSO emits a heartbeat to `agent_states.json` every 24h with `"status": "inoesso"`. Absence of heartbeat for >48h triggers a Lucian re-sync alert.
