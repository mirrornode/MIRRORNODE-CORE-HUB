# Agents — MIRRORNODE-CORE-HUB

> **Routing/registry reconciliation notice — 2026-08-13**
>
> The registry below reflects the earlier Lucian-centered runtime generation and must not be treated, by itself, as the current complete governance registry or current dispatch mandate.
>
> Current repository evidence includes a newer generic agent runtime with an Operator approval boundary and no direct Lucian `/dispatch` execution path. Because the historical registry and newer runtime evidence are not yet fully reconciled into one ratified current registry, **current dispatch/routing authority is UNRESOLVED pending explicit governance reconciliation**.
>
> Until that reconciliation is complete:
> - do not infer new authority from runtime eligibility;
> - do not bypass an applicable existing approval/governance gate;
> - do not treat the historical `POST /dispatch` model as automatically current merely because it is listed below;
> - do not assign a replacement dispatcher by inference.
>
> See `docs/continuity/LUCIAN_AND_RUNTIME_RECONCILIATION_2026-08-13.md` and `docs/continuity/AGENT_REGISTRY_EVIDENCE_SNAPSHOT_2026-08-13.md`.

## Resident Runtime

No agent runtime is hosted in this repository.

## Historical Org-Wide Runtime Registry Snapshot

| Agent | Port | Role | Source |
|---|---|---|---|
| LUCIAN | 7700 | Orchestration & Manifest | `lucian/runtime.py` |
| OSIRIS | 7701 | Payment & Commerce (Stripe) | `osiris/runtime.py` |
| HERMES | 7702 | Messaging & Protocol | Lucian registry |
| THOTH | 7703 | Services & Health | Lucian registry |
| THEIA | 7704 | Witness & Observation | Lucian registry |
| PTAH | 7705 | Creation & Bridge | Lucian registry |
| EVE | 7706 | Embodiment & Physical Manifest | Lucian registry |

Historical canonical port range for that runtime generation: 7700–7706.

This table is retained as historical runtime evidence. Presence does not prove current activation, current runtime eligibility, or current governance authority. Omission does not prove current exclusion.

## Governance Rules

- Agent capability changes must be reflected in current governance/registry evidence before release.
- Agent namespace assignments must be documented before new writes ship.
- No agent may expand its own authority without explicit human authorization.
- Runtime location, runtime eligibility, implementation presence, conceptual role, and governance authority must not be conflated.
- Where current routing authority is unresolved, preserve the conflict and escalate for explicit disposition rather than choosing a dispatcher by inference.

## Coding Agent Instructions

See `.github/copilot-instructions.md`.

## Specialized Terminal-Agent Phase Gate

Specialized coding and terminal agents must follow `docs/orchestration/TERMINAL_AGENT_EXECUTION_PROTOCOL_V0_1.md`.

- When an assignment requires inspection and a report before implementation, all work remains read-only until the report is delivered and a subsequent scoped authorization is recorded.
- Phase descriptions must match actual tool use; an agent may not claim inspection while creating or editing files.
- An authorized file scope binds each path to one explicit operation class (`CREATE`, `MODIFY`, `DELETE`, `MOVE`, `RENAME`, `RESTORE`); permission to modify a file is not permission to delete, move, rename, create, or restore it.
- Authorization must carry an explicit status and bounded validity. Revoked, superseded, or expired authorization supports no further work, and a missing expiry is never read as indefinite permission.
- Verification is not continued implementation authority. It runs only declared checks and may touch only declared artifact paths, never the implementation source allowlist.
- Premature mutations must be preserved in place, reported with exact paths and diffs, and placed in `BLOCKED_PREMATURE_MUTATION`; they must not be hidden through restore, deletion, formatting, stash, commit, or push.
- A premature-mutation report must include a structurally parsed worktree status whose path identities exactly match the declared changed paths and per-path diff evidence.
- Handing off requires a recorded completion report stating final head, changed paths, checks run, unresolved findings, whether any external mutation occurred, and the next disposition required.
- Authorization for implementation does not imply authorization to commit, push, mutate a pull request, merge, deploy, approve, or execute.
- Runtime eligibility, role identity, credentials, write access, and green checks do not create authority.
