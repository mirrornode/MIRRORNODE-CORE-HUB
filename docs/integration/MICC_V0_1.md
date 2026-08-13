# MIRRORNODE Integration Capability Contract (MICC) v0.1

**Status:** Accepted with conditions — Operator disposition filed under CG-0033  
**Version:** 0.1  
**Created:** 2026-08-12  
**Revision pass:** 2026-08-13 review-driven corrections  
**Authority effect:** Reviewed pre-canon governance definition only; no implementation, canon-promotion, deployment, publication, or merge authority  
**Canon status:** Pre-canon accepted-with-conditions; remains under `docs/integration/` until separate explicit promotion action

---

## Preamble

This document is the normative specification governing what an integration
means inside MIRRORNODE. It defines the semantics that providers implement
but cannot redefine. A provider gains no semantic authority over MIRRORNODE
by implementing a capability described here.

The MIRRORNODE Integration Manifest (MIM) v0.1 is the machine-readable
declaration schema derived from and validated against this contract. MIM
declares adapter instances. MICC defines what those declarations mean.

This contract does not authorize any adapter implementation. Implementation
requires separate operator authorization.

---

## Section 1 — Eight Primitive Capability Families

MIRRORNODE recognizes exactly eight primitive integration capability
families in v0.1. Every adapter must declare which family it implements.
An adapter may implement at most one family per MIM declaration.

| ID | Family | Semantic responsibility |
|---|---|---|
| `IDENTITY` | Identity Authority | Principal identity, session, organization membership, authentication claims |
| `CREDENTIAL` | Credential Authority | Principal, scope, environment, lifetime, revocation, access receipt for secrets and machine credentials |
| `STATE` | State / Record Store | Schema-governed persistent state: transactions, consistency, query |
| `ARTIFACT` | Artifact Store | Binary/blob storage: key, ownership, retention policy, access policy |
| `EXECUTION` | Durable Execution | Step, retry, checkpoint, concurrency, schedule, failure recovery |
| `TRANSPORT` | Event Transport | Stream, durability, consumer group, replay, delivery semantics |
| `EVIDENCE` | Evidence / Telemetry | Receipt emission, trace, execution_nonce, OTel interoperability |
| `METERING` | Economic Metering | Usage event, unit, rate, period, settlement record |

No provider may introduce a ninth family by extension. A new family
requires a MICC revision matter.

---

## Section 2 — Universal Adapter Identity Fields

Every adapter declaration (MIM instance) must carry:

```
adapter_id:        globally unique identifier for this adapter instance
adapter_name:      human-readable name
micc_version:      the MICC version this adapter declares conformance against
capability_family: one of the eight IDs from Section 1
provider_name:     the external provider or system being wrapped
provider_version:  the provider API/SDK version targeted
adapter_version:   semver of this adapter declaration
maintained_by:     principal responsible for this adapter
created_at:        ISO8601 UTC
updated_at:        ISO8601 UTC
```

These fields are immutable after an adapter reaches AUTHORIZED state.
Changes require a new adapter_version and re-entry at DECLARED.

---

## Section 3 — Principal and Authority Semantics

**3.1 Integration adapter principals are a distinct class** from MIRRORNODE
lattice identities. An adapter does not inherit lattice authority. An adapter
operates only under authority explicitly granted through the current applicable
MIRRORNODE governance and approval boundary.

**3.2 A provider is not a principal.** The external provider system
(Infisical, Inngest, Stripe, etc.) is not a MIRRORNODE principal. The
adapter that wraps it is a principal. The provider cannot grant,
escalate, or revoke MIRRORNODE authority.

**3.3 Intra-lattice identity and authority are external dependencies of MICC.**
MICC does not freeze a historical runtime registry or dispatcher model into
this integration contract. Requests must resolve requesting identity,
authorizing basis, executing adapter identity, and applicable authority from
the current governance/registry evidence in force at invocation time.

Historical runtime contracts may remain evidence of prior generations but do
not become current authority merely because an integration references them.

**3.4 Authority direction is MIRRORNODE-governed principal/approval → adapter
→ provider.** No adapter may receive MIRRORNODE authority from its provider.
No adapter may claim authority not established by the applicable governance
or approval record.

**3.5 Role separation is preserved.** Requesting principal, maintaining
principal, authorizing authority, executing adapter, and provider are distinct
identities where they differ and must remain separately attributable.

---

## Section 4 — Capability and Scope Declaration

Each adapter must declare provider and MIRRORNODE scope requirements plus an
implementable operation contract for every capability.

```
capabilities:      list of operation contracts
scopes_required:   list of provider-side access scopes required
scopes_granted:    list of MIRRORNODE scopes permitted
scope_ceiling:     explicit maximum MIRRORNODE scope vocabulary entry
```

Each capability operation contract must declare:

```
name:                    stable operation identifier
description:             human-readable purpose
approval_class:          Section 6 approval class
input_schema_ref:        schema/reference for request shape
output_schema_ref:       schema/reference for successful result shape
side_effect_class:       READ_ONLY | STATE_CHANGE | EXTERNAL_EFFECT
idempotency:             REQUIRED | SUPPORTED | NOT_APPLICABLE
retry_policy:            NONE | SAFE_RETRY | IDEMPOTENCY_KEY_REQUIRED
timeout_seconds:         positive integer upper bound
conformance_test_ref:    test/fixture identifier for operation conformance
```

An adapter may not exercise a scope not listed in `scopes_granted`.
An adapter may not request a provider scope not listed in `scopes_required`.
Scope escalation requires a new adapter declaration at DECLARED state.

`scope_ceiling` must be an entry from the same governed MIRRORNODE scope
vocabulary used by `scopes_granted`; implementations may not infer ordering
from arbitrary free text.

---

## Section 5 — Credential Requirement Declaration

Adapters declare credential requirements without carrying credential
contents. A MIM declaration is not a credential store.

```
credential_requirements:
  - name:          non-sensitive human-readable requirement label
    kind:          API_KEY | OAUTH_TOKEN | MTLS_CERT | MACHINE_IDENTITY | OTHER
    capabilities:  one or more declared capability names requiring it
    environment:   PRODUCTION | STAGING | DEVELOPMENT | ALL
    lifetime:      SHORT_LIVED | LONG_LIVED | ROTATING | STATIC
    revocable:     true | false
    required:      true | false
```

Credential declarations MUST NOT contain credential contents, bearer values,
secret-store paths, raw token identifiers, or provider/internal topology.
Tenant/account identifiers or other sensitive metadata may appear only when
required for validation and explicitly allowed by the applicable disclosure
policy.

The Credential Authority implementation is responsible for satisfying declared
credential requirements at runtime through a separate credential-resolution
boundary. Credential contents never appear in MIM or MICC receipts.

---

## Section 6 — Approval Classification

Each adapter capability must declare its approval class:

```
APPROVAL_NONE       — read-only and no external effect; no state change
APPROVAL_AUTOMATED  — automated gate; policy evaluation required before execution
APPROVAL_OPERATOR   — explicit operator approval required before execution
APPROVAL_COUNCIL    — Council matter/disposition required before activation/use
```

Approval class may not be downgraded without a new adapter declaration and
re-authorization. The approval class is machine-readable and must be evaluated
before execution.

Any approval-bearing invocation must carry a machine-verifiable approval
reference. VERIFIED state, a successful health check, or provider success may
never substitute for authorization.

---

## Section 7 — Health and Readiness Semantics

Adapters must declare health and readiness checks:

```
health_check:
  method:            HTTP_GET | RPC | INTERNAL
  endpoint:          path or identifier where applicable
  interval_seconds:  polling interval
  timeout_seconds:   maximum check duration
  healthy_criteria:  machine-readable condition for HEALTHY verdict
  degraded_criteria: machine-readable condition for DEGRADED verdict
```

A passing health check does not imply authorization. Health automation may
change state only through transitions expressly allowed by Section 10.

---

## Section 8 — Execution, Invocation Envelope, and Failure Semantics

**8.1 Governed invocation envelope.** Every capability invocation must arrive
through a governed MIRRORNODE invocation context that resolves at minimum:

```
requesting_actor
executing_actor / adapter_id
approval_class
approval_object (when required)
policy_version
execution_nonce
requested_scope
scope_decision
adapter_lifecycle_state
```

An adapter must fail closed when required invocation context is absent,
invalid, replayed, unauthorized, or outside the declared scope ceiling.
Knowing a provider endpoint or adapter endpoint is insufficient authority to
invoke a capability.

This rule is protocol-neutral and applies equally to REST, SDK, event,
provider callback, or any future authorized protocol surface.

**8.2 Execution contract.** Every adapter capability invocation must:
- verify lifecycle state is ACTIVE or DEGRADED before proceeding;
- verify the governed invocation envelope;
- enforce the declared operation contract and scope decision;
- emit an `AUDIT_EMISSION`-conformant canonical receipt (Section 9);
- return a machine-readable outcome from the bounded vocabulary below;
- never emit a free-text-only failure classification.

**8.3 Bounded outcome vocabulary:**

```
OUTCOME_SUCCESS
OUTCOME_FAILURE_PROVIDER
OUTCOME_FAILURE_AUTH
OUTCOME_FAILURE_SCOPE
OUTCOME_FAILURE_CONTRACT
OUTCOME_BLOCKED
OUTCOME_DEGRADED
OUTCOME_TIMEOUT
```

Free-text detail may accompany an outcome code but may not substitute for it.
Unknown conditions map to `OUTCOME_FAILURE_CONTRACT`. Providers and adapters
may not introduce new outcome codes without MICC revision.

**8.4 Provider semantic non-escalation is conformance-tested.** Conformance
must verify that provider responses cannot alter approval class, lifecycle
authority, MIRRORNODE outcome vocabulary, canonical evidence ownership, or
MIRRORNODE principal authority.

---

## Section 9 — Canonical Receipt Requirements

Every capability execution must emit a canonical receipt conforming to the
locked `canon/contracts/AUDIT_EMISSION.md` contract. MICC adds nested evidence
semantics but does not redefine locked top-level audit fields or vocabularies.

**9.1 Locked top-level audit semantics remain controlling.**

MICC implementations must populate the top-level `AUDIT_EMISSION` record using
only values permitted by the locked contract in force. MICC-specific precision
is carried inside the existing `evidence` object.

Until a separate `AUDIT_EMISSION` revision creates adapter-specific top-level
vocabulary:

- use the nearest existing conformant `event_type` for execution/invocation;
- use the locked coarse actor class (`human`, `agent`, or `system`) as applicable;
- map MICC outcomes to locked verdicts (`SUCCESS`, `FAILURE`, `BLOCKED`, or
  `ESCALATED` where the audit event genuinely represents escalation).

The exact MICC outcome remains recorded under `evidence.micc.outcome_code`.

**9.2 MICC evidence placement.**

The Osiris disclosure/evidence review determines that MICC-specific evidence
is carried inside the existing audit `evidence` object under a namespaced
`micc` extension:

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

For lifecycle transitions, `evidence.micc` must additionally record prior
state, next state, transition reason, and authorization reference where
required.

**9.3 Evidence disclosure boundary.** Adapter-specific evidence fields must be
sanitized and purpose-bounded. They must not emit credential contents, bearer
references, secret-store paths, unrestricted provider response bodies,
provider-internal identifiers without explicit necessity/allowance, or
filesystem/internal topology not approved for evidence disclosure.

Provider extensions may name evidence fields but cannot make sensitive
provider state canonical merely by declaring it.

**9.4 Canonical evidence is owned by MIRRORNODE.** External telemetry systems
(LangSmith, Axiom, Datadog, etc.) are observers only. OTel may carry
interoperable projections, but no external telemetry product may write,
mutate, supersede, approve, become the sole retention point for, or become the
historical authority over the canonical evidence record.

---

## Section 10 — Lifecycle States and Transition Rules

Lifecycle semantics and authorization invariants are normative in MICC. A
separate Runtime Registry may persist and enforce these states but is
subordinate to MICC semantics and may not broaden transition authority.

### 10.1 Lifecycle states

```
DECLARED
IMPLEMENTED
VERIFIED
AUTHORIZED
ACTIVE
DEGRADED
SUSPENDED
RETIRED
```

### 10.2 Authorized transitions

| From | To | Permitted initiator |
|---|---|---|
| DECLARED | IMPLEMENTED | Adapter maintainer |
| IMPLEMENTED | VERIFIED | Automated verification + Ptah confirmation |
| VERIFIED | AUTHORIZED | Operator only, with approval reference |
| AUTHORIZED | ACTIVE | Automated, post-authorization health pass |
| ACTIVE | DEGRADED | Automated health check |
| DEGRADED | ACTIVE | Automated health recovery |
| ACTIVE | SUSPENDED | Operator or authorized automated policy gate |
| DEGRADED | SUSPENDED | Operator or authorized automated policy gate |
| SUSPENDED | AUTHORIZED | Operator only, with re-authorization reference |
| AUTHORIZED | RETIRED | Operator only |
| ACTIVE | RETIRED | Operator only |
| SUSPENDED | RETIRED | Operator only |

### 10.3 Invariants

- VERIFIED → AUTHORIZED and SUSPENDED → AUTHORIZED require explicit Operator
action plus machine-verifiable authorization evidence.
- A health or conformance pass cannot self-authorize an adapter.
- An adapter outside ACTIVE or DEGRADED may not execute capabilities.
- RETIRED is terminal and its adapter_id may not be reused.
- Every transition emits an `AUDIT_EMISSION`-conformant record with precise
transition detail under `evidence.micc`.
- A Runtime Registry must reject transitions not allowed by this table and
record the authorizing basis for gated transitions.

---

## Section 11 — Provider-Specific Extension Rules

Adapters may declare provider-specific extensions in a `provider_extensions`
block. Extensions:

1. may add namespaced metadata but not redefine MICC fields;
2. may not introduce new capability families;
3. may not modify approval or lifecycle rules;
4. may not introduce outcome codes;
5. must use `x_<provider_name>_<field>` namespacing;
6. are provider-specific metadata, not MICC semantic authority;
7. must comply with Section 9.3 disclosure restrictions.

---

## Section 12 — Protocol Boundary Rules

**12.1 MCP.** CG-0032 remains governing for MCP as a downstream read-only
projection surface. Dependency direction is canonical MIRRORNODE outward to
external MCP runtime.

MCP is not classified as a MICC integration adapter or provider. No MICC
adapter may invert CG-0032 dependency direction. Any inbound, write-capable,
or execution-bearing MCP path requires separate Council authority.

Canonical MIRRORNODE mechanisms may not depend on MCP output for authority,
approval, truth, integrity, or execution permission.

**12.2 Bypass resistance.** A client of any protocol, including a malformed or
unauthorized MCP client, cannot bypass the governed invocation envelope in
Section 8.1. Direct adapter/provider reachability does not confer invocation
authority.

**12.3 Other external protocols.** REST, SDK, callbacks, and other protocol
surfaces approach the governed capability boundary from outside. They do not
become providers or authorities merely by invoking capabilities.

---

## Section 13 — Conformance Requirements

An adapter is MICC-conformant if and only if:

1. its MIM validates against the applicable MIM schema;
2. every declared operation has a complete machine-readable operation contract;
3. it implements all declared capabilities;
4. every invocation validates the governed invocation envelope;
5. every invocation emits a locked-`AUDIT_EMISSION`-conformant receipt with
   MICC detail under `evidence.micc`;
6. every outcome uses the MICC bounded vocabulary and maps to a locked audit
   verdict without redefining that verdict vocabulary;
7. it does not exercise scopes beyond `scopes_granted` or `scope_ceiling`;
8. it does not accept execution while outside ACTIVE or DEGRADED;
9. it does not emit credential contents or prohibited sensitive metadata;
10. provider responses cannot redefine MIRRORNODE approval, lifecycle,
    authority, outcomes, or evidence ownership;
11. conformance tests evaluate machine-readable fields; free-text
    interpretation alone does not satisfy conformance.

---

## Section 14 — Provider Semantic Authority Prohibition

**This prohibition is unconditional and conformance-enforced.**

A provider does not become a semantic authority over MIRRORNODE by
implementing a MICC capability family. Implementation does not grant authority
to define capability meaning, approval classification, lifecycle permission,
canonical evidence, principal identity, or canon.

If provider-native semantics conflict with MICC semantics, MICC governs and
the adapter must translate or fail closed. Provider-native claims do not
propagate upward as MIRRORNODE authority.

This prohibition survives adapter retirement, provider contract changes,
provider API evolution, and provider-initiated semantic changes.

---

## Appendix A — Relationship to Existing Governance and Contracts

| Document / surface | Relationship |
|---|---|
| `canon/contracts/AUDIT_EMISSION.md` | Locked top-level audit contract. MICC adds nested `evidence.micc` semantics and does not redefine top-level vocabularies. |
| Current CORE-HUB governance / registry evidence | Governs intra-lattice identity and authority used by MICC invocations. MICC does not freeze a historical runtime registry. |
| Historical `SYSTEM_CONTRACT.md` v1.1 runtime generation | Historical operational evidence only where later reconciliation marks it superseded by runtime change. |
| CG-0032 MCP Surface Contract | Governs MCP downstream read-only projection. MICC preserves the dependency direction and separate-authorization boundary. |

### Compatibility rule

MIM may version independently for representational, validation, tooling, or
optional-metadata improvements that preserve MICC meaning. Any MIM change that
alters MICC-defined semantics requires a MICC revision matter rather than
schema-only evolution.

---

*This document is an accepted-with-conditions, pre-canon governance definition under CG-0033. The Operator disposition does not authorize implementation, canon promotion, deployment, publication, or merge. Do not implement against this document without separate explicit implementation authorization.*
