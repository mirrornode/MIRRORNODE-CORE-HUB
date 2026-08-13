# MIRRORNODE Integration Capability Contract (MICC) v0.1

**Status:** Draft — Under Council Review (CG-0033)  
**Version:** 0.1  
**Created:** 2026-08-12  
**Authority effect:** None until operator disposition on CG-0033  
**Canon status:** Pre-canon draft; lives under `docs/integration/` until separate explicit promotion action

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

**3.1 Integration adapter principals are a distinct class** from lattice
agents defined in SYSTEM_CONTRACT. An adapter does not inherit lattice
agent authority. An adapter operates under the authority explicitly
granted to it by operator authorization.

**3.2 A provider is not a principal.** The external provider system
(Infisical, Inngest, Stripe, etc.) is not a MIRRORNODE principal. The
adapter that wraps it is a principal. The provider cannot grant,
escalate, or revoke MIRRORNODE authority.

**3.3 Principal identity for intra-lattice claims** defers to
SYSTEM_CONTRACT v1.1. Lucian's execution authority (POST /dispatch)
is not modified by this contract.

**3.4 Authority direction is always operator → adapter → provider.**
No adapter may receive authority from its provider. No adapter may
claim authority not explicitly granted by the operator.

---

## Section 4 — Capability and Scope Declaration

Each adapter must declare:

```
capabilities:      list of named operations this adapter exposes
scopes_required:   list of access scopes the adapter requires from the provider
scopes_granted:    list of MIRRORNODE scopes this adapter is permitted to exercise
scope_ceiling:     the maximum scope level this adapter may ever request
```

An adapter may not exercise a scope not listed in `scopes_granted`.
An adapter may not request a provider scope not listed in `scopes_required`.
Scope escalation requires a new adapter declaration at DECLARED state.

---

## Section 5 — Credential Requirement Declaration

Adapters declare credential requirements without carrying credential
contents. A MIM declaration is not a credential store.

```
credential_requirements:
  - name:          human-readable name for this credential
    kind:          API_KEY | OAUTH_TOKEN | MTLS_CERT | MACHINE_IDENTITY | OTHER
    scope:         which adapter capabilities require this credential
    environment:   PRODUCTION | STAGING | DEVELOPMENT | ALL
    lifetime:      SHORT_LIVED | LONG_LIVED | ROTATING | STATIC
    revocable:     true | false
    required:      true | false
```

The Credential Authority adapter (CREDENTIAL family) is responsible
for satisfying declared credential requirements at runtime. Credential
contents never appear in a MIM declaration or in any MICC record.

---

## Section 6 — Approval Classification

Each adapter capability must declare its approval class:

```
APPROVAL_NONE       — read-only, no state change, no external call
APPROVAL_AUTOMATED  — automated gate; policy evaluation required before execution
APPROVAL_OPERATOR   — explicit operator approval required before execution
APPROVAL_COUNCIL    — Council matter required before this capability may be activated
```

Approval class may not be downgraded without a new adapter declaration
and operator re-authorization. The approval class is machine-readable
and must be evaluable at the capability level before execution is permitted.

---

## Section 7 — Health and Readiness Semantics

Adapters must declare health and readiness endpoints or check contracts:

```
health_check:
  method:          the check mechanism (HTTP_GET | RPC | INTERNAL)
  endpoint:        path or identifier
  interval_seconds: polling interval
  timeout_seconds:  maximum check duration
  healthy_criteria: machine-readable condition for HEALTHY verdict
  degraded_criteria: machine-readable condition for DEGRADED verdict
```

A passing health check does not imply authorization. An adapter that
passes health checks while in VERIFIED state has not been authorized
to operate. See Section 10 (lifecycle).

---

## Section 8 — Execution and Failure Semantics

**8.1 Execution contract.** Every adapter capability invocation must:
- Verify adapter lifecycle state is ACTIVE before proceeding
- Emit a canonical receipt (Section 9) at invocation boundary
- Return a machine-readable outcome from the bounded vocabulary below
- Never emit a free-text-only failure classification

**8.2 Bounded outcome vocabulary:**

```
OUTCOME_SUCCESS          — capability executed and completed
OUTCOME_FAILURE_PROVIDER — provider returned error; adapter intact
OUTCOME_FAILURE_AUTH     — credential or authorization failure
OUTCOME_FAILURE_SCOPE    — requested scope not granted
OUTCOME_FAILURE_CONTRACT — capability invocation violated MICC contract
OUTCOME_BLOCKED          — approval gate prevented execution
OUTCOME_DEGRADED         — executed under degraded conditions; result uncertain
OUTCOME_TIMEOUT          — execution did not complete within contract bounds
```

Free-text detail may accompany an outcome code but may not substitute
for it. Conformance tests must evaluate outcome codes, not free text.

**8.3 Failure behavior is closed.** An unknown condition maps to
`OUTCOME_FAILURE_CONTRACT`. Adapters may not introduce new outcome
codes without a MICC revision.

---

## Section 9 — Canonical Receipt Requirements

Every capability execution must emit a canonical receipt. Receipt
requirements are additive to the locked AUDIT_EMISSION contract
(`canon/contracts/AUDIT_EMISSION.md`). MICC does not redefine
AUDIT_EMISSION fields.

**9.1 AUDIT_EMISSION fields that must be present in every receipt:**

```
timestamp        (ISO8601 UTC)
repo             (repository name)
repo_hash        (git commit SHA at time of execution)
event_type       ("adapter_invocation")
actor            (adapter_id)
verdict          (mapped from Section 8.2 outcome vocabulary)
evidence         (object; see 9.2)
audit_id         (UUID v4)
```

**9.2 MICC evidence candidates (placement unresolved — see open question):**

The following fields are required by MICC but their placement relative
to the AUDIT_EMISSION schema is an open question for Osiris to determine
(see CG-0033 matter.yaml open questions):

```
execution_nonce      — unique per-invocation identifier preventing replay
requesting_actor     — principal that initiated the capability request
executing_actor      — adapter_id executing the capability (may differ from requesting_actor)
approval_object      — reference to approval record if APPROVAL_OPERATOR or APPROVAL_COUNCIL
policy_version       — version of the policy evaluated at execution time
```

Until Osiris issues a placement determination, these fields must be
present in the receipt but their canonical location (inside `evidence`,
as a parallel record, or pending AUDIT_EMISSION revision) is unresolved.

**9.3 Canonical evidence is owned by MIRRORNODE.**  
External telemetry systems (LangSmith, Axiom, Datadog, etc.) are
observers only. They consume OTel-formatted emissions and have no
write authority over the canonical evidence record. No external
telemetry product becomes the historical authority for a MIRRORNODE
determination. OTel is the interoperability format; it is not the
evidence store.

---

## Section 10 — Lifecycle States and Transition Rules

**Note:** Whether this lifecycle state machine is normative in MICC
or lives in a separate Runtime Registry specification is an open
question for Ptah and Thoth (see CG-0033 open questions). It is
included here as a normative candidate.

### 10.1 Lifecycle states

```
DECLARED     — MIM declaration exists; no implementation verification performed
IMPLEMENTED  — implementation exists and has been submitted for verification
VERIFIED     — technical verification passed; adapter is functional
AUTHORIZED   — operator has explicitly granted authority to operate
ACTIVE       — adapter is operating within authorized scope
DEGRADED     — adapter is operating but health checks indicate reduced capability
SUSPENDED    — adapter is halted; authority temporarily withdrawn
RETIRED      — adapter is permanently decommissioned; no further operation permitted
```

### 10.2 Authorized transitions

| From | To | Permitted initiator |
|---|---|---|
| DECLARED | IMPLEMENTED | Adapter maintainer |
| IMPLEMENTED | VERIFIED | Automated verification + Ptah confirmation |
| VERIFIED | AUTHORIZED | Operator only |
| AUTHORIZED | ACTIVE | Automated (post-authorization health pass) |
| ACTIVE | DEGRADED | Automated (health check) |
| DEGRADED | ACTIVE | Automated (health recovery) |
| ACTIVE | SUSPENDED | Operator or automated policy gate |
| DEGRADED | SUSPENDED | Operator or automated policy gate |
| SUSPENDED | AUTHORIZED | Operator only (re-authorization) |
| AUTHORIZED | RETIRED | Operator only |
| ACTIVE | RETIRED | Operator only |
| SUSPENDED | RETIRED | Operator only |

### 10.3 Invariants

- VERIFIED → AUTHORIZED requires explicit operator action. A health
  check pass does not constitute authorization.
- An adapter in any state other than ACTIVE or DEGRADED may not execute
  capabilities.
- RETIRED is terminal. A retired adapter_id may not be reused.
- Every state transition must emit an AUDIT_EMISSION-conformant record.

---

## Section 11 — Provider-Specific Extension Rules

Adapters may declare provider-specific extensions in a `provider_extensions`
block in their MIM declaration. Extension rules:

1. Extensions may add fields; they may not redefine MICC-normative fields.
2. Extensions may not introduce new capability families.
3. Extensions may not modify approval classification or lifecycle rules.
4. Extensions may not introduce outcome codes outside Section 8.2.
5. Extension fields must be namespaced: `x_<provider_name>_<field>`.
6. Extensions are not MICC-canonical. They are provider-specific metadata.

---

## Section 12 — Protocol Boundary Rules

**12.1 MCP.**  
CG-0032 (MCP Surface Contract v0.1) is the governing definition for MCP
as a downstream read-only projection surface. Dependency direction is
from canonical MIRRORNODE outward to the external MCP runtime.

MICC does not classify MCP as an integration adapter. MCP is not a
provider under any MICC capability family. No adapter created under
MICC may invert the CG-0032 dependency direction.

Any inbound invocation path, write-capable MCP surface, or
MCP-mediated execution path requires separate Council authority.
Canonical MIRRORNODE mechanisms may not depend on MCP output for
authority, approval, truth, integrity, or execution permission.

**12.2 Other external protocols.**  
REST, SDK, and other external protocol surfaces that invoke MIRRORNODE
capabilities approach the governed capability surface from outside.
They do not become integration providers by invoking capabilities.
Protocol clients have no authority over adapter lifecycle, approval
classification, or evidence records.

---

## Section 13 — Conformance Requirements

An adapter is MICC-conformant if and only if:

1. Its MIM declaration validates against MIM v0.1 schema without errors.
2. It implements all capabilities declared in its MIM.
3. Every capability invocation emits a canonical receipt per Section 9.
4. Every capability outcome is expressed using the Section 8.2 vocabulary.
5. It does not exercise scopes beyond those declared in `scopes_granted`.
6. It does not modify its `adapter_id`, `capability_family`, or
   `micc_version` after reaching AUTHORIZED state.
7. It does not accept execution requests while outside ACTIVE or DEGRADED state.
8. It does not emit credential contents in any receipt or log.
9. Conformance tests must evaluate machine-readable fields; free-text
   interpretation does not satisfy a conformance requirement.

---

## Section 14 — Provider Semantic Authority Prohibition

**This prohibition is unconditional.**

A provider does not become a semantic authority over MIRRORNODE by
implementing a MICC capability family. Implementation grants operational
status under MIRRORNODE authority. It does not grant:

- Authority to define what a capability means
- Authority to modify approval classification
- Authority to determine what constitutes valid execution evidence
- Authority to alter lifecycle state except as permitted in Section 10.2
- Authority to define MIRRORNODE principal identity
- Authority to determine what is canonical

If a provider's native semantics conflict with MICC semantics, MICC
semantics govern. The adapter is responsible for translation. The
provider's native model does not propagate upward.

This prohibition survives adapter retirement, provider contract changes,
provider API evolution, and any provider-initiated redefinition of its
own service semantics.

---

## Appendix A — Relationship to Existing Canon

| Document | Relationship |
|---|---|
| `AUDIT_EMISSION.md` | MICC Section 9 is additive. MICC does not redefine AUDIT_EMISSION fields. |
| `SYSTEM_CONTRACT.md` | MICC Section 3 defers to SYSTEM_CONTRACT for intra-lattice principal identity. Lucian's authority is unchanged. |
| CG-0032 MCP Surface Contract | MICC Section 12 preserves CG-0032 governing definition. MCP is not a MICC adapter. |

---

*This document is a pre-canon draft under Council review. It has no authority effect until operator disposition on CG-0033. Do not implement against this document until disposition is issued.*
