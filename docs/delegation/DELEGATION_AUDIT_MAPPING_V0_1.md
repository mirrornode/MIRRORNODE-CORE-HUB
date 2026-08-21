# Delegation Audit Mapping v0.1

**Status:** Draft additive mapping under CG-0036.  
**Governing envelope:** `canon/contracts/AUDIT_EMISSION.md` remains locked and
unchanged. This mapping does not replace or weaken it.

Each delegation execution event emits the required audit record and an
authenticated `EXECUTION_RECEIPT_V0_1`. The two records share the same
`audit_id`. The audit record is an operational index; the receipt is the typed,
hash-bound evidence object.

| AUDIT_EMISSION field | Delegation mapping |
|---|---|
| `timestamp` | execution receipt `issued_at` |
| `repo` / `repo_hash` | repository and corrected normative/runtime head that performed enforcement |
| `charter_hash` | unchanged governing audit semantics |
| `event_type` | `execution` |
| `actor` | receipt issuer and MICC executor, sanitized for the audit envelope |
| `verdict` | `SUCCEEDED`→`SUCCESS`; `FAILED`/`NO_EFFECT`→`FAILURE`; pre-dispatch denial→`BLOCKED`; `UNCERTAIN`→`ESCALATED` |
| `evidence.inputs` | decision, delegation, holder, MICC, resource, precondition, revocation, aggregate, and approval hashes |
| `evidence.outputs` | dispatch state, effect outcome, effect-receipt hash, and decision/approval consumption states |
| `evidence.duration_ms` | measured enforcement duration |
| `evidence.error` | sanitized reason code or `null` |
| `audit_id` | exact execution receipt `audit_id` |

Secrets, credentials, proof values, native payloads, and unsanitized provider
responses MUST NOT be copied into the audit envelope. Their authenticated
references/hashes remain in the execution receipt. An audit record without a
retrievable, authentic receipt cannot prove successful delegated effect; a
receipt without the required audit record violates `AUDIT_EMISSION`.

The 90-day audit minimum does not shorten the longer preimage/evidence retention
period required by the bound receipt policy and
`REFERENCE_INTEGRITY_PROFILE_V0_1.md`.
