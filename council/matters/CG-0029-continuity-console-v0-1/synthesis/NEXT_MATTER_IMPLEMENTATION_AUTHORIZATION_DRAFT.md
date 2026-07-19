# Draft — Continuity Console v0.1 Implementation Authorization Matter

**Status:** Preparation only  
**Matter ID:** To be assigned after PR #29 merges  
**Authority effect:** None

## Proposed decision question

Should the Operator authorize a bounded implementation of Continuity Console v0.1 in `mirrornode-platform` under the revised and confirmed definition recorded by CG-0029?

## Proposed authorized scope

- create a dedicated implementation branch in `mirrornode-platform`,
- implement the static `/continuity` route,
- implement the strict snapshot contract and validation schema,
- implement checked-in source, field, path, enum, evidence-origin, and redirect allowlists,
- implement separate `continuity:generate` and `continuity:validate` commands,
- add safe fixtures containing no production or private records,
- implement stale, partial, disputed, corrected, withdrawn, and unavailable rendering,
- implement retained-valid-artifact failure behavior,
- implement public-history limits and non-enumerable identifiers,
- add automated tests and completed-build disclosure scanning,
- produce local verification evidence for review.

## Proposed prohibited scope

- generating or publishing a populated production snapshot,
- deploying the route to production,
- exposing private MOPCON or runtime data,
- ingesting email, calendar, finance, customer, audit, or personal data,
- request-time GitHub or private-system access,
- cross-repository writes,
- autonomous Council transitions or Operator decisions,
- publication authorization,
- changing MOPCON or the agent runtime.

## Required evidence before implementation completion

- strict schema and unknown-field rejection tests,
- allowlist enforcement tests,
- freshness-window and rendering-time recalculation tests,
- generation failure and atomic-retention tests,
- no-valid-artifact production-build failure test,
- partial and unavailable section tests,
- disputed, corrected, withdrawn, and tombstone tests,
- Council workflow/disposition separation tests,
- built-output scan for prohibited fields, URLs, identifiers, and private data,
- type-check, lint, test, accessibility, responsive, and production-build results,
- repository diff inspection,
- confirmation that fixtures contain no private or production records.

## Proposed required reviews

- Ptah — implementation feasibility and evidence completeness,
- Osiris — disclosure boundary and deployable-artifact inspection,
- Theia — synthesis and authority-boundary confirmation.

## Proposed disposition boundary

Implementation authorization would permit code and local verification only.

It would not authorize:

- populated-snapshot generation from real sources,
- production deployment,
- public publication,
- any private-data projection.

A separate disclosure review and Operator publication decision would remain mandatory.
