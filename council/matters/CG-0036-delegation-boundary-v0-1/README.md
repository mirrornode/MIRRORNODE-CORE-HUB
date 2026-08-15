# CG-0036 — Delegation Boundary v0.1

**Status:** OPEN — bounded architecture matter  
**Type:** Governance definition / authority architecture  
**Initiator:** Operator  
**Opened:** 2026-08-14

## Objective

Define an internal MIRRORNODE delegation boundary that reduces routine Operator intervention without transferring Operator sovereignty or allowing delegated authority to expand itself.

The design is internal-first and product-ready by design.

## Core principle

> Operator authority remains maximal while delegated authority remains bounded, inspectable, revocable, expiring where appropriate, and incapable of self-expansion.

## Draft.2 authority classes

The matter defines four machine-readable classes:

1. **AUTONOMOUS_WITHIN_POLICY** — may proceed only inside a pre-authorized deterministic envelope after current policy/state/aggregate-authority checks pass.
2. **ADVISORY_ONLY** — may analyze, recommend, draft, simulate, or prepare but cannot cause the governed effect.
3. **OPERATOR_APPROVAL_REQUIRED** — action cannot proceed without a verifiable Operator approval bound to the current request, subject, action, resource, state, policy, delegation, and lifetime.
4. **NON_DELEGABLE** — authority cannot be delegated through this layer and requires direct Operator action or an explicitly higher governing process.

Unmatched, ambiguous, stale, unverifiable, conflicting, or policy-error requests default to `NON_DELEGABLE` / deny-or-escalate behavior; they never imply permission.

## Mandatory invariants

- Delegated authority cannot modify its own scope, class, ceiling, expiry, revocation rule, governing policy, resource mappings, classifier inputs, or aggregate-authority logic.
- The actor that requests an action cannot silently become the sole authority lowering the action's class or risk.
- Every delegated action remains attributable to requesting actor, governing delegation, policy bundle, decision, executing actor, current-state reference, approval object where required, and result.
- Revocation must take effect without requiring consent from the delegated actor and must satisfy an explicit freshness bound.
- Expired or unverifiable delegation fails closed.
- Delegation does not imply identity merger, authority inheritance, or provider authority.
- Security weakening, canon/final-authority changes, authority expansion, audit suppression, and exceptions to governing policy are presumptively non-delegable unless later governance explicitly establishes otherwise.
- Delegation must not convert advisory model output into execution authority.
- Multiple individually valid grants must be evaluated in aggregate before autonomous execution.

## Operator-load objective

The system should escalate only when the action exceeds verified policy/delegation bounds, encounters material ambiguity, conflicts with policy, crosses risk or aggregate ceilings, requires an exception, or reaches a non-delegable class.

The goal is not maximal autonomy. The goal is **provable bounded autonomy with minimal necessary escalation**.

## Product-readiness constraint

Although this begins as MIRRORNODE internal architecture, terminology and machine-readable semantics should be provider-neutral and suitable for later exposure in MOPCON or a standalone governance product without changing the underlying authority model.

## Explicit non-authorizations

Opening CG-0036 does not authorize runtime implementation, production policy changes, new agent permissions, automatic merges, deployment, credential access, execution expansion, canon promotion, publication, or merge.
