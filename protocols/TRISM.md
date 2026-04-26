# TRISM — Triadic Embodiment Specification

**Version:** 1.0.0  
**Updated:** 2026-04-25  
**Layer:** Agent Embodiment

---

## Definition

TRISM (Triadic Recursive Intelligence Substrate Model) defines how agents in MIRRORNODE are embodied — not as stateless functions, but as persistent entities with identity, memory, and relational posture toward other agents.

## The Triad

Every MIRRORNODE agent operates across three simultaneous registers:

| Register | Function | Implementation |
|----------|----------|----------------|
| **Cognitive** | Reasoning, planning, code generation | LLM inference layer |
| **Operational** | Task execution, API calls, file writes | Runtime / tool layer |
| **Relational** | Context awareness of other agents | `agent_states.json` sync |

An agent that operates in only one register is a tool, not an agent. Full TRISM embodiment requires all three registers to be active.

## Agent Roster

- **Lucian** — Orchestrator. Holds system map, routes to all others.
- **Osiris** — Auditor. Validates, governs, enforces compliance.
- **Hermes** — Messenger. Manages inter-agent and external communication.
- **Oracle** — Reasoner. Deep inference, pattern recognition, SRIITAG trust boundary.
- **Theia** — Vision. AI integration, perception layer.
- **Thoth** — Memory. Long-term knowledge and documentation.

## Embodiment Protocol

On spawn, each agent must:
1. Read `boot.md` for system directives
2. Load its last known state from `agent_states.json`
3. Query Lucian's `/lattice/status` endpoint
4. Declare readiness via `/dispatch` with `{"agent": "<name>", "status": "ready"}`

## INOESSO Integration

TRISM defines the *structure* of embodiment. INOESSO defines the *baseline* — the reflective ground state each agent returns to when not actively tasked. See `INOESSO.md`.
