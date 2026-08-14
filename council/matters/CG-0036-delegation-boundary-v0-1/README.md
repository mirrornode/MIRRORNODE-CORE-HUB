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

## Initial authority classes

The matter will define four machine-readable classes:

1. **AUTONOMOUS_WITHIN_POLICY** — may proceed only inside a pre-authorized deterministic envelope.
2. **PROPOSAL_ONLY** — may analyze, recommend, draft, or prepare but cannot cause the governed effect.
3. **OPERATOR_APPROVAL_REQUIRED** — action cannot proceed without explicit Operator authorization tied to the current state and requested effect.
4. **NON_DELEGABLE** — authority cannot be delegated through this layer and requires direct Operator action or an explicitly higher governing process.

## Mandatory invariants

- Delegated authority cannot modify its own scope, class, ceiling, expiry, revocation rule, or governing policy.
- The actor that classifies an action as routine cannot silently be the sole authority that benefits from that classification.
- Every delegated action remains attributable to requesting actor, governing delegation, executing actor, policy/version, current-state reference, and result.
- Revocation must take effect without requiring consent from the delegated actor.
- Expired or unverifiable delegation fails closed.
- Delegation does not imply identity merger, authority inheritance, or provider authority.
- Security, canon promotion, irreversible external effects, authority expansion, and exceptions to governing policy are presumptively non-delegable unless a later explicit governance matter establishes otherwise.
- Delegation must not convert advisory model output into execution authority.

## Operator-load objective

The system should escalate only when the action exceeds a verified delegation envelope, encounters material ambiguity, conflicts with policy, crosses a defined risk threshold, requires an exception, or reaches a non-delegable class.

The goal is not maximal autonomy. The goal is **provable bounded autonomy with minimal necessary escalation**.

## Product-readiness constraint

Although this begins as MIRRORNODE internal architecture, terminology and machine-readable semantics should be provider-neutral and suitable for later exposure in MOPCON or a standalone governance product without changing the underlying authority model.

## Explicit non-authorizations

Opening CG-0036 does not authorize runtime implementation, production policy changes, new agent permissions, automatic merges, deployment, credential access, execution expansion, canon promotion, publication, or merge.
