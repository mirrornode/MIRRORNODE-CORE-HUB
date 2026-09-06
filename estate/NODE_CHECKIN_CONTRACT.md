# Node Check-in Contract v0.1

Every MIRRORNODE node must resolve and state its work subject before analysis, review, or mutation.

## Required preflight

A node must report:

```text
NODE:
REPOSITORY:
PR: <number> | N/A
BRANCH:
EXACT_HEAD:
MODE: inspect | review | execute
```

For PR-backed work, PR must resolve to a number. For non-PR branch/provider/local work, use `PR: N/A` and bind the subject to the repository/surface + branch or provider object + exact immutable revision/config identity when one exists.

If a required identity field for the applicable subject type is unresolved, the node must stop execution and resolve identity first.

## Subject identity invariant

Never treat `PR #N` as sufficient identity.

For PR-backed work, the executable key is:

```
repository_full_name + PR number + branch + exact head SHA
```

For non-PR work, use:

```
repository_or_provider_surface + PR:N/A + branch/config identity + exact revision when available
```

Examples include a branch-only maintenance subject, a Vercel/Supabase provider inspection, or a local-machine census receipt.

## Check-off states

Use only:

- `PENDING`
- `IN_PROGRESS`
- `UNKNOWN`
- `CLEAR`
- `CORRECTION_REQUIRED`
- `BLOCKED`
- `STALE_HEAD`

A node check-off must name the exact head it inspected.

## Head-change invalidation

If the live PR head differs from the checked head, the prior check becomes `STALE_HEAD` for execution purposes.

Do not silently transfer:
- CI clearance,
- review clearance,
- database evidence,
- security evidence,
- exact-head claims,
- Operator approval.

Content-scoped predecessor evidence may be cited only when its older head and bounded relevance are explicit.

## Interactive check-off

The companion GitHub issue is the immediate interactive surface.

A node with GitHub write access may update its checkbox or post a structured receipt. A node without write access must return this receipt for Operator/Copilot recording:

```text
NODE_CHECKIN
node:
subject:
head:
state:
evidence:
remaining_findings:
authority_effect:
```

## No authority inference

Presence in the tree or a checked box proves only the recorded step. It does not authorize merge, deployment, migration application, live-case mutation, secret access, or authority expansion.
