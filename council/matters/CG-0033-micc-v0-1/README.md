# CG-0033 — MIRRORNODE Integration Capability Contract v0.1 + Integration Manifest v0.1

**Status:** ACCEPTED_WITH_CONDITIONS — reviewed pre-canon artifacts  
**Type:** Governance Definition  
**Initiator:** Operator  
**Opened:** 2026-08-12  
**Disposition:** 2026-08-13  
**Branch:** `cg-0033-micc-v0-1`

---

## Disposition

The Operator accepted MICC v0.1 and MIM v0.1 with the conditions preserved in
the four reviewer positions and the cross-position synthesis.

This disposition does not authorize merge, canon promotion, adapter
implementation, credential access, Runtime Registry or MOPCON changes,
deployment, or publication. Each remains separately gated.

- Disposition record: `history/2026-08-13-operator-disposition.md`
- Review synthesis: `synthesis/REVIEW_SYNTHESIS.md`
- Post-merge review closure: `history/2026-08-13-post-merge-review-closure.md`

---

## Accepted pre-canon artifacts

| Artifact | Current location | Possible canon location after separate promotion |
|---|---|---|
| MICC v0.1 specification | `docs/integration/MICC_V0_1.md` | `canon/contracts/MICC_V0_1.md` |
| MIM v0.1 JSON Schema | `docs/integration/MIM_V0_1.schema.json` | `canon/schemas/MIM_V0_1.schema.json` |
| MIM v0.1 example manifest | `docs/integration/examples/mim-v0.1.example.yaml` | reference only |

Canon promotion requires a separate explicit Operator action and then-current
canon index/navigation validation.

---

## Governing relationships

| Anchor | Final relationship |
|---|---|
| CG-0032 MCP Surface Contract | MCP remains a downstream read-only projection surface. MICC does not authorize inbound, write-capable, or execution-bearing MCP behavior. |
| `AUDIT_EMISSION` | Locked top-level audit fields and vocabularies remain controlling. MICC-specific detail is additive under `evidence.micc`. |
| Current governance and registry evidence | The April Lucian `/dispatch` model is historical for its runtime generation. Current interpretation is sourced from `docs/continuity/LUCIAN_AND_RUNTIME_RECONCILIATION_2026-08-13.md` and `docs/continuity/AGENT_REGISTRY_EVIDENCE_SNAPSHOT_2026-08-13.md`; runtime eligibility does not confer authority. |

---

## Review record

| Reviewer | Final position |
|---|---|
| Ptah | APPROVED_WITH_CONDITIONS |
| Thoth | APPROVED_WITH_CONDITIONS |
| Osiris | APPROVED_WITH_CONDITIONS |
| Theia | APPROVED_WITH_CONDITIONS |

All four positions are filed under `positions/`. Review-driven corrections and
the triggered Theia re-review are reflected in the synthesis.

---

## Resolved questions

1. **Evidence placement:** MICC-specific evidence is nested under the locked
   `AUDIT_EMISSION.evidence.micc` object.
2. **Lifecycle placement:** MICC owns lifecycle semantics; a Runtime Registry
   may implement them only as a subordinate enforcement surface.
3. **Schema format:** JSON Schema is canonical for machine validation; YAML is
   an example/serialization format, not a second canonical schema.

---

## Remaining gate

Verify PR #44's corrected head, configured checks, and fresh Codex review
state. A separate explicit Operator merge authorization is required before
merge.

No implementation work is authorized by this matter.
