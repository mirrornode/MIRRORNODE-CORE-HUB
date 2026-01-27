# MIRRORNODE-CORE-HUB

**Central coordination hub for the MIRRORNODE distributed intelligence lattice**

---

## What's Here

This repository contains:

### 📋 **Schemas** (`/schemas/`)
Canonical data schemas for MIRRORNODE systems:
- `audit.v1.0.0.py` - Osiris audit artifact schema (Pydantic)

### 📦 **Examples** (`/examples/`)
Reference implementations and golden samples:
- `audit.sample.v1.json` - Sample Osiris audit artifact

### 🎛️ **Lucian** (Coming Soon: `/lucian/`)
Command orchestration layer:
- Boot protocols
- Command definitions (@Lucian prime, @mirror sweep, etc.)
- Intelligence aggregation
- Drift detection

---

## Osiris: Constrained Static Audit Engine

### What Osiris Is
✅ A **static code analyzer** that crawls repositories  
✅ A **governance checker** for project-declared policies  
✅ An **audit artifact generator** for internal review  
✅ A **read-only HUD** for exploring findings  

### What Osiris Is NOT
❌ **Not a compliance certification tool** (no SOC2, ISO, GDPR validation)  
❌ **Not a penetration testing platform** (no runtime exploit validation)  
❌ **Not a CVE database** (no live vulnerability matching)  
❌ **Not a security monitoring service** (no runtime instrumentation)  

### When to Use Osiris
- Pre-deployment architecture reviews
- Internal governance audits
- Third-party code vetting (static analysis only)
- Baseline security hygiene checks

### When NOT to Use Osiris
- Regulatory compliance certification
- Production runtime security monitoring
- Penetration testing or red team exercises
- Dependency vulnerability scanning (use Snyk, Dependabot, etc.)

---

## Glossary

### Security (in Osiris context)
**Static security pattern detection** - Osiris scans code for common vulnerability patterns (hardcoded secrets, insecure configurations, etc.) using deterministic analyzers. It does **not** perform:
- Penetration testing
- Runtime exploit validation
- CVE matching against live systems

**UI Display:** "Security (Static Analysis Only)"

### Governance (in Osiris context)
Governance claims validate that a repository's structure and metadata align with **its own declared policies**, such as:
- Presence of required files (LICENSE, README, CONTRIBUTING)
- Adherence to naming conventions specified in project docs
- Consistency with package.json declarations

**Governance checks do NOT:**
- Certify compliance with external regulations (GDPR, HIPAA, etc.)
- Validate against industry standards (PCI-DSS, NIST, etc.)
- Replace legal or compliance audits

Think of it as "internal consistency checking" rather than "external standard validation."

### Constraints
Every Osiris audit artifact explicitly documents what was **NOT** analyzed:
- `runtime_access: false` - No runtime monitoring or behavior analysis
- `third_party_deps: excluded` - External dependencies not scanned
- `test_files: excluded` - Test code not included in analysis

This ensures transparency and legal defensibility.

---

## Architecture: Engine-HUD Contract

Osiris follows an **immutable artifact architecture**:

```
┌─────────────┐
│   ENGINE    │  Produces canonical audit.json
│  (Producer) │  • Runs analyzers
│             │  • Validates referential integrity
│             │  • Emits immutable artifact
└──────┬──────┘
       │
       │ audit.json (immutable blob)
       │
       ▼
┌─────────────┐
│     HUD     │  Consumes audit.json (read-only)
│  (Consumer) │  • Validates schema
│             │  • Indexes metadata
│             │  • Renders views
│             │  • Never mutates artifact
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  ASSISTANT  │  Query interface (constrained)
│   (Index)   │  • Explains entities
│             │  • Traces relationships
│             │  • Mandatory citations
│             │  • Cannot create new entities
└─────────────┘
```

**Key Invariants:**
1. **Single source of truth** - Engine produces exactly one `audit.json` per run
2. **Immutability** - Artifacts cannot be modified after emission
3. **Referential integrity** - All entity IDs resolve within the artifact
4. **Zero mutation surface** - HUD and Assistant are pure consumers

---

## Usage

### Validate an Audit Artifact

```python
from schemas.audit_v1_0_0 import AuditArtifact
import json

# Load artifact
with open('examples/audit.sample.v1.json') as f:
    data = json.load(f)

# Validate schema
artifact = AuditArtifact(**data)

# Validate references
artifact.validate_references()

# Compute integrity hash
hash_value = artifact.compute_hash()
print(f"Artifact hash: {hash_value}")
```

### Generate IDs for New Entities

```python
from schemas.audit_v1_0_0 import (
    generate_claim_id,
    generate_evidence_id,
    generate_finding_id,
    generate_risk_id
)

claim_id = generate_claim_id()  # CLAIM-01JGQM8K9T1XYZ...
evidence_id = generate_evidence_id()  # EVIDENCE-01JGQM9K0T2XYZ...
```

---

## Repository Structure

```
MIRRORNODE-CORE-HUB/
├── schemas/
│   └── audit.v1.0.0.py          # Osiris artifact schema
├── examples/
│   └── audit.sample.v1.json     # Golden sample artifact
├── lucian/                       # [Coming Soon] Command orchestration
│   ├── boot.md
│   ├── commands/
│   ├── intelligence/
│   ├── protocols/
│   └── audit/
└── README.md
```

---

## Contributing

This is the canonical source of truth for MIRRORNODE schemas and protocols.

### Schema Changes
- All schema changes require ADR (Architectural Decision Record)
- Breaking changes require major version bump (semver)
- New fields should be optional when possible

### Golden Samples
- Must pass schema validation
- Must pass reference integrity checks
- Should demonstrate all entity types
- Should include edge cases (ABSENCE evidence, UNSUPPORTED findings, etc.)

---

## License

[To be determined by Commander Siseon]

---

## Status

**Last Updated:** 2026-01-26  
**Osiris Schema:** v1.0.0 (Production Ready)  
**Lucian Layer:** In Development  

---

**MIRRORNODE** - Distributed Intelligence Lattice  
**Commander:** Siseon Sogol  
**Orchestrator:** Lucian (URSO)
