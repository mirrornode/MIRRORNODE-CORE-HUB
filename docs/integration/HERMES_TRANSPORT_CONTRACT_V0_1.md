# Hermes Transport Contract v0.1

**Status:** PROPOSED / NON-CANONICAL  
**Authority effect:** None. This document defines implementation acceptance semantics only.  
**Provider status:** Unselected. No provider is authorized by this contract.  
**Scope:** Hermes message acceptance, persistence, claim, delivery, retry, dead-letter, rejection, and audit truth.

## 1. Purpose

Hermes must never report transport success that has not occurred. Runtime health, in-memory acceptance, provider acknowledgement, or enqueue API success may not be promoted into a stronger MIRRORNODE delivery claim.

This contract is provider-neutral. It does not select Redis, Inngest, QStash, Supabase, or any other transport or execution substrate.

## 2. Canonical transport states

A Hermes event may occupy only the following transport states:

- `ACCEPTED` — request shape and invocation context passed ingress validation.
- `PERSISTED` — event has been durably recorded in the authorized transport substrate.
- `CLAIMED` — an authorized consumer has acquired a bounded delivery lease or equivalent claim.
- `DELIVERED` — the intended consumer has positively acknowledged the event under the governed delivery contract.
- `RETRY_SCHEDULED` — a prior delivery attempt failed and a bounded retry has been durably scheduled.
- `DEAD_LETTERED` — delivery attempts are exhausted or policy requires human review.
- `REJECTED` — validation, authority, scope, or policy rejected the event before execution.
- `FAILED_CLOSED` — an unknown, missing, stale, contradictory, or unverifiable condition prevented safe advancement.

Unknown states are invalid and must fail closed.

## 3. Required event identity

Every event must bind at minimum:

- `event_id`
- `operation_id` or `journey_id`
- `event_type`
- `producer`
- `intended_consumer`
- `payload_digest`
- `created_at`
- `attempt`
- `policy_version`
- `authority_ref`
- `approval_ref` when the operation class requires approval
- `transport_state`
- `receipt_id` for every state transition recorded as evidence

`event_id` must be globally unique and stable across retries. Retries increment `attempt`; they do not mint a semantically new event.

## 4. Truth invariants

### 4.1 Persistence invariant

**No durable persistence, no `PERSISTED` acknowledgement.**

An in-memory append is never durable persistence. A provider API response is not sufficient unless the configured adapter contract proves that the event is durably retained under the declared transport semantics.

### 4.2 Authority invariant

**No authority resolution, no dispatch.**

Producer identity, intended consumer identity, scope decision, policy version, and approval basis where required must be resolved before Hermes advances an event into executable delivery.

Caller-supplied identity strings are claims, not authority.

### 4.3 Delivery invariant

**No confirmed consumer acknowledgement, no `DELIVERED` claim.**

Queue insertion, publish success, HTTP 2xx from an intermediary, function scheduling, or worker claim does not equal delivery unless the governed consumer acknowledgement contract explicitly defines it as such.

### 4.4 Idempotency invariant

Every consumer path capable of side effects must enforce idempotency by `event_id` or a bound idempotency key. At-least-once transport must never imply at-most-once side effects.

### 4.5 Retry invariant

Retries must be bounded, observable, and deterministic under declared policy. Retry scheduling must not erase prior failed-attempt evidence.

### 4.6 Dead-letter invariant

Exhausted or policy-blocked events must enter a reviewable terminal or held state. Dead-letter contents must preserve event identity, failure classification, attempt count, and last authoritative transport receipt without leaking secrets.

### 4.7 Evidence invariant

Every transport state transition must emit MIRRORNODE-owned canonical evidence. External telemetry may observe but may not become the sole authority for transport history.

## 5. Outcome semantics

Hermes transport responses must distinguish acceptance from delivery.

Examples:

- `ACCEPTED` means ingress accepted the request for further processing.
- `PERSISTED` means durable storage is proven.
- `DELIVERED` means governed consumer acknowledgement is proven.
- `REJECTED` and `FAILED_CLOSED` are non-success outcomes.

The terms `routed`, `sent`, `delivered`, `completed`, or equivalent may not be returned unless their contractually defined condition has actually been satisfied.

## 6. Provider boundary

MIRRORNODE integration semantics remain controlling. A provider does not become Hermes and does not gain lattice authority by supplying transport or execution capability.

Transport and durable execution are separate capability families. A future provider may implement one or both only through separately authorized adapter declarations and conformance evidence.

## 7. Approval boundary

Transport may carry operations of different side-effect classes. Hermes must not infer that transport acceptance authorizes execution.

An event that requires approval must remain non-executable until the applicable governed approval object is verified against the exact event/operation subject and current policy.

## 8. Minimum conformance tests before production use

An implementation is not production-ready until automated tests prove at least:

1. Process restart does not lose a `PERSISTED` event.
2. Duplicate delivery of one `event_id` does not duplicate a protected side effect.
3. Missing or invalid authority evidence produces `REJECTED` or `FAILED_CLOSED` and no consumer dispatch.
4. A transport enqueue cannot be reported as `DELIVERED`.
5. Retry attempts preserve one stable `event_id` and monotonically increasing `attempt`.
6. Exhausted retries enter `DEAD_LETTERED` with reviewable evidence.
7. Unknown transport state or provider response fails closed.
8. Provider health or provider success cannot manufacture MIRRORNODE authorization.

## 9. Current implementation disposition

The legacy `hermes/runtime.py` in-memory queue does not satisfy this contract. It may remain a development prototype only if its API responses and evidence claims are narrowed so they do not imply durable routing or delivery.

Promotion of a durable Hermes implementation requires a separate implementation change and provider/adaptor authorization under the applicable MIRRORNODE integration governance.
