# MIRRORNODE Delegation Boundary v0.1

**Status:** Draft under CG-0036 — not canon, not implementation authority  
**Version:** 0.1-draft  
**Created:** 2026-08-14

## 1. Purpose

This specification defines how MIRRORNODE may delegate bounded authority without transferring Operator sovereignty or requiring the Operator to become the mandatory transit point for every routine action.

Delegation is a revocable grant to perform a specific class of action under a specific policy, scope, state, time window, and authority ceiling. Delegation is not ownership of the governing authority.

## 2. Delegation classes

### AUTONOMOUS_WITHIN_POLICY
The delegated actor may proceed without a new Operator approval only when all declared preconditions are satisfied and the requested effect remains within the pre-authorized envelope.

### PROPOSAL_ONLY
The actor may analyze, draft, recommend, simulate, prepare, or emit a typed action proposal. It may not cause the governed effect.

### OPERATOR_APPROVAL_REQUIRED
The actor may prepare the action, but execution requires an explicit Operator decision tied to the current request and state.

### NON_DELEGABLE
The authority cannot be conveyed through this delegation layer. Direct Operator action or a separately governed higher-authority process is required.

## 3. Delegation envelope

Every delegation must be attributable and machine-readable. At minimum it identifies:

- `delegation_id`
- `delegator`
- `delegate_actor`
- `authority_class`
- `governing_policy_ref`
- `policy_version`
- `allowed_operations`
- `resource_scope`
- `environment_scope`
- `authority_ceiling`
- `decision_preconditions`
- `risk_ceiling`
- `issued_at`
- `effective_at`
- `expires_at`
- `revocation_ref`
- `receipt_policy_ref`
- `delegation_version`

A delegation is invalid if its governing policy, authority ceiling, scope, or validity period cannot be verified at decision time.

## 4. Anti-self-expansion rule

A delegated actor must never be able, through the authority being delegated, to modify or reinterpret any field that increases its own effective authority.

This includes:

- adding operations;
- broadening resource or environment scope;
- increasing authority or risk ceilings;
- extending expiry;
- disabling or weakening revocation;
- changing the governing policy or its applicable version;
- reclassifying a governed action into a less restrictive delegation class;
- changing evidence requirements in a way that makes its own actions easier to approve;
- delegating onward authority that it did not itself receive with explicit subdelegation permission.

Any such change requires authority from outside the affected delegation envelope.

## 5. Classification separation

The system must separate:

1. the actor proposing or requesting an action;
2. the mechanism classifying the action under policy;
3. the authority granting or denying permission;
4. the actor executing the permitted action;
5. the mechanism verifying the result.

One principal may occupy more than one role only when explicitly allowed by policy. A delegated actor may not be the sole authority for lowering the class or risk of an action it seeks to perform.

## 6. Decision preconditions

Autonomous delegated execution requires all preconditions to pass at the moment permission is resolved. Preconditions may include:

- current state hash or equivalent state reference;
- target version/reference;
- operation and resource membership in the envelope;
- environment match;
- risk threshold;
- required deterministic checks;
- conflict absence;
- policy/version match;
- non-expiry;
- non-revocation;
- dependency state;
- idempotency or replay safeguards where applicable.

A stale approval or stale delegation must not be silently reused against materially changed state.

## 7. Revocation and expiry

Delegation is revocable without consent of the delegate actor.

Revocation must be attributable, timestamped, and visible to the authorization boundary. New work must fail closed after effective revocation.

For already-started work, each delegation must state one of:

- `CANCEL_ON_REVOCATION`
- `COMPLETE_CURRENT_ATOMIC_STEP`
- `COMPLETE_CURRENT_TRANSACTION`
- `NON_INTERRUPTIBLE_WITH_EXPLICIT_RATIONALE`

Expiry prevents new authorization after `expires_at`. Expiry must not silently convert active work into ungoverned work.

## 8. Subdelegation

Subdelegation is prohibited by default.

If allowed, the parent delegation must explicitly declare:

- `subdelegation_allowed: true`
- maximum delegation depth;
- operations eligible for subdelegation;
- maximum child scope and authority ceiling;
- child expiry not later than parent expiry;
- requirement that every child remain traceable to the root delegation.

Authority must be monotonically non-increasing across the delegation chain. Composition may narrow authority but never multiply or expand it.

## 9. Escalation conditions

The delegated path must escalate rather than act when:

- requested operation is outside scope;
- evidence/preconditions are incomplete or contradictory;
- policy classification is ambiguous;
- risk exceeds the declared ceiling;
- an exception or override is requested;
- a non-delegable action is encountered;
- required checks fail;
- the governing state materially changed;
- delegation is expired, revoked, unverifiable, or conflicting;
- two valid delegations produce incompatible instructions;
- the actor requests additional authority to complete the task.

Escalation should present the smallest decision that genuinely requires Operator judgment rather than transferring the entire underlying workload.

## 10. Presumptively non-delegable actions

Unless separately authorized by explicit governance, the following are non-delegable through v0.1:

- expansion of an actor's own authority;
- weakening of security controls or security verdict requirements;
- exceptions to governing approval policy;
- canon promotion or modification of final authority rules;
- creation of new non-delegable authority classes;
- irreversible high-impact external effects outside a pre-established deterministic policy;
- alteration or destruction of authoritative audit evidence;
- disabling revocation or evidence emission;
- self-approval of a previously approval-bearing action.

This list is deliberately conservative and may be refined by later governance.

## 11. Receipts and verification

Every delegated effect must be reconstructible from an evidence chain sufficient to establish:

- what was requested;
- who requested it;
- which delegation was evaluated;
- which policy/version governed;
- what state/preconditions were evaluated;
- what decision was produced;
- who executed it;
- what effect occurred;
- whether the result matched the authorized target;
- whether revocation, expiry, retry, or exception conditions were involved.

Execution success must not substitute for proof that execution was authorized.

## 12. Relationship to cognition

Generated model output, analysis, confidence, or a tool/function proposal carries no execution authority by itself.

A cognition layer may produce a `PROPOSAL_ONLY` object. A separate delegation/approval boundary resolves whether an action is permitted. Any resulting execution remains attributable to the executing principal and governing delegation rather than to the model's recommendation.

## 13. Operator-load boundary

The system should minimize unnecessary Operator intervention by resolving actions that are demonstrably inside a valid delegation envelope and escalating only genuine authority, ambiguity, conflict, exception, or non-delegable questions.

Operator attention is not a substitute for missing policy. Conversely, absence of Operator attention is not permission to infer broader authority.

## 14. Product-readiness

Implementations may later surface this architecture through MOPCON or another product interface, including delegation maps, expiry/revocation controls, pending escalations, authority provenance, and execution receipts.

The product layer must visualize the governing authority state; it may not redefine it.

## 15. Explicit exclusions

v0.1 does not itself grant new permissions, implement runtime enforcement, change current agent authority, authorize deployment, permit automatic merges, or promote this specification to canon.
