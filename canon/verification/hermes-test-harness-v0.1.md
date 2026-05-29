# Hermes Test Harness v0.1

**Status:** ACTIVE CANON  
**Owner:** Thoth (Verification) and Ptah (Governance)  
**Purpose:** Canonical verification specification for Phase 1 Observable Core initialization.

## Authority Split

- **Thoth** emits security and verification verdicts.
- **Ptah** records governance and canon verdicts.
- **Hermes** transports validated events.
- **Situation Room** displays live state only.

## Canonical First Event

```json
{
  "event_id": "uuid",
  "event_type": "security_verdict",
  "source_node": "thoth",
  "source_product": "mirrornode_core",
  "subject_id": "system",
  "session_id": "system_boot",
  "timestamp": "2026-05-14T03:21:00Z",
  "payload": {
    "verdict": "hermes_bridge_validated",
    "details": "POST /event, persistence, and status route passed local checks.",
    "risk_level": "low"
  },
  "severity": "info"
}
```

## Pass Conditions

The core system is authorized to advance beyond Phase 1 only when every condition below returns TRUE without silent failures, stale state, or hardcoded fictional state.

### I. Environment Verification

- [ ] Hermes directory exists.
- [ ] Entrypoint (`main.py` or equivalent) exists.
- [ ] Dependencies install without error.
- [ ] Environment variables are documented and loaded.
- [ ] No hardcoded fictional config exists.

### II. Event Emission Validation — Thoth

- [ ] Thoth node successfully emits `security_verdict` on `system_boot`.
- [ ] Payload matches the canonical first event schema.
- [ ] `severity` is `info`.
- [ ] `payload.risk_level` is `low`.
- [ ] `source_node` is `thoth`.
- [ ] `source_product` is `mirrornode_core`.
- [ ] `subject_id` is `system`.
- [ ] `session_id` is `system_boot`.

### III. Hermes Transit Validation

- [ ] `POST /event` accepts the canonical payload.
- [ ] `POST /event` returns 200 or 201 HTTP status.
- [ ] Response body acknowledges receipt.
- [ ] No schema errors occur.
- [ ] No missing fields occur.
- [ ] No silent failures occur.

### IV. Database Persistence

- [ ] Events table exists.
- [ ] Test event appears in the table.
- [ ] All fields are present.
- [ ] Payload is intact.
- [ ] Timestamp is correct.
- [ ] No truncation occurs.
- [ ] No schema violations occur.

### V. WebSocket Broadcast

- [ ] WebSocket endpoint is reachable.
- [ ] Listener receives the broadcast.
- [ ] Broadcast matches the event payload.
- [ ] No delay beyond expected local latency occurs.
- [ ] No dropped messages occur.

### VI. Status Route Verification

- [ ] `/api/status` or equivalent exists.
- [ ] Status route returns live data, not fictional state.
- [ ] Response includes uptime.
- [ ] Response includes last event timestamp.
- [ ] Response includes database connection status.
- [ ] Response includes WebSocket status.
- [ ] Response includes service identifier.

### VII. Security Verdict Logging

- [ ] Hermes logs event receipt.
- [ ] Hermes logs schema validation.
- [ ] Hermes logs persistence success.
- [ ] Hermes logs broadcast success.
- [ ] Hermes logs no warnings or errors during passing run.
- [ ] Hermes logs verdict classification.

### VIII. Situation Room Update

- [ ] Thoth node shows online.
- [ ] Last event is `security_verdict`.
- [ ] Timestamp matches the event.
- [ ] No placeholder data exists in the Situation Room.
- [ ] No hardcoded fictional status exists in the UI.
- [ ] No stale state is rendered.

## Final PASS/FAIL Rule

### PASS

Phase 1 Observable Core passes only if:

- Every section above passes.
- No drift is detected.
- No missing authority surfaces are detected.
- No schema violations occur.
- No silent failures occur.

### FAIL

Phase 1 Observable Core fails if:

- Any checklist item fails.
- Any drift category is triggered.
- Any missing or fictional data is detected.
- Any persistence, broadcast, or status route failure occurs.

## Operator Sign-Off

After running the harness, return one of the following:

- `PASS` → Proceed to wiring ROTAN-q and Surface Layer nodes.
- `FAIL` → Classify failure, escalate to the correct node, and re-run the harness.

## Next After PASS

Wire ROTAN-q and Surface Layer nodes.
