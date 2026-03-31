# UPDATES

---

## [Infrastructure Core] — Manifest Architecture Migration
**Date:** 2026-03-31
**Deployment:** RISING_STAR v1.1.2
**Commit:** `2e52538`

### Changes
- Introduced `lib/agents.ts` as the canonical agent registry and single source of truth for the MIRRORNODE lattice
- Defined `Agent` type with fields: `id`, `name`, `domain`, `status`, `description`, `symbolic_depth`, `last_heartbeat_ts`
- Implemented `getAgent(id)` helper for safe manifest access across routes and components
- Added `/api/agents` route returning full manifest as structured JSON
- Added `/api/agents/[id]` route returning single agent with 404 handling for unknown IDs
- Deployed `/agents` Situation Room grid index with status indicators and domain labels
- Decoupled frontend from static data — all agent state now sourced from manifest

### Deprecated
- Pre-manifest static agent data structures (removed from frontend components)

### Active Tasks
- `TELEMETRY_SYNC`: Wire `/agents` UI to live heartbeat metrics from `/api/engines/status`
- `SYMBOLIC_MAPPING`: Integrate `lib/agents.ts` manifest into Fusion Engine `processGlyph()` recursion
- `PERSISTENCE_UPGRADE`: Evaluate Upstash/Redis for cross-session manifest state stability

---

## [Osiris] — Audit Schema v1.0.0
**Date:** 2026-01-26

### Changes
- Published canonical Osiris audit artifact schema (Pydantic) at `schemas/audit.v1.0.0.py`
- Published golden sample artifact at `examples/audit.sample.v1.json`
- Defined Engine → HUD → Assistant immutable artifact pipeline
- Documented Osiris constraints: static analysis only, no runtime, no CVE matching
