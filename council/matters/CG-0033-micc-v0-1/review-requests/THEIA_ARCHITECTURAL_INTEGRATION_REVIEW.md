# Theia — Architectural Integration Review
## CG-0033: MICC v0.1 + MIM v0.1

**Requesting:** Theia  
**Matter:** CG-0033  
**Review class:** Architectural Integration Review  
**Artifacts under review:**
- `docs/integration/MICC_V0_1.md`
- `docs/integration/MIM_V0_1.schema.json`
- `docs/integration/examples/mim-v0.1.example.yaml`

---

## What you are reviewing

The architectural coherence of MICC v0.1 with existing MIRRORNODE canon:
the relationship between MICC and SYSTEM_CONTRACT v1.1, the relationship
between MICC and CG-0032 (MCP Surface Contract), the placement of draft
artifacts under `docs/integration/`, and the architectural stability of
the MICC/MIM separation (normative spec vs. machine-readable declaration).

---

## Questions requiring your determination

**1. Canon placement.**  
Draft artifacts are placed under `docs/integration/` in this matter,
with canon promotion deferred to a separate explicit action. Does the
existing `canon/INDEX.md` imply any constraint on where MICC would
eventually be promoted? Should MICC land in `canon/contracts/` (alongside
AUDIT_EMISSION) or does its normative status warrant a distinct path
such as `canon/specs/`?

**2. SYSTEM_CONTRACT coherence.**  
MICC introduces integration adapter principals as a distinct class from
lattice agents. SYSTEM_CONTRACT v1.1 establishes Lucian's execution
authority and the agent registry. Are these coherent? Is the MICC
statement—"integration adapter principals defer to SYSTEM_CONTRACT for
intra-lattice identity"—sufficient, or does MICC need to define more
precisely how adapter principal identity relates to the lattice agent
registry?

**3. CG-0032 MCP boundary coherence.**  
CG-0032 defines MCP as a downstream read-only projection surface with
dependency direction canonical → MCP. MICC's CG-0032 anchor preserves
that direction and explicitly prohibits inversion. Are the two
characterizations architecturally coherent? Is there any tension
between them that must be resolved in MICC text before acceptance?

**4. MICC/MIM separation stability.**  
MICC owns normative semantics; MIM declares adapter instances against
those semantics. Is this separation architecturally stable? Is there
a realistic risk that MIM schema evolution forces MICC semantic changes,
collapsing the normative/declarative distinction over time?

**5. CG-0032 Theia re-review trigger determination.**  
Your re-review condition from CG-0032 states: re-review required only
if revision changes architectural role, authority direction, or
separate-authorization gates. State explicitly:
  - Does CG-0033 constitute a change to architectural role, authority
    direction, or separate-authorization gates relative to CG-0032?
  - Is a Theia re-review of CG-0032 triggered by CG-0033?

---

## What you must not determine

- Whether any specific provider should be used
- Implementation decisions for any adapter
- Security boundary details (Thoth's scope)
- Credential or evidence field placement (Osiris's scope)

---

## Required output

`council/matters/CG-0033-micc-v0-1/positions/THEIA_POSITION.md`

State one of: `APPROVED` / `APPROVED_WITH_CONDITIONS` / `REVISION_REQUIRED`

Address the CG-0032 re-review trigger question explicitly.
