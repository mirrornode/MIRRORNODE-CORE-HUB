# Canonical Sources

## Current-state routing

For current operational truth, start with the Estate Worktree candidate on PR #63:

- `estate/README.md`
- `estate/repos.v1.json`
- `estate/surfaces.v1.json`
- `estate/roles.v1.json`
- `estate/workstreams.v1.json`
- `estate/CONSOLIDATION_SPINE_2026-09-06.md`
- `estate/MIRRORNODE_ENGINEERING_DOCTRINE_V1.md`

Until PR #63 is reviewed and promoted, these files are **candidate current-state controls**, not self-promoted canon. Historical documents remain evidence but must not override fresher verified state.

## Governance
`MIRRORNODE-CORE-HUB`

## Production / revenue platform
`mirrornode-platform`

## Production domain
`mirrornode.xyz`

## GitHub operations / proof-audit integration
`mirrornode-github-ops`

Current role: read-only GitHub Ops foundation and credibility/proof-audit lane. Mutation authority is not implied.

## Infrastructure / estate protection
`MIRRORNODE-INFRA`

Current role: estate protection, execution-entrypoint safety, and infrastructure verification.

## Operator surface
`mirrornode-operator-console`

Current broad expansion state: PARK unless first-dollar operation exposes a concrete visibility/control blocker.

## Backend / contract support
`mirrornode-backend`

## Cross-repo index
`mirrornode-index`

## Monorepo / orchestration root
`mirrornode`

## Agent runtime / symbolic support
`mirrornode-py`

Branch and authority status must be verified before modifying this repo because local checkout may be on a freeze branch.

## Reviewer / arbitration support
- `mirrornode-merlin` — arbitration/review support
- `mirrornode-theia` / `theia-core` — review/verifier support
- `mirrornode-osiris` / `osiris-audit` — audit/review support

Presence does not itself grant runtime, governance, merge, deployment, migration, or live-mutation authority.

## Deprecated / historical Vercel surface
`mirrornode-hub`

`mirrornode-hub` is not the production deployment target. Do not treat it as the live platform surface unless new provider verification supersedes this record.

## Provider data planes

Provider/project identity and lifecycle state are tracked in `estate/surfaces.v1.json`.

Current high-value observations include:
- Supabase `Mirrornode OS` — ACTIVE production data plane.
- Supabase `mirrornode-schema-reconciliation-replay` — VERIFY/test-replay surface.
- Vercel `inphase` team — project census in progress; project existence does not prove production authority.
- Stripe `Mirrornode` live account — ACTIVE payment surface; test sandbox retained separately.

## Rule

If a downstream tool, model, dashboard, provider badge, or historical document claims a different current source:
1. identify the exact subject;
2. verify repository/provider/database state;
3. preserve UNKNOWN when evidence is incomplete;
4. update the current-state register rather than rewriting reality to match documentation.
