# Thoth — Security and Authority Boundary Position
## CG-0033: MICC v0.1 + MIM v0.1

**Reviewer role:** Thoth security-boundary lane  
**Procedural provenance:** Role-bound review executed in the current THEIA/ChatGPT integration session against the preserved CG-0033 artifacts and Thoth review packet. This file does not claim a separate live Thoth runtime invocation.  
**Matter:** CG-0033  
**Review class:** Security and Authority Boundary Review  
**State:** REVISION_REQUIRED  
**Reviewed against:** preserved CG-0033 head `3a15b749a16bf873ff3c32fc1a95d278dde54eb8`, with current CORE-HUB reconciliation state considered where it changes authority assumptions.

---

## Determination

MICC establishes the correct security direction: providers do not acquire MIRRORNODE authority, authorization is distinct from technical verification, credential contents do not belong in MIM, and MCP must not invert the canonical dependency direction.

The remaining gaps are enforcement gaps rather than conceptual failures. They must be closed before the contract can be treated as security-sufficient.

---

## 1. Provider authority prohibition

**Determination:** Normatively strong, not yet fully machine-auditable.

Sections 3 and 14 clearly prohibit provider-originated semantic authority. The MIM schema also prevents arbitrary top-level field redefinition. However, schema validation alone cannot prove that an adapter implementation does not defer semantic decisions to provider-native behavior at runtime.

### R1 — Conformance enforcement for semantic authority

MICC conformance must include an executable/policy-verifiable check that:

- provider responses cannot alter approval class;
- provider responses cannot alter lifecycle authority;
- provider responses cannot redefine outcome vocabulary;
- provider responses cannot become canonical evidence by themselves;
- provider-native principal/role claims cannot be promoted to MIRRORNODE authority without an authorized translation boundary.

The prohibition must be testable at the adapter boundary, not only stated in prose.

---

## 2. Credential requirement declaration

**Determination:** Credential contents are correctly excluded, but credential metadata can still disclose sensitive operational information.

Names, scopes, environment labels, provider-specific identifiers, secret-store paths, tenant identifiers, and internal topology can all become sensitive even when the secret value itself is absent.

### R2 — Credential metadata disclosure boundary

MICC/MIM must prohibit credential requirement fields from carrying:

- secret contents;
- secret-store paths;
- opaque credential IDs that function as bearer references;
- tenant/account identifiers unless specifically approved for disclosure;
- internal host/path topology not required for validation.

Human-readable `name` values should be descriptive requirement labels, not secret identifiers. Runtime credential resolution must occur outside MIM.

---

## 3. VERIFIED vs AUTHORIZED

**Determination:** The conceptual separation is correct and Section 10's `VERIFIED → AUTHORIZED | Operator only` rule is sufficient as the authority rule.

A health check or verification pass must never produce AUTHORIZED state.

### R3 — Authorization evidence requirement

The AUTHORIZED transition must require a machine-verifiable reference to the authorizing Operator disposition/approval object. A state mutation without that evidence must fail closed.

The same principle applies to re-authorization from SUSPENDED.

---

## 4. MCP inversion prohibition

**Determination:** MICC preserves the CG-0032 policy direction in prose, but direct invocation bypass resistance is not sufficiently specified.

Section 12 says inbound/write/execution-bearing MCP requires separate authority and that external clients approach the governed capability surface. It does not yet state what an adapter must reject when a client attempts to bypass that surface.

### R4 — Governed invocation envelope

An adapter must reject any invocation that cannot demonstrate a valid MIRRORNODE invocation context containing, as applicable:

- requesting principal;
- adapter identity;
- approval classification result/reference;
- lifecycle ACTIVE/DEGRADED state;
- policy version;
- execution nonce;
- scope decision.

A malformed MCP client, REST client, SDK client, or provider-native callback must not be able to reach adapter execution merely by knowing the adapter endpoint.

This is protocol-neutral and does not authorize inbound MCP.

---

## 5. Evidence chain integrity

**Determination:** Section 9.3 correctly places external telemetry products in observer-only status. OTel is an interoperability format and must not become the canonical evidence store.

External telemetry may receive projections/copies but must have no authority to mutate, approve, supersede, or become the sole retention point for canonical MIRRORNODE evidence.

Osiris must resolve the exact locked `AUDIT_EMISSION` mapping before acceptance.

---

## 6. Lifecycle placement

**Determination:** The security-critical lifecycle semantics must remain normative in MICC even if persistence/enforcement code lives in a separate Runtime Registry.

Moving the state machine entirely out of MICC would create a contract/enforcement divergence risk. A separate registry specification may refine storage, APIs, and mechanics only if it is explicitly subordinate to MICC transition semantics and cannot broaden transition authority.

---

## Current-authority reference correction

MICC Section 3.3 and Appendix A currently rely on the April Lucian `/dispatch` `SYSTEM_CONTRACT` as current authority. CORE-HUB has now formally classified that runtime generation as historical.

### R5 — Current authority reference

Final CG-0033 text must remove or version-bound the stale claim that Lucian's April `/dispatch` execution authority is the current runtime truth. The integration contract should defer intra-lattice authority to the **current applicable governance/registry authority source**, not hard-code a superseded runtime generation.

Because this changes an architectural authority reference, the revised text requires Theia re-review before synthesis.

---

## Position

**REVISION_REQUIRED**

R1–R5 are bounded security/authority corrections. The underlying MICC direction remains viable. No implementation, canon promotion, deployment, or merge is authorized by this position.
