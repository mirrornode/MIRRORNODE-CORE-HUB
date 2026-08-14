# CG-0034 — Gemini Cognition Capability Boundary

**Status:** OPEN — exploratory governance matter  
**Type:** Governance / integration classification  
**Initiator:** Operator  
**Opened:** 2026-08-14

---

## Why this matter exists

The first bounded Gemini integration pass exposed a contract-level classification gap.

MICC v0.1 recognizes exactly eight primitive capability families: `IDENTITY`, `CREDENTIAL`, `STATE`, `ARTIFACT`, `EXECUTION`, `TRANSPORT`, `EVIDENCE`, and `METERING`. A Gemini model invocation that receives bounded context and returns analysis, synthesis, or inference does not cleanly fit any of those families.

`EVIDENCE` is not a safe substitute: MICC defines that family around receipt emission, trace, `execution_nonce`, and telemetry interoperability. Labeling model cognition as evidence would collapse two distinct semantics simply to satisfy the schema.

MICC also prohibits provider extensions from creating a ninth primitive family. Therefore no Gemini MIM declaration should be authored until this classification question is resolved.

---

## Decision question

**How should MIRRORNODE represent bounded external AI cognition/inference without granting provider authority, weakening existing approval boundaries, or misclassifying the capability under an unrelated MICC family?**

The matter must compare at least three paths:

1. Revise MICC to add a ninth primitive family such as `INFERENCE` or `COGNITION`.
2. Define a separate contract class for model cognition that interoperates with MICC without pretending inference is a conventional integration capability.
3. Demonstrate, with explicit semantic justification, that an existing MICC family is sufficient without changing its meaning.

No option is preferred by this filing.

---

## Gemini pilot constraints

Any eventual Gemini pilot arising from this matter is initially bounded to:

- receive explicitly supplied, bounded context;
- return analysis, position, synthesis, structured output, or uncertainty;
- perform no repository writes, deployment, credential mutation, external side effects, or autonomous promotion;
- carry provider/model/version and invocation provenance in receipts;
- remain distinguishable from any later instantiated Gemini presence in the Room;
- preserve MIRRORNODE authority resolution independently of provider identity;
- preserve direct Operator access to source evidence and competing positions rather than making Gemini a privileged representation layer.

---

## Provider versus presence

This matter explicitly separates two layers:

- **Gemini provider adapter:** transport, credential boundary, model/version selection, request/response contract, provenance, metering, and provider-specific failure semantics.
- **Gemini presence:** any later independently bounded participant represented in the Room/HUD with identity, continuity, position history, access limits, and interaction state.

The provider does not become the presence, and neither gains MIRRORNODE authority merely by successful invocation.

---

## Explicit non-authorizations

Opening CG-0034 does **not** authorize:

- MICC or MIM revision;
- Gemini API credential access or storage;
- adapter implementation;
- runtime registry changes;
- Room/HUD implementation;
- MCP direction changes;
- production or staging deployment;
- publication;
- canon promotion;
- merge.

Each remains separately gated.

---

## Initial test after classification

If a valid bounded cognition contract is approved and implemented later, the first architectural test should use the existing epistemic-capture inquiry as a fixed fixture. The test should preserve Gemini's original position as evidence and compare it with other independently produced positions without requiring consensus.

The goal is not merely a successful model response. The goal is to verify that cognition can enter MIRRORNODE while remaining attributable, contestable, bounded, and non-sovereign over representation.
