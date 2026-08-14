# Initial Capability-Fit Analysis — Gemini Bounded Cognition

**Status:** exploratory; not a disposition  
**Matter:** CG-0034

## Candidate operation

A bounded external model invocation receives explicitly supplied context and instructions and returns generated analysis, synthesis, classification, structured reasoning output, or uncertainty. The invocation itself performs no repository mutation, deployment, credential mutation, or other external effect.

## MICC v0.1 fit check

| Family | Fit | Reason |
|---|---|---|
| `IDENTITY` | No | The operation does not establish identity, membership, session, or authentication claims. |
| `CREDENTIAL` | No | Credentials may be required to call the provider, but credential authority is not the semantic responsibility of the model invocation. |
| `STATE` | No | The operation may consume state as context but does not primarily provide a persistent record store. |
| `ARTIFACT` | No | Generated text may become an artifact later, but artifact storage is downstream of cognition. |
| `EXECUTION` | Weak / misleading | Provider-side inference is computation, but MICC `EXECUTION` concerns durable step/retry/checkpoint/concurrency/schedule/failure-recovery semantics. Treating all compute as durable execution would erase the distinction MICC intended. |
| `TRANSPORT` | No | Request/response transport carries the invocation but is not its semantic responsibility. |
| `EVIDENCE` | Weak / misleading | Model output may become evidence, and receipts must record provenance, but MICC `EVIDENCE` concerns receipt emission, trace, execution nonce, and telemetry. Cognition is not telemetry. |
| `METERING` | No | Token/usage accounting is ancillary rather than the semantic responsibility of inference. |

## Preliminary conclusion

No existing primitive family is an honest semantic fit without stretching the current definition. This is sufficient to block a Gemini MIM declaration under MICC v0.1 until governance resolves the classification gap.

This is **not** yet evidence that MICC must gain a ninth family. A separate cognition/model contract may be cleaner if model inference carries invariants fundamentally different from provider integrations such as stores, transport, credentials, or durable execution.

## Invariants any solution should preserve

1. **Provider non-authority.** A model provider cannot grant MIRRORNODE authority.
2. **Attribution.** Provider, model/version, requesting principal, authorizing basis where applicable, and receiving/recording principal remain separately attributable.
3. **Bounded context.** Input context is deliberately scoped and its provenance can be inspected.
4. **Output contestability.** Generated analysis is a position or generated result, not automatically truth, evidence verdict, authorization, or canon.
5. **No implicit side effects.** Model generation alone cannot smuggle execution through tool calls, remote MCP, callbacks, or provider-specific extensions.
6. **Failure visibility.** Safety refusal, truncation, schema failure, timeout, model substitution, provider degradation, and uncertainty must not collapse into a generic success state.
7. **Version visibility.** The model/version used for a material output is inspectable; floating aliases must not silently change the epistemic source of a recorded position.
8. **Presence separation.** An instantiated Room participant is not identical to the external provider adapter that transports model invocations.

## Classification options for Council review

### Option A — Ninth MICC family

Add a primitive family such as `INFERENCE` or `COGNITION` and define its operation, provenance, side-effect, versioning, and receipt semantics within MICC/MIM.

**Strength:** one integration grammar.  
**Risk:** MICC may become too broad and conflate infrastructure capabilities with cognitive actors.

### Option B — Separate cognition contract

Define a sibling contract for model cognition/presence, with explicit interoperation points to MICC for transport, credentials, evidence, and metering.

**Strength:** preserves semantic separation.  
**Risk:** additional contract surface and cross-contract conformance complexity.

### Option C — Existing-family classification

Permit an existing MICC family only if reviewers can demonstrate semantic sufficiency without redefining that family by convenience.

**Strength:** no contract expansion.  
**Risk:** highest chance of hidden semantic debt.

## Required next result

Council positions should answer the classification question before any Gemini manifest, credential wiring, runtime adapter, Room presence, or HUD work is authored.
