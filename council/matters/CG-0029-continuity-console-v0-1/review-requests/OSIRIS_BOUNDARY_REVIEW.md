# Osiris Review Request — CG-0029

## Matter

**CG-0029 — Continuity Console v0.1 Definition**

## Role

Review privacy, authority, freshness, disclosure, and failure boundaries. Do not ratify the product decision or perform implementation design beyond what is necessary to identify risk.

## Decision under review

Whether MIRRORNODE should implement a public, read-only `/continuity` route from a typed, build-generated, allowlisted snapshot while retaining all private operational actions inside MOPCON.

## Required sources

1. `docs/continuity/CONTINUITY_CONSOLE_V0_1_DEFINITION.md`
2. `apps/mirrornode-scorecard/`
3. `mirrornode-platform` public-orientation boundary
4. `mirrornode-operator-console` PR #3
5. Council matter `CG-0029`

## Questions

1. Could any proposed field reveal private operational state, internal topology, customer data, secrets, or sensitive workflow details?
2. Does the freshness model prevent old verification from appearing live?
3. Does `source-verified` risk implying that the underlying system, decision, or product is approved?
4. Are public GitHub links, evidence links, and Council matter summaries safe by default?
5. Could an `Operator action required` label leak the existence or nature of a sensitive action?
6. What should the page display when generation fails, sources disagree, or only part of the snapshot is current?
7. What data must be explicitly prohibited from the build artifact?
8. What abuse, scraping, inference, or enumeration risks arise from a public continuity history?
9. Are corrections and disputed records handled safely without silently rewriting history?
10. What conditions must be satisfied before public deployment?

## Required response shape

```markdown
# Osiris boundary review

## Stance
support | support-with-conditions | oppose | insufficient-evidence

## Boundary finding

## Public-data risks

## Freshness and authority risks

## Failure and disagreement behavior

## Explicitly prohibited fields

## Deployment conditions

## Requested definition changes

## Recommendation
```

## Attribution rule

Return the response as Osiris's own position. Preserve exact wording when it is registered under `positions/`; summaries belong only in synthesis.
