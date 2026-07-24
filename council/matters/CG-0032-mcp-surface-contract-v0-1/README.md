# CG-0032 — MCP Surface Contract v0.1

**Workflow state:** Proposed  
**Authority effect:** None until Operator disposition  
**Matter type:** Governance definition  
**Implementation authority:** Not granted

## Decision question

Should MIRRORNODE adopt `MCP_SURFACE_CONTRACT_V0_1.md` as the governing definition for a read-only downstream MCP projection surface, while preserving the current four-tool local prototype as frozen evidence and requiring separate later authorization for executable remediation, relocation, additional model-runtime attachment, remote exposure, or capability expansion?

## Why this matter exists

A local MCP prototype has now been demonstrated through Claude Code. The prototype exposes four read-only tools and successfully returned an integrity-check result covering 45 local ledger events with no reported errors.

That technical observation established feasibility. It did not establish architectural authorization.

The Council review that followed identified four governance gaps:

1. the executable is local and untracked;
2. raw ledger and local-path disclosure are not yet governed as projection-safe output;
3. integrity language can be mistaken for authority, truth, approval, or safety;
4. the dependency direction between canonical MIRRORNODE state and MCP has not been contractually fixed.

CG-0032 addresses those gaps at the **definition layer only**.

## Operator authorization for this step

The Operator authorized the documentation step after Council review.

Authorized now:

- draft the MCP Surface Contract;
- record CG-0032;
- prepare review requests;
- open a documentary review PR.

Not authorized now:

- edit `~/code/mirrornode-mcp/server.py`;
- add a fifth tool;
- relocate the executable;
- create a repository for the executable;
- remediate current tool output shapes;
- alter Claude registration scope;
- connect additional model runtimes;
- expose the MCP remotely;
- deploy or daemonize the service;
- create any write-capable MCP function.

## Proposed architectural role

The draft defines MCP as a **downstream read-only projection surface**.

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

MCP does not create authority and canonical MIRRORNODE mechanisms may not depend on MCP output for authorization, truth, approval, or execution permission.

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

The observation is evidence only. The current output shapes are not approved by this matter.

## Known review flags

- `mirrornode_status`: exposes local paths and requires output minimization review.
- `ledger_summary`: exposes a local path and requires output minimization review.
- `recent_ledger_events`: returns raw ledger events and is marked nonconforming as currently shaped.
- `validate_ledger_provenance`: requires neutral semantics and resolution of duplicated canonical validation logic.

No remediation is authorized while this matter is under review.

## Required reviews

- Theia — architectural integration and dependency direction
- Ptah — implementation contract and canonical-rule ownership
- Thoth — security boundary, prompt injection, and anti-capabilities
- Osiris — disclosure, authority language, and failure presentation

## Review target

`../../../docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md`

## Required sequence

1. Review the actual contract text.
2. Record attributable positions.
3. Synthesize disagreements and conditions without resolving them by implication.
4. Reserve final disposition to the Operator.
5. If accepted, open a separate later matter for executable remediation and implementation location.

## Boundary

This matter is documentary governance only.

An accepting disposition on CG-0032 would not authorize MCP implementation changes, deployment, remote exposure, ChatGPT attachment, additional model runtimes, capability expansion, or write authority.
