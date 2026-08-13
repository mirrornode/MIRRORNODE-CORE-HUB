# Ptah — Implementation Contract Review
## CG-0033: MICC v0.1 + MIM v0.1

**Requesting:** Ptah  
**Matter:** CG-0033  
**Review class:** Implementation Contract Review  
**Artifacts under review:**
- `docs/integration/MICC_V0_1.md`
- `docs/integration/MIM_V0_1.schema.json`
- `docs/integration/examples/mim-v0.1.example.yaml`

---

## What you are reviewing

The proposed MIRRORNODE Integration Capability Contract (MICC) v0.1 normative
specification and the Integration Manifest (MIM) v0.1 schema. This is
specification and schema only. No provider implementation is in scope.

---

## Questions requiring your determination

**1. Implementability of the eight primitive families.**  
Are the capability family definitions sufficiently precise that an adapter
author can implement against them without interpreting undefined behavior?
Identify any family whose boundary is too vague to implement against.

**2. MIM schema structure and format.**  
Is MIM v0.1 as a JSON Schema declaration sufficient for runtime
interrogation? Should it carry a canonical YAML schema alongside the
JSON Schema for tooling validation? What fields are missing or ambiguous?

**3. Lifecycle state machine placement.**  
Is the DECLARED → IMPLEMENTED → VERIFIED → AUTHORIZED → ACTIVE → DEGRADED
→ SUSPENDED → RETIRED sequence implementable as a runtime registry concern?
Should any transition require an explicit operator gate rather than an
automated health check? Should the lifecycle state machine live in MICC
as a normative requirement, or in a separate Runtime Registry specification
that implements MICC?

**4. Credential requirement declaration.**  
Does the pattern of declaring credential requirements without credential
contents create any implementation ambiguity for the Credential Authority
primitive?

**5. Adapter 01 readiness gate.**  
What would need to be true in MICC/MIM before you would accept a work
order to implement Infisical Adapter 01 against the contract? State the
minimum acceptance conditions from an implementation perspective.

---

## What you must not determine

- Whether any specific provider should be used
- Whether Infisical is the right Credential Authority adapter
- Any implementation decisions for providers not yet in scope
- Whether canon promotion is appropriate (separate action)

---

## Required output

`council/matters/CG-0033-micc-v0-1/positions/PTAH_POSITION.md`

State one of: `APPROVED` / `APPROVED_WITH_CONDITIONS` / `REVISION_REQUIRED`

If REVISION_REQUIRED, identify specific revision themes (as R1, R2, etc.)
with bounded scope, consistent with the CG-0032 revision theme format.
