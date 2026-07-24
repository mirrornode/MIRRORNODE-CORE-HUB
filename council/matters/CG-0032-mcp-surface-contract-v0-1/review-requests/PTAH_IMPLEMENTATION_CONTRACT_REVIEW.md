# Ptah Implementation Contract Review — CG-0032

## Role

Review the actual `MCP_SURFACE_CONTRACT_V0_1.md` definition from the Ptah implementation-reality position.

This is advisory review only. Do not write code, move the prototype, create an executable repository, or alter MCP registration.

## Authority state

The Operator authorized contract drafting and Council review only.

No executable MCP change is authorized.

## Required sources

1. `docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md`
2. `council/matters/CG-0032-mcp-surface-contract-v0-1/matter.yaml`
3. `tools/@mirror`
4. current CORE-HUB source-of-truth and governance declarations as needed

## Review questions

1. Is the contract technically implementable without creating a second source of canonical validation logic?
2. Does section 6 correctly identify the present provenance-validator duplication as temporary rather than architectural?
3. Are the lifecycle and reproducibility requirements sufficient before executable acceptance?
4. Are the failure-contract requirements precise enough to test deterministically?
5. Does the contract avoid prematurely deciding executable repository placement?
6. Are any current prototype facts overstated, unsupported, or missing from the definition?
7. Does the expansion gate provide enough implementation evidence before a fifth tool or larger output surface could be proposed?
8. What is the smallest definition-level revision, if any, required before an accepting disposition?

## Required response structure

Return only:

- Verified Current Implementation
- Contract Assessment
- Identified Implementation Risks
- Required Revisions
- Residual Future Questions
- Recommendation

Keep proposed implementation mechanics separate from defects in the contract definition.
