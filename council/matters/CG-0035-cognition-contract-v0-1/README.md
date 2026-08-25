# CG-0035 — Cognition Contract v0.1

**Status:** OPEN — bounded drafting matter  
**Type:** Governance definition / contract drafting  
**Initiator:** Operator  
**Opened:** 2026-08-14

---

## Authority basis

CG-0034 ratified Option B: bounded external AI cognition/inference will be governed by a provider-neutral sibling cognition contract interoperating with MICC.

CG-0035 is the separately authorized drafting matter arising from that disposition.

---

## Drafting objective

Define a provider-neutral Cognition Contract v0.1 and machine-readable declaration schema that govern bounded model invocation without granting provider authority, collapsing generated output into verified evidence, or creating an implicit execution path.

The contract must be suitable for Gemini as the first conformance target without becoming Gemini-specific.

---

## Required draft artifacts

1. `docs/cognition/COGNITION_CONTRACT_V0_1.md`
2. `docs/cognition/COGNITION_DECLARATION_V0_1.schema.json`
3. provider-neutral context/input envelope schema
4. generated-position/output envelope schema
5. failure-state vocabulary
6. cognition invocation receipt mapping to existing `AUDIT_EMISSION`
7. tool-proposal boundary semantics
8. provider-adapter reference semantics into MICC
9. conformance fixture using the epistemic-capture inquiry

---

## Locked inherited invariants

CG-0035 may refine implementation semantics but may not silently weaken these CG-0034 invariants:

- provider non-authority;
- first-slice side-effect ceiling `NONE`;
- function/tool proposals remain inert until separately authorized and executed;
- generated output is attributed model-produced content, not verified truth by default;
- bounded context with provenance and disclosure controls;
- explicit refusal/truncation/safety/schema/timeout/provider/model-substitution states;
- MCP directionality and existing approval boundaries remain intact;
- provider adapter and Room presence remain separate identities;
- contestability, dissent, uncertainty, and source-evidence navigability are preserved.

---

## Explicit non-authorizations

Opening CG-0035 does **not** authorize:

- Gemini credentials;
- Gemini API invocation;
- runtime or adapter implementation;
- Runtime Registry changes;
- Room/HUD implementation;
- tool execution or remote MCP;
- deployment;
- publication;
- canon promotion;
- merge.

---

## Drafting principle

The contract must describe cognition as a bounded, attributable transformation of declared context into generated output. It must not treat model fluency, confidence, successful completion, provider safety labeling, or schema validity as evidence that generated claims are true.
