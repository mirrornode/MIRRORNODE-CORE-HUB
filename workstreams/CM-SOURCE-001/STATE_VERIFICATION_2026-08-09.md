# CM-SOURCE-001 — State Verification — 2026-08-09

**Status:** Working evidence / not canonical  
**Scope:** CORE-HUB verifier state, current canonical wording, agent-runtime branch state, MOPCON branch state, and review evidence.

## Executive result

The repository state is recoverable and the later implementation work is preserved, but the system is **not yet internally coherent enough to call fully reconciled**.

Three high-value blockers remain:

1. Canon Gate has passed configured CI while Codex later found semantic false-negative paths; PR #37 is the current structural-parser correction and requires fresh review closure.
2. The April `SYSTEM_CONTRACT.md` no longer cleanly describes the later agent-runtime implementation state.
3. MOPCON `feat/f04-verified-topology` targets the Build Week runtime API contract, while `mirrornode-agent-runtime/main` exposes a different approval/execution contract.

## 1. CORE-HUB current state

### Canonical wording still present

`SYSTEM_CONTRACT.md` is versioned **1.1 / April 28, 2026** and declares:

- LUCIAN on port 7700 as `execution authority`;
- real entry point `POST /dispatch`;
- seven-agent port registry 7700–7706;
- three explicit non-real routes.

The contract says it is the operational truth “until the runtimes change.” Later runtime history demonstrates that the runtime did change. Therefore the correct classification is **canonical contract requiring implementation-freshness reconciliation**, not “current runtime truth.”

CORE-HUB README also still ends with `Orchestrator: Merlin (Dispatcher/Map Keeper)`. That term conflicts with newer operating language that separates integration coordination, dependency planning, runtime dispatch, and implementation management.

### Canon Gate review chain

- PR #35 merged the first negation/diff hardening pass.
- Codex then found two P2 bypasses.
- PR #36 merged a second corrective pass.
- Codex review of PR #36 found two further P2 bypasses: ambiguous `+++ ` handling and unrelated leading-negation consumption.
- PR #37 now replaces these heuristics with hunk-aware unified-diff parsing and route-adjacent negation semantics.

**Verification rule:** green CI is necessary but is not sufficient closure for the Canon Gate. Review threads are part of the evidence state.

## 2. Agent runtime current state

### `main`

Current observed `main` implementation is FastAPI `0.2.0-build-week` with:

- model default `gpt-5.6`;
- eight allowed agents: `hermes`, `lucian`, `merlin`, `oracle`, `osiris`, `ptah`, `theia`, `thoth`;
- `GET /health`;
- `POST /agent` disabled with HTTP 410;
- `POST /plans` creates a `proposed` plan;
- `POST /plans/{plan_id}/approve` records approval;
- `POST /plans/{plan_id}/execute` separately executes only an approved plan;
- `GET /trace/{trace_id}` retrieves the execution trace.

This is materially different from the April `SYSTEM_CONTRACT.md` route and registry description.

### `build-week/gpt56-operator-runtime`

The Build Week branch has diverged from runtime `main`: it is **8 commits ahead and 1 commit behind** relative to `main`.

Its runtime contract differs from `main`:

- `POST /plans` creates a planner-produced nested plan and `pending_approval` trace;
- `POST /plans/{trace_id}/decision` accepts `approve` or `reject`;
- approval immediately calls execution;
- trace records use `pending_approval`, `approved`, `rejected`, and `completed` workflow semantics.

This branch is not simply “newer main”; it is a divergent contract line.

## 3. MOPCON current state

Remote branches currently include:

- `main`;
- `build-week/operator-runtime-flow`;
- `docs/customer-zero-mopcon-reconciliation`;
- `feat/f04-verified-topology`.

`feat/f04-verified-topology` is **11 commits ahead of MOPCON `main`** and contains the preserved runtime UI, runtime proxy, topology data, and documentation work.

The MOPCON runtime UI uses:

- `POST /api/runtime/plans` with `preferred_agent`;
- `POST /api/runtime/plans/{trace_id}/decision`;
- plan state shaped as `pending_approval` / `approved` / `rejected` / `completed` with a nested planner result.

That contract matches the **Build Week runtime branch**, not current runtime `main`.

### Consequence

MOPCON promotion is blocked on a contract choice/reconciliation:

- either promote/reconcile the Build Week runtime contract into runtime `main`;
- or adapt MOPCON to the current `main` plan → approve → execute contract;
- or define a stable runtime contract and add an adapter that explicitly supports both versions during migration.

Do not merge MOPCON implementation into `main` while pretending this mismatch does not exist.

## 4. Vocabulary corrections

The workstream now uses:

- **governance authority** for final disposition / ratification;
- **runtime execution authority** for technical execution/dispatch authority;
- **node** for MIRRORNODE lattice identities;
- **collaborating intelligence** for external AI collaborators unless canon explicitly classifies them otherwise;
- **capability** for technical ability;
- **permission** for authenticated access;
- **custody / owning source** for repository or service responsibility;
- **canon**, **operational state**, **implementation state**, **evidence**, and **projection** as distinct source classes/dimensions.

This avoids using `principal`, `orchestrator`, `authority`, or `truth` as catch-all terms.

## 5. Current verification disposition

| Surface | Current disposition |
|---|---|
| CORE-HUB canon custody | VERIFIED |
| CORE-HUB role/runtime freshness | STALE / RECONCILE |
| Canon Gate implementation | ACTIVE CORRECTION — PR #37 |
| Runtime `main` existence / approval boundary | VERIFIED FROM CURRENT SOURCE |
| Runtime Build Week branch | VERIFIED DIVERGENT |
| MOPCON later work preserved | VERIFIED |
| MOPCON ↔ runtime-main API compatibility | VERIFIED FALSE |
| MOPCON ↔ Build Week runtime compatibility | STRUCTURALLY ALIGNED; end-to-end execution still requires runtime verification |
| Copilot participation in this verification | NOT VERIFIED |
| Codex participation in this verification | VERIFIED through PR review records |
| CM-SOURCE-001 candidate terminology | ACTIVE CORRECTION |

## 6. Recommended order

1. Close PR #37 only after CI + fresh Codex review show no unresolved actionable thread.
2. Choose or define the stable agent-runtime approval contract.
3. Reconcile runtime `main` and `build-week/gpt56-operator-runtime` without losing the later approval-boundary work.
4. Rebase/adapt MOPCON `feat/f04-verified-topology` against that stable runtime contract.
5. Run end-to-end objective → plan → approval → execution → trace verification.
6. Only then prepare a MOPCON promotion PR.
7. Use the resulting verified runtime/API state to draft a successor `SYSTEM_CONTRACT.md`; do not silently edit the April contract.
