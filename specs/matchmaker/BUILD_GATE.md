# Matchmaker Build Gate

Status: proposed  
Lane: Resonance Matchmaker  
Repository: MIRRORNODE-CORE-HUB  
Depends on: specs/matchmaker/PREFLIGHT.md  
Implementation repository: not yet authorized  
Platform code changes: blocked until this gate lands

## Purpose

This document defines the first implementation boundary for Matchmaker.

The goal is to authorize a minimal, private, internal surface for structured intake and evaluation without creating public claims, hidden scoring, sensitive profiling, or automated authority.

## Authorized First Surface

The first Matchmaker implementation may be:

- a private internal intake/evaluation page or route
- accessible only to the Operator or explicitly authorized maintainers
- structured around declared inputs, visible constraints, and reviewable outputs
- non-public
- non-autonomous
- non-final

## First Surface Must Capture

Each evaluation must declare:

- request source
- matching objective
- available evidence
- explicit constraints
- disallowed inference zones
- output type requested
- review authority
- recommended next step

## First Surface May Output

The first surface may output:

- match category
- confidence level
- supporting evidence
- missing information
- disqualifying concerns
- recommended next step
- review gate

## First Surface Must Not Output

The first surface must not output:

- hidden psychological labels
- spiritual claims
- medical, legal, or political inferences
- intimate or protected-attribute assumptions
- permanent social ranking
- irreversible access decisions
- claims that override Operator, Theia, THOTH, or security review

## Storage Boundary

Until a separate storage decision is approved, Matchmaker output must be treated as ephemeral.

No persistent sensitive profiles are authorized by this gate.

Allowed storage for the first implementation:

- source-controlled interface code
- non-sensitive test fixtures
- local/manual review notes outside production data paths

Blocked storage:

- permanent user profiles
- inferred traits
- collaborator rankings
- sensitive personal data
- automated trust scores

## Security Boundary

The first implementation must not read private repositories, email, calendar, customer records, payment records, or uploaded files unless a later document explicitly grants that access.

The first implementation may only use:

- manually entered text
- explicit operator-provided context
- non-sensitive test examples

## Review Boundary

The first implementation must label every output as advisory.

Any recommendation involving access, responsibility, covenant, customer fit, or security must pass through human review.

## Recommended Implementation Target

After this build gate lands, open a separate branch in `mirrornode-platform` for a private internal prototype.

Recommended target:

- `/internal/matchmaker`
- protected route or local-only prototype
- form-based intake
- deterministic output shape
- no database writes
- no public navigation link

## Acceptance Criteria

This build gate is complete when:

- this document lands on `main`
- @mirror records the build-gate approval
- platform implementation remains blocked until a new implementation branch is opened
- first implementation target is named
- storage, security, and review boundaries are explicit
