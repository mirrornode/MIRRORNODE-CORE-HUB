# MIRRORNODE Effect/Consumption Commit Protocol v0.1

**Status:** Draft under CG-0036 — architecture/conformance profile only  
**Purpose:** Define durable, fail-closed coupling of `ALLOW` consumption to downstream effects without requiring an impossible single database transaction across an external effect.

This profile does not authorize a runtime, store, or message bus.

## 1. Identifiers

- **ID** — stable identifier within an authenticated issuer trust domain. Issuer-scoped uniqueness is required. IDs are not entropy.
- **Nonce** — unpredictable CSPRNG replay-prevention value with at least 128 bits of entropy, encoded as unpadded base64url (`^[A-Za-z0-9_-]{22,64}$`).

Consumption and effect keys are:

```text
decision_key  = (authenticated_issuer, decision_id, decision_nonce)
approval_key  = (authenticated_issuer, approval_id, approval_nonce)
```

`authenticated_issuer` is taken from **protected proof metadata**, not from `pdp_identity`, `approver`, or schema `issuer_credential_ref` hints. Cross-PDP collisions of bare `decision_id`/`decision_nonce` pairs MUST NOT share a consumption slot.

## 2. When a single transaction is required

If the effect record and the consumption record share one transactional resource, reservation, effect outcome, receipt, and approval accounting MUST commit in **one** transaction.

## 3. Otherwise: durable state machine

If the effect is external (separate store, API, or side effect), implementations MUST use a transactional outbox/inbox or an equivalent durable state machine. Silent in-memory flags are non-conformant.

### States

| State | Meaning |
|---|---|
| `IDLE` | No reservation. |
| `RESERVED` | `decision_key` atomically reserved; effect not dispatched. |
| `DISPATCHED` | Effect requested; outcome unknown. |
| `EFFECT_RECORDED` | Downstream reports completion; receipt not yet durable. |
| `RECEIPTED` | Effect receipt durable, keyed by `decision_key`. |
| `APPROVAL_ACCOUNTED` | Required approval counters updated. |
| `COMPLETED` | Receipt and approval-consumption outcome durably reconciled. |
| `UNCERTAIN` | Crash or timeout after dispatch without a verified receipt. |
| `FAILED` | Denied, rolled back, or escalated; reservation released only if no effect could have occurred. |

`COMPLETED` MUST NOT be recorded until the effect receipt **and** any required approval-consumption outcome are durably reconciled.

## 4. Protocol

1. Verify the decision `issuer_proof` and all PEP bindings.
2. Atomically **reserve/consume** `decision_key` **before** dispatch. A second reservation of the same key fails.
3. Dispatch the effect using `decision_key` as the idempotency key.
4. Where the downstream supports idempotency, replay of the same key MUST NOT create a second effect.
5. Persist an effect receipt bound to the same `decision_key`.
6. Account approval consumption (`ONE_TIME` consume, or `BOUNDED_REUSE` decrement). Counters MUST NOT remain under-decremented after a successful effect.
7. Mark `COMPLETED` only after steps 5–6 reconcile.

## 5. Crash recovery

- Crash **before reservation**: no effect; safe to start over.
- Crash **after reservation, before dispatch**: do not dispatch a new distinct effect; resume the same reserved key or fail closed for operator reconciliation. Do not release the reservation if dispatch might have occurred.
- Crash **after effect, before receipt**: state is `UNCERTAIN`. Query downstream by `decision_key`. Do **not** silently retry a non-idempotent effect.
- Crash **after receipt, before approval accounting**: replay approval accounting for that key (idempotent decrement/consume). Do not re-dispatch.
- Concurrent duplicate dispatch: the second actor MUST observe the reservation and fail or attach to the existing key.
- Uncertain outcomes **escalate for reconciliation**; they never auto-retry a non-idempotent effect.

A successful effect with a missing approval decrement is a conformance failure.

## 6. Crash-boundary tests (normative)

Every transition below MUST have a documented fixture whose expected result is fail-closed, resume-same-key, or escalate — never silent double-effect.

1. crash before reservation;
2. crash after reservation but before dispatch;
3. crash after effect but before receipt;
4. crash after receipt but before approval accounting;
5. concurrent duplicate dispatch of the same `decision_key`;
6. reconciliation after an uncertain outcome;
7. bounded-reuse counter not decremented after successful effect (must fail/reconcile, not complete);
8. weak nonce below 128 bits (must fail schema/validation);
9. cross-issuer ID/nonce collision treated as distinct keys.

Fixtures: `EFFECT_CONSUMPTION_COMMIT_VECTORS_V0_1.json`.
