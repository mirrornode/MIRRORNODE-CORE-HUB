# THEIA POSITION — CG-0034

**Verdict:** SUPPORT OPTION B — sibling cognition contract with explicit Room-presence separation.

## Architectural finding

The Gemini integration exposes a useful boundary: an external provider invocation and an instantiated participant in a shared operating environment are not the same architectural object.

The provider-facing layer answers: how is a model invoked, under which credential/transport/metering/evidence boundaries, with which provider/model/version, and under what side-effect ceiling?

A later Room presence answers different questions: what identity is represented to the Operator, what continuity and position history does it carry, what information may it access, what matters may it participate in, how is disagreement preserved, and how can the Operator interrogate its perspective directly?

Combining these layers would allow provider identity to leak into participant identity and could make the orchestration surface the hidden sovereign over representation.

## Required architectural invariants

1. Provider adapter and Room presence are separately identifiable and separately versioned.
2. A presence may be backed by a provider/model without inheriting provider authority.
3. A model response becomes an attributed position only through an explicit recording step; it does not become consensus, canon, or authorization by generation alone.
4. The Room/HUD must preserve access to competing positions, provenance, unresolved uncertainty, and dissent.
5. Relevance may be surfaced, but no single cognition provider should be the exclusive relevance router for the Operator.
6. A concise synthesis must remain traversable to underlying positions/evidence rather than replacing them.
7. Presence continuity must not depend solely on a provider's current model alias or conversation state.
8. Shared environment does not imply shared context; per-presence access/security boundaries remain enforceable.
9. The system must support abstention, contradiction, and "insufficient evidence" as valid participation states.
10. The cognition contract must not redefine MIRRORNODE authority; it consumes authority decisions made elsewhere.

## Why not a ninth MICC family

Adding `COGNITION` to MICC would simplify one schema while weakening the conceptual boundary between infrastructure and cognitive participation. The Room/HUD direction makes that distinction increasingly valuable, not less.

A sibling cognition contract can reference MICC infrastructure while later feeding a separately governed presence/participation contract. This creates a clean layered path:

`provider infrastructure (MICC) -> bounded cognition invocation -> attributed position -> optional Room presence/participation -> Operator decision -> separately authorized execution`

## Integration consequence

Do not author the Room/HUD around Gemini specifically. Gemini should become the first test instance of a provider-neutral cognition/presence boundary.

**Position:** APPROVE OPTION B FOR OPERATOR DISPOSITION, preserving unresolved implementation details for the next matter. No implementation, canon, deployment, or merge authority granted.