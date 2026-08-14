# MIRRORNODE Cognition Contract v0.1

**Status:** Draft under CG-0035 — not canon, not implementation authority  
**Version:** 0.1-draft  
**Created:** 2026-08-14

---

## 1. Purpose

This contract defines the semantics of bounded external model cognition inside MIRRORNODE.

A cognition invocation is a governed transformation of declared context and instructions into attributable generated output. Successful generation does not confer authority, verify generated claims, or authorize execution.

This contract is provider-neutral. Provider-specific transport, credentials, metering, evidence plumbing, durable execution, state, and other infrastructure remain governed through MICC-compatible integration surfaces where applicable.

---

## 2. Core objects

### 2.1 Cognition Declaration

A versioned machine-readable declaration describing one bounded cognition configuration.

Required identity fields:

- `cognition_id`
- `cognition_name`
- `contract_version`
- `declaration_version`
- `provider_adapter_ref`
- `provider_name`
- `model_id`
- `model_version_policy`
- `maintained_by`
- `created_at`
- `updated_at`
- `lifecycle_state`

### 2.2 Context Manifest

A bounded manifest of material supplied to the model. The manifest records provenance and disclosure class without requiring unrestricted duplication of protected content.

Each context item must identify:

- stable `context_item_id`;
- `source_type`;
- `source_ref` or integrity reference;
- provenance class;
- disclosure class;
- trust class;
- whether the item may contain instructions;
- whether the item may be quoted or reproduced;
- integrity hash where applicable.

### 2.3 Invocation Envelope

The attributable request boundary for a cognition event.

It must identify:

- declaration/version;
- requesting principal;
- authorizing basis where applicable;
- effective provider/model identity;
- context manifest reference;
- instruction/policy references;
- output contract reference;
- side-effect ceiling;
- tool-proposal policy;
- timeout/retry policy;
- invocation identifier and timestamp.

### 2.4 Generated Position

The model-produced result of a cognition invocation.

A generated position is attributable content. It may contain analysis, synthesis, classification, structured output, uncertainty, refusal, or tool proposals. It is not automatically evidence, canon, consensus, authorization, or truth.

### 2.5 Cognition Receipt

The evidence record that an invocation occurred under a particular declared boundary and produced a particular preserved result or failure state.

A receipt may establish facts about the invocation. It does not establish the truth of generated assertions.

---

## 3. Authority semantics

1. A provider is not a MIRRORNODE authority.
2. A model is not a MIRRORNODE authority merely by invocation or successful output.
3. A cognition declaration consumes authority established elsewhere; it does not create or expand authority.
4. Requesting principal, authorizing basis, provider adapter, model identity, recording principal, and any later executing principal remain separately attributable where they differ.
5. Generated content cannot self-ratify, alter its own policy, promote itself to canon, or authorize its own execution.

---

## 4. Side-effect ceiling

Every cognition declaration must declare a `side_effect_ceiling`.

v0.1 recognizes:

- `NONE` — generated output only; no tool, state, transport, credential, repository, deployment, or external-effect execution is permitted by the cognition layer.
- `PROPOSAL_ONLY` — generated output may contain structured proposals for actions, but proposals are inert until handled by a distinct MIRRORNODE authorization/execution path.

`PROPOSAL_ONLY` does not authorize execution. No cognition provider or model may directly cross from proposal to effect.

The first Gemini conformance target is constrained by CG-0034 to `NONE` unless separately authorized later.

---

## 5. Tool and function-call boundary

1. Function/tool calls emitted by a model are generated content.
2. They must be represented as typed proposals, never trusted commands.
3. Tool proposals must identify the proposed operation and arguments without carrying secrets or authority tokens.
4. A proposal cannot invoke remote MCP, callbacks, repository writes, state mutation, deployment, credential operations, or external effects from inside the cognition boundary.
5. Any future execution path must resolve authority independently and produce its own execution receipt.
6. Failure or refusal of the external execution path must not be rewritten as successful cognition execution.

---

## 6. Context and disclosure semantics

### 6.1 Bounded context

All model-visible context must be explicitly included by policy or referenced through a bounded context manifest. Unbounded ambient access is non-conformant.

### 6.2 Instruction-bearing data

External or user-provided content, repository text, webpages, documents, prior model outputs, and retrieved artifacts must be treated as potentially instruction-bearing data unless explicitly promoted to trusted policy through a separate governed process.

### 6.3 Disclosure classes

At minimum, v0.1 distinguishes:

- `PUBLIC`
- `INTERNAL`
- `RESTRICTED`
- `SECRET_PROHIBITED`

`SECRET_PROHIBITED` material may not be placed in model-visible context.

### 6.4 Protected references

Where raw content cannot be stored in a receipt or generated-position record, stable references and integrity metadata should be preserved under existing access controls.

---

## 7. Model identity and version policy

Every material output must preserve observable model identity.

A declaration must specify one of:

- `EXACT_REVISION_REQUIRED`
- `STABLE_MODEL_ID_ALLOWED`
- `ALIAS_ALLOWED_WITH_RUNTIME_CAPTURE`

If the effective model differs from the declared policy, the invocation must fail closed or be recorded in a distinct degraded/non-conformant state according to policy.

A mutable alias must never be treated as an immutable epistemic identity.

---

## 8. Output contract and epistemic status

Every generated position must declare:

- output type;
- schema/version where structured output is required;
- completion state;
- uncertainty state where available;
- citation/source references where applicable;
- integrity reference for the preserved output.

MIRRORNODE must preserve the distinction between:

1. **invocation evidence** — evidence that a model invocation occurred;
2. **generated content** — what the model produced;
3. **source evidence** — external material supporting or contradicting generated claims.

No schema-valid response automatically upgrades generated claims into verified evidence.

---

## 9. Failure-state vocabulary

v0.1 must distinguish at least:

- `COMPLETED`
- `REFUSED`
- `SAFETY_BLOCKED`
- `TRUNCATED`
- `TIMEOUT`
- `PROVIDER_ERROR`
- `SCHEMA_INVALID`
- `CONTEXT_POLICY_VIOLATION`
- `MODEL_IDENTITY_MISMATCH`
- `TOOL_POLICY_VIOLATION`
- `CREDENTIAL_BOUNDARY_FAILURE`
- `CANCELLED`

Implementations must not collapse materially distinct failure states into `COMPLETED` or generic success.

---

## 10. Retry and reproducibility semantics

Model generation is not presumed deterministic.

A retry creates a new invocation identity and must not overwrite the prior attempt. The system may correlate retries under a shared parent/reference but must preserve each generated result and completion state independently where retained.

Reproducibility claims must distinguish:

- reproducible invocation boundary;
- reproducible input/context manifest;
- reproducible effective model identity;
- reproducible generated output.

The last of these is not assumed unless demonstrated.

---

## 11. Receipt relationship to AUDIT_EMISSION

Existing `AUDIT_EMISSION` top-level semantics remain controlling.

Cognition-specific details may be added only through an explicitly approved additive mapping. Such details may include:

- cognition declaration/version;
- provider adapter reference;
- effective model identity;
- context manifest reference;
- policy/instruction references;
- completion/failure state;
- usage/metering references;
- generated-output integrity reference;
- provider request/response identifiers where safe and available.

The receipt must not contain secret contents, reusable bearer material, unrestricted protected context, or unrestricted provider response bodies merely for audit convenience.

---

## 12. Provider adapter relationship to MICC

A cognition declaration may reference MICC-governed infrastructure adapters but may not redefine their semantics.

Typical dependencies may include:

- `CREDENTIAL` for provider authentication;
- `TRANSPORT` where an explicit transport adapter exists;
- `EVIDENCE` for telemetry/receipt plumbing;
- `METERING` for usage accounting;
- `STATE` or `ARTIFACT` for separately governed persistence;
- `EXECUTION` only for externally authorized durable workflows, never to reinterpret generated cognition as execution authority.

No provider-specific extension may create authority or bypass the cognition side-effect ceiling.

---

## 13. Provider versus presence

A cognition provider/declaration is not identical to a persistent participant in the Room/HUD.

A later presence layer may reference cognition declarations as backing capabilities while separately governing identity, continuity, participation, access, position history, dissent, and Operator interaction.

Successful model invocation does not instantiate, authorize, or promote a Room presence by itself.

---

## 14. Contestability requirement

Material generated positions must remain contestable.

A conformant system must support navigation from a synthesis or displayed position toward the underlying attributed model output, invocation provenance, available source evidence, competing positions, and unresolved uncertainty subject to access controls.

No cognition provider may become the exclusive representation path through which the Operator can inspect a matter.

---

## 15. Conformance requirements

A cognition declaration is not conformant unless automated or reviewable checks can establish:

1. declaration schema validity;
2. provider adapter reference validity where required;
3. model/version policy validity;
4. bounded context manifest validity;
5. disclosure-policy compliance;
6. side-effect ceiling enforcement;
7. tool-proposal boundary enforcement;
8. output schema handling;
9. distinct failure-state handling;
10. receipt/provenance completeness;
11. provider non-authority;
12. no implicit Room-presence instantiation;
13. no implicit promotion of generated content to verified evidence or authorization.

---

## 16. Explicit exclusions from v0.1

This contract does not define:

- autonomous tool execution;
- provider-native agents as MIRRORNODE authorities;
- Room/HUD presence governance;
- memory/continuity semantics for persistent cognitive presences;
- model training or fine-tuning governance;
- provider account administration;
- credential contents;
- deployment authority;
- canon promotion.

Those require separate governed surfaces.
