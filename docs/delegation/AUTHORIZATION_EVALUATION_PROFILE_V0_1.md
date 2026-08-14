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
3. **Canonicalize resource** — resolve aliases to one registry-backed canonical resource identity; reject ambiguity.
4. **Normalize action** — resolve operation identifier and hash material parameters.
5. **Freeze evaluation context** — obtain current state/version and context digest used by the decision.
6. **Load immutable policy bundle** — verify `policy_content_hash` and `policy_bundle_hash`.
7. **Apply non-delegable/forbid guardrails** — a matching guardrail cannot be overridden by a permit or delegation.
8. **Load all active applicable delegations** — not only the grant cited by the requester.
9. **Validate each delegation** — identity, signature/integrity where applicable, scope, dates, revocation freshness, parent-chain monotonicity, policy hashes.
10. **Compute aggregate authority snapshot** — evaluate the union of active grants against the separately governed root ceiling and composition constraints.
11. **Classify the requested action** — derive the delegation class from governing policy, not from requester-supplied labels.
12. **Cross-check MICC** — both approval systems apply; the stricter gate wins.
13. **Evaluate risk and action-chain composition** — reject/escalate if the requested action or known chain exceeds risk, budget, cardinality, sequence, or blast-radius constraints.
14. **Evaluate decision preconditions** — current state, target version, deterministic checks, conflicts, dependencies, replay/idempotency controls.
15. **Resolve required human authority** — if Operator/Council/non-delegable authority is required, absence of a valid bound approval prevents `ALLOW`.
16. **Emit decision** — `ALLOW`, `DENY`, or `ESCALATE` with decision nonce, reason, obligations, state/policy/aggregate digests, and expiry.

## 3. Aggregate authority algebra

For an actor `A` at time `t`:

- `G(A,t)` = all active, valid delegation grants applicable to A;
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

- decision signature/integrity and issuer are trusted;
- decision has not expired;
- one-time-use constraints have not already been consumed;
- resource/action/parameter identities match the pending effect;
- bound state/target version still matches;
- revocation freshness is within the required bound;
- decision obligations are understood and satisfiable.

If any binding fails, the PEP denies and requests a fresh evaluation.

## 6. Policy changes

A policy author publishes a new immutable policy/bundle version. The PDP may evaluate it only after governance/publishing controls have accepted that version. Neither PDP nor PEP may mutate the policy bundle during evaluation/enforcement.

Any policy change capable of increasing the author's own effective authority must require approval outside that affected authority path.

## 7. Compromised component posture

No single component is assumed infallible:

- compromised requester: bounded by identity, canonical resource/action, PDP, and PEP;
- compromised PDP: constrained by independently verifiable policy/decision hashes, PEP acceptance rules, and audit/verifier checks;
- compromised PEP: detectable through execution/effect receipts and downstream resource controls; production design should minimize its credentials and scope;
- compromised policy publisher: bounded by policy-governance and separation-of-duty requirements;
- compromised registry: treated as a high-impact integrity event; resource-registry writes are non-delegable by default where they can expand writer authority.

Runtime implementation must add cryptographic authentication/attestation and tamper-resistant logging appropriate to deployment.
