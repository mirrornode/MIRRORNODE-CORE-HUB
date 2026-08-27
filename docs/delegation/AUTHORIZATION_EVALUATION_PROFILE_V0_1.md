# MIRRORNODE Authorization Evaluation Profile v0.1

**Status:** Draft under CG-0036 — architecture/conformance profile only  
**Purpose:** Define a deterministic evaluation order without selecting a policy language or runtime.

## 1. Input

Every effect-bearing authorization request is normalized to:

- Subject: verified principal identifier and relevant trusted attributes;
- Action: exact operation identifier plus parameter digest;
- Resource: canonical resource type/id/URI;
- Context: environment, state/version, time, dependencies, risk inputs, request identity;
- Governing surfaces: applicable MICC approval class, root authority policy, active delegation envelopes, non-delegable guardrails.

Unverified actor identity, unknown resource identity, unknown operation, or missing mandatory context produces `DENY` or `ESCALATE`, never `ALLOW`.

## 2. Evaluation order

A conformant PDP evaluates in this order:

1. **Verify evaluator state** — evaluator identity/version and policy-bundle integrity are known.
2. **Verify subject identity** — subject identity is authenticated/attested to the assurance level required by policy.
3. **Canonicalize resource** — resolve aliases through the authoritative registry to one canonical URI; freeze `resource_registry_ref` and `resource_registry_snapshot_hash`; set decision `resource.canonical_uri` = that URI, `resource.id` = that URI, and `resource.type` = the registry record type. Ambiguous or remapped provider/native targets fail.
4. **Normalize action** — resolve operation identifier and hash material parameters.
5. **Freeze evaluation context** — obtain current state/version and context digest used by the decision.
6. **Load immutable policy bundle** — verify `policy_content_hash` and `policy_bundle_hash`.
7. **Apply non-delegable/forbid guardrails** — a matching guardrail cannot be overridden by a permit or delegation.
8. **Load the complete active-grant inventory** — resolve a schema-valid `ACTIVE_GRANT_INVENTORY_V0_1` for the subject and exact `evaluation_time`. Verify its issuer proof against an independently trusted grant-registry authority, verify its RFC 8785 payload hash excluding `issuer_proof`, require a fresh monotonic `registry_sequence`, and require `query_semantics = ALL_ACTIVE_DELEGATIONS_FOR_AUTHORITY_HOLDER_AT_EVALUATION_TIME`. `active_delegation_payload_hashes` MUST be sorted ascending by lowercase hexadecimal digest bytes and MUST contain every active candidate grant returned by the authoritative registry query. The aggregate evaluator is not allowed to self-attest completeness. Missing, stale, duplicated, unverifiable, or selectively omitted inventory fails closed.
9. **Authenticate then authorize each delegation** — resolve every payload hash from the bound active-grant inventory, then: (a) verify issuer proof over the RFC 8785 canonical envelope payload excluding `issuer_proof`; derive algorithm and credential from protected proof metadata; map the credential to `logical_issuer_id` via the bound issuer registry. A trusted credential proves identity only. (b) **Authorize the issuer’s delegable scope** against a hash-bound authority source (`issuer_authority_kind` / `issuer_authority_ref` / `issuer_authority_hash`) covering the exact operations, resources, environments, authority rank and ceiling, risk ceiling, authenticated `budget_ceiling`, subdelegation depth, and validity period. (c) **For child grants (`PARENT_ENVELOPE`), bind child issuer identity to the parent delegate before any scope monotonicity check.** The child's authenticated `logical_issuer_id` MUST equal the parent envelope's `delegate_logical_issuer_id`. That equality is a trust-rooted identity-registry mapping (`delegate_identity_registry_ref` / `delegate_identity_registry_snapshot_hash`), not a comparison of `delegator` / `delegate_actor` display strings. The child's verified credential MUST map to that same `logical_issuer_id`. A peer that can read or resolve another actor's parent envelope MUST NOT cite its payload hash and issue a child grant. Matching display names with a different logical identity fail. Unresolved or stale identity-registry snapshots fail closed. For `ROOT_RECORD`, schema validity, possession of a matching record preimage, or the grant issuer's own signature is insufficient to establish root authority. The resolved `ISSUER_AUTHORITY_RECORD_V0_1` MUST contain `governance_attestation`, and that attestation MUST verify the exact record under an independently trusted governance authority and hash-bound governance-registry snapshot outside both the grant issuer's and grantee's authority path. The attestation credential MUST map to `governance_authority_logical_issuer_id`; the governance registry MUST independently authorize that logical issuer to admit root-authority records; and the attestation's `signed_payload_hash` MUST equal the RFC 8785 hash of the exact authority-record payload governed by that attestation. Missing, stale, self-issued, requester-controlled, or unverifiable governance evidence fails closed. For `ROOT_RECORD`, the envelope's `authority_ceiling` MUST exactly equal the bound root record's `authority_ceiling`. For `PARENT_ENVELOPE`, the child's `authority_ceiling` MUST exactly equal the parent envelope's `authority_ceiling`. In v0.1 `authority_ceiling` is an opaque inheritance token: no implementation may infer a wider/narrower ordering from different strings, and any difference or unknown token fails closed until a separately governed typed strengthening relation exists. Other independently typed constraints may narrow only according to their own defined monotonic rules. For `ROOT_RECORD`, the record's `budget_unit` MUST equal the bound aggregate-authority policy unit and the envelope's `budget_ceiling` MUST NOT exceed the record's independently governed `budget_ceiling`; missing or mismatched bounds fail closed. Unknown, unauthenticated, excessive, expired, self-issued, or self-authorized authority fails closed. An authenticated peer that does not possess the signed scope never enters `G(A,t)`. Then validate dates, revocation freshness, parent-chain monotonicity, and policy hashes. Compute `delegation_payload_hash` as that SHA-256; it MUST equal `issuer_proof.signed_payload_hash`.
10. **Compute aggregate authority snapshot** — derive `G(A,t)` only from the complete bound inventory after step 9 validation; resolve the schema-valid `AGGREGATE_AUTHORITY_POLICY_V0_1`; require every member of `G(A,t)` to bind the identical `aggregate_authority_policy_ref` and `aggregate_authority_policy_hash`, with any mismatch failing closed because v0.1 does not combine policies; execute the deterministic `CG0036_AGGREGATE_V0_1` algorithm in §3; bind `active_grant_inventory_ref` and `active_grant_inventory_hash`; require `applicable_delegation_payload_hashes` to equal the sorted hashes of every member of `G(A,t)`; then authenticate and hash a schema-valid `AGGREGATE_AUTHORITY_SNAPSHOT_V0_1` excluding `issuer_proof`.
11. **Classify the requested action** — derive the delegation class from governing policy, not from requester-supplied labels.
12. **Cross-check MICC** — resolve and hash-verify `MICC_INVOCATION_BINDING_V0_1`; compare its exact MIM, adapter, capability, lifecycle, scope, requester, executor, approval class, and execution nonce to the request and decision. Both approval systems apply; the stricter gate wins. Every decision records `micc_approval_class`. When no additional MICC approval gate applies, record `APPROVAL_NONE`; do not omit the field.
13. **Evaluate risk and action-chain composition** — reject/escalate if the requested action or known chain exceeds risk, budget, cardinality, sequence, or blast-radius constraints.
14. **Evaluate decision preconditions** — validate `DECISION_PRECONDITIONS_V0_1`, evaluate every typed check with `ALL_MUST_PASS`, and bind the canonical evaluation hash in the decision. Child delegations must carry the exact parent precondition hash until a separately governed typed strengthening relation exists.
15. **Resolve required human authority** — if Operator/non-delegable authority is required, absence of a valid bound approval prevents `ALLOW`. Required Operator approvals MUST carry a `delegation_payload_hash` equal to the current envelope payload hash and a verifiable `issuer_proof`. If MICC classifies `APPROVAL_COUNCIL`, v0.1 MUST emit `DENY` or `ESCALATE`; `ALLOW` is schema-invalid even when a Council approval object is present. A future schema revision is required after a separately governed constitution/quorum validator is ratified.
16. **Emit and authenticate decision** — produce `ALLOW`, `DENY`, or `ESCALATE` with the distinct authority-holder and PDP-issuer identities; exact delegation, resource, precondition/evaluation, aggregate, revocation, MICC, policy, state, nonce, and expiry bindings. Sign the complete canonical decision excluding `issuer_proof`. `pdp_identity`/`pdp_version`/`kid` are not authority-holder identities. Every v0.1 `ALLOW` is one-time-use.

## 3. Aggregate authority algebra

For an actor `A` at time `t`:

- `Inventory(A,t)` = the independently authenticated `ACTIVE_GRANT_INVENTORY_V0_1` result for A at t;
- `G(A,t)` = every inventory member that passes step 9 issuer, authority, scope, lifetime, revocation, parent-chain, and policy validation;
- `Permit(A,t)` = union of explicitly permitted operation/resource/environment tuples in `G(A,t)`;
- `Root(A,t)` = separately governed maximum authority ceiling for A;
- `Forbid(t)` = non-delegable and explicit deny guardrails;
- `Effective(A,t)` = `(Permit(A,t) ∩ Root(A,t)) - Forbid(t)` subject to the deterministic aggregate constraints below.

`CG0036_AGGREGATE_V0_1` is defined as follows. There is no implementation-defined freedom in these metrics:

1. Sort `G(A,t)` by lowercase hexadecimal `delegation_payload_hash` bytes. This ordered hash array is `applicable_delegation_payload_hashes`.
2. `distinct_delegations = len(G(A,t))`. If it exceeds `max_distinct_delegations`, aggregate evaluation fails.
3. `effective_authority_rank = max(grant.authority_rank for grant in G(A,t))`. If greater than `max_authority_rank`, aggregate evaluation fails. The maximum is used because a single higher-rank grant is sufficient to expose that authority surface.
4. Map each `risk_ceiling` through the fixed order `LOW < MODERATE < HIGH < CRITICAL`. `cumulative_risk` is the highest risk token present in `G(A,t)`. If its ordinal exceeds `max_cumulative_risk`, aggregate evaluation fails.
5. Every grant MUST carry authenticated `budget_ceiling` in the single `budget_unit` named by the bound aggregate policy. A root grant's unit and ceiling MUST be authorized by its bound `ISSUER_AUTHORITY_RECORD_V0_1`; a root envelope may narrow but never exceed that bound. Every member of `G(A,t)` MUST bind the identical aggregate-policy reference and hash. Mixed or unresolved units fail closed. `cumulative_budget = sum(grant.budget_ceiling for grant in G(A,t))` using checked safe-integer arithmetic; overflow or a value greater than `9007199254740991` fails closed. If `cumulative_budget > max_cumulative_budget`, aggregate evaluation fails.
6. Let `R` be the set union of all canonical `resource_scope` URIs in `G(A,t)`. `cumulative_cardinality = len(R)`. If it exceeds `max_cumulative_cardinality`, aggregate evaluation fails. `resource_scope` in the snapshot is the request-relevant intersection of `R` with `Root(A,t)` after `Forbid(t)` removal; an empty request-relevant intersection cannot authorize. After validation and duplicate rejection, sort this set-like array only by the UTF-8 bytes of each item's RFC 8785 canonical representation as required by `CANONICALIZATION_V0_1.md`. Raw string-byte ordering is not a separate rule.
7. Let `E` be the set union of all environment tokens in `G(A,t)`. Snapshot `environment_scope` is the request-relevant intersection of `E` with root/forbid constraints; an empty intersection cannot authorize. After validation and duplicate rejection, sort this set-like array only by the UTF-8 bytes of each item's RFC 8785 canonical representation as required by `CANONICALIZATION_V0_1.md`; do not introduce an independent ASCII/raw-string ordering rule.
8. Let `O` be the set union of every `allowed_operations` token in `G(A,t)`. For each `forbidden_operation_sets` entry, if all members of that entry are present in `O`, aggregate evaluation fails. No subset, ordering, or pairwise shortcut is permitted.
9. `effective_authority_digest` is `sha256:` plus SHA-256 over the RFC 8785 canonical object `{authority_holder_logical_issuer_id, applicable_delegation_payload_hashes, resource_scope, environment_scope, effective_authority_rank, cumulative_risk, cumulative_budget, cumulative_cardinality, budget_unit}` after the ordering rules above. Any implementation producing different bytes fails conformance.
10. The snapshot MUST bind the exact `ACTIVE_GRANT_INVENTORY_V0_1` reference/hash used. A verifier independently resolves that inventory, verifies its trusted-registry proof and completeness semantics, resolves every inventory member, recomputes `G(A,t)` and all metrics, and requires exact equality with the snapshot. A stale or compromised aggregate evaluator cannot make an omitted grant disappear by signing an incomplete snapshot.

An individual request may be allowed only if its tuple is in `Effective(A,t)` **and** every aggregate constraint passes. Any unknown metric, missing grant, unresolved inventory member, arithmetic overflow, mixed budget unit, unsupported combination, or recomputation mismatch fails closed.

Thus multiple harmless grants cannot become authorized merely because no pair directly conflicts.

## 4. No delegation exists

If `G(A,t)` contains no valid grant covering the request, delegation evaluation returns `NON_DELEGABLE`. A separate direct approval path may still exist, but the absence of delegation never becomes implicit autonomy.

## 5. Decision enforcement

The PDP decision is not itself the effect. A PEP enforces the decision only if:

- decision `issuer_proof` verifies against a PDP trust root using protected proof metadata; the credential maps to the decision `logical_issuer_id`; `pdp_identity` and `kid` are not sufficient;
- decision has not expired;
- every `ALLOW` declares one-time use and `(logical_issuer_id, decision_id, decision_nonce)` has not already been consumed;
- required approval objects carry `resource_registry_ref`, `resource_registry_snapshot_hash`, and `resource_record_hash` equal to the decision and current registry mapping; a remapped provider/native target under the same URI invalidates the approval;
- `delegation_payload_hash` still equals the currently resolved envelope's RFC 8785 payload hash excluding `issuer_proof` and equals that envelope's `issuer_proof.signed_payload_hash`;
- `resource.canonical_uri` equals `resource.id` and remains in the evaluated grant scope;
- `resource_registry_snapshot_hash` still identifies the same registry mapping; a changed provider/native target for the same canonical URI fails;
- `aggregate_authority_snapshot_hash` still matches the schema-valid snapshot the PDP hashed;
- the aggregate snapshot's `active_grant_inventory_hash` resolves to the independently authenticated complete inventory for the authority holder and evaluation time, and independent recomputation of `G(A,t)` and §3 metrics exactly matches the snapshot;
- resource/action/parameter identities match the pending effect;
- bound state/target version still matches;
- revocation freshness is within the required bound;
- decision obligations are understood and satisfiable.

The PEP MUST follow `EFFECT_CONSUMPTION_COMMIT_V0_1.md`: atomically reserve `(logical_issuer_id, decision_id, decision_nonce)` **and** any required approval-use capacity before dispatch; commit durable dispatch intent before invoking the effect; never treat `RESERVED` as prior dispatch; escalate the send-to-persist window as `UNCERTAIN`. Every v0.1 `ALLOW` is one-time-use. A replayed `ALLOW` fails even if unexpired and even if an associated approval has remaining bounded uses. Approval reuse does not imply decision reuse. A mutated envelope with unchanged `delegation_id` and `delegation_version` fails closed.

If any binding or atomic consumption step fails, the PEP denies and requests a fresh evaluation.

## 6. Policy changes

A policy author publishes a new immutable policy/bundle version. The PDP may evaluate it only after governance/publishing controls have accepted that version. Neither PDP nor PEP may mutate the policy bundle during evaluation/enforcement.

Any policy change capable of increasing the author's own effective authority must require approval outside that affected authority path.

## 7. Compromised component posture

No single component is assumed infallible:

- compromised requester: bounded by identity, canonical resource/action, authenticated delegation provenance, PDP, and PEP;
- compromised PDP: constrained by independently verifiable policy/decision hashes, PEP acceptance rules, and audit/verifier checks;
- compromised aggregate evaluator: cannot establish completeness itself; the PEP/verifier resolves the independently authenticated active-grant inventory and recomputes the aggregate metrics;
- compromised PEP: detectable through execution/effect receipts and downstream resource controls; production design should minimize its credentials and scope;
- compromised policy publisher: bounded by policy-governance and separation-of-duty requirements;
- compromised registry: treated as a high-impact integrity event; resource-registry and active-grant-registry writes are non-delegable by default where they can expand writer authority.

Runtime implementation must add cryptographic authentication/attestation and tamper-resistant logging appropriate to deployment.
