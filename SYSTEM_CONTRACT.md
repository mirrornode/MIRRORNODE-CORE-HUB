# SYSTEM_CONTRACT.md

> **Historical runtime contract notice (2026-08-13):** This document records the verified Lucian-centered runtime generation as of **April 28, 2026**. Its own boundary states that it remains operational truth only until the runtimes change. The runtimes have since changed: current `mirrornode-agent-runtime` uses a generic plan → Operator approval → execute → trace lifecycle and does not expose this document's Lucian `/dispatch` boundary as the current execution path. Preserve this file as historical operational evidence; do not use its embedded agent registry or Lucian execution-authority claim as the current governance registry without reconciliation. See `docs/continuity/LUCIAN_AND_RUNTIME_RECONCILIATION_2026-08-13.md`.

## MIRRORNODE System Contract

**Ground Truth Version:** 1.1 (April 28, 2026)  
**Repository:** mirrornode/MIRRORNODE-CORE-HUB

### Execution Authority
**LUCIAN (Port 7700)** — Orchestration & Manifest — execution authority  
**Real Entry Point:** `POST /dispatch`

### Lattice Truth Surface
- `GET /manifest`
- `GET /lattice/status`
- `GET /health`
- `GET /heartbeat`
- `GET /identity`

### Audit Mechanism
`emit_audit(repo, event_type, actor, verdict, evidence)`

### Core Principles
- Nodes do not self-route
- LUCIAN dispatches commands through canon
- No silent failures
- Documentation must reflect real code paths only

### Confirmed Agent Registry
| Agent | Port | Role | Source |
|---|---:|---|---|
| LUCIAN | 7700 | Orchestration & Manifest | `lucian/runtime.py` |
| OSIRIS | 7701 | Payment & Commerce (Stripe) | `osiris/runtime.py` |
| HERMES | 7702 | Messaging & Protocol | Lucian registry |
| THOTH | 7703 | Services & Health | Lucian registry |
| THEIA | 7704 | Witness & Observation | Lucian registry |
| PTAH | 7705 | Creation & Bridge | Lucian registry |
| EVE | 7706 | Embodiment & Physical Manifest | Lucian registry |

### Canon Structure
- `canon/contracts/`
- `canon/charters/`
- `canon/api/`
- `canon/dossiers/`

### Explicit Non-Claims
- `/system/execute` is not a real route
- `/system/replay` is not a real route
- `/execute-task` is not a real route
- `mirrornode/osiris` is not the execution engine

This file is the operational truth until the runtimes change.
