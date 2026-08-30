# Claude Intersection Review — Disposition — 2026-08-21

**Source posture:** single-model advisory review supplied by the Operator; not repository-state evidence, not a merge gate, and not corroboration of another lane.

**Position received:** SUPPORT_WITH_CONDITIONS.

## Blocking findings accepted

### Routing independence

Accepted. Intersection-derived state is now forbidden from selecting authority-bearing reviewers or attesters. Authority Decision Record routing provenance records the selection function, selected principals, independence evidence, and `intersection_input_used: false`.

### Prompt/context laundering

Accepted. Authority-bearing reviews/attestations must use canon-pinned/governed prompt templates, exclude Intersection-derived context and prior Deliberation Graph influence during the independent pass, and record the prompt hash plus evidence inputs.

### Blocking attestation semantics

Accepted with terminology refinement. A mandatory attestation is explicitly modeled as **bounded negative control**, not positive execution authority or co-sovereignty. Withholding can block eligibility. Scope, target, identity, freshness, revocation, and override semantics are therefore governed. Normal execution cannot bypass it. Degraded/emergency override is exceptional, Operator-authored, time-bounded, flagged, and subject to retroactive ratification.

### Assent perishability

Accepted. ASSERT and SYNTHESIS are bound to target-state hash and move to `REASSESS_REQUIRED` after material target change. DEFER likewise becomes `REASSESS_REQUIRED` when its dependency/target changes. DISSENT remains durable.

## Additional findings accepted

- dissent disposition requires typed reason, rationale, actor, and timestamp and does not erase historical visibility;
- reversibility class/path/cost/window are required in Authority Envelope and Operator Delta Digest;
- deference depth is capped at one;
- deference ratio and substantive non-deferred position count are visible in Operator Digest;
- relationship intelligence may be absent from the final authorization surface rather than merely visually separated;
- only Authority state may expose execute/merge/mutate affordances;
- high-consequence actions may require an Operator-authored risk statement as a comprehension receipt;
- degraded platform/emergency action must use a flagged Authority Decision Record rather than out-of-band mutation;
- unknown execution outcome is a modeled state and requires bounded recorded re-authorization before retry;
- counterfactual scrutiny delta is recorded when Intersection state escalates scrutiny;
- non-escalation results cannot be cached as fast-path authority evidence.

## Deliberately not adopted as stated

### Stale deference becomes dissent

Not adopted. Staleness is lack of current knowledge, not opposition. Stale deference becomes `REASSESS_REQUIRED`.

### Mandatory cryptographic anchoring of every dissent at this stage

Not yet adopted as a protocol requirement. Stable identifiers, target binding, append-only provenance, durable visibility, typed disposition, and receipt propagation are required now. Cryptographic anchoring remains an implementation option to evaluate once the canonical persistence/integrity mechanism is chosen.

## Resulting architecture

`Covenant -> Intersection Record (non-authority) -> Deliberation Graph (non-authority) -> Operator Delta Digest -> Authority Envelope -> Authority Decision Record -> Bounded Action -> Verification Receipt`

Intersection/Deliberation may inform human understanding and non-authority workflow behavior. They may not supply permission predicates. Authority-bearing reviewer/attester selection and authority-bearing prompts are isolated from Intersection influence.

## Remaining gate

These corrections materially change PR #52. The new exact head requires fresh independent review. No previous Codex/AI review clears the changed head.
