# Osiris — Disclosure Authority Position
## CG-0033: MICC v0.1 + MIM v0.1

**Reviewer role:** Osiris disclosure/evidence lane  
**Procedural provenance:** Role-bound review executed in the current THEIA/ChatGPT integration session against the preserved CG-0033 artifacts, locked `AUDIT_EMISSION`, and the Osiris review packet. This file does not claim a separate live Osiris runtime invocation.  
**Matter:** CG-0033  
**Review class:** Disclosure Authority Review  
**State:** REVISION_REQUIRED  
**Reviewed against:** preserved CG-0033 head `3a15b749a16bf873ff3c32fc1a95d278dde54eb8` plus current locked `canon/contracts/AUDIT_EMISSION.md`.

---

## Determination

MICC's evidence model is directionally compatible with the locked audit invariant, and the five additional MICC evidence candidates can be carried without changing the top-level `AUDIT_EMISSION` schema.

However, MICC Section 9.1 currently redefines several locked top-level audit semantics while stating that it is additive only. That conflict must be corrected before acceptance.

---

## 1. Additive coherence with AUDIT_EMISSION

The MICC evidence candidates do not inherently duplicate locked fields:

- `execution_nonce` — new replay/correlation evidence;
- `requesting_actor` — initiating principal identity distinct from the locked coarse actor classification;
- `executing_actor` — concrete adapter/principal identity;
- `approval_object` — reference to the authorizing record;
- `policy_version` — policy basis at execution time.

These can coexist with the locked schema if carried inside the existing `evidence` object.

### Evidence placement determination

Use option **(a)** for all five fields: carry them inside the existing `evidence` object under a namespaced MICC extension object:

```json
"evidence": {
  "inputs": {},
  "outputs": {},
  "duration_ms": 0,
  "error": null,
  "micc": {
    "execution_nonce": "...",
    "requesting_actor": "...",
    "executing_actor": "...",
    "approval_object": "...",
    "policy_version": "...",
    "outcome_code": "..."
  }
}
```

This preserves the locked top-level contract and avoids parallel-record divergence.

A future `AUDIT_EMISSION` revision may later formalize the nested extension shape, but such a revision is not required to resolve placement for CG-0033.

---

## 2. Locked top-level field conflicts

MICC Section 9.1 currently conflicts with the locked contract in three places:

1. MICC proposes `event_type = "adapter_invocation"`, while locked `AUDIT_EMISSION` bounds event type to its existing vocabulary.
2. MICC proposes `actor = adapter_id`, while the locked contract describes actor using the coarse human/agent/system classification.
3. MICC proposes mapping the Section 8.2 outcome vocabulary directly into `verdict`, while locked `AUDIT_EMISSION` bounds verdict to `SUCCESS | FAILURE | BLOCKED | ESCALATED`.

These are not additive changes.

### R1 — Preserve locked top-level semantics

MICC must stop redefining those top-level fields.

For adapter execution, use an AUDIT_EMISSION-conformant top-level record and preserve adapter-specific detail inside `evidence.micc`.

Recommended interim mapping:

- locked `event_type`: use the nearest existing conformant execution/invocation class until a separate audit-contract revision adds an adapter-specific event type;
- locked `actor`: `agent` or `system` according to the actual executing class, with the concrete `adapter_id` in `evidence.micc.executing_actor`;
- locked `verdict`: map MICC outcomes into `SUCCESS`, `FAILURE`, or `BLOCKED`; retain the precise MICC outcome code in `evidence.micc.outcome_code`.

`ESCALATED` remains available only where the audit event actually represents escalation.

---

## 3. Adapter-declared evidence fields

**Determination:** Provider-/adapter-specific evidence declarations require an explicit disclosure boundary.

### R2 — Evidence declaration safety

Adapter-specific evidence must be restricted to sanitized, non-secret, purpose-bounded fields. It must not emit:

- credential contents;
- bearer references;
- secret-store paths;
- raw authorization tokens;
- provider-internal identifiers unless explicitly allowed and necessary;
- filesystem paths/internal topology unless specifically required and approved;
- unrestricted provider response bodies.

Provider extensions may name evidence fields, but they may not make sensitive provider state canonical merely by declaration.

---

## 4. Observer vs authority

**Determination:** MICC Section 9.3 is coherent with the Osiris evidence invariant.

OTel is a transport/interoperability representation only. External telemetry products may receive observational projections but must not:

- write or mutate the canonical record;
- determine historical truth;
- become the sole evidence-retention surface;
- overwrite or supersede an Osiris/MIRRORNODE determination.

No revision is required on this point beyond preserving the rule during implementation.

---

## 5. Lifecycle transitions as audit records

**Determination:** Every lifecycle transition should emit an `AUDIT_EMISSION`-conformant record, as MICC already requires.

Until a future audit-contract revision creates a dedicated lifecycle event type, use an existing conformant event type and place precise transition semantics in `evidence.micc`, including:

- prior state;
- next state;
- transition reason;
- authorizing/reference object where required;
- concrete initiating principal;
- policy version where applicable.

For Operator-initiated transitions:

- top-level `actor`: `human`;
- concrete Operator identity/reference: inside `evidence.micc.requesting_actor` or a future dedicated identity field.

For automated health/policy transitions:

- top-level `actor`: `system`;
- concrete registry/policy mechanism: inside `evidence.micc.executing_actor`.

A future `AUDIT_EMISSION` revision to add explicit `adapter_invocation` and `adapter_lifecycle_transition` event types would improve semantic precision, but CG-0033 need not block on that revision if it remains conformant with the locked contract in the interim.

---

## R3 — MICC Section 9 finalization

Revise Section 9 to:

1. place the five MICC evidence candidates under `evidence.micc`;
2. preserve all locked top-level `AUDIT_EMISSION` fields and vocabularies;
3. define a bounded mapping from MICC outcome codes to locked verdicts;
4. retain precise MICC outcome/state-transition detail in the nested evidence object;
5. prohibit adapter-declared evidence from expanding the disclosure boundary.

---

## Position

**REVISION_REQUIRED**

The primary open placement question is resolved: **option (a), nested inside the existing `evidence` object, preferably under `evidence.micc`.**

Revision is required because current MICC Section 9.1 contradicts locked top-level `AUDIT_EMISSION` semantics while describing itself as additive. This is bounded and repairable without redesigning the evidence architecture.
