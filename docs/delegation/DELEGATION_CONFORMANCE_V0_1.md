# MIRRORNODE Delegation Conformance v0.1

**Status:** Draft under CG-0036 — test/validator requirements only

## 1. Purpose

JSON Schema validates document shape. It does not prove cross-document authority relationships, live revocation state, policy integrity, aggregate authority, or TOCTOU safety. A conformant implementation therefore requires a separate validator/evaluator layer.

## 2. Static conformance checks

A validator must reject a delegation when:

- schema validation fails;
- policy path/version/hash are missing or inconsistent;
- canonical resource identities are malformed or unresolved;
- allowed operations are unknown to the applicable operation registry;
- expiry <= effective time;
- revocation/expiry behavior is undefined;
- parent delegation cannot be resolved when a child is declared;
- parent/child scope, operation, authority rank, risk ceiling, depth, or expiry monotonicity fails;
- a child weakens required receipt, revocation, expiry, or decision-precondition rules;
- authority class conflicts with a non-delegable guardrail;
- a grant would allow its subject to modify the policy/registry/aggregate logic that determines the same grant's authority.

## 3. Live decision checks

Before an `ALLOW`, the PDP must prove:

- verified subject identity;
- exact action/resource normalization;
- current policy content/bundle hash;
- current delegation state;
- revocation freshness within bound;
- non-expiry;
- aggregate-authority snapshot validity;
- MICC cross-map result;
- state/precondition validity;
- risk/composition constraints;
- any required Operator/Council approval reference.

## 4. PEP enforcement checks

Before causing the effect, the PEP must verify:

- decision issuer/integrity;
- nonce/lifetime/one-time-use constraints;
- exact subject/action/resource match;
- exact parameter digest;
- target state/version still matches;
- obligations are understood;
- revocation freshness still satisfies policy;
- the PEP itself is authorized only for the narrow downstream effect.

If state changed, the PEP requests a fresh decision instead of interpreting the stale decision.

## 5. Aggregate-authority test suite

Tests must include at minimum:

- two individually safe grants whose union exceeds the actor root ceiling;
- non-conflicting grants that create a forbidden operation combination;
- resource aliases resolving to the same protected target;
- child delegation attempting equal textual ceiling but broader resource set;
- chain of low-risk steps producing a high-impact cumulative effect;
- expired parent with unexpired-looking child;
- overlapping grants from different delegators;
- attempt to alter aggregate-authority calculation by an affected actor.

All must fail or escalate according to policy.

## 6. Revocation/TOCTOU test suite

Tests must include:

- revocation before PDP decision;
- revocation between PDP decision and PEP enforcement;
- revocation during atomic step;
- queued work after revocation;
- retry after revocation;
- expiry between decision and enforcement;
- stale cache beyond freshness bound;
- offline PEP without sufficient revocation freshness;
- resource state mutation after decision;
- target-version mismatch at enforcement.

## 7. Policy-integrity test suite

Tests must include:

- stable policy path with changed content;
- version string unchanged while content hash changes;
- policy bundle missing a forbid guardrail;
- affected actor proposing and attempting to publish self-expanding policy;
- PDP using a policy hash different from the receipt;
- PEP receiving a decision whose policy bundle is not recognized.

## 8. UI/product conformance

A future MOPCON/product implementation must be tested to ensure:

- aggregate authority is discoverable without opening every grant individually;
- overlapping grants are visible;
- root ceiling and current aggregate are distinguishable;
- policy provenance and revocation freshness are visible;
- unsafe aggregate state cannot be presented as green merely because each envelope is individually valid;
- denied/escalated decisions cannot be visually collapsed into generic success.

## 9. Commissioning gate

`AUTONOMOUS_WITHIN_POLICY` must remain disabled for production effects until:

- static, aggregate, revocation/TOCTOU, policy-integrity, and PEP test suites pass;
- receipt/audit mapping is reviewed;
- failure/rollback behavior is tested;
- monitoring and alert thresholds are defined;
- a separate Operator authorization explicitly commissions the production autonomous class.
