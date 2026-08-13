# Osiris — Disclosure Authority Review
## CG-0033: MICC v0.1 + MIM v0.1

**Requesting:** Osiris  
**Matter:** CG-0033  
**Review class:** Disclosure Authority Review  
**Artifacts under review:**
- `docs/integration/MICC_V0_1.md` (Section 9: canonical receipt requirements)
- `docs/integration/MIM_V0_1.schema.json` (evidence field declarations)

---

## What you are reviewing

The canonical receipt requirements (Section 9) and lifecycle state
definitions (Section 10) of MICC v0.1, and the evidence field declaration
structure in MIM v0.1 — specifically for coherence with the locked
AUDIT_EMISSION contract and for disclosure boundary integrity.

---

## Questions requiring your determination

**1. Additive coherence with AUDIT_EMISSION.**  
The locked AUDIT_EMISSION contract defines: `timestamp`, `repo`,
`repo_hash`, `charter_hash`, `event_type`, `actor`, `verdict`,
`evidence` (object), and `audit_id`. MICC introduces additional evidence
candidates: `execution_nonce`, requesting actor, executing actor,
`approval_object`, and `policy_version`. Do any of these conflict with
or duplicate an existing AUDIT_EMISSION field with different semantics?

**2. Evidence field placement determination (open question resolution).**  
This is the primary open question you must resolve. The additional MICC
evidence fields are currently unplaced. Determine which of the following
applies to each field:
  - (a) Adapter-receipt extension carried inside the existing
    `evidence` object of the AUDIT_EMISSION schema
  - (b) Parallel MICC record that references `audit_id` but is not
    part of the AUDIT_EMISSION record itself
  - (c) Grounds for a future AUDIT_EMISSION revision matter

Your determination here gates MICC Section 9 finalization.

**3. Adapter-declared evidence fields.**  
MIM allows individual adapters to declare adapter-specific evidence
fields beyond the MICC baseline. Does this create a disclosure risk if
an adapter declares fields that expose provider-internal state, credential
identifiers, path information, or other sensitive data? What constraints
should MICC place on adapter evidence field declarations?

**4. Observer vs. authority.**  
MICC treats OTel as the interoperability layer and external tools
(LangSmith, Axiom, etc.) as observers with no write authority over the
evidence chain. Does this treatment satisfy the Osiris requirement that
no external telemetry product becomes the historical authority for an
Osiris determination?

**5. Lifecycle transitions as audit records.**  
Should each adapter lifecycle transition (e.g., VERIFIED → AUTHORIZED,
ACTIVE → SUSPENDED) generate an AUDIT_EMISSION-conformant record?
If so, what is the required `event_type` and `actor` field value for:
  - Operator-initiated transitions
  - Automated health-check-triggered transitions (e.g., ACTIVE → DEGRADED)

---

## What you must not determine

- Whether any specific provider should be used
- Implementation decisions for any adapter
- Canon promotion decisions
- Changes to the AUDIT_EMISSION contract (flag as revision matter if needed)

---

## Required output

`council/matters/CG-0033-micc-v0-1/positions/OSIRIS_POSITION.md`

State one of: `APPROVED` / `APPROVED_WITH_CONDITIONS` / `REVISION_REQUIRED`

If the evidence field placement determination (question 2) cannot be
resolved without an AUDIT_EMISSION revision, state that explicitly and
identify it as a condition on MICC acceptance rather than a blocker.
