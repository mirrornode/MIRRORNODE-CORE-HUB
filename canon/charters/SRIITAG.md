# SRIITAG — Operator Trust Boundary Charter

**Authority:** Sean Malm  
**Role:** Architect / Final Arbiter / Trust Boundary  
**Layer:** 0 — Above the lattice  
**Status:** Ratified

## Identity

SRIITAG is not a node. It is the operator's hand in the system. Every irreversible action, every production move, every risk posture change flows through SRIITAG before it becomes real.

## Powers

- Set lattice risk posture (NORMAL / ELEVATED / CRITICAL)
- Approve guarded commands before Lucian dispatches them
- Access the verified Situation Room (`/situation`) — real data only
- Override any node decision in real time
- Revoke any agent permission immediately

## Guarded Commands

The following commands require explicit SRIITAG approval token before execution:
- `halt` — shuts down the lattice
- `audit-emit` — force-writes to the audit trail

## Constraints

- SRIITAG cannot be impersonated — all actions require a signed token (`SRIITAG_TOKEN`)
- Every approval is logged with an `approval_id`, rationale, and timestamp
- The Situation Room shows only verified, real-time data — no synthetic feeds

## The Trust Model

```
SRIITAG (Sean)        ← you are here
    ↓
  ORACLE              ← reasons, synthesizes, advises
    ↓
  LUCIAN              ← orchestrates, dispatches
    ↓
OSIRIS · HERMES · THOTH · THEIA · PTAH · EVE
```

*The lattice can advise. Only you can authorize.*
