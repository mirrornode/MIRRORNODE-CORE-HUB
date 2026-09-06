# MIRRORNODE Engineering Doctrine v1.0

Status: DRAFT CANDIDATE — exact-subject engineering discipline. Not canonical until reviewed and promoted through the Operator gate.

## Core doctrine

MIRRORNODE is built as a network of narrowly authoritative components that exchange exact-subject evidence.

Read paths project truth. Write paths require explicit authority. Consequential state changes are atomic and idempotent. UNKNOWN never collapses to PASS. Every material conclusion is bound to its exact source. Engineering stops when the bounded claim is proven.

Commercially, build the smallest truthful slice that improves purchase, fulfillment, proof, or removes a concrete blocker to one of those outcomes.

## 1. Subject identity

Never identify consequential work by a friendly label alone.

Minimum code subject:

```text
repository_full_name
pull_request_number
source_branch
execution_worktree_branch (when different)
exact_head_sha
base_sha
```

Canonical shorthand:

```text
<owner>/<repo>#<pr>@<exact-head-sha>
```

A head change invalidates exact-head execution clearance. Predecessor evidence may remain only when explicitly retained as dated/content-scoped history.

## 2. State vocabulary

Use explicit state labels rather than implication:

```text
PROPOSED
IMPLEMENTED
VERIFIED
MERGED
DEPLOYED
ACTIVE
AUTHORIZED
CANONICAL
HOLD
UNKNOWN
STALE
FAILED
RETIRED
```

These states are not interchangeable.

In particular:

```text
MERGED != DEPLOYED
DEPLOYED != ACTIVE
ACTIVE != AUTHORIZED
TESTED != APPROVED
IMPLEMENTED != CANONICAL
MISSING EVIDENCE != PASS
```

## 3. Admission rule

Before engineering begins, record:

```text
why_now
revenue_relation
risk_if_deferred
exit_condition
```

Default admission classes:

- PURCHASE
- FULFILLMENT
- PROOF
- BLOCKER

Exceptions require a concrete security, legal, data-loss, or critical-infrastructure reason.

If the work does not materially improve one of the admission classes and is not a justified exception, defer it.

## 4. Claim, invariants, and non-goals

Every consequential slice states one sentence:

> This slice proves ______.

Then records a small set of invariants and explicit non-goals.

A non-goal is a control. It prevents architecture from expanding sideways while a bounded claim is being proven.

## 5. Read/write separation

Projectors are read-only:

```text
provider/API
  -> collector
  -> normalizer
  -> evidence record
  -> projector
  -> Operator view
```

Projectors may return VERIFIED, UNKNOWN, STALE, HOLD, or FAILED. Observation does not grant mutation authority.

Consequential writes use explicit commands containing, at minimum:

```json
{
  "subject": {},
  "idempotency_key": "...",
  "operator": {
    "actor_id": "...",
    "reason": "..."
  }
}
```

The server authenticates, binds the subject, validates authoritative prerequisites, serializes/locks where needed, performs one atomic transition, records durable effect evidence, and returns a receipt.

## 6. Atomicity and idempotency

Prefer:

```text
BEGIN
lock authoritative subject
validate authoritative state
write state
write receipt
COMMIT
```

over check-now/mutate-later workflows.

Same intended effect + same idempotency key should resolve to the same authoritative receipt. Cross-subject key reuse must fail closed.

## 7. Evidence classes

Every proof states what it proves.

- Unit/integration tests: covered implementation behavior.
- CI: repository-defined checks passed at exact SHA.
- Database harness: migration/RPC behavior in the named disposable environment.
- Provider observation: the provider returned a specific state at a specific time.
- Semantic/adversarial review: no material finding was found under the named rubric at the exact subject.
- Operator disposition: authorizes only the explicitly named next action.

No evidence class silently inherits authority from another.

## 8. False-PASS resistance

Consequential code deliberately considers:

```text
NULL
empty
malformed
unknown
stale
revoked
wrong subject
wrong actor
wrong producer
old success + newer failure
replay
duplicate
concurrency
partial response
pagination omission
timeout
provider unavailable
base/head change
```

UNKNOWN is a valid result and must never be converted into PASS for convenience.

## 9. Provider boundary

Provider configuration is evidence about that provider, not universal system authority.

A repository setting does not prove project-wide containment. A project setting does not prove account-wide containment. A provider success badge does not prove business authorization.

Normalize provider evidence before making system claims.

## 10. Migration discipline

Before merge, an unmerged migration owned entirely by the PR may be amended in place.

After merge/deployment, migration history is append-only; use a successor migration.

Any material migration change invalidates prior database execution evidence for the changed behavior and requires fresh proof.

## 11. Reproducible proof

A proof mechanism used more than once becomes a retained verification asset.

Prefer repository locations such as:

```text
scripts/verify/
tests/integration/
tests/adversarial/
fixtures/
evidence/
```

Disposable data may remain disposable. The mechanism for reproducing consequential proof should not.

## 12. Separation of functions

Separate:

```text
BUILD
REVIEW
AUTHORIZE
EXECUTE
```

Separation of function does not require fake separation of human identity.

Recommended seats:

| Seat | Inspect | Edit | Authorize |
|---|---:|---:|---:|
| Operator | yes | through approved executor | yes |
| Builder | yes | bounded branch/worktree | no |
| Reviewer | yes | no | no |
| Arbitrator | yes | no | no |
| Final Review Seat | yes | no | no |
| Projector service | yes | no | never |

The seat defines authority, not the model or vendor.

## 13. Final Review Seat

The Final Review Seat is isolated by role and context, not by pretending to be another human.

It is:

- read-only;
- exact-head bound;
- unable to edit, push, merge, deploy, or alter its own rubric;
- given the exact subject, invariants, diff, proof, known findings, non-goals, and authority boundary;
- required to return CLEAR, CORRECTION_REQUIRED, or BLOCKED.

Preferred long-term implementation: publish a machine check/status bound to the exact SHA with rubric version and evidence identity.

## 14. Standard lifecycle

1. Admission.
2. Subject lock.
3. One-sentence claim.
4. Invariants.
5. Non-goals.
6. Inspect authoritative current truth.
7. Smallest coherent implementation.
8. Local verification.
9. Exact-head CI.
10. Semantic/adversarial review.
11. Domain proof.
12. Fresh final review at the resulting head.
13. Operator disposition: MERGE / HOLD / CORRECT / ABANDON.
14. Merge.
15. Separately authorized rollout.
16. Runtime receipt.

Merge authorization does not imply deployment, migration, or live-mutation authorization.

## 15. Stop rule

```text
material finding -> bounded correction
no material finding -> stop engineering
```

Improvement ideas become explicit debt/backlog. They do not reopen a clean revenue-critical subject.

## 16. Definition of Done

A MIRRORNODE slice is done when:

- the claim is explicit;
- invariants are satisfied;
- non-goals stayed untouched;
- subject identity is exact;
- tests and domain proof pass;
- no material review finding remains;
- evidence belongs to the exact final head;
- documentation accurately describes resulting state;
- remaining debt is explicitly nonblocking;
- the appropriate Operator disposition exists;
- consequential proof is reproducible.

It is not done merely because more improvements can be imagined.
