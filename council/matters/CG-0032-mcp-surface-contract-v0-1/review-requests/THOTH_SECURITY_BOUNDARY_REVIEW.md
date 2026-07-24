# Thoth Security Boundary Review — CG-0032

## Role

Review the actual `MCP_SURFACE_CONTRACT_V0_1.md` definition from the Thoth security-boundary position.

This is advisory review only. Do not add tools, alter output shapes, change registration scope, or create remote exposure.

## Authority state

The Operator authorized contract drafting and Council review only.

No executable MCP change is authorized.

## Required sources

1. `docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md`
2. `council/matters/CG-0032-mcp-surface-contract-v0-1/matter.yaml`
3. `tools/@mirror`
4. relevant security and authority contracts in CORE-HUB as needed

## Review questions

1. Does the contract adequately treat raw canonical text as untrusted model input and block prompt-injection authority escalation?
2. Are the prohibited-data and anti-capability lists sufficient for a read-only projection class?
3. Does the user-scope discussion correctly separate client discovery from authorization and security boundaries?
4. Are local process, executable replacement, dependency compromise, and environment inheritance represented accurately enough?
5. Is the failure contract sufficiently fail-closed and disclosure-minimized?
6. Does neutral integrity language still leave any route for a model to confuse digest consistency with truth, safety, approval, or authorization?
7. Are there any absolute prohibitions that must be added before this contract can safely govern implementation?
8. What is the smallest definition-level revision, if any, required before an accepting disposition?

## Required response structure

Return only:

- Verified Current Implementation
- Contract Assessment
- Identified Security Risks
- Required Revisions
- Permanent Anti-Capabilities
- Recommendation

Do not infer that local read-only access is safe merely because no write tool exists.
