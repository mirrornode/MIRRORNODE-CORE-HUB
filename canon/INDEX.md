# MIRRORNODE Canon - Master Index

**Status:** Operational  
**Last Updated:** 2026-09-01  
**Authority:** Desktop Commander + Oracle

---

## What This Is

Constitutional governance infrastructure for MIRRORNODE.

Every repo has declared boundaries.  
Every execution emits audits.  
Every charter is signed and locked.

This is not aspirational documentation - this is **enforced reality**.

---

## Current Operational Truth

For questions about **current** MIRRORNODE operating state, begin with:

- [MIRRORNODE-00 — Operational Addendum — 2026-09-01](./dossiers/2026-09/MIRRORNODE-00-OPERATIONAL-ADDENDUM-2026-09-01.md)

That record currently covers the MOPCON / governed Oracle / Osiris integration state, exact-head verification lineage, local authority boundaries, live read-only case projection, derived Operator Debt, commercial/fulfillment state, unresolved offer drift, and known security/dependency debt.

Earlier dossiers remain historical evidence. A newer operational record supersedes them only for present-state questions and does **not** rewrite earlier exact-head attestations or authority dispositions.

See also [`../CANONICAL_SOURCES.md`](../CANONICAL_SOURCES.md) for the current source map and precedence rule.

---

## Directory Structure
```text
canon/
├── README.md              # Overview
├── INDEX.md               # This file - navigation
│
├── charters/              # Constitutional authority
│   ├── LUCIAN_PRIME.md
│   ├── OSIRIS.md
│   ├── CORE_HUB.md
│   ├── INFRA.md
│   └── MIRRORNODE_PY.md
│
├── contracts/             # Technical specifications
│   ├── AUDIT_EMISSION.md
│   └── sdk/
│       ├── audit.py       # Python audit SDK
│       └── audit.ts       # TypeScript audit SDK
│
├── scripts/               # Executable tools
│   ├── bootstrap.sh       # Initialize canon structure
│   ├── charter_lucian.sh # Lock Lucian charter
│   ├── audit.sh           # Audit external repos
│   ├── index.sh           # Index GitHub org
│   ├── halt.sh            # Emergency stop
│   └── enforce_audits.sh # Check compliance
│
├── dossiers/              # Dated audit and operational records
│   └── YYYY-MM/
│       ├── audit-*.json
│       └── MIRRORNODE-00-*.md
│
├── index/                 # System maps
│   └── github-{org}.json
│
└── status/                # Progress reports and metrics
    ├── PROGRESS_REPORT_2026-06-01.md
    ├── canon_completion_register.csv
    ├── mirrornode_metrics.json
    └── mirrornode_metrics_table.csv
```

---

## Progress Reports

- [MIRRORNODE Progress Report — 2026-06-01](./status/PROGRESS_REPORT_2026-06-01.md) — historical canon-visible completion tally (9/14 complete, 64%), Phase 1 locked, Phase 2 active, architecture integrity 89.5/100 at that date.

Do not treat dated progress metrics as current unless a newer report explicitly reaffirms them.

---

## Quick Reference

### Bootstrap New System
```bash
./canon/scripts/bootstrap.sh
./canon/scripts/charter_lucian.sh
```

### Daily Operations
```bash
make audit-check          # Check compliance (warnings only)
make audit-strict         # Check compliance (fail on violations)
make audit-test           # Test audit SDK
make charters             # List all active charters
```

### Audit External Repo
```bash
./canon/scripts/audit.sh https://github.com/org/repo
```

### Emergency Stop
```bash
./canon/scripts/halt.sh
```

---

## Integration Guide

### Python Projects
```python
from canon.contracts.sdk.audit import emit_audit, audit_execution

# Manual emission
audit_id = emit_audit(
    repo="your-repo",
    event_type="execution",
    actor="system",
    verdict="SUCCESS",
    evidence={"duration_ms": 123, "error": None}
)

# Decorator (automatic)
@audit_execution("your-repo", actor="agent")
def process_data(data):
    return {"result": "success"}
```

### TypeScript Projects
```typescript
import { emitAudit, auditExecution } from '@/canon/contracts/sdk/audit';

const auditId = emitAudit({
  repo: 'your-repo',
  event_type: 'execution',
  actor: 'system',
  verdict: 'SUCCESS',
  evidence: { duration_ms: 123, error: null }
});
```

---

## Governance Principles

1. **Declared State Must Match Observable Reality**
   - What current governance records say must match current evidence.
   - Dated historical records stay historical rather than being silently reinterpreted.

2. **Authority is Traceable**
   - Every consequential decision references its authority boundary.
   - No implementation state implies merge, deployment, release, or provider-promotion authority by itself.

3. **Reversibility is Built In**
   - Clean git history.
   - Signed charters.
   - Immutable or dated evidence trails.
   - `halt.sh` exists.

4. **Contradictions Must Be Visible**
   - Stale maps, stale status claims, authority conflicts, and source drift are reconciliation work—not facts to average together.

---

## Support

- **Canon Issues:** File in the appropriate MIRRORNODE governance workflow.
- **Charter Conflicts:** Escalate to the Operator.
- **Audit SDK Bugs:** Include `audit_id` in the report.
