# CG-0034 — Council Review Packet

**Scope:** capability classification only.  
**No implementation, credential access, deployment, canon promotion, or merge authority is requested.**

## Shared question

MIRRORNODE wants to integrate Gemini first as a bounded, non-executing external cognition provider: explicit context in; analysis/synthesis/structured output out; no repository writes, deployment, credential mutation, external side effects, or autonomous promotion.

MICC v0.1 has eight primitive capability families and none cleanly describes model cognition/inference. Review `analysis/CAPABILITY_FIT_ANALYSIS.md` and answer whether the correct architecture is:

- a ninth MICC primitive family (`INFERENCE` / `COGNITION` or better name),
- a separate sibling cognition contract interoperating with MICC,
- or an existing MICC family, but only with explicit proof that its present semantics are sufficient.

Do not optimize for the easiest schema change. Preserve provider non-authority, output contestability, provenance, bounded context, and explicit side-effect boundaries.

---

## Ptah — implementation-contract position

Determine which option yields the cleanest implementable contract without semantic overloading. Identify the minimum machine-readable fields, conformance checks, versioning rules, and failure states required before a Gemini adapter could be implemented. Flag any changes that would improperly couple provider SDK behavior to MIRRORNODE authority semantics.

**Deliverable:** `positions/PTAH_POSITION.md`

---

## Thoth — security-boundary position

Determine how model invocation, tool/function calling, remote MCP, callbacks, prompt/context injection, provider-side model substitution, and credential use could create authority or execution bypasses. State whether cognition must be separated from infrastructure capability families to preserve the security boundary.

**Deliverable:** `positions/THOTH_POSITION.md`

---

## Osiris — evidence/disclosure position

Determine what provenance makes generated model output inspectable and contestable without misclassifying the output itself as verified evidence. Specify which facts belong in receipts, which generated content must remain clearly attributed as model output, and what disclosure boundaries apply to input context and provider metadata.

**Deliverable:** `positions/OSIRIS_POSITION.md`

---

## Theia — architectural-integration position

Determine whether the provider adapter and a later Room presence should be separate architectural identities, and whether adding cognition to MICC strengthens or weakens the larger integration model. Evaluate how this choice affects future Room/HUD participation, disagreement preservation, continuity, and Operator access without creating a privileged synthesis layer.

**Deliverable:** `positions/THEIA_POSITION.md`

---

## Cross-position synthesis gate

Do not synthesize toward consensus by default. Preserve disagreements that materially affect the classification. The synthesis must state:

1. which classification option each reviewer supports;
2. which invariants all reviewers require;
3. unresolved disagreements;
4. exact schema/contract artifacts that would need revision under each viable option;
5. whether a bounded Gemini MIM declaration is permitted under current MICC v0.1 before any revision.

Operator disposition is required before any contract revision or implementation begins.
