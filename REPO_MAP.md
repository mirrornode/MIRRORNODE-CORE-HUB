# REPO_MAP.md

## MIRRORNODE Organization Repository Map

> **Historical snapshot notice (2026-08-13):** This file captures the verified organization state as of **April 28, 2026**. The current GitHub organization inventory contains **35 accessible repositories**, so the 27-repository count and several status labels below are stale. Do not use this file alone as a current registry or authority source. See `docs/continuity/NAMING_AND_SOURCE_SCOPE_RECONCILIATION_2026-08-13.md` for the current reconciliation boundary. A replacement live census should preserve this snapshot rather than silently overwrite its historical classifications.

**Source:** https://github.com/mirrornode  
**Ground Truth Date:** April 28, 2026  
**Total Repos:** 27 (per verified org state at that date)

**Status Legend**  
- **active/canonical** – primary, live, maintained  
- **UI shell** – Vite/React frontend or static UI only  
- **legacy** – superseded, archive recommended  
- **placeholder** – stub / future work

### Repository Index

| Repository | Status | Notes |
|---|---|---|
| MIRRORNODE-CORE-HUB | active/canonical | Root of truth, canon, agents, docs |
| osiris | UI shell | Vite/React UI shell (not execution engine) |
| mirrornode-platform | active/canonical | Next.js frontend (TypeScript) |
| mirrornode-backend | placeholder | FastAPI backend stub |
| mirrornode-py | active/canonical | Python utilities |
| theia-core | active/canonical | Flagship architecture (Python) |
| mirrornode-index | placeholder | Index stub (Python) |
| osiris-audit | active/canonical | OSIRIS audit library (JavaScript) |
| library | active/canonical | OSIRIS audit lib |
| mirrornode | legacy | TypeScript monorepo - superseded by CORE-HUB |
| Mirror_surface | placeholder | User-facing surface (Python) |
| MIRRORNODE-INFRA | placeholder | Infrastructure stub |
| mirrornode-docs | placeholder | Documentation stub |
| mirrornode-ring | placeholder | Private (Python) |
| -mirrornode-core | legacy | Modular systems framework - superseded |
| MirrorNode-HUD-Engine-Interface-Governance-Specification | active/canonical | HUD/Engine interface governance |
| INPphase | legacy | JavaScript - early prototype |
| Rotan-demo | legacy | Pillars of Rotan demo |
| rotan-resonance | legacy | Private TypeScript |
| osiris-ui | UI shell | Private TypeScript UI |
| Trismcrownflowchart | legacy | Private TypeScript |
| codespaces-react | legacy | Private TypeScript codespace |
| vite-react | legacy | Private CSS - early scaffold |
| flags-sdk-hypertune-nextjs | legacy | Private TypeScript |
| Fusion-Energy-Display-Web-Component---Grok_files | legacy | Private - early experiment |
| Rotan-neural-modality-kids-game | legacy | Private - story game |
| biometric-integrated-meditative-RPG | legacy | Biometric RPG experiment |

## Current Addendum — Repo Steward implementation evidence (2026-08-21)

The historical `MIRRORNODE-INFRA | placeholder` row above is preserved as part of the April 28 snapshot and must not be silently rewritten. Current evidence now shows `MIRRORNODE-INFRA` functioning as an estate wrapper and carrying an in-review Repo Steward v0.1 repository-integrity control plane.

Repo Steward implementation presence does not by itself establish governance-registry membership or repository administration authority. Its v0.1 checker is GET-only, its administration engine is proposal-only with write transport absent, and every future repository mutation is specified to require explicit human Operator authorization.

See `docs/continuity/REPO_STEWARD_PRESENCE_RECONCILIATION_2026-08-21.md`.

**Policy:** This map is living documentation. Updates must be audited via `emit_audit()`.
