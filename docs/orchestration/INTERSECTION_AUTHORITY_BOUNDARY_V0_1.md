# Intersection-to-Authority Boundary v0.1

**Status:** PROPOSAL / REVIEW REQUIRED

## Purpose

Define a hard separation between learned collaboration state and executable authority in the MOPCON Triad architecture.

## Core invariant

**Intersection history may change attention, non-authority task routing, ordinary prompting, scrutiny, and synthesis posture. It may not change authority-bearing reviewer/attester selection or authority-bearing prompt context.**

No calibration history, productive pairing, deference pattern, trust history, confidence score, historical success rate, or Operator preference trace may directly or indirectly grant merge rights, secret or credential access, execution privilege, irreversible-action privilege, permission expansion, authority-class reduction, bypass standing, lower review requirements, reviewer selection, or attester selection.

## Object boundary

### Intersection Record

Descriptive relational state. It may influence non-independent work routing, challenge selection, semantic clarification, evidence presentation, additional scrutiny, and synthesis posture. It carries `authority_effect: NONE` and `non_authority_taint: true`.

### Deliberation Graph

Records claims, challenges, revisions, deferrals, dissent, evidence requests, and synthesis. It preserves the reasoning path and disagreement history. It carries `authority_effect: NONE`.

### Authority Envelope

The only object in this set that may represent execution eligibility or permission state. It must be independently grounded in explicit Operator authorization and governing approval/delegation contracts. It must not be derived from or modified by Intersection state.

### Authority Decision Record

Binds an Authority Envelope to exact target state, routing provenance, admissible authority sources, platform state, digest, decision, dissent status, and execution-attempt state. It records why an action was considered eligible or blocked; it does not itself create authority.

## Reviewer and attester selection boundary

Intersection-derived values are forbidden inputs to selection of any reviewer or attester whose output can satisfy or block an Authority Envelope requirement.

The Authority Decision Record must carry routing provenance that includes:

- selection-function reference;
- selected reviewers and attesters;
- independence evidence;
- `intersection_input_used: false`.

Independence is evaluated against the selection process and influence path, not merely the names on the resulting roster.

## Authority-bearing prompt isolation

Any review or attestation capable of satisfying or blocking an Authority Envelope requirement must use a canon-pinned prompt/template or equivalent governed instruction set that excludes Intersection-derived context and excludes the Deliberation Graph before the independent pass.

The attestation must bind:

- exact target reference/state hash;
- prompt template hash;
- concrete issuer identity;
- model/runtime identity;
- evidence inputs;
- session/job identity where available;
- issue and expiry timestamps;
- implementer-independence basis.

Prompt/context selection derived from Intersection state remains permitted only for non-authority-bearing work.

## Information-flow allowlist

Downstream components may consume Intersection Record fields only for:

- non-independent/non-authority work routing;
- ordinary prompting/context selection that cannot produce authority-bearing evidence;
- scrutiny escalation;
- synthesis presentation or challenge selection.

They may not consume direct, derived, aggregate, cached, embedded, or UI-mediated Intersection/Deliberation values to lower risk, reduce reviewer cardinality, satisfy independence, alter quorum, select authority-bearing reviewers/attesters, grant credentials, alter platform permissions, or mark an Authority Envelope satisfied.

An execution gate must not consume Deliberation Graph convergence, consensus, deference, confidence, synthesis, or derived representations as a substitute for any Authority Envelope requirement.

If a downstream component cannot prove its use falls within this allowlist, it must fail closed.

## Counterfactual scrutiny rule

If Intersection data raises scrutiny, the resulting record must preserve the baseline scrutiny level that would have applied without Intersection input and the escalated level actually applied. Non-escalation results must not be cached as reusable fast-path authority evidence.

## Hidden reputation-engine prohibition

The system must not maintain or infer a hidden scalar such as `trust score`, `node rank`, `winning rate`, or `authority confidence` that automatically alters permissions, reviewer selection, or approval thresholds.

Historical performance may be descriptive calibration evidence, but any routing or scrutiny adjustment it causes must remain inspectable and must not reduce an existing authority/security requirement.

## Blocking attestation semantics

A required advisory attestation is not co-sovereignty or positive execution authority. However, because withholding it can block eligibility, the blocking function is explicitly modeled as `BOUNDED_NEGATIVE_CONTROL` in the Authority Envelope.

That negative control must be scoped, target-bound, identity-bound, time-bounded, revocable, and independently auditable. Normal execution cannot ignore it. Any degraded-mode or emergency override must be explicit, Operator-authored, short-lived, flagged in the Authority Decision Record, and subject to bounded retroactive ratification. An override never rewrites the original attestation state.

## Assent perishability and dissent durability

ASSERT and SYNTHESIS are target-state-bound. A material target hash change moves them to `REASSESS_REQUIRED`; they do not silently roll forward as support.

DEFER is also target-bound and may not cascade beyond depth 1. If its dependency materially changes, the defer state becomes `REASSESS_REQUIRED`, not DISSENT.

DISSENT remains visible even after typed disposition. Disposition changes status, not history. It requires a typed reason, rationale, actor, and timestamp.

## UI anti-collapse rule

MOPCON must visually separate relationship intelligence, deliberative state, and authority state. Relationship intelligence should not appear on the final authorization surface when its presence would influence the decision without an explicit governance purpose.

No UI aggregate score, badge, color, confidence value, ordering, or status may mathematically or semantically blend relational trust, deliberative convergence, and authority eligibility into one indicator.

Only Authority state may expose execute/merge/mutate affordances.

## Operator legibility rule

Before consequential authorization, MOPCON must render an Operator Delta Digest that separately presents:

- deterministic mechanical change;
- dissent-authored lines in their own words;
- deference ratio and substantive non-deferred position count;
- worst credible outcome and the source that raised it;
- risk assumed;
- reversibility path, cost, and window;
- friction class proportional to consequence.

For high/maximum-friction actions, the Operator may be required to produce a plain-language risk statement as a comprehension receipt rather than merely click Approve.

## Audit consequence

Any action that changes authority must cite its Authority Envelope and governing authorization record. Intersection and Deliberation records may be cited as context, never as the authority source.

Audit/test suites must verify information flow, selection provenance, prompt isolation, target freshness, dissent persistence, override receipts, and downstream taint handling—not merely schema shape.
