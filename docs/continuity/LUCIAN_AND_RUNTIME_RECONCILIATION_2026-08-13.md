# Lucian and Runtime Reconciliation — 2026-08-13

Status: Evidence-grounded clarification for review  
Authority: Documentation clarification only; no new execution authority, node activation, canon promotion, or deployment is authorized.

## Finding

The April 28, 2026 `SYSTEM_CONTRACT.md` explicitly states that it is operational truth **until the runtimes change**.

The runtimes have changed.

The current `mirrornode-agent-runtime` uses a generic plan lifecycle:

1. create proposed plan;
2. obtain Operator approval;
3. execute only an approved plan;
4. emit a trace record.

Direct `/agent` execution is disabled with HTTP 410. The current runtime does not expose the historical Lucian `POST /dispatch` entrypoint as its execution boundary.

Therefore, the April 28 statement that Lucian is the live execution dispatcher is classified as **historical operational truth for that runtime generation**, not current execution authority.

## Lucian namespace layers

### Lucian Prime

Source: `canon/charters/LUCIAN_PRIME.md`

Locked charter role:

> Audit Oversight & Lattice Coherence Authority

This remains the strongest locked identity statement found for Lucian Prime. This reconciliation does not alter it.

### Historical CORE-HUB Lucian runtime

Source: `lucian/runtime.py` + April 28 `SYSTEM_CONTRACT.md`

Historical implementation characteristics:

- FastAPI service on port 7700;
- `/dispatch` routed commands through the canon command palette;
- `/manifest` exposed an embedded lattice registry;
- role strings included both `Audit Oversight & Lattice Coherence Authority` and `Orchestration & Manifest`;
- the embedded registry included LUCIAN, OSIRIS, HERMES, THOTH, THEIA, PTAH, and EVE.

Classification: **historical runtime implementation retained as evidence/code unless separately retired**. Its presence in CORE-HUB does not prove that it is the current execution surface.

### Dedicated `mirrornode-lucian` repository

Source: `mirrornode-lucian/agent/manifest.yaml`

Manifest role: `memory`

Capabilities:

- long-term memory;
- semantic search;
- knowledge graph;
- context injection.

Classification: **dedicated Lucian implementation facet / candidate node manifest**. The manifest demonstrates a memory-oriented implementation identity but does not, by itself, supersede the locked Lucian Prime charter or grant governance/execution authority.

### Current generic agent runtime

Source: `mirrornode-agent-runtime/app/main.py`

Current runtime facts:

- version `0.2.0-build-week`;
- allowlist contains `oracle`, `thoth`, `osiris`, `ptah`, `theia`, `merlin`, `hermes`, and `lucian`;
- direct agent execution is disabled;
- execution requires an approved plan;
- approval and execution are separate state transitions;
- execution writes a trace record.

Important distinction:

The runtime allowlist is a **technical eligibility list**, not a governance registry. Name presence in `ALLOWED_AGENTS` does not confer authority, ratification, or confirmed-node status.

## Current operating interpretation

Until superseded by stronger authority:

- **Lucian Prime** refers to the locked audit-oversight/lattice-coherence identity.
- **Lucian historical dispatcher** refers specifically to the April CORE-HUB runtime generation and must not be assumed to describe current execution architecture.
- **Lucian memory implementation** refers to the dedicated `mirrornode-lucian` manifest/repository facet.
- **Lucian in `mirrornode-agent-runtime`** is an eligible role-bound runtime target subject to the generic Operator approval boundary; eligibility is not authority.

These layers may later be reconciled into a single versioned Lucian contract, but this document does not collapse them prematurely.

## Registry consequence

The `SYSTEM_CONTRACT.md` "Confirmed Agent Registry" is also tied to the historical runtime generation because it is sourced primarily from the old Lucian embedded registry.

It must not be used as the current complete governance registry without fresh reconciliation.

Specifically:

- omission from that April table does not prove a current node is invalid;
- presence in that table does not prove a node remains currently active or ratified;
- the newer generic runtime's eight-name allowlist does not replace it as governance registry;
- a current registry must distinguish at least: identity, implementation surface, runtime eligibility, governance status, authority boundary, source evidence, and last review date.

## Immediate routing consequence

Do not route work on the assumption that Lucian is the universal dispatcher.

For current work:

- sequencing can be proposed by Merlin within its advisory boundary;
- routing can be handled/recommended by Hermes within its advisory boundary;
- current execution through `mirrornode-agent-runtime` requires explicit plan approval;
- governance authority remains external to runtime eligibility and must be established by CORE-HUB / Operator disposition and applicable ratified boundaries.

## Still unresolved

This document does not decide:

- whether Lucian Prime should eventually absorb the memory/Librarian implementation;
- whether the historical `/dispatch` runtime should be formally deprecated or retained as a compatibility/reference implementation;
- whether a future Lucian seat should hold any orchestration capability beyond coherence oversight;
- final complete agent registry status;
- Eve/Bastet status;
- Librarian seat/capability placement.

Those require separate evidence or Operator disposition.
