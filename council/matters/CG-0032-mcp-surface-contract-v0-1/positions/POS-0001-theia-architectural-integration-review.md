# POS-0001 — Theia Architectural Integration Review — CG-0032

## Verified Current Implementation

- CG-0032 is a proposed governance-definition matter with `authorityEffect: none-until-operator-disposition`; its current authority covers documentation and review only, not executable MCP change.
- `MCP_SURFACE_CONTRACT_V0_1.md` records the observed local four-tool prototype as evidence only and explicitly states that the observation does not approve the listed tools, output shapes, registration scope, executable location, or prototype as ratified architecture.
- The contract defines MCP as a downstream read-only projection surface and explicitly excludes authority, Council disposition, Operator approval, runtime execution, canonical-state ownership, publication approval, and inferred permission roles.
- The dependency direction is stated as Operator / Council authority → CORE-HUB → canonical mechanisms such as `@mirror` → approved projection contract → MCP surface → external model runtime.
- The Operator Continuity Ledger independently preserves the same authority separation: Operator disposition outranks subordinate evidence, and a validated artifact does not imply implementation, deployment, or publication authority.
- `@mirror` remains a canonical mechanism with both recording and validation behavior; the current prototype’s duplicated digest validation is accurately recorded as temporary implementation fact rather than architectural ownership.

## Contract Assessment

The contract is architecturally coherent and suitable for an accepting definition-level disposition.

1. **Architectural role:** Correct. Defining this MCP class as a downstream projection surface is the right placement. It prevents a read-only integration mechanism from being mistaken for orchestration, execution, governance, or canonical continuity.
2. **Dependency direction:** Sufficiently explicit. The prohibition on canonical MIRRORNODE surfaces depending on MCP output for authority, validity, approval, truth, or execution permission prevents dependency inversion and blocks MCP from becoming an alternate authority path.
3. **Role separation:** Preserved. CORE-HUB remains governance/canon; canonical mechanisms such as `@mirror` remain upstream sources; Council and Operator remain authority-bearing; MOPCON and agent runtime remain separate operative surfaces rather than dependencies of MCP; the external model runtime remains a downstream consumer. The contract correctly does not place MOPCON or runtime inside the MCP chain merely because they exist elsewhere in the ecosystem.
4. **Executable ownership:** Correctly unresolved. Choosing CORE-HUB, a dedicated repository, or another execution surface is an implementation-location decision and should follow definition acceptance rather than be smuggled into the definition.
5. **Authorization gates:** Sufficient. Contract acceptance, executable relocation/versioning, output remediation, projection-schema implementation, additional runtime attachment, remote exposure, persistent operation, capability expansion, and any write-capable class are separated into distinct future decisions.
6. **Authority semantics:** Clear. No wording in the reviewed contract grants Council or Operator authority to an MCP response. The integrity semantics explicitly narrow digest matching to payload/digest correspondence and deny truth, approval, identity, authorization, freshness, safety, or publication implications.
7. **Prototype freeze:** Correctly prevents a successful feasibility experiment from becoming architecture by inertia.

## Identified Architectural Risks

- **Composition risk remains external to the MCP contract.** A consuming model runtime may possess other tools or connectors independently of MCP. The contract correctly states that projected content cannot grant new tool authority or authorize execution, but a later implementation review must test that the surrounding client integration does not operationally treat MCP output as permission.
- **Canonical-source plurality must remain explicit in implementation.** The phrase “canonical mechanisms such as `@mirror`” is correct; implementation must not collapse all MIRRORNODE canonical state into `@mirror` merely because the prototype currently reads it.
- **Projection ownership can drift into source ownership.** A future MCP implementation must not become the place where canonical validation rules, Council semantics, or disclosure policy are independently redefined.
- **Read-only does not equal non-operative at ecosystem scale.** Even without writes, projected information can influence a model that has separate operative capabilities. This is appropriately addressed as an authority and injection boundary in the definition, but it must remain a testable implementation concern.
- **Tool-name continuity may create accidental precedent.** The current four names are evidence, not reserved architecture. Later remediation should be free to rename, remove, or reshape them under separate authorization.

## Required Revisions

None at definition level.

The reviewed draft already contains the architectural constraints that would otherwise be required revisions:

- explicit downstream-only dependency direction;
- no authority inference from MCP output;
- canonical-state allowlisting before the model boundary;
- separation of integrity from truth and authorization;
- permanent anti-capabilities for the read-only class;
- unresolved executable ownership;
- explicit future implementation evidence requirements;
- separate authorization gates; and
- a current-prototype freeze.

No implementation concern identified in this review requires changing the governing definition before disposition.

## Residual Future Questions

These are future implementation questions and are not blockers to definition acceptance:

- Which repository or execution surface should own the MCP executable?
- Which canonical owner should expose the side-effect-free integrity primitive so the MCP layer does not duplicate canonical validation logic?
- What exact projection schema and field allowlists should replace the current raw/local-path outputs?
- Should the four prototype tools survive, be renamed, be narrowed, or be removed?
- Is user-scoped registration acceptable after security and lifecycle review, or should availability be constrained differently?
- How should the consuming model runtime demonstrate that MCP information cannot elevate permissions available through its other tools?
- What lifecycle, dependency-lock, startup, rollback, and conformance evidence is sufficient for governed infrastructure acceptance?

## Recommendation

**Support.**

CG-0032 may proceed toward an accepting Operator disposition as a governance definition, subject to the remaining Ptah, Thoth, and Osiris reviews and preservation of any disagreement in synthesis.

This recommendation authorizes no executable change. Acceptance should establish only the governing definition and permission to open a later, separately authorized implementation-remediation matter.