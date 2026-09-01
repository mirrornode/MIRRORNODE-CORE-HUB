# MIRRORNODE-00 — Operational Verification Delta

**Date:** 2026-09-01  
**Status:** CANDIDATE OPERATIONAL EVIDENCE / UNRATIFIED  
**Authority effect:** NONE  
**Canonical precedence:** NONE  
**Promotion gate:** Ptah evaluation + explicit Operator ratification + canonical promotion record in accordance with `MASTER_INDEX.md`

## Scope

This delta updates only current exact-head, verification, and review state for the MOPCON / Platform read-only Osiris case integration.

Earlier addenda, exact-head tests, reviews, and live observations remain historical evidence for the commits they name. This delta does not transfer verification across commits, authorize merge/deployment, apply database migrations, mutate customer state, or canonize implementation branches.

---

## 1. MOPCON current head

Repository: `mirrornode/mirrornode-operator-console`  
Draft PR: `#27`  
Branch: `feat/local-runtime-console-2026-08-31`  
Current exact head: `b9e788ac6e508973872013c09ced93b838d21c40`

State:

- open / draft / unmerged;
- current-head local type-check is **pending**;
- current head contains the bounded correction set from the exact-head Codex review of predecessor `de3e7c7b5de03d00c3213e5ec24372f89d72411e`.

### Latest independent-review findings and corrections

Codex reviewed exact predecessor `de3e7c7...` and reported 2 P1 + 2 P2 findings. Current head corrects all four:

1. **P1 — valid evidence binding required before APPROVE:** the Operator-recognized `[MOPCON EVIDENCE BINDING]` label is emitted only after the server parses and structurally validates the envelope and verifies its evidence SHA-256. Invalid/truncated bindings receive a distinct invalid label and remain non-approvable.
2. **P1 — approval-boundary value visible in bound review state:** the reviewable system-surface summary now includes validated `approval_boundary=true|false` metadata when present.
3. **P2 — session termination truth:** SIGN OUT redirects only after the session DELETE response is successful; failure is shown to the Operator and does not masquerade as logout.
4. **P2 — runtime-health timeout:** `/health` transport receives a bounded 4-second timeout when no caller signal is supplied, preventing stalled evidence capture from hanging indefinitely.

Earlier hardening remains intended: strict minimum case allowlisting, all-or-nothing malformed projection rejection, redirect rejection, HTTPS-only non-loopback case-reader transport, strict Osiris flow and masked-customer validation, stale-plan gate removal, truthful post-execution trace errors, reserved evidence-marker rejection, and exclusion of private customer rows from Oracle evidence envelopes.

### Verification lineage preserved

- `de3e7c7b5de03d00c3213e5ec24372f89d72411e` owns the latest reported clean local `npm run type-check` / `tsc --noEmit` evidence before this correction set.
- `fe63850aa1371126c159d3a64b044ee7b1db6fe2` owns the authenticated private-case E2E predecessor: unauthenticated `401`, Operator auth `200`, projection `available`, projected mutation state `disabled`, and three paid Osiris cases observed.

Neither predecessor result is represented as exact-head proof for `b9e788ac...`.

---

## 2. Platform current head

Repository: `mirrornode/mirrornode-platform`  
Draft PR: `#53`  
Branch: `feat/mopcon-readonly-case-projection-2026-08-31`  
Current exact head: `0ab0bd69266fb4831fcb89551acc3031702ab174`

State:

- open / draft / unmerged;
- current-head local route-test execution is **pending**;
- current head contains the bounded correction from the exact-head Codex review of predecessor `95e2fec8deec09f67e62d4eae8f9a0a7fbfa2542`, plus adversarial test coverage for that correction.

### Latest independent-review finding and correction

Codex reviewed exact predecessor `95e2fec...` and reported one P2 concurrency finding: a case observed actionable could transition terminal after the actionable scan but be too old to appear in the bounded latest-100 terminal history, leaving a stale actionable observation.

Current head corrects that condition by:

- retaining immutable UUID-keyset pagination for the initial actionable scan;
- querying bounded terminal history;
- then re-reading **every initially actionable case UUID** in bounded ID batches after the terminal query;
- requiring every collected actionable ID to be returned or failing closed;
- using that later ID recheck as the final observation for those cases;
- adding adversarial tests for a transitioned case outside the terminal-history cap and for sanitized recheck failures.

The checked-in additive UUID migration remains repository-only and has **not** been applied to production. The bearer-secret GET-only projection, server-side service-role confinement, minimum masked field set, sanitized errors, and no-mutation semantics remain intended invariants.

### Verification lineage preserved

- `95e2fec8deec09f67e62d4eae8f9a0a7fbfa2542` owns the latest reported clean current-route test evidence before this correction.
- `56bfd1d31b8a5964f5de870b59f5e8c3568b418b` owns prior route-test + Vercel-success evidence.
- `062ad630ad3c795dd27c2e84d251880b8c615c3f` owns the authenticated local production-ledger read-path evidence.
- `b78152011c81c4d4fa2d09a3c9f1c7e70f9fd78f` owns the earlier unauthenticated preview `401` / no-projection evidence.

Those predecessor results are not silently transferred to `0ab0bd69...`.

---

## 3. CORE-HUB source navigation correction

`CANONICAL_SOURCES.md` now routes current operational state to this verification delta first and retains the larger operational addendum as broader predecessor reconciliation.

This fixes the exact-head navigation ambiguity identified by Codex at predecessor CORE-HUB head `a2f8a7af157a99b321fd29916383191ea216faf5`.

The source-map correction does not create canonical precedence. `MASTER_INDEX.md` remains unchanged.

---

## 4. Live-case observation remains dated

The latest authenticated live-case observation remains predecessor E2E evidence:

- 3 paid Osiris cases total;
- 2 at `intake_complete`;
- 1 at `fulfillment_started`;
- derived customer-case Operator Debt at that observation: 2.

This delta does **not** re-attest that count or debt value at the current heads. A fresh current-head read-only E2E is still required before treating the distribution as current.

---

## 5. Current disposition

**MOPCON `b9e788ac...`: latest review findings corrected; exact-head local type-check pending; fresh exact-head independent review pending after local verification.**

**Platform `0ab0bd69...`: latest concurrency finding corrected with adversarial tests; exact-head local route test pending; fresh exact-head independent review pending after local verification.**

**CORE-HUB source navigation:** latest review finding corrected; final governance candidate head will require fresh exact-head review after the implementation verification anchors are bound.

**Projected mutation state remains designed as DISABLED. Customer mutation / fulfillment advancement / release / delivery remain NOT AUTHORIZED.**

**The Platform UUID migration remains checked in only and is NOT AUTHORIZED for production application by this record.**

**No implementation branch is authorized for merge or production promotion by this delta.**

**Canon status remains CANDIDATE ONLY.** Ordinary review or merge does not create canonical precedence; Ptah evaluation + explicit Operator ratification + promotion record remain required.
