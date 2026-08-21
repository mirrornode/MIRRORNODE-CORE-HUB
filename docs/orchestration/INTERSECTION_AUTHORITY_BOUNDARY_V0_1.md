# Intersection-to-Authority Boundary v0.1

**Status:** PROPOSAL / REVIEW REQUIRED

## Purpose

Define a hard separation between learned collaboration state and executable authority in the MOPCON Triad architecture.

## Core invariant

**Intersection history may change attention, routing, prompting, scrutiny, and synthesis posture. It may not change authority.**

No calibration history, productive pairing, deference pattern, trust history, confidence score, historical success rate, or Operator preference trace may directly or indirectly grant merge rights, secret or credential access, execution privilege, irreversible-action privilege, permission expansion, authority-class reduction, bypass standing, or lower review requirements.

## Object boundary

### Intersection Record

Descriptive relational state. It may influence routing, challenge selection, semantic clarification, evidence presentation, additional scrutiny, and synthesis posture. It carries `authority_effect: NONE`.

### Deliberation Graph

Records claims, challenges, revisions, deferrals, dissent, evidence requests, and synthesis. It preserves the reasoning path and disagreement history. It carries `authority_effect: NONE`.

### Authority Envelope

The only object in this three-object set that may represent permissions or execution eligibility. It must be independently grounded in explicit Operator authorization and the governing approval/delegation contracts.

The Authority Envelope must not be derived from an Intersection Record. The schema fixes `derived_from_intersection: false` and `intersection_may_modify: false`.

## Information-flow allowlist

Downstream components may consume Intersection Record fields only for:

- routing;
- prompting/context selection;
- scrutiny escalation;
- synthesis presentation or challenge selection.

They may not consume Intersection Record fields to lower risk, reduce reviewer cardinality, satisfy independence, alter quorum, grant credentials, alter platform permissions, or mark an Authority Envelope satisfied.

An execution gate must not consume Deliberation Graph convergence, consensus, deference, confidence, or synthesis as a substitute for any Authority Envelope requirement.

If a downstream component cannot prove that its use of relational/deliberative state falls within this allowlist, the use is non-conformant and must fail closed.

## Hidden reputation-engine prohibition

The system must not maintain or infer a hidden scalar such as `trust score`, `node rank`, `winning rate`, or `authority confidence` that automatically alters permissions or approval thresholds.

Historical performance may be descriptive calibration evidence, but any routing or scrutiny adjustment it causes must remain inspectable and must not reduce an existing authority/security requirement.

Examples: recurring standards-drift catches may route standards review earlier; recurring specification-ambiguity catches may increase challenge selection; successful integration history may support coordination assignment. None may authorize a merge, waive a review, expose a secret, lower a risk class, or increase execution privilege.

## Deference rule

A node may defer on analysis when another lane has stronger domain evidence. Deference means `I add no material objection within my stated scope`.

Machine invariants:

- deference contributes to synthesis posture only;
- deference does not count toward quorum;
- deference does not satisfy reviewer cardinality or independence requirements;
- every deference records actor, `defer_to`, scope, confidence, and timestamp;
- deference does not transfer authority or erase unresolved security/governance objections.

## Dissent persistence rule

Dissent survives synthesis until explicitly resolved, superseded by new evidence, or dispositioned by the applicable authority. Majority support does not extinguish a security or authority objection.

Surviving dissent must remain addressable through persistence and receipt generation. A synthesis or execution receipt that omits still-live dissent is non-conformant.

## UI anti-collapse rule

MOPCON must visually separate:

1. **relationship intelligence** — what the system has learned about collaboration;
2. **deliberative state** — what the nodes currently think and why;
3. **authority state** — what is actually authorized and under which contract.

No UI aggregate score, badge, color, confidence value, or status may mathematically or semantically blend relational trust, deliberative convergence, and authority eligibility into one indicator.

These states may appear adjacent, but authority eligibility must be rendered from Authority Envelope/governing-contract state alone.

## Audit consequence

Any action that changes authority must cite its Authority Envelope and governing authorization record. An Intersection Record or Deliberation Graph may be cited as context, never as the authority source.

Audit and test suites should verify information flow, not merely schema shape: a structurally non-authoritative field becomes a security defect if a downstream consumer translates it into permission.
