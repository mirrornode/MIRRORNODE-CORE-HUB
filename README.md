# MIRRORNODE-CORE-HUB

**Governance, canon, and promotion register for the MIRRORNODE distributed intelligence lattice**

---

## Authority Boundary

MIRRORNODE-CORE-HUB is the governed canonical surface for MIRRORNODE charters, contracts, schemas, promotion records, and source-of-truth decisions.

This repository is not the runtime monorepo and does not claim that application code lives here unless the path exists in this repository. Runtime implementation belongs in the appropriate execution repository and must be referenced with its current repo and path.

Promotion into canon requires Ptah evaluation and explicit Operator ratification. No document, workflow, agent, or generated artifact self-ratifies.

---

## Source-of-Truth Map

| Surface | Authority |
|---|---|
| `MASTER_INDEX.md` | Promotion register for ratified canonical artifacts |
| `canon/` | Declared canon root for charters, contracts, dossiers, scripts, and index material |
| `schemas/` | Versioned schemas for governed artifacts such as Osiris audit output |
| `examples/` | Sample artifacts that demonstrate schema shape without promoting new doctrine |
| Runtime repositories | Execution code, UI, APIs, deployments, and implementation evidence |
| Documentation staging repositories | Migration, operational notes, protocols, and drafts before promotion |

If an execution repository or documentation surface conflicts with a ratified CORE-HUB artifact, the ratified CORE-HUB artifact governs until a newer entry is promoted through `MASTER_INDEX.md`.

---

## Current Canon Register

`MASTER_INDEX.md` is the active promotion register.

Current promoted entry:

| Artifact | Promotion Date | Status |
|---|---:|---|
| Leg 2 Rev B - MIRRORNODE Architecture Review | 2026-06-24 | Ratified |

The promoted Leg 2 Rev B entry preserves these governance constraints:

- Confidence tiers remain unflattened.
- Public/core boundary is a contract requirement.
- Technical enforcement must be separately verified where implemented.
- Osiris Audit v1 shipping priority remains separate and protected.
- Promotion authority requires explicit Operator ratification.

---

## Runtime Implementation Boundary

Earlier versions of this README described a runtime layout centered on `lib/agents.ts`, `app/api/agents`, and `/agents` UI routes. Those references describe execution surfaces, not CORE-HUB root paths.

Treat those runtime references as stale unless they are verified in the current execution repository and linked with a current repo/path. CORE-HUB should record the governing decision, schema, or ratified contract; execution repositories should carry the implementation details.

---

## Osiris: Constrained Static Audit Engine

### What Osiris Is

- A static code analyzer that crawls repositories
- A governance checker for project-declared policies
- An audit artifact generator for internal review
- A read-only HUD for exploring findings

### What Osiris Is Not

- Not a compliance certification tool
- Not a penetration testing platform
- Not a CVE database
- Not a security monitoring service

---

## Schemas (`/schemas/`)

- `audit.v1.0.0.py` - Osiris audit artifact schema (Pydantic)

## Examples (`/examples/`)

- `audit.sample.v1.json` - Sample Osiris audit artifact

---

## Repository Structure

```text
MIRRORNODE-CORE-HUB/
├── MASTER_INDEX.md
├── canon/
├── examples/
├── schemas/
└── README.md
```

Additional directories may exist for work in progress, but they do not become canonical authority until represented by a promoted artifact or an explicit canon entry.

---

## Status

**Last Updated:** 2026-06-29  
**Governance Register:** `MASTER_INDEX.md` active  
**Canon Root:** `canon/` active  
**Osiris Schema:** v1.0.0 production ready  
**Runtime Manifest Claims:** Not asserted by CORE-HUB without current execution-repo evidence

---

**MIRRORNODE** - Distributed Intelligence Lattice  
**Operator:** Sean Malm  
**Orchestrator:** Merlin (Dispatcher/Map Keeper)
