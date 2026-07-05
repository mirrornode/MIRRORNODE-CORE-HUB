# CANON_TO_PLATFORM_PROMOTION_BOUNDARY_v0_1

Status: Draft
Authority Class: Governance Boundary
Canonical Home: MIRRORNODE-CORE-HUB
Applies To:
- MIRRORNODE-CORE-HUB
- mirrornode-platform
- any downstream execution repository inheriting MIRRORNODE canon
Oversight:
- Theia: boundary review and governance coherence
- Ptah / Operator: promotion authority
- execution surfaces: implementation only after valid promotion

## Purpose

Define the minimum valid boundary between canon and execution so that no platform surface,
repository, deployment, interface, schema, automation path, or payment-capable flow
claims authority it has not been explicitly granted.

This document exists to prevent drift between:
- ratified governance and platform behavior
- canonical definitions and implementation assumptions
- approved release lanes and ungoverned scope expansion

## Authority Rule

MIRRORNODE-CORE-HUB is the canonical authority for governance, canon, schemas,
and promotion registration.

mirrornode-platform is an execution monorepo and operational surface. It does not
originate canon authority. It may only inherit, implement, or operationalize authority
that has been explicitly defined and promoted from CORE-HUB.

No runtime surface, deployable artifact, README, configuration file, API contract,
or product claim may represent itself as canonical unless that status is explicitly
recorded in CORE-HUB.

## Promotion Boundary

A concept, rule, schema, flow, interface, or release lane crosses from canon into
platform only when all of the following are true:

1. The source artifact exists in CORE-HUB.
2. The artifact states enough authority and boundary language to be implementable.
3. The intended execution target is named.
4. The promotion purpose is named.
5. The promotion is recorded in a reviewable way.
6. The responsible authority has not placed the item on hold.

If any one of these conditions is missing, the item remains non-promoted and must
not be treated as implementation authority.

## What May Be Promoted

The following may be promoted from CORE-HUB into execution surfaces:
- ratified governance rules
- approved schemas and interface contracts
- explicit release-lane definitions
- approved authority matrices
- approved risk handling requirements
- bounded implementation directives tied to a named execution surface

The following may not be promoted by implication alone:
- aspirational architecture language
- naming experiments
- narrative positioning
- partial seat concepts without manifest authority
- draft ideas not marked for implementation
- broad product assumptions inferred from discussion

## Promotion Record Requirements

Every valid promotion from canon to platform should include:

- source artifact name
- source version
- source repository
- target repository or execution surface
- promotion intent
- scope included
- scope excluded
- approving authority
- review date
- implementation status
- rollback or invalidation condition

A promotion lacking any of the above is incomplete and should be treated as draft,
unless explicitly waived by Ptah / Operator.

## Execution Constraints

Execution surfaces may:
- implement explicitly promoted artifacts
- create local implementation details that do not alter canon
- add operational notes, tests, adapters, and deployment mechanics consistent with canon

Execution surfaces may not:
- redefine authority
- promote themselves to canonical status
- widen scope beyond the promoted lane
- convert draft concepts into implied requirements
- bypass boundary review for money-touching or public-facing behavior
- silently alter schema meaning, governance meaning, or release criteria

## Public and Money-Touching Rule

Any feature that is:
- publicly exposed,
- payment-capable,
- customer-facing,
- record-creating,
- identity-bearing,
- or likely to be interpreted as an official MIRRORNODE capability

requires explicit promotion boundary review before launch and should not rely on
implementation inference alone.

Implementation work may begin earlier only if:
- the promoted slice is already defined,
- launch remains unauthorized,
- and the work does not widen the approved lane.

## Draft vs Ratified Material

Draft artifacts may inform discussion and planning.
Draft artifacts do not grant implementation authority by themselves.

Ratified or explicitly approved artifacts may grant implementation authority,
but only within the named scope and only for the named target surface.

Anything not explicitly promoted remains out of scope for enforcement,
launch claims, or dependency assumptions.

## Boundary Failure Conditions

A boundary failure exists when any of the following occur:
- platform documentation claims canon authority
- implementation assumes approval that is not recorded
- public behavior exceeds promoted scope
- payment or release behavior appears before boundary review
- schemas or interfaces drift from ratified meaning
- repositories disagree about which surface is authoritative

Boundary failures should trigger:

1. Hold on promotion-dependent work.
2. Review by Theia.
3. Correction or downgrade.
4. Re-clearance before continuation.

## Minimum Artifact Pair for First-Dollar Work

Before first-dollar platform work is treated as clean, the following pair must exist
in CORE-HUB:

- FIRST_DOLLAR_RELEASE_LANE_v0_1.md
- CANON_TO_PLATFORM_PROMOTION_BOUNDARY_v0_1.md

A deferred risk register should also exist before launch review, and preferably
before build expansion.

## Review Cadence

This boundary document should be reviewed when:
- a new release lane is proposed
- a new execution repo is introduced
- a public surface changes authority posture
- a payment flow is added or materially changed
- a schema begins driving runtime behavior
- an agent or seat moves from draft into active operational role

## Initial Operating Interpretation

Until superseded:
- CORE-HUB is canonical
- mirrornode-platform is execution-only
- first-dollar work must remain narrow
- public launch authority is separate from build authority
- no repo may claim authority by convenience, recency, or implementation momentum
