# CG-0034 — Gemini Cognition Capability Boundary

**Status:** RATIFIED — Option B selected by Operator  
**Type:** Governance / integration classification  
**Initiator:** Operator  
**Opened:** 2026-08-14  
**Disposition:** 2026-08-14

---

## Disposition

The Operator accepted **Option B**: bounded external AI cognition/inference will be governed by a **provider-neutral sibling cognition contract interoperating with MICC**, rather than being forced into an existing MICC v0.1 capability family or added as a ninth MICC primitive at this stage.

- Disposition record: `history/2026-08-14-operator-disposition.md`
- Review synthesis: `synthesis/REVIEW_SYNTHESIS.md`

The next authorized action is a separate bounded drafting matter for Cognition Contract v0.1 and its machine-readable companion artifacts.

---

## Why this matter existed

The first bounded Gemini integration pass exposed a contract-level classification gap.

MICC v0.1 recognizes exactly eight primitive capability families: `IDENTITY`, `CREDENTIAL`, `STATE`, `ARTIFACT`, `EXECUTION`, `TRANSPORT`, `EVIDENCE`, and `METERING`. A Gemini model invocation that receives bounded context and returns analysis, synthesis, or inference does not cleanly fit any of those families.

`EVIDENCE` is not a safe substitute: MICC defines that family around receipt emission, trace, `execution_nonce`, and telemetry interoperability. Labeling model cognition as evidence would collapse two distinct semantics simply to satisfy the schema.

MICC also prohibits provider extensions from creating a ninth primitive family. Therefore no Gemini MIM declaration should be authored under MICC v0.1.

---

## Final classification

The filed Ptah, Thoth, Osiris, and Theia positions support a sibling cognition contract for distinct reasons:

- Ptah: implementation semantics and avoidance of schema overloading;
- Thoth: security separation between generated proposals and executable authority;
- Osiris: generated content must remain distinct from verified evidence;
- Theia: provider invocation and Room presence are separate architectural identities.

The synthesis preserves the shared invariants and unresolved implementation details.

These filed positions are preserved as governance inputs. This matter does not claim that they constitute independent exact-head reviews of this pull request.

---

## Provider versus presence

This matter explicitly separates two layers:

- **provider-facing infrastructure:** transport, credential boundary, model/version selection, metering, evidence plumbing, and provider-specific failure semantics;
- **later Room presence:** independently bounded participant identity, continuity, position history, access limits, and interaction state.

The provider does not become the presence, and neither gains MIRRORNODE authority merely by successful invocation.

---

## Explicit non-authorizations

CG-0034 does **not** authorize:

- Gemini credential access or storage;
- Gemini API invocation;
- adapter or runtime implementation;
- Runtime Registry changes;
- Room/HUD implementation;
- MCP direction changes or remote-MCP execution paths;
- deployment;
- publication;
- canon promotion;
- merge.

Each remains separately gated.
