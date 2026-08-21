# Intersection-to-Authority Boundary v0.1

**Status:** PROPOSAL / REVIEW REQUIRED

## Purpose

Define a hard separation between learned collaboration state and executable authority in the MOPCON Triad architecture.

## Core invariant

**Intersection history may change attention, routing, prompting, scrutiny, and synthesis posture. It may not change authority.**

No calibration history, productive pairing, deference pattern, trust history, confidence score, historical success rate, or Operator preference trace may directly or indirectly grant:

- merge rights;
- secret or credential access;
- execution privilege;
- irreversible-action privilege;
- permission expansion;
- authority-class reduction;
- bypass standing;
- lower review requirements.

## Object boundary

### Intersection Record

Descriptive relational state. May influence:

- which lane should inspect first;
- which node should be asked to challenge a proposal;
- which semantic ambiguity deserves extra clarification;
- which evidence form may be more persuasive;
- where additional scrutiny is warranted;
- how a synthesis should preserve known disagreement patterns.

It carries `authority_effect: NONE`.

### Deliberation Graph

Records claims, challenges, revisions, deferrals, dissent, evidence requests, and synthesis. It preserves the reasoning path and disagreement history.

It carries `authority_effect: NONE`.

### Authority Envelope

The only object in this three-object set that may represent permissions or execution eligibility. It must be independently grounded in explicit Operator authorization and the governing approval/delegation contracts.

The Authority Envelope must not be derived from an Intersection Record. The schema therefore fixes:

- `derived_from_intersection: false`
- `intersection_may_modify: false`

## Hidden reputation-engine prohibition

The system must not maintain or infer a hidden scalar such as "trust score," "node rank," "winning rate," or "authority confidence" that automatically alters permissions or approval thresholds.

Historical performance may be used as descriptive calibration evidence, but any routing or scrutiny adjustment it causes must remain inspectable and must not reduce an existing authority/security requirement.

Examples:

- "Perplexity often catches standards drift" may route a standards check to Perplexity earlier.
- "Claude has historically found specification ambiguity" may increase the probability that Claude receives a challenge request.
- "THEIA has successfully integrated prior packets" may support coordination assignment.

None of those observations may authorize a merge, waive a review, expose a secret, lower a risk class, or increase execution privilege.

## Deference rule

A node may defer on analysis when another lane has stronger domain evidence. Deference means "I add no material objection within my scope." It does not transfer the deferring node's authority, satisfy an independent-review requirement unless policy explicitly allows abstention, or erase unresolved security/governance objections.

## Dissent rule

Dissent survives synthesis until explicitly resolved, superseded by new evidence, or dispositioned by the applicable authority. Majority support does not extinguish a security or authority objection.

## UI consequence

MOPCON must visually separate:

1. **relationship intelligence** — what the system has learned about collaboration;
2. **deliberative state** — what the nodes currently think and why;
3. **authority state** — what is actually authorized and under which contract.

These may appear adjacent, but must not be visually collapsed into one confidence/permission indicator.

## Audit consequence

Any action that changes authority must cite its Authority Envelope and governing authorization record. An Intersection Record or Deliberation Graph may be cited as context, never as the authority source.
