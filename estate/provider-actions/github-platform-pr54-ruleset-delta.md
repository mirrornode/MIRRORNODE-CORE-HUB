# GitHub Provider Action — mirrornode-platform PR #54 Ruleset Delta

Status: OPERATOR AUTHORIZED / PROVIDER WRITE PENDING

Observed repository:
`mirrornode/mirrornode-platform`

Observed ruleset:
- name: `MIRRORNODE Baseline Main Protection`
- ruleset id: `21815948`
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

Re-read the live ruleset and require:

```text
required_approving_review_count = 0
require_last_push_approval       = false

dismiss_stale_reviews_on_push    = true
required_review_thread_resolution = true
require_extra_approval_for_unattributed_changes = true
allowed_merge_methods            = [squash]
deletion protection              = present
non-fast-forward protection      = present
required linear history          = present
bypass actors                    = none
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

Before merge, re-read PR metadata and exact head. If the head differs, STOP as STALE_HEAD.

## Authority boundary

This authorization covers:
1. the two-field ruleset correction above;
2. verification that unrelated protections remain intact;
3. merge of PR #54 at the exact cleared head if and only if the provider rule no longer blocks it.

It does not authorize deployment, hosted Supabase migration, Vercel mutation, secret/config changes, or live customer-case mutation.

## Execution limitation recorded 2026-09-06

The current connected GitHub action surface exposes ruleset reads but not an administrative ruleset-write operation. The active execution environment also does not expose an authenticated `gh` CLI.

Therefore the provider write cannot be truthfully claimed complete from this session. All other preparatory and verification state is retained here so the remaining administrative action is narrow and auditable.
