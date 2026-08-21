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
9. **Authenticate and validate each delegation** — require verifiable issuer proof over the RFC 8785 canonical envelope payload excluding `issuer_proof` (`CANONICALIZATION_V0_1.md`, `ISSUER_PROOF_V0_1.md`); derive algorithm and credential from protected proof metadata, not from schema hints; verify the issuer against a trusted root outside the delegate's authority path, then validate scope, dates, revocation freshness, parent-chain monotonicity, and policy hashes. Compute `delegation_payload_hash` as that SHA-256; it MUST equal `issuer_proof.signed_payload_hash`. An unsigned, self-asserted, fabricated, unverifiable, hint-only, algorithm-substituted, or payload-hash-mismatched envelope never enters `G(A,t)`.
10. **Compute aggregate authority snapshot** — emit a schema-valid `AGGREGATE_AUTHORITY_SNAPSHOT_V0_1` covering subject, evaluation time, applicable authenticated delegation payload hashes, root-ceiling ref/hash, forbid/composition-policy ref/hash, resource/environment scope, cumulative risk/budget/cardinality, effective-authority digest, evaluator identity/version, and snapshot id/version; hash it with RFC 8785.
11. **Classify the requested action** — derive the delegation class from governing policy, not from requester-supplied labels.
12. **Cross-check MICC** — both approval systems apply; the stricter gate wins. Every decision records `micc_approval_class`. When no additional MICC approval gate applies, record `APPROVAL_NONE`; do not omit the field.
13. **Evaluate risk and action-chain composition** — reject/escalate if the requested action or known chain exceeds risk, budget, cardinality, sequence, or blast-radius constraints.
14. **Evaluate decision preconditions** — current state, target version, deterministic checks, conflicts, dependencies, replay/idempotency controls. Child delegations must carry the exact parent precondition hash until a separately governed typed strengthening relation exists.
15. **Resolve required human authority** — if Operator/non-delegable authority is required, absence of a valid bound approval prevents `ALLOW`. Required Operator approvals MUST carry a `delegation_payload_hash` equal to the current envelope payload hash and a verifiable `issuer_proof`. If MICC classifies `APPROVAL_COUNCIL`, v0.1 MUST emit `DENY` or `ESCALATE`; `ALLOW` is schema-invalid even when a Council approval object is present. A future schema revision is required after a separately governed constitution/quorum validator is ratified.
16. **Emit and authenticate decision** — produce `ALLOW`, `DENY`, or `ESCALATE` with `decision_id`, ≥128-bit CSPRNG `decision_nonce`, `delegation_payload_hash`, resource-registry snapshot bindings, RFC 8785 aggregate snapshot hash, unconditional `micc_approval_class`, and expiry. Sign the complete canonical decision excluding `issuer_proof`. `pdp_identity`/`pdp_version` are labels only. Every v0.1 `ALLOW` is one-time-use.

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

- decision `issuer_proof` verifies against a PDP trust root using protected proof metadata (`alg`/`kid` or equivalent); `pdp_identity` is not sufficient;
- decision has not expired;
- every `ALLOW` declares one-time use and `(authenticated_issuer, decision_id, decision_nonce)` has not already been consumed;
- `delegation_payload_hash` still equals the currently resolved envelope's RFC 8785 payload hash excluding `issuer_proof` and equals that envelope's `issuer_proof.signed_payload_hash`;
- `resource.canonical_uri` equals `resource.id` and remains in the evaluated grant scope;
- `resource_registry_snapshot_hash` still identifies the same registry mapping; a changed provider/native target for the same canonical URI fails;
- `aggregate_authority_snapshot_hash` still matches the schema-valid snapshot the PDP hashed;
- resource/action/parameter identities match the pending effect;
- bound state/target version still matches;
- revocation freshness is within the required bound;
- decision obligations are understood and satisfiable.

The PEP MUST follow `EFFECT_CONSUMPTION_COMMIT_V0_1.md`: atomically reserve `(authenticated_issuer, decision_id, decision_nonce)` before dispatch; use that tuple as the effect idempotency key; never mark `COMPLETED` until receipt and approval accounting reconcile; escalate uncertain non-idempotent outcomes. Every v0.1 `ALLOW` is one-time-use. A replayed `ALLOW` fails even if unexpired and even if an associated approval has remaining bounded uses. Approval reuse does not imply decision reuse. A mutated envelope with unchanged `delegation_id` and `delegation_version` fails closed.

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
