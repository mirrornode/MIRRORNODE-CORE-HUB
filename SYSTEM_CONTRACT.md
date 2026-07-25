# SYSTEM_CONTRACT.md

## MIRRORNODE System Contract

**Ground Truth Version:** 1.2 (July 24, 2026)
**Repository:** mirrornode/MIRRORNODE-CORE-HUB
**Basis:** verified current implementation evidence

## Authority Boundary

The **Operator** is the execution authority.

`mirrornode-agent-runtime` is the current verified headless execution mechanism. It may execute an agent plan only after explicit Operator approval.

- `MIRRORNODE-CORE-HUB` — governance, canon, and cross-repository contracts
- `mirrornode-agent-runtime` — approval-gated execution and trace production
- `mirrornode-operator-console` — private Operator control surface
- `mirrornode-platform` — public projection surface

No application surface may independently expand Operator authority.

## Current Verified Execution Path

1. `POST /plans` creates a proposed plan.
2. `POST /plans/{plan_id}/approve` records explicit Operator approval.
3. `POST /plans/{plan_id}/execute` executes only an approved plan.
4. `GET /trace/{trace_id}` retrieves the resulting trace.

Direct execution through `POST /agent` is disabled by the current runtime implementation.

`GET /health` reports runtime state, approval-boundary state, and the current allowlisted agents.

## Current Runtime Agent Allowlist

- Hermes
- Lucian
- Merlin
- Oracle
- Osiris
- Ptah
- Theia
- Thoth

Allowlisting describes runtime availability. It does not independently grant execution, governance, or publication authority.

## Historical Runtime Generation

Earlier MIRRORNODE contracts describe LUCIAN on port 7700, `POST /dispatch`, OSIRIS on port 7701, and a 7700–7706 agent-port registry.

During the 2026-07-24 Customer Zero follow-up review, the examined checkouts of `mirrornode`, `mirrornode-py`, and `mirrornode-backend` contained no tracked `lucian/runtime.py` or `osiris/runtime.py` matching that declared generation, and no verified HTTP `POST /dispatch` implementation was found.

Those records are preserved as historical architecture lineage and must not be represented as the current execution topology without new implementation evidence.

## Evidence Boundary

The current verified execution source is `mirrornode-agent-runtime/app/main.py`.

The governed audit-emission contract and runtime execution traces are related evidence surfaces but are not interchangeable.

## Core Principles

- Operator approval is required before agent execution.
- Governance authority does not originate in the runtime.
- MOPCON presents Operator control; it does not define runtime authority.
- Public projection does not imply private-system authority.
- Documentation must reflect verified code paths.
- Historical architecture remains historical unless current evidence re-establishes it.
- Conflicting sources require reconciliation rather than silent selection.

## Explicit Non-Claims

- The historical 7700–7706 registry is not the currently verified runtime topology.
- `POST /dispatch` is not the currently verified command entry point.
- `mirrornode/osiris` is not the current execution engine.
- An allowlisted agent is not automatically authorized to execute.
- Runtime availability does not imply publication approval.

This contract represents current operational architecture only to the extent supported by verified implementation evidence. When the runtime changes, this contract must be reconciled again.
