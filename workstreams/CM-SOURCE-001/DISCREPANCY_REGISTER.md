# CM-SOURCE-001 — Discrepancy Register

**Status:** Active working evidence register  
**Rule:** Do not silently resolve discrepancies. Record evidence, owner, disposition path, and supersession result.

| ID | Claim / surface | Current evidence | Classification | Status | Required action |
|---|---|---|---|---|---|
| D-001 | CORE-HUB is governance canon and promotion register | Current README states CORE-HUB is the governed canonical surface; MASTER_INDEX is active promotion register | Canon ownership | VERIFIED | Preserve |
| D-002 | CORE-HUB current role descriptions reflect present operating model | README last-updated block is 2026-06-29 and names Merlin as Orchestrator | Canon/documentation freshness | STALE / RECONCILE | Review role model; supersede through promotion process if approved |
| D-003 | Workspace is canon | Workspace README explicitly says it is operational workspace, not governance canon or authoritative runtime source | Source ownership | VERIFIED FALSE | Preserve boundary |
| D-004 | Workspace is currently a major operational synthesis surface | Recent commits add decision protocol, metadata standard, continuity log, action queue, institutional evidence/credentials lanes and operating status | Operational state | VERIFIED | Map into source architecture |
| D-005 | MOPCON remote reflects latest known implementation work | Reconciliation on 2026-08-09 found `main` still at the July 10 scaffold, while remote branches preserve later implementation: `build-week/operator-runtime-flow` is 7 commits ahead of `main`; `docs/customer-zero-mopcon-reconciliation` descends from that runtime branch; and `feat/f04-verified-topology` is 11 commits ahead of `main` and contains the runtime flow plus topology/documentation work | Implementation freshness | PARTIALLY RESOLVED | Treat later remote branches as preserved implementation evidence; consolidate the `feat/f04-verified-topology` lineage into one validated promotion PR rather than rebuilding MOPCON |
| D-006 | Perplexity is adequately described by older research/Judge/Librarian framing | Operator reports sustained action-taking and exceptional implementation follow-through | Principal role | STALE / OPERATOR-REPORTED | Inventory current permissions/actions; propose Implementation & Execution Manager role |
| D-007 | Grok is advisory-only | GitHub sent an updated-permissions request for the installed Grok GitHub App on 2026-08-08 | Principal capability | PARTIALLY VERIFIED | Determine exact effective scopes and repositories; separate capability from authority |
| D-008 | Merlin repo README reflects current state | README says role is reasoning/planning/decomposition and status is Initializing | Principal role/state | STALE / UNKNOWN | Reconcile repo implementation and current intended role |
| D-009 | Principal action capability is fully documented | Current records do not yet provide one authoritative effective-capability registry | Governance/operations | GAP | Build Principal & Capability Registry with evidence and review dates |
| D-010 | `@mirror` has one current, enforceable protocol definition | Existing usage/history is distributed and no reconciled protocol is yet promoted in this workstream | Reference/handoff | GAP | Inventory prior definitions and prepare versioned handoff standard |
| D-011 | Canon Gate post-review state is fully closed | PR #35 merged the first workflow hardening pass, but Codex subsequently identified two P2 bypasses on the merged head: unrelated negation text could exempt a prohibited route, and added source beginning with `++` could be mistaken for a diff header | Workflow assurance | ACTIVE CORRECTION | Apply a bounded follow-up patch with regression tests; require green Canon Gate/Audit and close the review findings before treating the gate repair as complete |

## Status vocabulary

- `VERIFIED`
- `VERIFIED FALSE`
- `PARTIALLY VERIFIED`
- `OPERATOR-REPORTED`
- `STALE`
- `UNKNOWN`
- `CONTRADICTORY`
- `GAP`
- `SUPERSEDED`
- `RESOLVED`
- `PARTIALLY RESOLVED`
- `ACTIVE CORRECTION`

Each resolution must retain the prior row and add the resolving evidence rather than deleting history.
