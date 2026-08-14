# OSIRIS POSITION — CG-0034

**Verdict:** SUPPORT OPTION B — separate cognition contract; generated output is attributable material, not verified evidence by default.

## Evidence distinction

A model response may be preserved as evidence that **Gemini produced a particular output under a particular invocation context**. That does not make the propositions inside the output verified evidence.

The system must therefore distinguish at least three layers:

1. **Invocation evidence** — provider/model identity, timestamps, request/response identifiers where available, policy/context references, token/usage metadata, termination/failure state, and integrity references.
2. **Generated content** — the actual model-produced position, analysis, classification, structured result, uncertainty, refusal, or tool proposal.
3. **External/source evidence** — documents, repository state, measurements, or other evidence that generated claims cite or depend on.

Collapsing these layers would create the exact epistemic failure CG-0034 is intended to avoid.

## Minimum provenance for contestability

For any material Gemini output, retain or reference:

- cognition declaration/version;
- provider adapter identity/version;
- provider name;
- effective model identity/version or revision where observable;
- requesting principal;
- authorizing basis when applicable;
- invocation timestamp;
- context manifest/reference set, including provenance and disclosure class rather than unrestricted raw duplication;
- prompt/policy version references sufficient to explain the operating boundary;
- output schema/version where applicable;
- provider request/response identifiers when non-sensitive and available;
- completion/termination status;
- refusal, truncation, safety block, parse failure, or provider error classification;
- usage/metering facts if available;
- integrity hash/reference for the preserved generated output.

## Disclosure boundary

Receipts must not duplicate secrets, bearer values, protected raw context, unrestricted provider response bodies, or sensitive internal topology merely for audit convenience. Where raw context cannot be disclosed, the receipt should preserve a stable reference plus disclosure classification and access path under existing authority.

## AUDIT_EMISSION relationship

Existing `AUDIT_EMISSION` should remain controlling for top-level audit semantics. Cognition-specific provenance may be additive under a dedicated nested object only after the contract/schema relationship is explicitly approved. It must not redefine locked evidence vocabularies.

The generated model output itself should remain separately stored/referenced as attributed content. A receipt may prove that the output was generated and preserved; it does not prove that the output's assertions are true.

## Room/HUD implication

A later Room presence should be able to expose:

- the model's attributed position;
- the provenance of that position;
- source evidence it relied upon;
- competing positions;
- unresolved uncertainty or contradiction.

The UI must not visually collapse "model said X" into "X is verified."

**Position:** APPROVE OPTION B WITH EVIDENCE-SEPARATION CONDITIONS. No evidence-contract amendment or implementation authority granted.