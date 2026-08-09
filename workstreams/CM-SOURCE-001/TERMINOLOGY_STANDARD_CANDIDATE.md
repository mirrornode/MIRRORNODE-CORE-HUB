# CM-SOURCE-001 — Terminology Standard Candidate

**Status:** Candidate / not canonical  
**Purpose:** Establish one coherent vocabulary for governance, implementation, node identity, collaboration, and evidence before any promotion work proceeds.

## Core terms

### Operator / Siseon
The human final decision authority for MIRRORNODE priorities, ratification, covenants, exceptions, and consequential governance dispositions.

### Node
A named MIRRORNODE presence within the lattice. Node identity, role, capability, permission, and authority are separate properties and MUST NOT be collapsed into one another.

### Collaborating intelligence
An external AI collaborator participating in MIRRORNODE work without being silently promoted into the canonical node registry. Examples may include Perplexity, Gemini, Grok, Codex, or Copilot unless and until canon explicitly classifies them otherwise.

### Role
The responsibility or function a node, collaborator, person, repository, or service is expected to perform. A role is descriptive and does not itself grant permission or authority.

### Capability
What an actor or system can technically do, based on demonstrated behavior or verified interface support.

### Permission
What an authenticated identity is currently allowed to do in a particular service, repository, account, or environment.

### Authority
The right to decide, approve, ratify, veto, or direct an action within a defined governance envelope. Authority MUST NOT be inferred from capability, permission, trust, reliability, or implementation ownership.

### Runtime execution authority
Authority within a runtime or execution protocol to dispatch or perform a defined technical action. This is narrower than governance authority and MUST be named as such whenever there is risk of confusion.

### Custody / owning source
The repository, service, or record responsible for maintaining the authoritative implementation or operational record for a given surface. Custody does not create governance authority.

### Canon
Ratified MIRRORNODE governance state and its explicit supersession history. Canon governs until replaced through the established promotion process.

### Operational state
A current, provenance-backed account of what is happening now across owning sources. Operational state may be newer than canon but does not silently supersede canon.

### Implementation state
The code, configuration, deployment, API, or service behavior that actually exists in the owning implementation surface.

### Evidence
The attributable material that supports a claim: commits, reviews, tests, authenticated service records, decisions, receipts, deployments, correspondence, or other verifiable records.

### Review verdict
A bounded assessment produced by a designated reviewer such as Ptah, Thoth, Osiris, Oracle, Codex, or another reviewer. A review verdict is not ratification unless canon explicitly grants that reviewer the relevant disposition authority.

### Projection
A derived view of authoritative information for another audience or interface, such as MOPCON, `@mirror`, or a public-facing status surface. A projection MUST retain provenance and MUST NOT become a competing source of truth.

## Naming rules

1. Use **governance authority** when referring to ratification, final disposition, covenants, or policy decisions.
2. Use **runtime execution authority** when referring to technical dispatch or execution inside a runtime.
3. Use **permission** for authenticated service access; never substitute **authority**.
4. Use **capability** for demonstrated technical ability; never substitute **permission** unless the access is verified.
5. Use **node** only for MIRRORNODE identities that are treated as nodes by the relevant canonical or candidate registry. Use **collaborating intelligence** for external AI collaborators until classification is explicitly resolved.
6. Use **owning source** or **custody** for repository/service responsibility; never call repository ownership an authority grant.
7. Use **candidate**, **observed**, **operator-reported**, **verified**, **stale**, **contradictory**, and **ratified** explicitly. Avoid generic words such as “truth” when the source class can be named more precisely.
8. Avoid overloaded titles such as **orchestrator** unless the scope is stated. Prefer phrases such as **integration coordinator**, **runtime dispatcher**, **dependency planner**, or **implementation manager** when those are the actual responsibilities.

## Current reconciliation implications

- Siseon is the final governance authority. This does not conflict with a node holding narrower runtime execution authority.
- THEIA should be described as integration, continuity, reconciliation, and operating coordination; the term **orchestrator** is too overloaded to use without a scope qualifier.
- The current `SYSTEM_CONTRACT.md` uses **LUCIAN — execution authority**. Until that contract is superseded, interpret this specifically as the declared runtime execution authority of that contract, not as final MIRRORNODE governance authority.
- The current CORE-HUB README names Merlin as **Orchestrator (Dispatcher/Map Keeper)**, while newer operating descriptions separate integration, planning, and execution management among several participants. This is a documented vocabulary/state discrepancy and requires formal reconciliation rather than silent reinterpretation.
- Perplexity's candidate title **Implementation & Execution Manager** describes an operating responsibility. It does not grant governance authority or imply unrestricted service permission.

## Promotion requirement

No candidate architecture should be promoted until its key terms can be read consistently under this vocabulary or an explicitly approved successor vocabulary.
