# CM-SOURCE-001 — Discrepancy Register

**Status:** Active working evidence register  
**Rule:** Do not silently resolve discrepancies. Record evidence, custody, disposition path, and supersession result.

| ID | Claim / surface | Current evidence | Classification | Status | Required action |
|---|---|---|---|---|---|
| D-001 | CORE-HUB is governance canon and promotion register | Current README states CORE-HUB is the governed canonical surface; MASTER_INDEX is active promotion register | Canon custody | VERIFIED | Preserve |
| D-002 | CORE-HUB current role descriptions reflect present operating model | README last-updated block is 2026-06-29 and names Merlin as `Orchestrator (Dispatcher/Map Keeper)` while current operating practice separates integration, planning, runtime dispatch, and implementation management | Canon/documentation freshness + terminology | STALE / RECONCILE | Preserve existing canon; prepare explicit successor vocabulary/role map for review |
| D-003 | Workspace is canon | Workspace README explicitly says it is operational workspace, not governance canon or authoritative runtime source | Source class | VERIFIED FALSE | Preserve boundary |
| D-004 | Workspace is currently a major operational synthesis surface | Recent commits add decision protocol, metadata standard, continuity log, action queue, institutional evidence/credentials lanes and operating status | Operational state | VERIFIED | Map into source/custody architecture |
| D-005 | MOPCON remote reflects latest known implementation work | Reconciliation on 2026-08-09 found `main` still at the July 10 scaffold, while remote branches preserve later implementation: `build-week/operator-runtime-flow` is 7 commits ahead of `main`; `docs/customer-zero-mopcon-reconciliation` descends from that runtime branch; and `feat/f04-verified-topology` is 11 commits ahead of `main` and contains the runtime flow plus topology/documentation work | Implementation freshness | PARTIALLY RESOLVED | Treat later remote branches as preserved implementation evidence; consolidate the `feat/f04-verified-topology` lineage into one validated promotion PR rather than rebuilding MOPCON |
| D-006 | Perplexity is adequately described by older research/Judge/Librarian framing | Operator reports sustained action-taking and exceptional implementation follow-through | Collaborator role | STALE / OPERATOR-REPORTED | Inventory current permissions/actions; retain **Implementation & Execution Manager** as an operating-role candidate, not an authority grant |
| D-007 | Grok is advisory-only | GitHub sent an updated-permissions request for the installed Grok GitHub App on 2026-08-08 | Collaborator capability/permission | PARTIALLY VERIFIED | Determine exact effective scopes and repositories; separate capability, permission, and authority |
| D-008 | Merlin role descriptions are current and unambiguous | CORE-HUB README and other materials use planning/orchestration/dispatcher language with different scopes | Node role / terminology | STALE / CONTRADICTORY | Reconcile responsibility boundaries and stop using unqualified `orchestrator` as a catch-all |
| D-009 | Identity capability, permission, and authority are fully documented | No single reconciled registry currently separates node identity, collaborator classification, technical capability, effective permission, runtime execution authority, and governance authority | Governance/operations | GAP | Build the registry defined in `PRINCIPAL_REGISTRY_CANDIDATE.md` and terminology standard |
| D-010 | `@mirror` has one current, enforceable protocol definition | Existing usage/history is distributed and no reconciled protocol is yet promoted in this workstream | Projection/handoff | GAP | Inventory prior definitions and prepare versioned handoff standard |
| D-011 | Canon Gate semantic verification is closed | PR #35 and PR #36 both passed configured CI before later Codex review found additional P2 false-negative paths. PR #36 review specifically found ambiguous `+++ ` handling and unrelated leading-negation consumption. PR #37 now replaces those heuristics with hunk-aware diff parsing and route-adjacent negation rules and is pending fresh CI/Codex verification | Workflow assurance | ACTIVE CORRECTION | Do not treat green CI alone as closure; require PR #37 checks plus fresh Codex review and inspect all review threads before merge |
| D-012 | `SYSTEM_CONTRACT.md` remains implementation-current | The contract is versioned April 28, 2026, declares LUCIAN port 7700 and `POST /dispatch`, and says it remains operational truth until runtimes change. `mirrornode-agent-runtime` later recorded `feat: require operator approval before agent execution` on 2026-07-22, demonstrating that runtime behavior changed after the contract date | Canon vs implementation freshness | STALE / RECONCILE | Inventory the current runtime API/agent registry, compare to the April contract, and prepare an explicit successor contract rather than silently reinterpret the old one |
| D-013 | Workstream vocabulary is coherent | Earlier candidate text used `principal`, `authority`, `orchestrator`, `truth`, and `source of truth` with overlapping meanings and mixed external collaborators with MIRRORNODE nodes | Terminology / architecture readability | ACTIVE CORRECTION | Apply `TERMINOLOGY_STANDARD_CANDIDATE.md`; distinguish node, collaborator, role, capability, permission, authority, custody, evidence, and projection throughout candidate material |
| D-014 | Copilot collaboration state is verified | The current workstream has direct Codex review evidence but no equivalent authenticated inventory confirming Copilot review/permission state | Collaborator integration state | UNKNOWN | Do not claim Copilot verification; inventory it separately if/when a concrete repository integration or review record is available |

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
