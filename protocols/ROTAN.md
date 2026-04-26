# ROTAN — Architecture Layer Specification

**Version:** 1.0.0  
**Updated:** 2026-04-25  
**Layer:** Structural Topology

---

## Definition

ROTAN (Recursive Ontological Topology Architecture Node) defines how MIRRORNODE organizes its components across tiers. It is the *structural grammar* of the system — the rules that determine what belongs where and how layers relate.

## Four-Tier Model

| Tier | Color | Function | Repos |
|------|-------|----------|-------|
| REVENUE | 🟢 | External-facing, monetization | osiris, osiris-audit, HUD-Engine-Spec |
| CORE | 🔵 | Infrastructure, orchestration | mirrornode, mirrornode-py, CORE-HUB, theia-core |
| SURFACE | 🟣 | UI/presentation | Mirror_surface |
| EXPERIMENT | 🟠 | R&D, prototyping | INPphase, Rotan-demo, examples, TRISM-RPG |

## Flow Direction

```
EXPERIMENT → CORE → SURFACE
                  ↘ REVENUE
```

Ideas originate in EXPERIMENT, mature into CORE infrastructure, then surface either as user-facing UI (SURFACE) or revenue-generating products (REVENUE). Flow is one-directional by default; reverse flow (REVENUE → CORE) is permitted only for audit feedback loops via Osiris.

## Node Contracts

Each ROTAN node (repo) must:
1. Declare its tier in its manifest/README
2. Expose a health endpoint or status script
3. Register with `mirrornode-index` for canonical discovery
4. Log significant state changes to Lucian's intelligence layer

## Drift Detection

A ROTAN violation occurs when:
- A REVENUE-tier repo imports directly from EXPERIMENT without CORE mediation
- A node's declared tier conflicts with its actual dependency graph
- An unregistered repo is found operating in the ecosystem

All violations are written to `.lucian/intelligence/drift_log.json`.
