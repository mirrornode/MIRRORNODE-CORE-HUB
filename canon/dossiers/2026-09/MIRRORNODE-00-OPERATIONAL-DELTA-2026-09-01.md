# MIRRORNODE-00 — Operational Verification Delta

**Date:** 2026-09-01  
**Status:** CANDIDATE OPERATIONAL EVIDENCE / UNRATIFIED  
**Authority effect:** NONE  
**Canonical precedence:** NONE  
**Promotion gate:** Ptah evaluation + explicit Operator ratification + canonical promotion record in accordance with `MASTER_INDEX.md`

## Scope

This delta updates only the current exact-head and verification state recorded in `MIRRORNODE-00-OPERATIONAL-ADDENDUM-2026-09-01.md`.

The earlier addendum remains historical evidence for the heads and observations it names. This delta does not rewrite predecessor evidence, transfer verification across commits, authorize merge/deployment, or canonize either implementation branch.

---

## 1. MOPCON current head

Repository: `mirrornode/mirrornode-operator-console`  
Draft PR: `#27`  
Branch: `feat/local-runtime-console-2026-08-31`  
Current exact head: `de3e7c7b5de03d00c3213e5ec24372f89d72411e`

Exact-head local evidence reported by the Operator:

- `git rev-parse HEAD` matched `de3e7c7b5de03d00c3213e5ec24372f89d72411e`;
- `npm run type-check` completed cleanly;
- underlying command: `tsc --noEmit`.

Current head contains the latest review-correction pass, including:

- reviewable bound evidence state before APPROVE;
- redirect rejection for the private case reader;
- runtime-health schema validation before reporting approval-boundary state;
- strict Osiris-flow scope and local masked-customer validation;
- stale-plan gate removal when a replacement plan request starts;
- separate reporting of execution success vs trace-retrieval failure;
- explicit Operator sign-out;
- retained strict case allowlisting, malformed-projection fail-closed behavior, HTTPS-only non-loopback reader transport, and reserved evidence-marker rejection.

Fresh independent exact-head review has been requested for `de3e7c7...`.

### Verification lineage preserved

`fe63850aa1371126c159d3a64b044ee7b1db6fe2` remains the authenticated private-case E2E predecessor: unauthenticated `401`, Operator auth `200`, projection `available`, projected mutation state `disabled`, and three paid Osiris cases observed through the minimum projection.

That predecessor E2E result is **not** represented as exact-head E2E proof for `de3e7c7...`.

---

## 2. Platform current head

Repository: `mirrornode/mirrornode-platform`  
Draft PR: `#53`  
Branch: `feat/mopcon-readonly-case-projection-2026-08-31`  
Current exact head: `95e2fec8deec09f67e62d4eae8f9a0a7fbfa2542`

Exact-head local evidence reported by the Operator:

- `git rev-parse HEAD` matched `95e2fec8deec09f67e62d4eae8f9a0a7fbfa2542`;
- `npm test -- app/api/internal/mopcon/cases/route.test.ts` completed cleanly.

Current head contains the latest concurrency corrections:

- actionable case pagination now uses an immutable case-UUID keyset cursor rather than mutable offset pagination;
- actionable and terminal reads are deduplicated by case UUID, with the later terminal observation replacing a stale actionable copy if a transition occurs during the scan;
- prior checked-in UUID schema migration remains repository-only and has **not** been applied to production;
- read-only field minimization, sanitized errors, bearer-secret boundary, and no-mutation semantics remain intended invariants.

Fresh independent exact-head review has been requested for `95e2fec...`.

### Verification lineage preserved

- `56bfd1d31b8a5964f5de870b59f5e8c3568b418b` owns the prior exact-head route-test and Vercel-success evidence before the concurrency corrections.
- `062ad630ad3c795dd27c2e84d251880b8c615c3f` owns the authenticated local production-ledger read-path evidence.
- `b78152011c81c4d4fa2d09a3c9f1c7e70f9fd78f` owns the earlier unauthenticated preview `401` / no-projection evidence.

Those predecessor results are not silently transferred to `95e2fec...`.

---

## 3. Live-case observation remains dated

The latest authenticated live-case observation remains the predecessor E2E result:

- 3 paid Osiris cases total;
- 2 at `intake_complete`;
- 1 at `fulfillment_started`;
- derived customer-case Operator Debt at that observation: 2.

This delta does **not** re-attest that count or debt value at the current heads. A fresh current-head read-only E2E is still required before treating the distribution as current.

---

## 4. Current disposition

**MOPCON `de3e7c7...`: exact-head local type-check clean; fresh independent review pending.**

**Platform `95e2fec...`: exact-head local route test clean; fresh independent review pending; current-head live read-path verification still pending.**

**Projected mutation state remains designed as DISABLED. Customer mutation / fulfillment advancement / release / delivery remain NOT AUTHORIZED.**

**The Platform UUID migration remains checked in only and is NOT AUTHORIZED for production application by this record.**

**No implementation branch is authorized for merge or production promotion by this delta.**

**Canon status remains CANDIDATE ONLY.** Ordinary review or merge does not create canonical precedence; Ptah evaluation + explicit Operator ratification + promotion record remain required.
