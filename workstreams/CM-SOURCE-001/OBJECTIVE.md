# CM-SOURCE-001 — MIRRORNODE State, Authority & Source Reconciliation

**Status:** APPROVED FOR DISCOVERY / RECONCILIATION  
**Operator authorization:** Granted 2026-08-09  
**Promotion state:** Candidate only; no canon change without the existing evaluation and Operator-ratification path  

## Objective

Reconcile MIRRORNODE governance, current operational state, implementation custody, node and collaborator roles, verified capabilities and permissions, authority boundaries, evidence standards, handoff conventions, and external projections into one readable and auditable operating model.

This work preserves prior canon as history. A stale or contradicted canonical statement is recorded as a discrepancy until it is explicitly superseded through the established promotion process.

The vocabulary for this workstream is defined in `TERMINOLOGY_STANDARD_CANDIDATE.md`. Where an older artifact uses an overloaded term such as **authority**, **orchestrator**, **principal**, or **truth**, this workstream MUST state the intended scope rather than silently inherit the ambiguity.

## Authority and participation

- **Operator / Siseon** — final governance disposition, ratification, priorities, covenants, and exceptions.
- **THEIA** — integration, continuity, reconciliation, operating coordination, discrepancy custody, and cross-lane synthesis. THEIA prepares and coordinates; THEIA does not self-ratify or override Ptah evaluation or Thoth security verdicts.
- **MIRRORNODE nodes** — named lattice presences whose current identity, runtime role, capability, permission, and authority must be separately evidenced.
- **Collaborating intelligences** — external AI collaborators such as Perplexity, Gemini, Grok, Codex, or Copilot unless and until a canonical registry explicitly classifies them as MIRRORNODE nodes.

### Current collaborator lanes

- **Perplexity** — candidate operating title: **Implementation & Execution Manager**; converts approved direction into verified implementation progress and returns evidence/receipts within verified permissions.
- **Gemini** — broad-context synthesis, alternative framing, product/visual perspective, and contradiction discovery.
- **Codex / Copilot** — implementation and code-review collaborators used as adversarial verification surfaces; review output is evidence, not ratification.
- **Grok** — implementation/adversarial/prototyping collaborator; effective permissions require separate verification.

### Review lanes

- **Ptah** — evaluation/promotion gate under current CORE-HUB governance; candidate changes do not bypass Ptah.
- **Thoth** — security-boundary review and security verdicts where applicable.
- **Osiris** — structural assurance/audit review against declared policy and evidence.
- **Oracle** — evidence sufficiency and claim-verifiability review.
- **Merlin** — decomposition, dependency mapping, sequencing, and coordination architecture, subject to reconciliation with stale role descriptions.

## Required separations

1. Role does not imply capability.
2. Capability does not imply permission.
3. Permission does not imply governance authority.
4. Runtime execution authority is narrower than governance authority and must be named explicitly.
5. Repository/service custody does not imply governance authority.
6. Operational state does not silently supersede canon.
7. Canon does not prove that an implementation still matches it.
8. Every consequential action should retain actor, authority basis, changed artifact, evidence, and receipt where available.

## Source classes under review

### CANON — what has been ratified
Primary governed surface: `MIRRORNODE-CORE-HUB` and its explicit promotion records.

### OPERATIONAL STATE — what is happening now
A provenance-backed synthesis resolved from current owning sources. `mirrornode-workspace` may carry current business/continuity synthesis but does not override canon or implementation evidence.

### IMPLEMENTATION STATE — what actually exists or executes
Owned by the repository, deployment, or authenticated service implementing the surface, including:

- `mirrornode-agent-runtime` — current runtime implementation evidence;
- `mirrornode-operator-console` — MOPCON implementation and operator-facing projection;
- `mirrornode-platform` — public/product-facing implementation.

### EVIDENCE — what supports a claim
Commits, authenticated service records, permissions, tests, CI, deployments, decisions, reviews, receipts, and other attributable records.

### PROJECTION — what another audience receives
Derived views such as MOPCON, `@mirror` handoffs, advisor packets, and public status material. A projection must retain provenance and must not become a competing authority surface.

## Verified state conflicts already identified

- CORE-HUB `SYSTEM_CONTRACT.md` is versioned April 28, 2026 and declares LUCIAN on port 7700 as “execution authority” with `POST /dispatch`; later runtime evidence includes an Operator-approval execution flow and therefore requires explicit runtime-contract reconciliation rather than assuming the older contract is still implementation-current.
- CORE-HUB README still names Merlin as `Orchestrator (Dispatcher/Map Keeper)` while the current operating model separates integration, planning, runtime dispatch, and implementation management. This is a vocabulary and state discrepancy, not a reason to silently rewrite canon.
- MOPCON `main` is behind preserved later remote branches; later implementation evidence exists and should be consolidated, not rebuilt from memory.
- Codex has repeatedly demonstrated that green CI can coexist with semantic verifier defects. Review feedback must therefore be tracked as part of verification state rather than treated as optional commentary.

## Required outputs

1. Governance Authority Map.
2. Source & Custody Architecture.
3. Node / Collaborator Capability-Permission Registry.
4. Action & Provenance Standard.
5. `@mirror` Handoff Protocol.
6. MOPCON Projection Contract.
7. External Transparency Model.
8. Terminology Standard.
9. Discrepancy Register.
10. Promotion packet for the established evaluation and Operator-ratification path.

## Execution phases

A. Inventory evidence.  
B. Reconcile state.  
C. Classify canon / operational / implementation / evidence / projection.  
D. Reconcile identities, roles, capabilities, permissions, and authority.  
E. Resolve or explicitly retain discrepancies.  
F. Prepare candidate successor artifacts.  
G. Project verified state into MOPCON and handoff surfaces.  
H. Establish maintenance and re-verification cadence.

## Collaboration principle

Participants receive enough shared context to identify contradictions and dependencies, but assignments remain bounded. Cross-review is encouraged; silent authority transfer is not.

## Immediate evidence lane

Use GitHub as the first implementation inventory: verify repository custody, current branches/commits, open and merged PRs, review threads, CI results, stale documentation, runtime-contract differences, and the gap between canonical descriptions and current implementation evidence.
