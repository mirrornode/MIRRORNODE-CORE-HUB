# MIRRORNODE Canon - Master Index

**Status:** Operational  
**Last Updated:** 2026-06-01  
**Governance source:** MIRRORNODE-CORE-HUB (see `../CANONICAL_SOURCES.md`)  
**Final governance and conflict disposition:** Human Operator  
**Coordination / execution roles:** Desktop Commander + Oracle, only within separately authorized boundaries

---

## What This Is

Constitutional governance infrastructure for MIRRORNODE.

Every repo has declared boundaries.  
Every execution emits audits.  
Charter ratification and signature validity must be established individually from verified evidence; directory presence alone is not ratification.

This index describes governance intent and documented mechanisms. Enforcement claims require current, scope-specific verification; this index alone is not proof of production enforcement.

---

## Directory Structure
```
canon/
├── README.md              # Overview
├── INDEX.md              # This file - navigation
│
├── charters/             # Constitutional authority
│   ├── LUCIAN_PRIME.md
│   ├── OSIRIS.md
│   ├── CORE_HUB.md
│   ├── INFRA.md
│   └── MIRRORNODE_PY.md
│
├── contracts/            # Technical specifications
│   ├── AUDIT_EMISSION.md
│   └── sdk/
│       ├── audit.py      # Python audit SDK
│       └── audit.ts      # TypeScript audit SDK
│
├── scripts/              # Executable tools
│   ├── bootstrap.sh      # Initialize canon structure
│   ├── charter_lucian.sh # Lock Lucian charter
│   ├── audit.sh          # Audit external repos
│   ├── index.sh          # Index GitHub org
│   ├── halt.sh           # Emergency stop
│   └── enforce_audits.sh # Check compliance
│
├── dossiers/             # Audit records (auto-generated)
│   └── YYYY-MM/
│       └── audit-{repo}-{timestamp}.json
│
├── index/                # System maps
│   └── github-{org}.json
│
└── status/               # Progress reports and metrics
    ├── PROGRESS_REPORT_2026-06-01.md
    ├── canon_completion_register.csv
    ├── mirrornode_metrics.json
    └── mirrornode_metrics_table.csv
```

---

## Progress Reports

- [MIRRORNODE Progress Report — 2026-06-01](./status/PROGRESS_REPORT_2026-06-01.md) — Canon-visible completion tally (9/14 complete, 64%), Phase 1 locked, Phase 2 active, architecture integrity 89.5/100

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

// Manual emission
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

1. **Declared State = Observable Reality**
   - What charters say MUST match what code does
   - Audits prove alignment or surface drift

2. **Authority is Traceable**
   - Every decision references a charter
   - Every execution emits an audit
   - No silent changes

3. **Reversibility is Built In**
   - Clean git history
   - Verified charter signatures where established; unverified charters remain pending
   - Immutable audit trail
   - halt.sh exists

4. **Constitutional Violations are Visible**
   - Unchartered repos flagged
   - Failed executions logged
   - Blocked operations recorded

---

## Support

- **Canon Issues:** File in mirrornode/mirrornode repo
- **Charter Conflicts:** Escalate to Operator (Sean)
- **Audit SDK Bugs:** Include audit_id in report

---

## Cross-repository authority and ratification status (2026-10-15)

CORE-HUB is the governance source designated in `CANONICAL_SOURCES.md`. The `mirrornode-index` repository is the cross-repository index and technical/historical reference, not an overriding governance authority. Its `canon/MASTER_CANON.md` currently asserts precedence in a conflicting header; this remains an OPEN cross-repository correction until separately reviewed and amended.

The human Operator holds final governance and conflict-disposition authority. Coordination titles and tool access do not themselves confer authority to ratify, merge, deploy, or override security gates.

The current `canon/charters/` directory contains ten Markdown charter files and two matching `.sig` files (`LUCIAN_PRIME.md` and `OSIRIS.md`). This is a file-presence observation only: signature validity, charter scope, and ratification status remain to be checked individually. Do not claim all charters are signed or locked.

See `docs/governance/CANON_AUTHORITY_RECONCILIATION_2026-10-15.md` for source-level contradictions, proposed cross-repository correction, and unresolved review gates. House Ramses authoritative repository placement remains unverified and is not created by this note.
