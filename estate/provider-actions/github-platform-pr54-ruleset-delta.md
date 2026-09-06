# GitHub Provider Action — mirrornode-platform PR #54 Ruleset Delta

Status: EXECUTED / VERIFIED / PR #54 MERGED

Observed repository:
`mirrornode/mirrornode-platform`

Observed ruleset:
- name: `MIRRORNODE Baseline Main Protection`
- target: default branch
- enforcement: active

Observed pull-request rule parameters before correction:

```text
required_approving_review_count = 1
dismiss_stale_reviews_on_push   = true
required_reviewers              = []
require_code_owner_review       = false
require_last_push_approval      = true
required_review_thread_resolution = true
require_extra_approval_for_unattributed_changes = true
allowed_merge_methods           = [squash]
```

Other active rules observed:
- deletion protection
- non-fast-forward protection
- required linear history

Bypass actors observed: none.

## Authorized bounded delta

Change only:

```text
required_approving_review_count: 1 -> 0
require_last_push_approval:      true -> false
```

Preserve every other observed rule and parameter exactly.

## Rationale

The previous rule encoded a multi-human staffing assumption that the current single-Operator organization cannot satisfy honestly.

The replacement preserves separation of functions through:
- exact-head CI;
- Canon Gate;
- domain-specific proof;
- read-only independent review seats;
- explicit Operator disposition;
- no automatic merge/deploy/migration authority.

This is a policy-model correction, not a blanket weakening of repository protection.

## Verification after provider write

Exact provider identifiers are intentionally resolved live through GitHub and are not persisted in this public governance repository.

Re-read the live ruleset and require every preserved field:

```text
target                            = branch
enforcement                       = active
conditions.ref_name.include       = [~DEFAULT_BRANCH]
conditions.ref_name.exclude       = []

required_approving_review_count   = 0
dismiss_stale_reviews_on_push     = true
required_reviewers                = []
require_code_owner_review         = false
require_last_push_approval        = false
required_review_thread_resolution = true
require_extra_approval_for_unattributed_changes = true
allowed_merge_methods             = [squash]

deletion protection               = present
non-fast-forward protection       = present
required linear history           = present
bypass actors                     = none
current user bypass               = never
```

If any preserved field changes unexpectedly, STOP and classify the provider state as HOLD.

## PR #54 merge subject after successful verification

```text
repo: mirrornode/mirrornode-platform
PR: #54
source branch: feat/osiris-controlled-fulfillment-start-v1
expected head: f9365b801ecf0fdb7c4bb94758a5d7e99e334d31
merge method: squash
```

Before merge:
1. re-read PR metadata and exact head; if the head differs, STOP as STALE_HEAD;
2. require the Estate subject record for this exact head to show the fresh independent successor-head review as CLEAR_FOR_OPERATOR_DISPOSITION;
3. require no unresolved material exact-head review finding;
4. require Operator MERGE authorization for this exact subject.

The current successor-head Perplexity reconciliation is recorded in `estate/work/mirrornode-platform/pr-54/subject.v1.json` as review evidence. It is not a GitHub approval and must not be represented as one.

## Authority boundary

This authorization covers:
1. the two-field ruleset correction above;
2. verification that unrelated protections remain intact;
3. merge of PR #54 at the exact cleared head if and only if the provider rule no longer blocks it **and** the exact-head final-review/Operator prerequisites above remain satisfied.

It does not authorize deployment, hosted Supabase migration, Vercel mutation, secret/config changes, or live customer-case mutation.

## Execution receipt — 2026-09-06

Provider write was performed manually by the Operator and independently re-read through the connected GitHub API surface.

Verification result: PASS. Only the two authorized pull-request parameters changed; all preserved fields above remained intact.

PR #54 was then squash-merged at exact reviewed head:

```text
source head: f9365b801ecf0fdb7c4bb94758a5d7e99e334d31
merge commit: f68111bdd3b851350ce60efae55cd80df84e9458
main head after merge: f68111bdd3b851350ce60efae55cd80df84e9458
```

No deployment, hosted migration, Vercel mutation, secret/config change, or live customer-case mutation was performed.

## Prior execution limitation recorded 2026-09-06

The current connected GitHub action surface exposes ruleset reads but not an administrative ruleset-write operation. The active execution environment also does not expose an authenticated `gh` CLI.

That limitation applied before the Operator completed the provider-admin write manually. The subsequent live re-read and merge receipt above supersede that pending state.
