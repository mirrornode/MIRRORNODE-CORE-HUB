# Agents — MIRRORNODE-CORE-HUB

## Resident Runtime

No agent runtime is hosted in this repository.

## Org-Wide Agent Registry

| Agent | Port | Role | Source |
|---|---|---|---|
| LUCIAN | 7700 | Orchestration & Manifest | `lucian/runtime.py` |
| OSIRIS | 7701 | Payment & Commerce (Stripe) | `osiris/runtime.py` |
| HERMES | 7702 | Messaging & Protocol | Lucian registry |
| THOTH | 7703 | Services & Health | Lucian registry |
| THEIA | 7704 | Witness & Observation | Lucian registry |
| PTAH | 7705 | Creation & Bridge | Lucian registry |
| EVE | 7706 | Embodiment & Physical Manifest | Lucian registry |

Canonical port range: 7700–7706. Any agent claiming a port outside this range must be registered in AGENTS_TODO.md first.

## Governance Rules

- Agent capability changes must be reflected here before release.
- Agent namespace assignments must be documented before new writes ship.
- No agent may expand its own authority without explicit human authorization.
- Runtime location and conceptual role must not be conflated.

## Coding Agent Instructions

See `.github/copilot-instructions.md`.
