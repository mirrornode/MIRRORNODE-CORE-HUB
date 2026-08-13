# Theia — Architectural Integration Position
## CG-0033: MICC v0.1 + MIM v0.1

**Reviewer:** Theia  
**Matter:** CG-0033  
**Review class:** Architectural Integration Review  
**State:** APPROVED_WITH_CONDITIONS  
**Reviewed against:** `74392f5b3c27b96010b1852413f5f6707277be65`

---

## Determination

MICC v0.1 and MIM v0.1 are architecturally coherent as a contract-first integration boundary. The proposed separation is sound: MICC owns MIRRORNODE integration semantics; MIM declares adapter instances against those semantics; providers implement beneath that boundary and do not acquire semantic authority by implementation.

No provider implementation is authorized by this position. No canon promotion is authorized by this position.

Approval is conditioned on the bounded corrections and clarifications below being resolved during the CG-0033 review cycle before final disposition.

---

## 1. Canon placement

**Determination:** Draft placement under `docs/integration/` is correct for CG-0033.

If MICC is later promoted by separate explicit operator action, `canon/contracts/MICC_V0_1.md` is the coherent destination under the repository's present canon taxonomy: `canon/contracts/` is defined as the location for technical specifications. A new `canon/specs/` category is not justified by MICC v0.1 alone and would create a second overlapping classification for normative technical specifications.

MIM may be promoted separately under `canon/schemas/` if that path remains the established schema location at promotion time. Canon placement must be revalidated against the then-current index before promotion; this position does not itself promote either artifact.

**Condition A:** Any canon-promotion matter must update the canon index/navigation as required and must not treat acceptance of CG-0033 as implicit promotion authority.

---

## 2. SYSTEM_CONTRACT coherence

**Determination:** The principal models are coherent if the distinction in MICC Section 3 remains explicit.

Integration adapter principals are a distinct class from lattice agents. An adapter does not inherit the identity, role, or authority of the lattice agent that requests or maintains it. MICC correctly defers intra-lattice identity to SYSTEM_CONTRACT and does not redefine Lucian's execution authority.

The authority direction `operator → adapter → provider` is architecturally useful as a prohibition against provider-originated MIRRORNODE authority, but it must not be read as collapsing requesting actors, executing actors, maintainers, or delegated authorities into a single chain. Those remain separately attributable in evidence and approval records.

**Condition B:** Final MICC text must preserve distinct identities for requesting actor, executing adapter principal, maintainer, and authorizing authority wherever those roles differ. No adapter may inherit lattice authority merely because a lattice principal invoked, configured, or maintains it.

---

## 3. CG-0032 MCP boundary coherence

**Determination:** Coherent. No architectural conflict is introduced.

CG-0032 remains governing for MCP as a downstream read-only projection surface with dependency direction from canonical MIRRORNODE outward. MICC Section 12 correctly refuses to classify MCP as a provider adapter and explicitly prohibits a MICC adapter from inverting the CG-0032 dependency direction.

MICC Section 12.2 may describe other protocol clients as approaching a governed capability surface from outside, but that general protocol language does not broaden MCP authority. MCP remains subject to the narrower CG-0032 rule unless and until a separate Council matter explicitly changes it.

**Condition C:** The CG-0032-specific MCP rule must continue to take precedence over the generic external-protocol language in MICC. Any inbound, write-capable, or execution-bearing MCP design requires a separate Council matter and may not be inferred from MICC conformance.

---

## 4. MICC/MIM separation stability

**Determination:** Architecturally stable, with versioning discipline.

MICC defines semantics; MIM expresses declarations. MIM schema evolution does not require a MICC semantic revision when the schema change only improves validation, representation, optional metadata, or tooling while preserving MICC meaning.

A MICC revision is required when a proposed MIM change would alter normative meaning—for example by adding a capability family, changing approval semantics, changing authority direction, changing lifecycle meaning, expanding outcome vocabulary, weakening scope constraints, or allowing provider extensions to redefine MICC fields.

The current schema's `additionalProperties: false`, bounded enums, and namespaced provider extensions support that separation.

**Condition D:** The final specification must state a compatibility rule: representational MIM changes may version MIM independently, but any MIM change that alters MICC-defined semantics requires a MICC revision matter rather than schema-only evolution.

---

## 5. CG-0032 Theia re-review trigger

**Determination:** CG-0033 does **not** trigger a Theia re-review of CG-0032.

CG-0033 does not change MCP's architectural role, authority direction, or separate-authorization gates. It incorporates CG-0032 as the governing MCP boundary and preserves its downstream read-only direction. The new integration contract governs provider adapters beneath MIRRORNODE capability semantics; it does not revise the MCP projection contract.

A CG-0032 re-review would be triggered if a later revision of CG-0033 or another matter attempted to make MCP inbound, write-capable, execution-bearing, authoritative, or otherwise changed the separate-authorization boundary established by CG-0032.

**CG-0032 re-review triggered:** NO.

---

## Cross-review dependencies

This architectural approval does not pre-empt the bounded determinations assigned to the other reviewers:

- **Osiris:** placement and disclosure treatment of MICC evidence candidates relative to `AUDIT_EMISSION`.
- **Thoth:** security sufficiency of authority boundaries, credential declarations, lifecycle authorization, and bypass resistance.
- **Ptah:** implementability, lifecycle enforcement placement, schema/tooling sufficiency, and Adapter 01 readiness.

If any of those determinations requires a change to architectural role, authority direction, or separate-authorization gates, Theia re-review of the resulting revision is required before synthesis.

---

## Position

**APPROVED_WITH_CONDITIONS**

Conditions A–D are bounded architectural clarifications. They do not authorize implementation, canon promotion, deployment, publication, or merge.

CG-0033 may continue through the parallel review cycle. Final disposition should occur only after Ptah, Thoth, Osiris, and Theia positions are present and synthesized, and after any review-driven revisions have been checked against their respective re-review triggers.
