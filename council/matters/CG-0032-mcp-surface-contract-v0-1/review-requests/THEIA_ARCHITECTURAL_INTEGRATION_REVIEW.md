# Theia Architectural Integration Review — CG-0032

## Role

Review the actual `MCP_SURFACE_CONTRACT_V0_1.md` definition from the Theia architectural-integration position.

This is advisory review only. Do not implement, relocate, register, expose, or expand the MCP surface.

## Authority state

The Operator authorized contract drafting and Council review only.

No executable MCP change is authorized.

## Required sources

1. `docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md`
2. `council/matters/CG-0032-mcp-surface-contract-v0-1/matter.yaml`
3. `tools/@mirror`
4. `docs/continuity/OPERATOR_CONTINUITY_LEDGER_V0_1.md`
5. existing CORE-HUB authority and Council Grounds records as needed

## Review questions

1. Does the contract correctly place MCP as a downstream read-only projection surface rather than authority, orchestration, runtime, or Council?
2. Is the dependency direction explicit enough to prevent MCP from becoming an alternate authority path?
3. Does the contract preserve the distinct roles of CORE-HUB, `@mirror`, MOPCON, agent runtime, Council, and external model runtimes?
4. Is it correct to leave executable ownership and repository placement unresolved until a later implementation matter?
5. Are the separate authorization gates sufficient to prevent definition acceptance from laundering the prototype into architecture?
6. Does any wording accidentally imply that a model-runtime tool result can acquire Council or Operator authority?
7. What is the smallest definition-level revision, if any, required before an accepting disposition?

## Required response structure

Return only:

- Verified Current Implementation
- Contract Assessment
- Identified Architectural Risks
- Required Revisions
- Residual Future Questions
- Recommendation

Distinguish definition defects from future implementation questions. Do not resolve Operator authority by inference.
