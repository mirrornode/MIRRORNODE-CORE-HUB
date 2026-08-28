# INTER / OUTER Post-Merge Correction Record — 2026-08-28

## Status

**CORRECTION PREPARED / EXACT-HEAD REVIEW REQUIRED / NOT YET RATIFIED**

This record corrects three P2 findings returned after PR #58 had already merged. The original merge remains part of repository history; this successor change does not rewrite or erase that event.

## Affected merged subject

- PR #58 — `docs: add paired INTER / OUTER operating constitution v0.1`
- reviewed source head: `ed3c62d44f7dc2b57c2b976eabce60c9dde2edff`
- merged `main` commit: `401a7b49b72be441947ac374af933614413fb46f`

## Corrective findings

### P2-1 — RSR-1 workflow scope

The original RSR-1 procedure said all configured workflows must execute and pass. That was too broad because a recovery event may not be capable of triggering every required workflow.

**Correction:** RSR-1 now requires every policy-required workflow/check that is eligible for the recovery event and exact subject to execute and pass. Required but event-ineligible checks must use their own supported trigger or remain HOLD. RSR-1 cannot manufacture success for an ineligible workflow.

### P2-2 — Amendment authority

The original amendment language allowed a reviewed documentation change to appear sufficient to amend INTER/OUTER, which could bypass an existing constitutional ratification path.

**Correction:** documentation review is necessary evidence but not ratification. Amendments must follow the then-current applicable governance path, including Ptah evaluation, explicit Operator ratification, Council review, or another named authority step where governing canon requires it.

### P2-3 — Fresh review after reconciliation changes the head

The original human command sequence required checks after material changes but did not explicitly require a fresh independent review when reconciliation or correction produced a successor head.

**Correction:** any material change that alters the exact subject/head loops the sequence back through required exact-target checks and fresh independent exact-target review. Ancestor review does not clear a changed head.

## Non-grants

This corrective record and its companion edits do not grant constitutional standing, registry membership, dispatch authority, merge authority, repository permissions, or autonomous execution authority.

## Closure condition

The correction is eligible to close the post-merge P2 incident only after:

1. repository checks pass on the exact successor head;
2. independent review explicitly names and reviews that exact successor head;
3. no unresolved P1/P2 finding remains in the correction scope;
4. any required governance/ratification step is completed before the amended manual/charter is treated as ratified.

PR #4 / Repo Steward remains a separate HOLD and is not cleared by this correction.
