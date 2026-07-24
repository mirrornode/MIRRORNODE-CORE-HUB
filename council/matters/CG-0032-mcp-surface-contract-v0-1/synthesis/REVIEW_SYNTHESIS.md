# CG-0032 Review Synthesis — MCP Surface Contract v0.1

**Matter:** CG-0032 — MCP Surface Contract v0.1  
**Workflow stage:** Council review complete; Operator disposition pending  
**Authority effect:** none-until-operator-disposition  
**Executable MCP change authorized:** No

## Positions received

| Position | Result | Definition-level conclusion |
|---|---|---|
| POS-0001 — Theia Architectural Integration Review | support | Architectural role, dependency direction, authority separation, unresolved implementation ownership, and separate authorization gates are sufficient. No definition revision required. |
| POS-0002 — Ptah Implementation Contract Review | support-with-required-revision | Contract is technically implementable, but failure behavior requires stable machine-readable outcome/status and disclosure-safe reason-code semantics. |
| POS-0003 — Thoth Security Boundary Review | support-with-required-revision | Security model is sound, but projection and expansion gates must apply to the entire MCP primitive/capability surface rather than tools alone. |
| POS-0004 — Osiris Disclosure and Authority Review | support-with-incorporation-of-required-revisions | No independent disclosure blocker remains if the Ptah and Thoth definition revisions are incorporated. |

## Consensus

All four positions support the proposed architectural direction:

1. MCP is a **downstream read-only projection surface**.
2. MCP is not an authority source, Council mechanism, Operator approval mechanism, runtime execution boundary, canonical state store, or publication approval mechanism.
3. Canonical MIRRORNODE surfaces must not depend on MCP output for authority, approval, truth, integrity, or execution permission.
4. Raw canonical/private state is not approved for projection by default.
5. Integrity checking must not imply truth, safety, approval, authorization, actor identity, freshness, or publication permission.
6. The current four-tool prototype remains evidence only and must remain frozen pending later authorization.
7. Executable ownership and repository placement correctly remain unresolved for a future implementation matter.
8. Any write-capable MCP design is a different architectural class and requires a separate Council matter.

No position recommends rejecting the contract direction.

## Required definition revisions

Two substantive revision themes remain before an accepting disposition is recommended.

### R1 — Deterministic failure semantics

Requested by Ptah and supported by Osiris/Thoth.

The contract should require:

- a bounded machine-readable operation outcome/status vocabulary;
- stable disclosure-safe reason codes for every non-success outcome;
- explicit completeness semantics where partial scans are possible;
- prohibition on free-text-only failure classification; and
- conformance tests against the exact machine-readable failure semantics.

This revision need not define the complete future tool response schema.

### R2 — Primitive-independent MCP boundary

Requested by Thoth and supported by Osiris.

The contract should make clear that projection rules, prohibited data, anti-capabilities, and the surface-expansion gate apply to **any MCP server primitive, capability, extension, or output channel**, not only tools.

The revision should be capability-generic so protocol evolution cannot create an ungated channel. Tools, resources, prompts, templates, notifications/subscriptions, server instructions, extensions, or other negotiated capabilities may not bypass the same review boundary.

## Preserved distinctions

The synthesis preserves these differences rather than flattening them:

- Theia finds no definition defect and would support acceptance as currently architected.
- Ptah finds one implementation-contract defect: failure semantics are not deterministic enough for strong conformance testing.
- Thoth finds one protocol-surface defect: a tool-specific expansion gate is narrower than the MCP attack/disclosure surface.
- Osiris finds no additional independent disclosure defect but conditions support on incorporation of Ptah and Thoth revisions.

These positions are compatible. They do not represent an architectural disagreement about the role of MCP.

## Residual future questions — not definition blockers

The following remain intentionally deferred to a later implementation-remediation matter:

- executable repository/location and ownership;
- extraction or exposure of one side-effect-free canonical validation primitive;
- exact MCP-safe field schemas and allowlists;
- whether any current prototype tool survives, is renamed, narrowed, or removed;
- acceptable registration scope and executable identity pinning;
- package/runtime locking and reproducible startup;
- proof of no incidental writes;
- prompt-injection, secret-disclosure, unknown-field, and failure-mode test fixtures;
- count/cadence inference review;
- remote exposure or additional model-runtime attachment;
- deployment, persistence, and rollback;
- any public publication or product-surface reuse.

These questions require implementation evidence and separate authority. They should not be resolved inside CG-0032 merely to close the definition matter.

## Synthesis conclusion

The Council review supports the MCP Surface Contract v0.1 direction but identifies two bounded definition revisions before an accepting disposition is advisable.

**Recommended Operator disposition:** `revision-required`.

Recommended scope of revision authority, if granted:

- revise `docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md` only as necessary to resolve R1 and R2;
- update CG-0032 documentary records as needed to reflect the revision;
- perform confirmation review against the revised definition;
- do not modify, relocate, expand, register, remotely expose, or otherwise alter the MCP executable.

Suggested confirmation reviewers after revision:

- Ptah — confirm deterministic failure semantics;
- Thoth — confirm primitive-independent boundary/gate;
- Osiris — confirm the combined revisions preserve disclosure minimization and publication separation.

Theia re-review is not required unless the revision changes architectural role, authority direction, or separate-authorization gates.

Final disposition remains exclusively with the Operator.