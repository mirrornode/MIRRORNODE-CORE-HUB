# MIRRORNODE Effect/Consumption Commit Protocol v0.1

**Status:** Draft under CG-0036 — architecture/conformance profile only  
**Purpose:** Define durable, fail-closed coupling of `ALLOW` consumption and required approval-use capacity to downstream effects without requiring an impossible single database transaction across an external effect.

This profile does not authorize a runtime, store, or message bus.

## 1. Identifiers

- **ID** — stable identifier within a **logical issuer** namespace. IDs are not entropy.
- **Nonce** — unpredictable CSPRNG replay-prevention value with at least 128 bits of entropy, encoded as unpadded base64url (`^[A-Za-z0-9_-]{22,64}$`).
- **`logical_issuer_id`** — trust-rooted, immutable/versioned identifier for the issuing PDP or approver. It is **not** `kid`, `issuer_credential_ref`, or other proof metadata.

A verified credential maps to `logical_issuer_id` through an issuer registry (`issuer_registry_ref` + `issuer_registry_snapshot_hash`). Credential rotation preserves the logical issuer namespace. Unrelated credentials MUST NOT collapse into one issuer. A revoked credential MUST NOT create a new consumption namespace.

Consumption and effect keys are:

```text
decision_key  = (logical_issuer_id, decision_id, decision_nonce)
approval_key  = (logical_issuer_id, approval_id, approval_nonce)
```

## 2. When a single transaction is required

If the effect record, decision consumption, and approval-capacity records share one transactional resource, reservation, dispatch intent, effect outcome, receipt, and approval finalization MUST commit in **one** transaction.

## 3. Durable state machine

If the effect is external, implementations MUST use a transactional outbox/inbox or equivalent durable state machine.

### States

| State | Meaning |
|---|---|
| `IDLE` | No reservation. |
| `RESERVED` | `decision_key` **and** any required approval-use capacity are atomically reserved. **No dispatch intent exists. `RESERVED` is never evidence that an effect may already have occurred.** |
| `DISPATCH_INTENT` | Durable outbox/dispatch-intent committed **before** invoking the external effect. |
| `DISPATCHED` | External invocation attempted after `DISPATCH_INTENT`. |
| `EFFECT_RECORDED` | Downstream reports completion; receipt not yet durable. |
| `RECEIPTED` | Effect receipt durable, keyed by `decision_key`. |
| `APPROVAL_FINALIZED` | Reserved approval use finalized as consumed, or durably marked `RELEASED` after confirmed `NO_EFFECT`. |
| `COMPLETED` | Receipt and approval-consumption outcome durably reconciled. |
| `UNCERTAIN` | Crash or missing receipt **after** `DISPATCH_INTENT` (including the send-to-persist window). |
| `FAILED` | Denied or rolled back. Reservations may be released **only** if a confirmed no-effect is proven. |

`COMPLETED` MUST NOT be recorded until the effect receipt **and** any required approval-consumption outcome are durably reconciled.

## 4. Protocol

1. Verify the decision `issuer_proof`, map the credential to `logical_issuer_id`, and check all PEP bindings including resource-registry equality with any required approval.
2. Atomically, **before any effect dispatch and before `DISPATCH_INTENT`**:
   - reserve `decision_key`;
   - if an Operator (or other required) approval is bound, reserve approval capacity on `approval_key`:
     - `ONE_TIME`: reserve the sole use;
     - `BOUNDED_REUSE`: atomically reserve one remaining use.
   Insufficient remaining capacity, or a concurrent actor taking the last use, **prevents dispatch**.
3. Commit a durable **dispatch-intent / outbox** record for `decision_key`. Only after this commit may the PEP invoke the external effect.
4. Invoke the effect using `decision_key` as the idempotency key.
5. Persist an authenticated `EXECUTION_RECEIPT_V0_1` bound to the same `decision_key`, including the decision and applicable approval consumption states and the typed effect receipt reference/hash.
6. Finalize the approval reservation as **consumed**. Failure to finalize after a successful effect **MUST NOT restore usable capacity**.
7. Mark `COMPLETED` only after steps 5–6 reconcile.

Confirmed no-effect (never left `RESERVED`, or `DISPATCH_INTENT` never sent and downstream proves no accept) MAY release both reservations. The authenticated execution receipt MUST record `effect_outcome: NO_EFFECT` and, when an approval reservation existed, `approval_consumption: RELEASED`; `RELEASED` is invalid for every other outcome. An **uncertain** effect **retains** both reservations until reconciliation.

## 5. Crash recovery and the send-to-persist window

- Crash **before reservation**: no effect; safe to start over.
- Crash in `RESERVED` (no `DISPATCH_INTENT`): dispatch has **not** occurred. Recovery may later commit `DISPATCH_INTENT` and send **once**. Do **not** treat `RESERVED` as possible prior dispatch.
- Crash after `DISPATCH_INTENT` is committed, including:
  - local crash before the network call;
  - **send-to-persist window**: the downstream **accepts** the request and the PEP fails **before post-call persistence** of `DISPATCHED`/receipt;
  is `UNCERTAIN`. Redispatch is allowed **only** if the downstream operation is demonstrably idempotent **and** uses the identical `decision_key`. Non-idempotent uncertain effects require reconciliation. Missing receipt is not permission to redispatch a non-idempotent call.
- Crash after receipt, before approval finalization: replay finalization (idempotent consume of the already-reserved use). Do not re-dispatch. Do not restore capacity.
- Concurrent duplicate dispatch of the same `decision_key`: second actor fails or attaches.
- Concurrent decisions sharing a `ONE_TIME` approval or the last `BOUNDED_REUSE` use: only one reservation succeeds; the other MUST NOT dispatch.

## 6. Crash-boundary tests (normative)

Fixtures: `EFFECT_CONSUMPTION_COMMIT_VECTORS_V0_1.json`.

Required fixtures include: crash before reservation; `RESERVED` without dispatch intent; send-to-persist (external accept, local persist fail); concurrent last approval use; confirmed no-effect release; successful-effect finalization; uncertain retention of approval reservation; credential rotation preserving `logical_issuer_id`; unrelated credentials not collapsing issuers.
