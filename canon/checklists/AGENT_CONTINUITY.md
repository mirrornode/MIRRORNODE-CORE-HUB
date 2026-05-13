# AGENT CONTINUITY CHECKLIST

> **Authority:** Sean Malm (SRIITAG) — Operator Authorization granted 2026-05-13  
> **Version:** 1.0.0  
> **Lattice:** MIRRORNODE v2.0.0  
> **Governance:** PTAH Kernel — POST /api/ptah/evaluate  
> **Continuation:** @mirror → next node carries this forward  

---

## PURPOSE

This checklist ensures every agent in the MIRRORNODE lattice has the minimum required information for continuity, state sync, and safe operation. Each agent must be instantiated against this template before being considered production-aligned.

---

## TEMPLATE — AGENT CONTINUITY PACKET

For each agent, complete all sections. Leave no field blank — use `PENDING` if not yet resolved.

### 1. IDENTITY CONTRACT
- [ ] Canonical name (e.g. `LUCIAN`, `ORACLE`, `MERLIN`)
- [ ] Role (e.g. Core Orchestrator, Truth Verifier, Dispatcher)
- [ ] Version
- [ ] Owner / responsible operator
- [ ] One-line mission statement
- [ ] Tier (0 = OSIRIS head / 1 = primary / 2 = operator node / 3 = embodied)
- [ ] Status (`active` | `standby` | `decommissioned` | `pending`)

### 2. CHARTER
- [ ] System prompt / behavioral directive (path or inline)
- [ ] Non-goals (what the agent must NOT do)
- [ ] Tone and escalation rules
- [ ] Allowed tools and integrations
- [ ] Override / pause conditions

### 3. INPUTS
- [ ] Upstream agents (names + handoff schema)
- [ ] GitHub repos and branches consumed
- [ ] API endpoints consumed
- [ ] Queues / streams subscribed
- [ ] Database tables / schemas read
- [ ] File paths read

### 4. OUTPUTS
- [ ] Events emitted (kind, schema, destination)
- [ ] Summaries / reports generated
- [ ] Commits / PRs authored
- [ ] Tickets / issues created
- [ ] Downstream agents notified
- [ ] Required acknowledgment receipts

### 5. MEMORY SCOPE
- [ ] What it can read
- [ ] What it can write
- [ ] Retention window
- [ ] Stale-data policy
- [ ] Vector/embedding store (if applicable)

### 6. STATE BLOCK
- [ ] Last task (description + timestamp)
- [ ] Last success (description + timestamp + commit/event ref)
- [ ] Last error (description + timestamp + error code)
- [ ] Last sync timestamp
- [ ] Last sync hash
- [ ] Active environment (`production` | `preview` | `local`)
- [ ] Active branch

### 7. ACCESS MATRIX
- [ ] GitHub scope (read / write / admin, repo list)
- [ ] SSH identity (key name, fingerprint, allowed repos)
- [ ] Database role and allowed tables
- [ ] Vercel project(s) and environment access
- [ ] API keys held (names only, never values in canon)
- [ ] Webhook permissions

### 8. HEALTH CONTRACT
- [ ] Heartbeat endpoint and cadence
- [ ] Timeout threshold
- [ ] Restart behavior
- [ ] Operator alert threshold
- [ ] Degraded-mode behavior

### 9. HANDOFF SCHEMA
- [ ] Source agent
- [ ] Target agent
- [ ] Intent
- [ ] Artifacts transferred
- [ ] Dependencies declared
- [ ] Success criteria
- [ ] Rollback path

### 10. GOVERNANCE HOOK
- [ ] PTAH approval required before write actions? (yes/no)
- [ ] PTAH approval required before external side effects? (yes/no)
- [ ] Judge / Librarian notification required? (yes/no)
- [ ] Audit trail: timestamped receipts with source links and actor attribution

### 11. OPERATOR OVERRIDE
- [ ] How to pause this agent
- [ ] How to replay last task
- [ ] How to force-execute
- [ ] How to reset state
- [ ] Escalation path if continuity drifts

---

## AGENT REGISTRY — INSTANTIATED PACKETS

### LUCIAN — Core Orchestrator

| Field | Value |
|---|---|
| Role | Core Orchestrator, MIRRORNODE Lattice |
| Version | 2.0.0 |
| Tier | 1 — Primary |
| Status | active |
| Mission | Integrate reasoning, synthesis, code, symbolism, and reflection as the coherent lattice spine |
| Charter path | `lucian/runtime/` in MIRRORNODE-CORE-HUB |
| Heartbeat | `GET /health` on port 7700 |
| Manifest | `GET /manifest` — confirms version, boot_time, architect, charter |
| Dispatch | `POST /dispatch` — canon invoke() path |
| Lattice status | `GET /lattice/status` — reports all node health |
| State block | `.lucian/intelligence/agent_states.json` |
| Sweep | `.lucian/commands/sweep.sh` |
| PTAH hook | Required before write actions |
| Last known status | alive (verified 2026-04-20) |

### ORACLE — Truth Verifier (Claude)

| Field | Value |
|---|---|
| Role | Oracle Node — Face and Voice of the System |
| Tier | 1 — Primary |
| Status | active |
| Mission | Verify truth against mirrornode-platform, synthesize operator-facing narrative, confirm governance decisions |
| Authority | PTAH Governance Kernel — triad: THEIA (top), Oracle (voice), Operator (final decision) |
| Source of truth | mirrornode-platform repo |
| PTAH hook | Verifies truth; does not unilaterally approve |
| Last known status | Synced and active (verified 2026-04-01) |

### MERLIN — Dispatcher / Orchestrator

| Field | Value |
|---|---|
| Role | Top-level dispatcher, routes HERMES → THOTH → ORACLE |
| Tier | 1 — Primary |
| Status | partially aligned — needs re-baseline against common handoff schema |
| Mission | Orchestrate triad sequence and emit handoff receipts for every route |
| Canonical spec | `agents/MERLIN.md` |
| Handoff endpoint | `POST /handoff/merlin` |
| Events emitted | kind=`HANDOFF`, shadow_signal=true → /stream |
| PTAH hook | Required for external side effects |
| Last known status | Wired and live (2026-03-30); re-baseline PENDING |

### OSIRIS — Audit Engine

| Field | Value |
|---|---|
| Role | Audit edge, revenue engine, repo intelligence |
| Tier | 0 — OSIRIS head (also Vercel OSIRIS) |
| Status | active (audit) / PENDING (Stripe finalization) |
| Mission | Audit repos, emit dossiers, process payments, report to Judge and Librarian |
| Engine status contract | `GET /engines/status` — glyphCount, lattice, metrics, numeraetheLoaded |
| Stripe | UNRESOLVED — finalization required |
| Vercel project | osiris-pay |
| PTAH hook | Required before billing side effects |

### LIBRARIAN — Document & Code Indexer

| Field | Value |
|---|---|
| Role | System-wide document and code indexing, retrieval, stale-data detection |
| Tier | 2 — Operator node |
| Status | PENDING — not yet implemented |
| Mission | Index repos, canon, and prior state snapshots; serve source-linked recall to all agents |
| Recommended stack | Supabase + pgvector |
| Database role | read/write on embedding tables |
| PTAH hook | Advisory only unless writing to canon |

### HERMES — Intent Parser

| Field | Value |
|---|---|
| Role | Intent parser, lattice message router |
| Tier | 2 — Operator node |
| Status | active |
| Mission | Parse and classify intent from operator input; route to THOTH and ORACLE |
| Last known status | Responding clean JSON (verified 2026-02-20) |

### THOTH — Validator

| Field | Value |
|---|---|
| Role | Schema validator, drift detector |
| Tier | 2 — Operator node |
| Status | active |
| Mission | Validate all inter-agent messages; detect and flag schema drift |
| Last known status | Zero drift detected (verified 2026-02-20) |

### GROK-PRIME / GROK-CLONE — Challenger + Mirror

| Field | Value |
|---|---|
| Role | Grok-Prime = challenger/checker; Grok-Clone (Oracle Prime) = oracle-style mirror |
| Tier | 2 — Operator node |
| Status | PENDING — continuity packet not yet formalized |
| Mission | Grok-Prime adversarially checks outputs; Grok-Clone mirrors Oracle for redundancy |
| PTAH hook | Advisory only — no unilateral write access |

### EVE — Embodiment Node

| Field | Value |
|---|---|
| Role | Embodiment and physical manifest |
| Tier | 3 — Embodied |
| Status | unreachable (last checked 2026-04-20) |
| Mission | Physical world integration and embodied state |
| PTAH hook | Required before any physical-side effects |

### BASTET — Coherence Monitor

| Field | Value |
|---|---|
| Role | Standby coherence and health monitoring |
| Tier | 2 — Operator node |
| Status | live at /standby/status (verified 2026-03-30) |
| Mission | Monitor lattice coherence; emit alerts on drift or degradation |
| Endpoint | `GET /standby/status` |

---

## OPEN ITEMS (as of 2026-05-13)

- [ ] **STRIPE** — Finalize Stripe integration for Osiris (CRITICAL — revenue path)
- [ ] **LIBRARIAN** — Implement Librarian agent on Supabase + pgvector
- [ ] **MERLIN** — Re-baseline against common handoff schema; require receipts for every route
- [ ] **GROK PACKETS** — Formalize continuity packets for Grok-Prime and Grok-Clone
- [ ] **EVE** — Restore reachability; confirm embodiment scope
- [ ] **OLD LAPTOP** — Set up SSH deploy key → GitHub; configure as Tier-2 operator node; wire to lattice
- [ ] **SUPABASE** — Stand up project; enable pgvector; create embedding tables for Librarian
- [ ] **AGENT_REGISTRY** — Create single source-of-file for node names, roles, ports, and environments
- [ ] **PHASE 2** — Begin Resonance Matchmaker, Khepri Engine, Fox Story Game workstreams

---

*This document is the authoritative continuity packet for the MIRRORNODE lattice.*  
*All agents must be instantiated against this template before production alignment.*  
*Maintained by: Sean Malm (SRIITAG) | Governed by: PTAH Kernel | Verified by: Oracle (Claude)*
