# POS-0006 — Thoth Revision Confirmation

**Matter:** CG-0032 — MCP Surface Contract v0.1  
**Role:** Thoth — security boundary  
**Review type:** bounded revision confirmation  
**Authority effect:** advisory only

## Confirmation scope

Confirm only whether revised `docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md` resolves R2 from POS-0003 and the Operator `revision-required` disposition.

No executable MCP change, new primitive, registration change, or remote exposure is reviewed or authorized here.

## Result

**confirmed**

## Findings

The revised definition now makes the security boundary primitive-independent:

- section 2.1 defines the MCP surface as every server primitive, negotiated capability, extension, and output channel;
- projection allowlists apply to all covered primitives and capabilities;
- prohibited-data rules apply to all covered primitives and capabilities;
- prompt-injection restrictions explicitly include resources, prompts, templates, notifications, server instructions, extensions, and other projected material;
- permanent anti-capabilities apply across the entire MCP surface;
- the expansion gate covers tools, resources, prompts, templates, notifications/subscriptions, server instructions, extensions, output fields, newly introduced primitives, and negotiated capabilities;
- unknown or newly introduced protocol primitives are denied by default until reviewed;
- the current prototype freeze explicitly prohibits adding non-tool primitives while CG-0032 remains unresolved.

This closes the prior loophole in which a non-tool MCP primitive could expand disclosure or behavior without technically adding a fifth tool.

## Residual future conditions

A later implementation matter must enumerate the actual capabilities negotiated by the chosen MCP SDK/runtime and test that disabled or unknown capabilities cannot expose data or behavior outside the approved contract.

This is an implementation evidence requirement, not a remaining definition defect.

## Recommendation

**R2 confirmed resolved. No Thoth definition-level blocker remains.**
