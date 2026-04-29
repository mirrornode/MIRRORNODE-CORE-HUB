# SYSTEM CONTRACT

## SINGLE ENTRY POINT
All execution must go through:
POST `/system/execute`

## TRACE REQUIREMENT
Every run must produce:
- step‑by‑step trace
- structured logs
- timestamps

## CANON REQUIREMENT
All steps must be persisted:
- append‑only
- no silent failures

## REPLAY REQUIREMENT
Every run must be:
- reproducible
- traceable
- lineage‑linked (via `parentRunId` / `trace_id`)

## AGENT RULES
Agents:
- do not route
- do not manage global state
- only execute tasks

## FAILURE POLICY
- No silent errors
- All failures must be logged
