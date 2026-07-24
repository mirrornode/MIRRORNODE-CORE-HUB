# Osiris Disclosure and Authority Review — CG-0032

## Role

Review the actual `MCP_SURFACE_CONTRACT_V0_1.md` definition from the Osiris disclosure-and-authority position.

This is advisory review only. Do not infer publication safety, modify the prototype, or authorize new exposure.

## Authority state

The Operator authorized contract drafting and Council review only.

No executable MCP change, remote exposure, or publication is authorized.

## Required sources

1. `docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md`
2. `council/matters/CG-0032-mcp-surface-contract-v0-1/matter.yaml`
3. `tools/@mirror`
4. `docs/continuity/CONTINUITY_CONSOLE_V0_1_DEFINITION.md` for analogous disclosure-boundary precedent
5. relevant CORE-HUB authority records as needed

## Review questions

1. Does the contract sufficiently prohibit raw private canonical state from crossing into external model runtimes by default?
2. Is the allowlist-before-projection rule strong enough, or does any wording still permit model-side filtering of private material?
3. Are local paths, actors, contributors, topology, arbitrary free text, and integrity tokens correctly treated as non-projectable by default?
4. Does the contract sufficiently prevent `valid`, `provenance`, `authorityHash`, `verified`, or equivalent language from implying approval, truth, safety, or authority?
5. Are failure responses constrained enough to avoid leaking sensitive source conditions while remaining honest about unavailability or partial checks?
6. Is the distinction between canonical private state and MCP-safe projection state explicit and enforceable at the definition level?
7. Does any section accidentally imply publication permission or public-surface equivalence merely because a field is MCP-projectable?
8. What is the smallest definition-level revision, if any, required before an accepting disposition?

## Required response structure

Return only:

- Verified Current Implementation
- Contract Assessment
- Identified Disclosure or Authority Risks
- Required Revisions
- Residual Future Conditions
- Recommendation

Publication approval remains separate from MCP projection approval.
