# AGENTS_TODO

## SYSTEM CONTRACT (NON-NEGOTIABLE)
- All execution flows through `/system/execute`
- All runs must produce a trace
- All steps must be logged to canon
- All runs must be replayable

---

## CURRENT PRIORITY
- [ ] Ensure compliance with system contract
- [ ] Eliminate duplicate or parallel execution paths
- [ ] Standardize input/output schemas

---

## TRACE INTEGRATION
- [ ] Emit structured step logs
- [ ] Include `step`, `agent`, `input`, `output`, `timestamp`
- [ ] Ensure trace is consumable by UI

---

## REPLAY SUPPORT
- [ ] Accept `trace_id`
- [ ] Support deterministic execution (when requested)
- [ ] Preserve lineage (`parentRunId`)

---

## SELF-REPORTING
- [ ] Log all actions to canon
- [ ] Expose health/heartbeat endpoint
- [ ] Surface errors clearly

---

## CLEANUP
- [ ] Remove unused files and environments
- [ ] Consolidate duplicate logic
- [ ] Enforce single responsibility

---

## UI / FRONTEND PRIORITIES
- [ ] Implement `/trace/[runId]` viewer
- [ ] Add replay button (calls `/system/replay`)
- [ ] Display step "reason" clearly
- [ ] Add latency indicators per step

## UX REQUIREMENTS
- [ ] Timeline must be sequential and clickable
- [ ] Step detail must show input/output clearly
- [ ] No internal naming exposed (Rotan/PTAH hidden)
