# MIRRORNODE Estate Worktree v0.1

Status: DRAFT — candidate continuity/control surface. Not canonical until reviewed and merged through the normal Operator gate.

## Purpose

Prevent cross-repository and cross-head ambiguity between MIRRORNODE nodes.

The work-subject identity is never a PR number by itself. The minimum executable identity is:

```
repository_full_name
pull_request_number
branch
exact_head_sha
```

Canonical shorthand:

```
<owner>/<repo>#<pr>@<exact-head-sha>
```

Example:

```
mirrornode/mirrornode-platform#54@44368a27942dd8cee88e467024f01f298a89866d
```

## Layout

- `repos.v1.json` — current repository inventory from GitHub; machine-readable.
- `NODE_CHECKIN_CONTRACT.md` — mandatory node preflight/check-off rules.
- `work/<repo>/pr-<n>/subject.v1.json` — exact active work subject.
- GitHub issue "Estate Worktree — Active Subjects" — interactive human/node checklist.

## Exact-head rule

A node review/check is valid only for the exact subject it names.

When a PR head changes:
1. previous exact-head checks become stale for execution;
2. the subject record moves to the new head;
3. nodes re-check against the new immutable subject;
4. predecessor evidence may be retained only when explicitly labeled dated/content-scoped.

## Authority

This tree records identity, state, and evidence. It does not grant merge, deployment, migration, customer mutation, secret, or governance authority.
