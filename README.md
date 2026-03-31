# MIRRORNODE-CORE-HUB

**Central coordination hub for the MIRRORNODE distributed intelligence lattice**

---

## Architecture Overview

MIRRORNODE operates as a manifest-driven agent lattice. As of commit `2e52538`, all agent definitions are centralized in `lib/agents.ts` — the single source of truth for the entire AI network.

```
MIRRORNODE-CORE-HUB/          ← Canonical docs, schemas, coordination
platform/                      ← Runtime: app/, lib/, fusion/, api/
├── lib/
│   └── agents.ts              ← Agent manifest (single source of truth)
├── app/
│   ├── agents/
│   │   └── page.tsx           ← /agents Situation Room UI
│   └── api/
│       └── agents/
│           ├── route.ts        ← GET /api/agents (full manifest)
│           └── [id]/
│               └── route.ts   ← GET /api/agents/[id] (single agent)
└── fusion/
    └── index.ts               ← Symbolic lattice engine (manifest integration pending)
```

---

## Agent Manifest (`lib/agents.ts`)

The `Agent` type and manifest array govern all 6 primary agents in the lattice.

### Agent Type Definition

```typescript
export type Agent = {
  id: string
  name: string
  domain: string
  status: 'active' | 'pending' | 'offline'
  description: string
  symbolic_depth?: number
  last_heartbeat_ts?: string
}
```

### `getAgent(id)` Helper

Use `getAgent(id)` to retrieve a single agent by ID from the manifest:

```typescript
import { getAgent } from '@/lib/agents'

const agent = getAgent('lucian')
// Returns Agent | undefined
```

This helper is the standard access pattern for all internal routes and components. Do not import the raw manifest array directly in UI components — always go through `getAgent()` or the `/api/agents` endpoint.

---

## API Routes

| Route | Method | Description |
|---|---|---|
| `/api/agents` | GET | Returns full agent manifest as JSON |
| `/api/agents/[id]` | GET | Returns single agent by ID; 404 if not found |

### Example Response — `/api/agents`

```json
[
  {
    "id": "lucian",
    "name": "Lucian",
    "domain": "Command Orchestration",
    "status": "active"
  }
]
```

---

## UI — Situation Room (`/agents`)

The `/agents` grid index provides a live view of all agents in the manifest, including:
- Real-time status indicators
- Domain labels
- Lattice Depth (telemetry integration in progress)

**Live deployment:** [Lattice Index](https://www.mirrornode.io/agents) | [JSON Manifest](https://www.mirrornode.io/api/agents)

---

## Osiris: Constrained Static Audit Engine

### What Osiris Is
✅ A **static code analyzer** that crawls repositories
✅ A **governance checker** for project-declared policies
✅ An **audit artifact generator** for internal review
✅ A **read-only HUD** for exploring findings

### What Osiris Is NOT
❌ Not a compliance certification tool
❌ Not a penetration testing platform
❌ Not a CVE database
❌ Not a security monitoring service

---

## Schemas (`/schemas/`)

- `audit.v1.0.0.py` — Osiris audit artifact schema (Pydantic)

## Examples (`/examples/`)

- `audit.sample.v1.json` — Sample Osiris audit artifact

---

## Repository Structure

```
MIRRORNODE-CORE-HUB/
├── schemas/
│   └── audit.v1.0.0.py
├── examples/
│   └── audit.sample.v1.json
├── canon/
├── protocols/
├── state/
└── README.md
```

---

## Status

**Last Updated:** 2026-03-31
**Deployment:** RISING_STAR v1.1.2
**Agents Active:** 6
**Manifest:** `lib/agents.ts` (Active)
**Osiris Schema:** v1.0.0 (Production Ready)

---

**MIRRORNODE** — Distributed Intelligence Lattice
**Commander:** Sean Malm
**Orchestrator:** Merlin (Dispatcher/Map Keeper)
