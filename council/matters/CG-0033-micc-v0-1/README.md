# CG-0033 — MIRRORNODE Integration Capability Contract v0.1 + Integration Manifest v0.1

**Status:** Intake  
**Type:** Governance Definition  
**Initiator:** Operator  
**Opened:** 2026-08-12  
**Branch:** `cg-0033-micc-v0-1`

---

## Decision Question

Should MIRRORNODE adopt MICC v0.1 as the normative specification governing
what an integration means inside MIRRORNODE, and MIM v0.1 as the
machine-readable adapter declaration schema implementing it, while
explicitly prohibiting any provider from becoming semantic authority
merely by implementing a capability?

---

## What this matter produces (if accepted)

| Artifact | Location (draft) | Location (if promoted) |
|---|---|---|
| MICC v0.1 normative specification | `docs/integration/MICC_V0_1.md` | `canon/contracts/MICC_V0_1.md` |
| MIM v0.1 JSON Schema | `docs/integration/MIM_V0_1.schema.json` | `canon/schemas/MIM_V0_1.schema.json` |
| MIM v0.1 example manifest | `docs/integration/examples/mim-v0.1.example.yaml` | reference only |

Canon promotion requires a separate explicit operator action after acceptance.
This matter does not grant promotion authority.

---

## What this matter does NOT produce

- No adapter implementations
- No provider code or configuration
- No credential access
- No changes to `AUDIT_EMISSION.md`, `SYSTEM_CONTRACT.md`, or CG-0032
- No runtime, registry, or MOPCON changes
- No canon promotion
- No deployment or publication
- No merge authority (merge requires separate operator gate)

---

## Relationship to existing canon

| Canon anchor | Relationship |
|---|---|
| CG-0032 MCP Surface Contract | CG-0032 remains governing for MCP as a downstream read-only projection. MICC does not classify MCP as an adapter. Dependency direction (canonical → MCP) is not invertible by any MICC adapter or extension. |
| AUDIT_EMISSION contract | MICC receipt requirements are additive only. MICC does not redefine AUDIT_EMISSION fields. Additional evidence fields are unresolved pending Osiris determination (see open questions). |
| SYSTEM_CONTRACT v1.1 | MICC defers to SYSTEM_CONTRACT for intra-lattice principal identity. Lucian's execution authority is not redefined by MICC. |

---

## Reviews required

| Reviewer | Focus | Request |
|---|---|---|
| Ptah | Implementation contract, MIM schema, lifecycle state machine placement | `review-requests/PTAH_IMPLEMENTATION_CONTRACT_REVIEW.md` |
| Thoth | Security boundaries, provider authority prohibition, credential declaration, MCP inversion prohibition | `review-requests/THOTH_SECURITY_BOUNDARY_REVIEW.md` |
| Osiris | Disclosure authority, AUDIT_EMISSION additive coherence, evidence field mapping determination | `review-requests/OSIRIS_DISCLOSURE_AUTHORITY_REVIEW.md` |
| Theia | Architectural integration, canon placement, SYSTEM_CONTRACT coherence, CG-0032 Theia re-review trigger determination | `review-requests/THEIA_ARCHITECTURAL_INTEGRATION_REVIEW.md` |

---

## Open questions (for review cycle)

1. **Evidence field mapping** — Where do MICC-introduced fields (`execution_nonce`, requesting/executing actor separation, `approval_object`, `policy_version`) sit relative to the locked AUDIT_EMISSION schema? Osiris determines.
2. **Lifecycle state machine placement** — Normative in MICC itself, or in a separate Runtime Registry spec? Ptah and Thoth advise.
3. **MIM schema format** — JSON Schema only, or also a canonical YAML schema? Ptah advises.

---

## Next step

Distribute review-request packets. No implementation work proceeds until
all four reviews are received and operator issues a disposition.
