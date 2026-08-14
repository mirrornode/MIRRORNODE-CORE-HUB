# PTAH POSITION — CG-0034

**Verdict:** SUPPORT OPTION B — separate cognition contract interoperating with MICC.

## Rationale

MICC v0.1 is structurally coherent because its primitive families describe infrastructure capabilities with comparatively deterministic contracts: identity, credentials, state, artifacts, execution, transport, evidence, and metering. External model cognition introduces different semantics: context assembly, model/version provenance, stochastic generation, structured-output conformance, uncertainty, refusal, truncation, tool-call proposals, and generated positions that are not themselves verified facts.

Adding `COGNITION` or `INFERENCE` directly to MICC would make one contract carry two different classes of semantics. That is implementable, but it increases schema coupling and risks provider SDK behavior leaking into MIRRORNODE authority semantics.

A sibling cognition contract should therefore define model-facing invariants and reference MICC-declared adapters for infrastructure dependencies such as credentials, transport, evidence, and metering.

## Minimum machine-readable fields

Any cognition declaration should include at minimum:

- `cognition_id`
- `contract_version`
- `provider_adapter_ref`
- `provider_name`
- `model_id`
- `model_version_or_revision`
- `maintained_by`
- `input_contract_ref`
- `output_contract_ref`
- `context_policy_ref`
- `tool_policy_ref`
- `structured_output_required`
- `side_effect_ceiling`
- `approval_class`
- `timeout_seconds`
- `retry_policy`
- `conformance_test_ref`
- `lifecycle_state`

## Required conformance checks

1. Provider adapter reference resolves to an authorized/usable infrastructure adapter where required.
2. Model identity/version is explicit for material outputs; silent floating substitution is rejected or surfaced as degraded/non-conformant according to policy.
3. Input context conforms to the declared context boundary and provenance requirements.
4. Output conforms to the declared schema when structured output is required.
5. Tool/function proposals are data only unless separately authorized and executed by a distinct execution principal.
6. No cognition declaration may grant authority to its provider or model.
7. Side-effect ceiling for the first Gemini pilot is `NONE`; any tool call or external action must cross a separate approved execution boundary.
8. Refusal, timeout, truncation, safety block, malformed output, provider error, and model substitution remain distinct failure states.

## Versioning

Provider API version, cognition contract version, declaration version, and model identity/version must remain separately attributable. A model alias change that can materially alter behavior must not silently preserve the same epistemic identity in recorded outputs.

## Implementation constraint

Do not implement a Gemini MIM under MICC v0.1 as `EVIDENCE` or `EXECUTION`. Implement the cognition contract first, then bind its infrastructure dependencies to MICC adapters.

**Position:** APPROVE OPTION B FOR OPERATOR CONSIDERATION. No implementation authority granted.