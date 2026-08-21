# CG-0036 — Four-Position Review Synthesis

**Normative review target:** `1a3d92ea9f69e5ea0d631b0d19a9a9b5ee942312`  
**Status:** findings synthesized; bounded correction stage authorized by prior Operator direction; no disposition or merge authority  
**Positions:** Ptah, Thoth, Osiris, Theia

## Position record

| Position | Execution provenance | Disposition | Findings |
|---|---|---|---|
| Ptah | Perplexity; one disclosed prior advisory provenance | `HOLD` | 2 P1, 2 P2 |
| Thoth | Microsoft Copilot; model not disclosed by provider | `HOLD` | 3 P1, 5 P2 |
| Osiris | Claude (Anthropic), Osiris lane | `CLEAR-WITH-CONDITIONS` | 2 P1, 4 P2 |
| Theia | ChatGPT (OpenAI), Theia integration lane | `CLEAR-WITH-CONDITIONS` | 3 P1, 1 P2 |

Codex is the automated prerequisite and is not counted as a position. Earlier
Claude Hermes/Ptah advisory work and earlier Perplexity advisory work are
disclosed but are not separate positions or corroboration.

## Converged findings accepted for correction

### 1. Governed-reference integrity

The receipt, revocation, and aggregate-authority policy references did not
receive the immutable binding applied to policy, preconditions, issuer
authority, and registries. This is one systemic reference-integrity defect.

The correction must inventory every authority-relevant reference, bind
dereferenced governing content by hash or authenticated proof, identify
locator-only references explicitly, retain hash preimages, and fail closed on
unresolvable or mismatched content.

### 2. Typed evidence and receipt closure

A decision receipt is not evidence that the authorized effect succeeded.
CG-0036 needs a typed execution receipt binding decision consumption, approval
consumption, dispatch state, effect outcome, executing actor, authority holder,
MICC invocation, revocation evidence, and the canonical audit record.

Consumption transitions and hash preimages must be retained and retrievable as
auditable evidence. Tests must distinguish shape/presence assertions from
substantive cross-document and state-transition checks.

### 3. Identity and MICC integration

The end subject, requesting actor, delegated authority holder, PDP issuer,
approval issuer, and executing adapter are deliberately distinct identities.
They must be cross-bound, not collapsed.

The signed decision must bind the exact MIM declaration, adapter/capability,
side-effect class, lifecycle state, requested scope, scope decision, approval
class, executing actor, and execution nonce from which its MICC classification
was derived.

### 4. Preconditions, aggregate authority, registry, and revocation

Hash binding alone does not define semantics. Closed profiles are required for:

- deterministic decision preconditions and their evaluation result;
- aggregate-authority input closure, authority-holder identity, ceilings,
  conflict/combination semantics, and action-chain escalation;
- canonical resource-registry snapshot and record semantics;
- revocation-state source, sequence, freshness, and rollback resistance; and
- the cross-document validator contract that consumes these artifacts.

These profiles remain architecture/conformance contracts. They do not select
runtime products or authorize implementation.

### 5. Cross-contract and evidence status

The Cognition Contract reference is prospective while CG-0035 remains an open
stacked draft. MICC remains accepted pre-canon. The repaired
`AUDIT_EMISSION` contract is controlling, but CG-0036 still needs a
delegation-specific additive mapping.

Council-required `ALLOW` remains structurally unreachable. The missing
Council constitution/quorum validator is a blocking future dependency, not a
defect in v0.1's current fail-closed behavior.

## Findings preserved as commissioning dependencies

The following are not invented inside this correction pass:

- production policy engine or AuthZEN transport selection;
- production workload identity/attestation mechanism;
- concrete distributed revocation transport;
- numeric production risk, budget, blast-radius, and monitoring thresholds;
- Council seat composition or quorum rules;
- production registry, consumption-store, or telemetry product selection;
- canon promotion of MICC or CG-0035;
- runtime implementation or deployment.

`AUTONOMOUS_WITHIN_POLICY` remains disabled for production effects until the
draft profiles are ratified, implemented, and commissioned by a separate
explicit Operator action.

## Correction sequence

1. **Reference-integrity commit:** bind receipt, revocation, and aggregate
   policy references; define preimage retention/retrievability; correct packet
   target metadata.
2. **Semantic-integration commit:** add typed precondition, aggregate,
   revocation, registry, MICC binding, validator, execution-receipt, and
   end-to-end conformance artifacts; update existing specifications and tests.

The second commit becomes the sole corrected normative head. All four original
positions remain historical inputs against `1a3d92ea...`. Fresh automated
checks and Codex review are required, followed by exact-head confirmations from
all four execution provenances. A position requires full re-review only if the
correction materially changes its analyzed architecture.

## Correction disposition

The combined correction head accepts and addresses the current-specification
substance of all four positions:

- the reference-integrity commit performs the schema-wide governed-reference
  sweep and defines preimage retention/retrievability;
- the semantic-integration commit adds typed preconditions, a deterministic
  aggregate policy and authenticated holder-keyed snapshot, authenticated
  monotonic revocation state, an authenticated resource-registry snapshot, an
  exact MICC invocation binding, a provider-neutral validator contract, a typed
  authenticated execution receipt, and end-to-end compromise fixtures;
- successful-effect evidence and approval/decision consumption state are bound
  in the execution receipt and mapped to the repaired audit identifier;
- CG-0035 compatibility language is explicitly prospective; and
- the packet records Osiris packet-v1 metadata drift without rewriting the
  provenance of that review.

Findings that require runtime selection, deployment, ratification, production
thresholds, transport, workload identity, or a future Council constitution are
preserved as commissioning dependencies. They are not represented as
implemented by this documentation/schema correction.

## Current disposition

No Operator disposition is made by this synthesis. No merge, implementation,
deployment, promotion, commissioning, credential access, or thread resolution
is authorized by this artifact.
