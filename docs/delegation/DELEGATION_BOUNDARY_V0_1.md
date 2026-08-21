# MIRRORNODE Delegation Boundary v0.1

**Status:** Draft under CG-0036 — not canon, not implementation authority  
**Version:** 0.1-draft.2  
**Created:** 2026-08-14  
**Revision:** 2026-08-21 bounded hardening pass 3 (approval-capacity reservation, issuer-authority vs authentication, approval registry bindings, dispatch-intent, UTF-16 JCS, schema-valid vectors, set-like array order, logical issuer)

## 1. Purpose

This specification defines how MIRRORNODE may delegate bounded authority without transferring Operator sovereignty or requiring the Operator to become the mandatory transit point for every routine action.

Delegation is a revocable grant to perform a specific class of action under a specific policy, resource, state, time window, and authority ceiling. Delegation is not ownership of the governing authority.

The architecture separates policy decision from policy enforcement. A **Policy Decision Point (PDP)** evaluates a request against immutable/versioned policy and current state. A distinct **Policy Enforcement Point (PEP)** enforces only a valid decision. Neither component may rewrite the policy that governs the current decision.

## 2. Delegation classes

### AUTONOMOUS_WITHIN_POLICY
The delegated actor may proceed without a new Operator approval only when all declared preconditions are satisfied, the action is explicitly permitted by governing policy, aggregate authority remains below the applicable ceiling, and the requested effect remains inside the pre-authorized envelope.

### ADVISORY_ONLY
The actor may analyze, draft, recommend, simulate, prepare, or emit a typed action proposal. It may not cause the governed effect.

### OPERATOR_APPROVAL_REQUIRED
The actor may prepare the action, but execution requires an authenticated Operator approval bound to the current request, subject, action, resource, policy, state, delegation, and approval lifetime.

### NON_DELEGABLE
The authority cannot be conveyed through this delegation layer. Direct Operator action or a separately governed higher-authority process is required.

### Default rule

An action that matches no valid delegation or cannot be classified unambiguously defaults to **NON_DELEGABLE**. No-match, policy-error, unknown-resource, unknown-operation, stale-state, unverifiable-policy, or conflicting-authority conditions never imply permission.

## 3. Authorization information model

Each authorization evaluation is normalized into five objects:

- **Subject** — the principal on whose behalf the action would occur;
- **Action** — the exact requested operation and parameters;
- **Resource** — a canonical identifier for the target resource;
- **Context** — environment, current state, risk, time, dependency, and request metadata;
- **Decision** — allow/deny plus obligations, reason codes, policy references, decision lifetime, and receipt identifiers.

Canonical resource identifiers must be stable and collision-resistant within their namespace. Aliases must resolve to one canonical resource identifier before policy evaluation. Authorization MUST NOT be based on unnormalized free-text resource names.

Envelope `resource_scope` entries are canonical URIs. The deterministic mapping onto a decision resource is:

- `resource.canonical_uri` is that URI;
- `resource.id` MUST equal `resource.canonical_uri`;
- `resource.type` MUST equal the resource-registry record's type for that URI.

The decision MUST bind `resource_registry_ref`, `resource_registry_snapshot_hash`, and `resource_record_hash` identifying the exact immutable registry snapshot and record used by the PDP. Operator and Council approvals MUST carry the same three fields. Approval, decision, current envelope/resource identity, and PEP enforcement MUST be equal. A remapped provider/native target under the same URI invalidates the approval and the decision.

## 4. Delegation envelope

Every delegation must be attributable and machine-readable. At minimum it identifies:

- `delegation_id`
- `delegation_version`
- `delegator`
- `logical_issuer_id`, `issuer_registry_ref`, `issuer_registry_snapshot_hash`
- `issuer_authority_kind`, `issuer_authority_ref`, `issuer_authority_hash`
- `issuer_proof`
- `delegate_actor`
- `authority_class`
- `governing_policy_ref`
- `policy_version`
- `policy_content_hash`
- `policy_bundle_hash`
- `allowed_operations`
- `resource_scope`
- `environment_scope`
- `authority_ceiling`
- `authority_rank`
- `risk_ceiling`
- `decision_preconditions_ref`
- `decision_preconditions_hash`
- `issued_at`
- `effective_at`
- `expires_at`
- `revocation_behavior`
- `expiry_behavior`
- `max_revocation_propagation_seconds`
- `receipt_policy_ref`
- `subdelegation`

`issuer_proof` authenticates the RFC 8785 canonical envelope payload excluding `issuer_proof`, hashed per `CANONICALIZATION_V0_1.md`. Content integrity (a digest over payload bytes) proves that those bytes have not changed after hashing; it does not, by itself, prove who issued the envelope. Authenticated issuance requires a verifiable proof over that canonical payload, validated against a trust root outside the affected delegate's authority path. A hash string, a claimed `delegator` name, or an unsigned envelope cannot establish issuance.

A trusted credential proves **identity only**. Before an envelope enters `G(A,t)`, a hash-bound issuer-authority source MUST prove the logical issuer may delegate the exact operations, resources, environments, authority rank and ceiling, risk ceiling, subdelegation depth, and validity period. Child grants verify that source against the authenticated parent envelope. Root grants require a separately governed `ISSUER_AUTHORITY_RECORD_V0_1` outside the grantee’s control. Unknown, unauthenticated, excessive, expired, or self-issued authority fails closed.

`proof_type` and `issuer_credential_ref` are untrusted hints until authenticated. The proof mechanism MUST cryptographically protect the algorithm identifier, credential/key identifier, and signed payload hash using standard JOSE/COSE/WebAuthn protected-header semantics (`ISSUER_PROOF_V0_1.md`). Algorithm substitution, credential redirection, and trust-root substitution fail closed.

A delegation is invalid if its issuer proof, governing policy content hash, policy bundle hash, decision-precondition hash, authority ceiling, resource scope, validity period, or revocation state cannot be verified at decision time.

## 5. Authority Classification Boundary

The classification mechanism is not a sovereign policy author. It performs bounded evaluation only.

The following roles are distinct:

1. **requester/proposer** — asks for an action;
2. **policy author/governing authority** — establishes the versioned policy and non-delegable guardrails;
3. **PDP/classifier** — evaluates Subject, Action, Resource, Context against the exact policy bundle;
4. **authorizing authority** — supplies any approval required by the resulting class;
5. **PEP/executor** — enforces only a valid allow decision;
6. **verifier/auditor** — independently checks that decision and resulting effect matched policy and evidence requirements.

The PDP MUST be unable, through the authority used for evaluation, to modify the policy bundle it evaluates. The PEP MUST be unable to synthesize or upgrade an authorization decision. A delegated actor may not be the sole authority for lowering the class or risk of an action it seeks to perform.

Every decision must record at least:

- evaluator identity/version as correlating labels only (`pdp_identity` / `pdp_version` are not authentication);
- required decision `issuer_proof` over the RFC 8785 canonical decision excluding `issuer_proof`;
- policy bundle hash;
- immutable decision-preconditions hash;
- delegation identifier/version;
- `delegation_payload_hash` of the RFC 8785 canonical envelope payload excluding `issuer_proof`;
- subject/action/resource/context digest;
- `resource_registry_ref` and `resource_registry_snapshot_hash`;
- aggregate-authority snapshot digest of a schema-valid `AGGREGATE_AUTHORITY_SNAPSHOT_V0_1` object;
- state reference/hash;
- `micc_approval_class` (unconditional);
- authenticated Operator/Council approval references and hashes where required;
- allow/deny result;
- obligations and reason code;
- `logical_issuer_id` plus issuer-registry snapshot (not `kid`);
- `decision_id` (stable, issuer-scoped) and `decision_nonce` (≥128-bit CSPRNG);
- issued time and expiry time.

A fabricated schema-shaped `ALLOW` without a trusted PDP `issuer_proof` MUST fail. IDs are stable identifiers within an authenticated issuer trust domain. Nonces are unpredictable replay-prevention values. Consumption keys are `(authenticated_issuer, id, nonce)` taken from protected proof metadata.

`micc_approval_class` is recorded on every decision. When no additional MICC approval gate applies, the recorded class is `APPROVAL_NONE`. The field is never omitted to mean “no MICC gate.” Both MICC and delegation constraints apply, and the stricter gate wins.

`delegation_payload_hash` MUST equal the SHA-256 of the deterministic canonical envelope payload excluding `issuer_proof`, and MUST equal `issuer_proof.signed_payload_hash`. The decision is bound to that exact payload, not merely to `delegation_id` and `delegation_version`. A changed envelope with the same delegation ID and version fails closed. Operator and Council approvals MUST carry the same `delegation_payload_hash`; an approval bound only to those mutable coordinates cannot authorize a mutated envelope.

## 6. Policy semantics

Policy evaluation uses **default deny**. Explicit deny/forbid guardrails override permit rules. Errors or missing required attributes cannot produce `Allow`.

A policy change creates a new content hash and policy bundle hash. Stable path names or human-readable versions are insufficient by themselves. The PDP must evaluate the same immutable policy content whose hashes are emitted in the decision receipt.

Policy authorship is itself governed. A principal whose effective authority is determined by a policy may contribute proposals or review, but may not unilaterally publish a policy change that increases its own authority.

## 7. Anti-self-expansion rule

A delegated actor must never be able, through the authority being delegated, to modify or reinterpret any condition that increases its own effective authority.

This includes:

- adding operations;
- broadening resource or environment scope;
- increasing authority or risk ceilings;
- extending expiry;
- weakening revocation or expiry behavior;
- changing governing policy or applicable policy bundle;
- changing decision-precondition content without producing and governing a new immutable hash;
- changing canonical resource mappings to reach equivalent protected resources;
- reclassifying a governed action into a less restrictive delegation class;
- changing evidence requirements in a way that makes its own actions easier to approve;
- manipulating risk inputs or classifier inputs it controls without independent validation;
- fabricating or self-asserting approval provenance;
- delegating onward authority without explicit subdelegation permission;
- combining multiple grants to exceed the aggregate authority ceiling.

Any change that could increase effective authority requires authority from outside the affected envelope and must be evaluated as a new grant.

## 8. Aggregate authority

Authorization is evaluated against both the current envelope and the **aggregate authority** held by the delegate actor.

Before an autonomous allow decision, the PDP must compute or verify an aggregate-authority snapshot covering all active, applicable delegations for that actor, including overlapping resources, operations, environments, parent/child grants, and time windows.

The union of individually valid delegations must not exceed a separately governed root/actor ceiling. Non-conflicting grants can still compose into excessive authority; absence of direct contradiction is not sufficient.

The snapshot hashed as `aggregate_authority_snapshot_hash` MUST be a schema-valid `AGGREGATE_AUTHORITY_SNAPSHOT_V0_1` object, canonicalized with RFC 8785. The snapshot is not an opaque digest of an undefined document.

Workflow or action-chain policy must detect when a sequence of individually allowed low-risk actions can produce an outcome equivalent to a higher-risk or non-delegable action. Where composition cannot be bounded, the chain escalates.

## 9. Subdelegation

Subdelegation is prohibited by default.

When explicitly allowed, every child delegation must carry `parent_delegation_ref` and remain traceable to the root. A conformance validator—not JSON Schema alone—must verify:

- child authority rank <= parent authority rank;
- child risk ceiling <= parent risk ceiling;
- child operations are a subset of parent-eligible operations;
- child resource/environment scope is a subset of parent scope;
- child expiry <= parent expiry;
- child max depth is below the parent limit;
- child cannot weaken revocation, expiry, receipt, or decision-precondition requirements.

Authority is monotonically non-increasing across a delegation chain.

## 10. Decision preconditions and TOCTOU

Autonomous delegated execution requires all preconditions to pass immediately before enforcement.

The delegation binds the governing precondition artifact by both reference and content hash. The PDP records the exact `decision_preconditions_hash` it evaluated, and the PEP rejects enforcement if that immutable binding no longer matches.

At minimum, the decision request may bind:

- current state hash or equivalent state reference;
- target version/reference;
- canonical resource identifier;
- operation and parameter digest;
- environment;
- risk inputs and risk-policy version;
- required deterministic checks;
- conflict state;
- policy content/bundle hashes;
- decision-precondition hash;
- non-expiry and non-revocation;
- aggregate-authority snapshot;
- dependency state;
- replay/idempotency safeguards.

The PEP must reject a decision if bound state has materially changed before enforcement. For mutable resources, implementations should use compare-and-swap, version preconditions, transactions, locks, or an equivalent enforcement mechanism appropriate to the resource.

Retries of autonomous actions are new authorization events. They MUST re-evaluate current policy, delegation, revocation, expiry, aggregate authority, preconditions, and state.

### One-time ALLOW invariant (v0.1)

Every v0.1 `ALLOW` decision is one-time-use.

- Every `ALLOW` `decision_id` and `decision_nonce` MUST be atomically consumed before or as part of enforcement.
- Replay of an `ALLOW` fails even when the decision is unexpired.
- Approval reuse does not imply decision reuse. Remaining bounded uses on an associated approval cannot re-authorize a consumed `ALLOW`.
- Any future bounded decision-reuse profile requires separate governance and is outside v0.1.

Effect dispatch follows `EFFECT_CONSUMPTION_COMMIT_V0_1.md`. Reservation of `(logical_issuer_id, decision_id, decision_nonce)` **and** required approval-use capacity occurs atomically before dispatch. Durable dispatch intent is committed before invoking an external effect. `RESERVED` is not evidence of prior dispatch. Uncertain non-idempotent outcomes escalate. `COMPLETED` requires a durable effect receipt and finalized approval consumption.

## 11. Revocation and expiry

Delegation is revocable without consent of the delegate actor.

Each delegation declares a maximum tolerated revocation-propagation latency. If an enforcement point cannot prove its revocation state is fresh enough for that bound, it fails closed for new work.

Revocation behavior for already-started work is one of:

- `CANCEL_ON_REVOCATION`
- `COMPLETE_CURRENT_ATOMIC_STEP`
- `COMPLETE_CURRENT_TRANSACTION`
- `NON_INTERRUPTIBLE_WITH_EXPLICIT_RATIONALE`

The non-interruptible mode requires a meaningful, non-whitespace rationale that is retained as part of the delegation evidence.

Expiry behavior is separately declared as one of:

- `CANCEL_ON_EXPIRY`
- `COMPLETE_CURRENT_ATOMIC_STEP`
- `COMPLETE_CURRENT_TRANSACTION`
- `ALLOW_COMPLETION_IF_DECISION_WAS_VALID_AND_BOUND`

Queued work not yet enforced is new work and requires a fresh valid decision. Retries after revocation or expiry require fresh authorization and normally fail because the underlying delegation is no longer valid.

Offline enforcement that cannot meet revocation freshness requirements is not permitted for autonomous effects unless a separate bounded offline-capability profile is explicitly governed.

## 12. Approval provenance and consumption

Approval is an authenticated authority artifact, not a string assertion.

Operator approvals and Council approvals must:

- conform to their typed approval schema;
- carry authenticated issuer provenance verifiable against a trusted credential or attestation root outside the requester and affected delegate's authority path;
- bind the exact request, subject, action/parameters, resource, context, state, policy bundle, delegation identifier/version, `delegation_payload_hash`, and lifetime;
- carry a content hash referenced by the authorization decision;
- declare either `ONE_TIME` or `BOUNDED_REUSE` semantics;
- participate in authoritative, concurrency-safe consumption accounting.

A hash proves object integrity, not issuer identity. A claimed approver name without authenticated provenance cannot authorize execution.

`ONE_TIME` approvals are atomically consumed by their first authorized enforcement. `BOUNDED_REUSE` approvals declare `max_uses`; remaining uses are tracked in an authoritative consumption state. Unverifiable consumption state fails closed. Remaining approval uses never convert a consumed `ALLOW` into a reusable decision.

Where Council approval is required, the decision must carry a typed Council approval binding whose matter/disposition content integrity and exact current-action authorization can be independently verified.

`council_matter_ref`, `disposition_ref`, `disposition_hash`, and `issuer_proof` prove that a referenced artifact exists, is hash-bound, and that the approval object was authenticated. They do not prove that the referenced Council disposition was validly constituted.

This repository's `council/schemas/disposition.schema.yaml` records Operator dispositions of Council matters (`authority: operator`). CG-0031 verifies that a previously recorded Operator disposition authorizes an exact implementation scope. Neither contract defines Council seat composition, quorum, or a disposition-constitution validator.

Until a separately governed disposition validator proves required composition, provenance, and quorum, Council-required approval MUST fail closed. CG-0036 does not invent constitutional quorum rules inside the approval object.

v0.1 makes this structurally unreachable at the decision schema: `micc_approval_class: APPROVAL_COUNCIL` cannot validate with `decision: ALLOW` (only `DENY` or `ESCALATE`). Typed `COUNCIL_APPROVAL_V0_1` objects remain draft evidence structures; their presence cannot unlock v0.1 execution. A future schema revision is required after constitution/quorum validation is ratified.

## 13. Non-delegable guardrails

Unless separately authorized by explicit governance, the following are NON_DELEGABLE through v0.1:

- expansion of an actor's own authority or root/aggregate ceiling;
- modification of the policy-authoring or classification rules governing that actor's authority;
- weakening of security controls, security verdict requirements, identity verification, approval-provenance verification, or enforcement-point controls;
- exceptions to governing approval policy;
- canon promotion or modification of final authority rules;
- creation or weakening of non-delegable guardrails;
- irreversible high-impact external effects outside a pre-established deterministic policy;
- alteration, deletion, suppression, or fabrication of authoritative audit evidence;
- disabling revocation, expiry enforcement, evidence emission, approval consumption, or required verification;
- self-approval of a previously approval-bearing action;
- modifying the canonical resource-identity registry to broaden one's own reachable scope;
- modifying aggregate-authority computation or risk-classification logic to benefit the affected actor;
- issuance of root delegations or root policy-signing authority to oneself.

## 14. MICC approval-class relationship

Delegation class does not replace MICC approval classification. Both constraints apply, and the stricter requirement wins.

| Delegation class | MICC relationship |
|---|---|
| `AUTONOMOUS_WITHIN_POLICY` | May proceed only when the underlying MICC capability permits `APPROVAL_NONE` or `APPROVAL_AUTOMATED` and all delegation conditions pass. It can never downgrade `APPROVAL_OPERATOR` or `APPROVAL_COUNCIL`. |
| `ADVISORY_ONLY` | Produces no execution authorization. |
| `OPERATOR_APPROVAL_REQUIRED` | Requires authenticated, bound Operator approval even if MICC would otherwise allow automation. |
| `NON_DELEGABLE` | Delegation cannot authorize the action; any separately applicable MICC/Council/Operator gate remains controlling. |

If MICC requires `APPROVAL_OPERATOR`, a conformant `ALLOW` decision carries the validated Operator approval binding. If MICC requires `APPROVAL_COUNCIL`, v0.1 MUST emit `DENY` or `ESCALATE`; `ALLOW` is schema-invalid. When taxonomies disagree or cannot be mapped deterministically, deny/escalate.

## 15. Relationship to cognition

Generated model output, analysis, confidence, or a tool/function proposal carries no execution authority by itself.

The Cognition Contract term `PROPOSAL_ONLY` is a cognition side-effect ceiling. CG-0036 uses `ADVISORY_ONLY` for the delegation authority class to avoid semantic collision.

A cognition system may emit an action proposal, but the PDP evaluates the resulting action request independently. The proposal source cannot supply trusted authority class, risk score, resource identity, policy version, approval state, or approval provenance merely by asserting them.

## 16. Evidence, receipts, and verification

Every delegated effect must be reconstructible from an evidence chain sufficient to establish four distinct facts:

1. **authorized** — a valid decision plus any required authenticated approval permitted the action;
2. **correctly classified** — the PDP used the correct policy, immutable preconditions, subject/action/resource/context, MICC gate, and aggregate-authority state;
3. **policy-compliant** — all decision obligations, approval-consumption constraints, and preconditions were satisfied at enforcement time;
4. **successful** — the resulting effect matched the authorized target.

Success never substitutes for authorization.

Decision and execution receipts should include immutable references/hashes rather than mutable path names alone. Authorization receipts are separate from execution receipts but must be linkable by nonce/request/effect identifiers. Approval provenance and consumption state must be reconstructible without exposing secret credential material.

## 17. Product/HUD requirements

The product layer must visualize governing authority state; it may not redefine it.

A conformant UI must not show only per-envelope status. For every actor capable of delegated effects it must make available:

- aggregate active authority;
- overlapping grants and parent/child relationships;
- root ceiling and current utilization;
- policy bundle/version/hash provenance;
- decision-precondition integrity;
- delegation expiry/revocation freshness;
- approval provenance/status and bounded-use state where relevant;
- pending escalations;
- recent decisions and execution receipts;
- any action-chain/composition warning;
- any unresolved classifier/policy error.

A green status on one envelope must not imply the actor's aggregate authority is low-risk.

## 18. Standards-alignment posture

This draft intentionally aligns its architecture with established patterns without claiming certification or conformance:

- NIST SP 800-207 / 800-207A: no implicit trust, identity/resource-focused authorization, discrete decision and enforcement controls;
- OpenID AuthZEN Authorization API 1.0: PDP/PEP separation and Subject/Action/Resource/Context/Decision information model;
- RFC 8707: explicit target-resource identity and audience restriction principles;
- SPIFFE: first-class verifiable workload identity for distributed enforcement components;
- NIST SP 800-53 Rev.5 Release 5.2.0: access control, least privilege, audit/accountability, authorization, monitoring, and configuration-integrity control families;
- NIST AI RMF 1.0 and current revision program: explicit governance, risk tolerances, independent review, TEVV, monitoring, and go/no-go decisions;
- ISO/IEC 42001:2023 and ISO/IEC 23894:2023: management-system governance, traceability, continual improvement, and AI risk-management integration;
- OWASP LLM06:2025 / Agentic AI guidance: least-privilege agency, downstream user-context enforcement, human approval for high-impact actions, and containment of excessive agency.

Detailed crosswalk: `docs/delegation/STANDARDS_CROSSWALK_V0_1.md`.

## 19. Operator-load boundary

The system minimizes unnecessary Operator intervention by resolving only actions demonstrably inside valid policy and delegation envelopes. It escalates the smallest decision that genuinely requires human authority.

Operator attention is not a substitute for missing policy. Absence of Operator attention is not permission to infer broader authority.

## 20. Explicit exclusions

v0.1 does not itself grant permissions, implement a PDP/PEP, select a policy language, select approval-signing or consumption-store technology, change current agent authority, authorize deployment, permit automatic merges, or promote this specification to canon.
