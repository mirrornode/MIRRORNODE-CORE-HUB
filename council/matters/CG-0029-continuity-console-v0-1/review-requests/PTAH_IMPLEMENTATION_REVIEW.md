# Ptah Review Request — CG-0029

## Matter

**CG-0029 — Continuity Console v0.1 Definition**

## Role

Review implementation feasibility only. Do not ratify the product decision, rewrite the governing purpose, or infer Operator approval.

## Decision under review

Whether MIRRORNODE should implement a read-only `/continuity` route in `mirrornode-platform`, using a typed, build-generated, allowlisted snapshot and retaining all operational actions inside private MOPCON.

## Required sources

1. `docs/continuity/CONTINUITY_CONSOLE_V0_1_DEFINITION.md`
2. `apps/mirrornode-scorecard/`
3. `mirrornode-platform` current structure
4. `mirrornode-operator-console` PR #3 boundary
5. Council matter `CG-0029`

## Questions

1. Can Platform implement `/continuity` without importing the detached Vite scorecard application wholesale?
2. What is the smallest typed snapshot contract that supports:
   - current system,
   - active work,
   - council matters,
   - continuity record?
3. Where should the generated snapshot live in Platform?
4. What controlled script or build step should generate it?
5. How should generation failure behave so stale data is visible rather than silently refreshed or replaced?
6. Which scorecard components or patterns are reusable, and which should be rewritten for Next.js?
7. Can v0.1 avoid runtime GitHub credentials, request-time network calls, and cross-repository writes?
8. What tests are required before implementation is considered verified?
9. Are there any blockers that require revising the current definition?

## Required response shape

```markdown
# Ptah implementation review

## Stance
support | support-with-conditions | oppose | insufficient-evidence

## Feasibility finding

## Proposed file and route structure

## Minimal snapshot contract

## Generation and failure behavior

## Reuse versus rewrite

## Required tests

## Risks and blockers

## Requested definition changes

## Recommendation
```

## Attribution rule

Return the response as Ptah's own position. Preserve exact wording when it is registered under `positions/`; summaries belong only in synthesis.
