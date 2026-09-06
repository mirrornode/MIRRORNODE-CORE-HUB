# MIRRORNODE Estate Worktree v0.1

Status: DRAFT — candidate continuity/control surface. Not canonical until reviewed and merged through the normal Operator gate.

## Purpose

Prevent cross-repository, cross-head, cross-provider, and cross-role ambiguity between MIRRORNODE nodes.

The work-subject identity is never a PR number by itself.

Minimum executable identity:

```text
repository_full_name
pull_request_number (when applicable)
source_branch
execution_worktree_branch (when different)
exact_head_sha
base_sha (when material)
```

Canonical shorthand:

```text
<owner>/<repo>#<pr>@<exact-head-sha>
```

## Layout

- `repos.v1.json` — current repository census, lifecycle disposition, owner seat, and verification state.
- `surfaces.v1.json` — current cloud/provider/database/payment/local-surface register.
- `roles.v1.json` — current candidate operating seats and authority boundaries.
- `workstreams.v1.json` — ACTIVE and PARK work with restart conditions and no-hidden-work rule.
- `NODE_CHECKIN_CONTRACT.md` — mandatory node preflight/check-off rules.
- `MIRRORNODE_ENGINEERING_DOCTRINE_V1.md` — candidate code/design discipline.
- `CONSOLIDATION_SPINE_2026-09-06.md` — dated cleanup/revenue/continuity register.
- `provider-actions/` — bounded provider-admin deltas that are authorized but not yet executed or verified.
- `work/<repo>/pr-<n>/subject.v1.json` — exact active work subject.
- GitHub issue **Estate Worktree — Active Subjects** — interactive human/node checklist.

## Current-state routing

For current operational questions, start here rather than with older narrative dossiers.

Historical material remains evidence but does not override fresher exact-subject/provider observations.

## Exact-head rule

A node review/check is valid only for the exact subject it names.

When a PR head changes:
1. previous exact-head checks become stale for execution;
2. the subject record advances to the new head;
3. nodes re-check against the new immutable subject;
4. predecessor evidence remains only when explicitly labeled dated/content-scoped.

## No hidden work

No ACTIVE work exists without:

```text
domain
owner_seat
exact_subject
next_evidence_producing_action
```

Anything else is classified SUPPORT, VERIFY, PARK, SUPERSEDE, RETIRE, or EXPERIMENTAL.

## Authority

This tree records identity, state, evidence, ownership, and disposition.

It does not itself grant merge, deployment, hosted migration, customer mutation, secret, provider-admin, or governance authority.
