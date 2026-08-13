# MIRRORNODE Naming and Source-Scope Reconciliation — 2026-08-13

Status: Evidence-grounded clarification for review  
Authority: Documentation clarification only; does not ratify new authority, activate agents, authorize execution, or resolve open Council matters.

## Purpose

Reduce naming and source-scope drift discovered during the Continuity Unification Assessment without erasing historical artifacts or treating stale descriptions as current authority.

This document distinguishes:

- current organization-level governance;
- index/reference surfaces;
- named agent roles;
- functional orchestration concepts;
- overloaded historical names;
- unresolved items that still require Operator disposition.

## 1. Source precedence for this reconciliation

When descriptions conflict, this pass uses the following evidence order:

1. explicit Operator disposition;
2. ratified CORE-HUB Council/canon records;
3. current merged CORE-HUB governance/source maps;
4. current dedicated-repository manifests;
5. draft workspace manifests/specifications;
6. historical snapshots and self-descriptions;
7. conversation summaries.

A lower-ranked artifact is not deleted merely because it is stale. It is classified as historical, draft, scoped, or unresolved.

## 2. Governance and index naming

### MIRRORNODE-CORE-HUB

Current role: **organization-level governance and canonical governance record**.

Evidence:

- `GOVERNANCE.md`: "This repository holds organization-level governance."
- `GOVERNANCE.md`: `main` is the canonical governance record.
- `CANONICAL_SOURCES.md`: lists `MIRRORNODE-CORE-HUB` under Governance.

Clarification: CORE-HUB is the authority surface for organization-level governance. This does not mean every historical or operational artifact belongs inside CORE-HUB.

### mirrornode-index

Current CORE-HUB-scoped role: **Cross-Repo Index**.

Evidence:

- `CANONICAL_SOURCES.md` explicitly names `mirrornode-index` as `Cross-Repo Index`.
- `mirrornode-index/GOVERNANCE.md` describes `main` as the "canonical index state" and requires index entries to reflect real repository state.

Historical naming conflict:

- `mirrornode-index/README.md` calls the repo the "authoritative index for the MIRRORNODE system" and says it contains canonical system descriptions.
- `mirrornode-index/canon/MASTER_CANON.md` labels itself `MASTER (INTERNAL, AUTHORITATIVE)`.

Reconciliation:

- "authoritative" inside `mirrornode-index` is interpreted as authority over **index/reference state**, not organization-level governance.
- `mirrornode-index` must not override CORE-HUB governance where the two conflict.
- its existing `MASTER_CANON.md` is preserved as historical/reference evidence pending a separate decision about whether to rename, scope, migrate, or retire that internal document.

This clarification does not delete or rewrite `mirrornode-index` content.

## 3. Merlin, Hermes, and "Orchestrator"

### Merlin

Current evidence-supported role: **planning, sequencing, dependency mapping, orchestration advice**.

Evidence:

- `mirrornode-merlin/agent/manifest.yaml`: role `reasoning`; capabilities include task planning, LLM orchestration, goal tracking, and cognitive synthesis.
- `mirrornode-workspace/MERLIN_SEQUENCING_MANIFEST_v0_1.md`: planning/sequencing only; no autonomous execution or canon control.
- the same manifest explicitly blocks bypassing Hermes routing, authorizing execution, ratifying canon, and assigning authority by dependency order.

Naming rule:

- Do not call Merlin "the dispatcher" unless a later ratified record explicitly grants that role.
- "Merlin can say what should happen next" is a sequencing function, not execution authorization.

### Hermes

Current evidence-supported role: **advisory routing, progress reporting, registry-evidence collection, and handoff/event routing**.

Evidence:

- `mirrornode-workspace/HERMES_ROUTING_MANIFEST_v0_1.md`: routing, progress reporting, registry evidence collection.
- Hermes does not implement, ratify manifests, rewrite canon, promote agents, or convert routing into approval.

Naming rule:

- Hermes may route or recommend routing within its bounded lane.
- Routing is not approval and does not create authority.

### Orchestrator

Current evidence-supported meaning: **a capability-based coordination function**, not automatically a sovereign node name or authority seat.

Evidence:

- `docs/agent-stack/orchestrator/MODULAR_ADAPTIVE_ORCHESTRATOR_SPEC_v0_1.md` and its ratification appendix define an orchestrator that classifies work, resolves capability/service-area fit, applies policy gates, and produces reviewable routing recommendations.
- those documents explicitly state that the orchestrator does not grant authority, approve execution, ratify canon, promote agents, or bypass review.

Naming rule:

- `orchestrator` describes a system function unless a separately ratified node/seat record says otherwise.
- A provider product exposing an "Orchestrator" mode is an adapter/capability signal, not automatic MIRRORNODE authority.

## 4. ROTAN namespace split

The word `ROTAN` currently refers to multiple non-identical artifacts. They must not be collapsed into one thing by name alone.

### ROTAN architecture layer

Canonical historical definition in CORE-HUB:

- `protocols/ROTAN.md`: **Recursive Ontological Topology Architecture Node**.
- Function: structural grammar / topology classification across REVENUE, CORE, SURFACE, and EXPERIMENT tiers.

Use the label: **ROTAN architecture layer** or **ROTAN topology protocol**.

### Rotan-Q node

Dedicated agent repository:

- `mirrornode-rotan/agent/manifest.yaml`
- Display identity: **Rotan-Q**
- `node_id: rotan`
- role: `signal`
- capabilities include signal processing, pattern recognition, quantum cognitive modeling, and entropy routing.

Use the label: **Rotan-Q node**.

### Rotan-demo

- Separate repository.
- Current live repository size is zero.
- Historical CORE-HUB map classifies it as legacy and associates it with a Pillars of Rotan demo.

Use the label: **Rotan-demo repository**. Do not treat it as the Rotan-Q node or the ROTAN architecture layer.

### rotan-resonance

- Separate private repository.
- Treat as a distinct experimental/historical surface unless later evidence establishes a governed relationship.

Use the label: **rotan-resonance repository**.

### "Pillars of ROTAN"

Status: **UNRESOLVED ARTIFACT NAME**.

Current repository search finds references to the phrase, but no uniquely verified, non-empty canonical artifact that can safely be declared "the Pillars of ROTAN".

Do not alias this phrase to Rotan-Q, ROTAN topology protocol, Rotan-demo, or rotan-resonance without additional evidence or Operator disposition.

## 5. Repository census drift

`REPO_MAP.md` is an April 28, 2026 snapshot listing 27 repositories. The current GitHub organization inventory contains 35 accessible MIRRORNODE repositories.

Therefore:

- `REPO_MAP.md` remains useful as a historical classification snapshot;
- its repo count and some statuses must not be represented as current without refresh;
- newly created repositories such as `mirrornode-agent-runtime`, `mirrornode-operator-console`, `mirrornode-workspace`, `mn-supply-continuity`, `mirrornode-parallax`, and the dedicated agent repos require current classification before a replacement live map is promoted.

A new census should preserve historical status rather than silently overwrite it.

## 6. Draft workspace records are not current authority by themselves

The `mirrornode-workspace` agent-stack and orchestrator documents contain valuable design work, but several are explicitly marked Draft, pending boundary ratification, or advisory-scope confirmation.

Rule:

- use these documents as design evidence and candidate role definitions;
- do not use a draft workspace manifest to override later ratified CORE-HUB decisions or explicit Operator dispositions;
- where a workspace draft conflicts with a ratified Council record, preserve the conflict and prefer the ratified record.

## 7. Names still requiring separate reconciliation

The following are intentionally NOT resolved by this document:

- Lucian's layered roles across audit/coherence, orchestration, memory/Librarian, and runtime execution history;
- Eve/Bastet product-lattice status;
- the current complete confirmed-agent registry;
- whether `mirrornode` is legacy, orchestration root, or a historical monorepo with a narrower retained role;
- final treatment of `mirrornode-index/canon/MASTER_CANON.md` and associated public/internal canon files;
- the exact placement and authority of Librarian as a seat versus a capability;
- CG-0033 MICC/MIM disposition.

These require evidence or Operator disposition beyond naming cleanup.

## 8. Immediate operating vocabulary

Until superseded by stronger authority:

| Term | Use |
|---|---|
| CORE-HUB | organization-level governance / canonical governance record |
| mirrornode-index | cross-repo index / reference surface |
| Merlin | planning, sequencing, dependency mapping, orchestration advice |
| Hermes | advisory routing, progress reporting, registry-evidence collection |
| orchestrator | capability-based coordination function; no authority by name alone |
| ROTAN architecture layer | topology / structural grammar protocol |
| Rotan-Q node | signal-processing agent identity in `mirrornode-rotan` |
| Rotan-demo | separate legacy/empty demo repository |
| rotan-resonance | separate experimental/historical repository |
| Pillars of ROTAN | unresolved artifact name; do not alias by assumption |

## Boundary

This reconciliation is intended to reduce accidental name inheritance and stale-source promotion. It does not create new authority, change node sovereignty, authorize implementation, or close any unresolved governance matter.
