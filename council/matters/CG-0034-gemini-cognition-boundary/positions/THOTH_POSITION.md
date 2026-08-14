# THOTH POSITION — CG-0034

**Verdict:** SUPPORT OPTION B WITH HARD BOUNDARIES.

## Security finding

External model cognition creates a qualitatively different attack surface from ordinary infrastructure adapters because generated content can itself attempt to influence routing, authority, tool use, context selection, or Operator perception. Treating cognition as a conventional MICC family would make it too easy to confuse successful generation with permission to act.

The first Gemini integration must therefore be architecturally non-executing.

## Required security invariants

1. **Tool proposals are inert.** Function/tool calls emitted by Gemini are untrusted structured proposals. They cannot execute directly, invoke remote MCP, trigger callbacks, mutate state, or acquire credentials without a distinct MIRRORNODE execution path and approval evaluation.
2. **No inbound authority from provider.** Provider responses, safety classifications, function-call schemas, account roles, or model metadata cannot grant MIRRORNODE authority.
3. **Context is tainted input.** Repository text, external documents, webpages, user-supplied content, and prior model output passed into Gemini must be treated as potentially instruction-bearing data unless explicitly promoted to trusted policy through existing governance.
4. **Credential isolation.** The cognition layer may reference a credential requirement but must never receive reusable credential material inside prompts, logs, model-visible context, receipts, or generated output.
5. **MCP directionality remains unchanged.** Gemini remote-MCP support must not be used to create an inbound execution path or circumvent CG-0032/CG-0033 constraints.
6. **Model substitution is visible.** If the provider substitutes, aliases, or upgrades the effective model, material outputs must record that fact or fail closed when exact identity is required.
7. **Output has no intrinsic privilege.** Generated analysis cannot self-ratify, mark itself verified evidence, modify its own policy, or increase the authority of a later action.
8. **Context-release boundaries are explicit.** The system must know which data classes may leave MIRRORNODE for the provider before invocation.
9. **Prompt and tool-policy provenance is retained.** A recorded output without the governing system/developer instruction set, tool policy version, and bounded context references is insufficient for high-trust replay or audit.
10. **Failure cannot degrade into permissiveness.** Safety refusal, parser failure, provider outage, malformed tool proposal, or context-policy violation must never silently route to a less restricted fallback.

## Primary attack paths

- prompt injection embedded in context;
- model-generated requests to use tools outside the declared side-effect ceiling;
- function-calling payloads treated as trusted commands;
- provider feature updates enabling execution-like behavior without governance review;
- secret or protected-context exfiltration through prompts;
- over-trust in model confidence or safety labels;
- UI framing that presents one model's output as the canonical interpretation;
- chained cognition calls amplifying an injected instruction while obscuring provenance.

## Contract recommendation

Use a sibling cognition contract whose default side-effect ceiling is `NONE`. MICC remains responsible for the infrastructure adapters that satisfy credential, transport, evidence, and metering dependencies.

Any future change allowing cognition to propose actions must still keep proposal, authorization, and execution as separately attributable stages.

**Position:** APPROVE OPTION B WITH CONDITIONS. No credential access, execution path, remote MCP use, or deployment authorized.