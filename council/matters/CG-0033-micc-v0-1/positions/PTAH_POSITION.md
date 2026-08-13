# Ptah — Implementation Contract Position
## CG-0033: MICC v0.1 + MIM v0.1

**Reviewer role:** Ptah implementation-contract lane  
**Procedural provenance:** Role-bound review executed in the current THEIA/ChatGPT integration session against the preserved CG-0033 artifacts and Ptah review packet. This file does not claim a separate live Ptah runtime invocation.  
**Matter:** CG-0033  
**Review class:** Implementation Contract Review  
**State:** REVISION_REQUIRED  
**Reviewed against:** preserved CG-0033 head `3a15b749a16bf873ff3c32fc1a95d278dde54eb8`, with current CORE-HUB reconciliation state considered where it changes implementation assumptions.

---

## Determination

MICC v0.1 has a coherent contract-first shape and MIM v0.1 is structurally useful, but the present draft is not yet precise enough to accept an Adapter 01 implementation work order without material interpretation at the adapter boundary.

The required revisions are bounded. They do not require replacing MICC/MIM or changing the eight-family model.

---

## 1. Implementability of the eight primitive families

**Determination:** The eight family boundaries are adequate as taxonomy, but family semantics alone are not an implementable invocation contract.

MIM currently declares each capability using only:

- `name`
- `description`
- `approval_class`

There is no machine-readable declaration for request shape, response shape, idempotency/replay behavior, timeout behavior, side-effect class, or family-specific conformance requirements. MICC Section 13 nevertheless requires an implementation to implement all declared capabilities and produce bounded outcomes.

An adapter author would therefore have to invent part of the operational contract.

### R1 — Capability contract surface

Before Adapter 01 implementation, MICC/MIM must either:

1. add a bounded machine-readable operation-contract structure per declared capability; or
2. explicitly define and reference a separate adapter-interface specification that supplies request/response and execution semantics without allowing providers to redefine MICC meaning.

At minimum the implementable contract must resolve:

- input contract/reference;
- output contract/reference;
- side-effect/read-only classification;
- retry/idempotency expectation where applicable;
- timeout/termination expectation;
- capability-specific conformance test reference.

This is an implementation-contract gap, not a request to add provider-specific implementation detail.

---

## 2. MIM schema structure and format

**Determination:** JSON Schema is sufficient as the canonical validation schema. A second canonical YAML schema is not required.

YAML may remain a human-facing serialization/example format as long as YAML instances are normalized and validated against the JSON Schema. Maintaining two normative schemas would create avoidable drift.

The current schema's use of bounded enums and `additionalProperties: false` is helpful.

### R2 — Referential precision

Several MIM fields remain free-text where runtime validation needs stronger references:

- `credential_requirements[].scope` should resolve to one or more declared capability names or a defined scope vocabulary rather than unconstrained prose;
- `scope_ceiling` needs a governed vocabulary or explicit comparison semantics if runtime code is expected to enforce a ceiling;
- approval-record reference semantics must be machine-readable if `approval_object` becomes receipt evidence.

---

## 3. Lifecycle state machine placement

**Determination:** The lifecycle semantics and authorization invariants should remain normative in MICC. A Runtime Registry may implement and persist them, but it must not become free to redefine them.

The current transition table is implementable in principle.

The following transitions correctly require Operator action:

- VERIFIED → AUTHORIZED
- SUSPENDED → AUTHORIZED
- AUTHORIZED → RETIRED
- ACTIVE → RETIRED
- SUSPENDED → RETIRED

Automated health transitions are acceptable only after authority is already present and only within the transitions expressly permitted by MICC.

### R3 — Runtime enforcement contract

MICC should state explicitly that a runtime registry is an enforcement/persistence implementation of the MICC lifecycle, not the semantic owner of lifecycle state. Any registry implementation must reject transitions not authorized by the MICC transition table and must record the authorizing basis for gated transitions.

---

## 4. Credential requirement declaration

**Determination:** Declaring requirements without credential contents is implementable and preferable, but the current declaration still needs referential precision.

A credential requirement must never contain provider secret values, secret material, or secret-store paths. Runtime resolution should occur through a credential-authority reference outside the MIM declaration.

No canonical YAML schema is needed for this purpose.

---

## 5. Adapter 01 readiness gate

Ptah would accept an Adapter 01 work order only after all of the following are true:

1. R1 capability operation semantics are resolved.
2. R2 scope/credential/approval references are machine-enforceable.
3. R3 lifecycle enforcement ownership is explicit.
4. Osiris resolves MICC Section 9 receipt-field placement and any conflict with locked `AUDIT_EMISSION`.
5. Thoth closes any authorization, bypass, or credential-disclosure security gaps.
6. MICC's intra-lattice authority references are updated to current governance/runtime truth rather than relying on the now-historical April Lucian `/dispatch` model.
7. The resulting MIM validates with a conformance fixture for the proposed Adapter 01 declaration.

No statement here selects Infisical or authorizes implementation.

---

## Position

**REVISION_REQUIRED**

Revision themes R1–R3 are bounded to implementation-contract precision. They do not require redesigning the eight primitive families or abandoning MICC/MIM separation.
