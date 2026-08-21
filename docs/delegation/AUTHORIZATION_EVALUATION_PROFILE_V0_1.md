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
8. **Load all active applicable delegations** — not only the grant cited by the requester.
9. **Authenticate then authorize each delegation** — (a) verify issuer proof over the RFC 8785 canonical envelope payload excluding `issuer_proof`; derive algorithm and credential from protected proof metadata; map the credential to `logical_issuer_id` via the bound issuer registry. A trusted credential proves identity only. (b) **Authorize the issuer’s delegable scope** against a hash-bound authority source (`issuer_authority_kind` / `issuer_authority_ref` / `issuer_authority_hash`) covering the exact operations, resources, environments, authority rank and ceiling, risk ceiling, subdelegation depth, and validity period. (c) **For child grants (`PARENT_ENVELOPE`), bind child issuer identity to the parent delegate before any scope monotonicity check.** The child's authenticated `logical_issuer_id` MUST equal the parent envelope's `delegate_logical_issuer_id`. That equality is a trust-rooted identity-registry mapping (`delegate_identity_registry_ref` / `delegate_identity_registry_snapshot_hash`), not a comparison of `delegator` / `delegate_actor` display strings. The child's verified credential MUST map to that same `logical_issuer_id`. A peer that can read or resolve another actor's parent envelope MUST NOT cite its payload hash and issue a child grant. Matching display names with a different logical identity fail. Unresolved or stale identity-registry snapshots fail closed. Root grants MUST cite a separately governed `ISSUER_AUTHORITY_RECORD_V0_1` outside the grantee’s control. Unknown, unauthenticated, excessive, expired, or self-issued authority fails closed. An authenticated peer that does not possess the signed scope never enters `G(A,t)`. Then validate dates, revocation freshness, parent-chain monotonicity, and policy hashes. Compute `delegation_payload_hash` as that SHA-256; it MUST equal `issuer_proof.signed_payload_hash`.
10. **Compute aggregate authority snapshot** — emit a schema-valid `AGGREGATE_AUTHORITY_SNAPSHOT_V0_1` covering subject, evaluation time, applicable authenticated delegation payload hashes, root-ceiling ref/hash, forbid/composition-policy ref/hash, resource/environment scope, cumulative risk/budget/cardinality, effective-authority digest, evaluator identity/version, and snapshot id/version; hash it with RFC 8785.
11. **Classify the requested action** — derive the delegation class from governing policy, not from requester-supplied labels.
12. **Cross-check MICC** — both approval systems apply; the stricter gate wins. Every decision records `micc_approval_class`. When no additional MICC approval gate applies, record `APPROVAL_NONE`; do not omit the field.
13. **Evaluate risk and action-chain composition** — reject/escalate if the requested action or known chain exceeds risk, budget, cardinality, sequence, or blast-radius constraints.
14. **Evaluate decision preconditions** — current state, target version, deterministic checks, conflicts, dependencies, replay/idempotency controls. Child delegations must carry the exact parent precondition hash until a separately governed typed strengthening relation exists.
15. **Resolve required human authority** — if Operator/non-delegable authority is required, absence of a valid bound approval prevents `ALLOW`. Required Operator approvals MUST carry a `delegation_payload_hash` equal to the current envelope payload hash and a verifiable `issuer_proof`. If MICC classifies `APPROVAL_COUNCIL`, v0.1 MUST emit `DENY` or `ESCALATE`; `ALLOW` is schema-invalid even when a Council approval object is present. A future schema revision is required after a separately governed constitution/quorum validator is ratified.
16. **Emit and authenticate decision** — produce `ALLOW`, `DENY`, or `ESCALATE` with `decision_id`, ≥128-bit CSPRNG `decision_nonce`, `logical_issuer_id` plus issuer-registry snapshot, `delegation_payload_hash`, resource-registry snapshot and `resource_record_hash`, RFC 8785 aggregate snapshot hash, unconditional `micc_approval_class`, and expiry. Sign the complete canonical decision excluding `issuer_proof`. `pdp_identity`/`pdp_version`/`kid` are not consumption issuers. Every v0.1 `ALLOW` is one-time-use.

## 3. Aggregate authority algebra

For an actor `A` at time `t`:

- `G(A,t)` = all active, issuer-authenticated, valid delegation grants applicable to A;
- `Permit(A,t)` = union of explicitly permitted operation/resource/environment tuples in `G(A,t)`;
- `Root(A,t)` = separately governed maximum authority ceiling for A;
- `Forbid(t)` = non-delegable and explicit deny guardrails;
- `Effective(A,t)` = `(Permit(A,t) ∩ Root(A,t)) - Forbid(t)` subject to aggregate constraints.

An individual request may be allowed only if its tuple is in `Effective(A,t)` **and** aggregate constraints pass.

Aggregate constraints are first-class and may include:

- maximum authority rank;
- maximum risk ceiling;
- maximum number of concurrent active grants;
- maximum resource cardinality or namespace breadth;
- forbidden operation combinations;
- forbidden resource/operation combinations;
- time/budget/tool-call limits;
- sequence rules that classify a chain by its cumulative effect rather than each step independently;
- blast-radius ceilings;
- separation-of-duty requirements.

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
- compromised PEP: detectable through execution/effect receipts and downstream resource controls; production design should minimize its credentials and scope;
- compromised policy publisher: bounded by policy-governance and separation-of-duty requirements;
- compromised registry: treated as a high-impact integrity event; resource-registry writes are non-delegable by default where they can expand writer authority.

Runtime implementation must add cryptographic authentication/attestation and tamper-resistant logging appropriate to deployment.
