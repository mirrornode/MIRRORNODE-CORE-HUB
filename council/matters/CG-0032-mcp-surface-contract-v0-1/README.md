# CG-0032 — MCP Surface Contract v0.1

**Workflow state:** Closed  
**Operator disposition:** Accepted  
**Authority effect:** Governing definition only  
**Matter type:** Governance definition  
**Implementation authority:** Not granted

## Decision

The Operator accepted `MCP_SURFACE_CONTRACT_V0_1.md` as the governing definition for a read-only downstream MCP projection surface and authorized finalization and merge of PR #33 as a governance-definition record only.

The accepting disposition does not authorize executable remediation, relocation, additional model-runtime attachment, remote exposure, deployment, publication, capability expansion, or write authority.

## Why this matter exists

A local MCP prototype was demonstrated through Claude Code. The prototype exposes four read-only tools and successfully returned an integrity-check result covering 45 local ledger events with no reported errors.

That technical observation established feasibility. It did not establish architectural authorization.

CG-0032 defines the **governance layer only** for what a future MIRRORNODE MCP projection surface may become.

## Accepted architectural role

MCP is a **downstream read-only projection surface**.

```text
Operator / Council authority
        ↓
MIRRORNODE-CORE-HUB
        ↓
canonical mechanisms such as @mirror
        ↓
approved projection contract
        ↓
MCP surface
        ↓
external model runtime
```

MCP does not create authority and canonical MIRRORNODE mechanisms may not depend on MCP output for authorization, truth, approval, integrity, or execution permission.

The contract applies across the entire MCP protocol surface, including tools, resources, prompts, templates, notifications/subscriptions, server instructions, extensions, and future negotiated capabilities.

## Current prototype evidence

Observed local implementation:

`~/code/mirrornode-mcp/server.py`

Observed tools:

- `mirrornode_status`
- `ledger_summary`
- `recent_ledger_events`
- `validate_ledger_provenance`

Observed integrity-check result:

```json
{
  "valid": true,
  "events_checked": 45,
  "errors": []
}
```

The observation is evidence only. The current prototype is not accepted as a contract-conforming implementation by CG-0032.

## Current prototype review flags

- `mirrornode_status`: exposes local paths and requires output minimization review.
- `ledger_summary`: exposes a local path and requires output minimization review.
- `recent_ledger_events`: returns raw ledger events and is nonconforming as currently shaped.
- `validate_ledger_provenance`: requires neutral semantics and resolution of duplicated canonical validation logic.

These flags remain unresolved implementation questions. Acceptance of the contract does not remediate them.

## Council review

Initial positions:

- POS-0001 — Theia: support; no architectural definition defect.
- POS-0002 — Ptah: support with R1 revision required.
- POS-0003 — Thoth: support with R2 revision required.
- POS-0004 — Osiris: support conditioned on incorporation of R1/R2.

The Operator then recorded a `revision-required` disposition limited to:

- R1 — deterministic failure semantics;
- R2 — primitive-independent MCP boundary;
- bounded confirmation review.

Confirmation positions:

- POS-0005 — Ptah: confirmed.
- POS-0006 — Thoth: confirmed.
- POS-0007 — Osiris: confirmed with residual future implementation conditions.

No definition-level blocker remained after confirmation.

## Final Operator disposition

**Status:** `accepted`

The final disposition authorizes:

- acceptance of MCP Surface Contract v0.1 as a governance definition;
- finalization of the CG-0032 documentary record;
- finalization and merge of PR #33 as a governance-definition record only;
- opening a later separate Council matter for implementation remediation if the Operator chooses.

It does not authorize:

- editing `~/code/mirrornode-mcp/server.py`;
- adding or materially expanding any MCP primitive or capability;
- relocating or creating a repository for the executable;
- remediating current output shapes;
- altering Claude registration scope;
- connecting ChatGPT or any additional model runtime;
- exposing MCP remotely;
- deploying or daemonizing the service;
- shell, filesystem, repository, ledger, runtime, or Council writes;
- any write-capable MCP architectural class.

## Governing definition

`../../../docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md`

## Next boundary

CG-0032 is complete after PR #33 merges.

Any executable remediation or implementation decision must begin under separate future authority and must satisfy the accepted MCP Surface Contract v0.1. Canon promotion, if desired, is also a separate explicit action.
