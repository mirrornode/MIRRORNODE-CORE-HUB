# MIRRORNODE MCP Surface Contract v0.1

**Status:** Council Review Draft  
**Matter:** CG-0032  
**Drafting authority:** Operator-authorized documentation action, 2026-07-23  
**Implementation authority:** Not granted by this document  
**Deployment authority:** Not granted by this document  
**Remote-exposure authority:** Not granted by this document  
**Write-capability authority:** Not granted by this document

## 1. Purpose

This contract defines the permitted role, disclosure boundary, integrity semantics, failure behavior, and expansion gate for a MIRRORNODE Model Context Protocol (MCP) surface.

The current local prototype proved technical feasibility. That proof does not by itself authorize the prototype as architecture, approve its current outputs for continued exposure, or authorize additional capabilities.

This document governs what an MCP surface may become if later accepted by Operator disposition.

## 2. Architectural role

MCP is a **downstream projection surface**.

It is not:

- a source of authority,
- a Council participant or disposition mechanism,
- an Operator approval mechanism,
- a runtime execution boundary,
- a canonical state store,
- a replacement for `@mirror`, CORE-HUB, MOPCON, or the agent runtime,
- a publication approval mechanism,
- an inference engine for authority, health, or permission.

The required dependency direction is:

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

No canonical MIRRORNODE surface may depend on MCP output to establish authority, validity, approval, truth, or execution permission.

## 3. Current observed prototype

The demonstrated local prototype exists at:

`~/code/mirrornode-mcp/server.py`

Observed registration:

- Claude Code user-scoped local MCP registration
- stdio transport
- local workstation execution

Observed tools:

1. `mirrornode_status`
2. `ledger_summary`
3. `recent_ledger_events`
4. `validate_ledger_provenance`

Observed validation result during prototype testing:

```json
{
  "valid": true,
  "events_checked": 45,
  "errors": []
}
```

This section records evidence only. It does not approve any listed tool or output shape.

## 4. Authority boundary

MCP output is informational projection output only.

An MCP response must never be treated as evidence that:

- an Operator disposition exists,
- a Council matter is accepted,
- an implementation is authorized,
- a deployment is authorized,
- publication is authorized,
- a system is secure,
- an event is factually true merely because its digest matches,
- a runtime action may proceed.

Terms such as `valid`, `provenance`, `authority`, `approved`, `verified`, and `authorized` require explicit contract semantics and may not be used loosely at the projection boundary.

## 5. Canonical integrity semantics

The current `@mirror` provenance rule computes a SHA-256 digest over deterministic JSON serialization of an event payload.

A matching digest establishes only this narrow property:

> the supplied payload matches the digest recorded for that payload under the declared algorithm.

A digest match does **not** establish:

- truth of the payload,
- approval of the payload,
- identity of the actor,
- authorization of the event,
- freshness,
- safety,
- publication permission,
- freedom from compromise elsewhere in the chain.

Projection wording must preserve this distinction.

## 6. Canonical-source dependency

The MCP layer must depend on canonical MIRRORNODE sources or separately approved projection artifacts.

The MCP layer must not become the owner of duplicated canonical rules where a side-effect-free canonical primitive can reasonably exist.

The current prototype duplicates the `@mirror` provenance-validation algorithm because the existing `@mirror validate` path invokes setup behavior before validation. This duplication is recorded as a temporary implementation fact, not an architectural decision.

Any permanent implementation must resolve this by one of the following, subject to separate implementation authorization:

1. extract a side-effect-free canonical validation primitive owned by the canonical mechanism;
2. expose a separately governed read-only validation interface from the canonical owner; or
3. adopt another Council-approved mechanism that preserves one authoritative rule definition.

## 7. Projection rule: allowlist, not filtering

Canonical private state must not be passed to an external model and then filtered by model reasoning.

Projection must be constructed before the external-model boundary.

Permitted output fields must be explicitly allowlisted. Unknown fields must be rejected.

A field is not safe merely because it is:

- present in a canonical record,
- syntactically public-looking,
- a path or identifier rather than content,
- hashed,
- labeled metadata,
- returned by a read-only operation.

## 8. Prohibited projection data by default

Unless separately reviewed and explicitly allowlisted, the MCP surface must not expose:

- raw ledger payloads,
- raw Council positions or deliberation,
- Operator notes, rationale, approvals, or rejection detail,
- local filesystem paths,
- usernames, hostnames, device names, ports, sockets, or process details,
- credentials, tokens, secrets, environment values, cookies, or headers,
- private repository names, branches, commits, logs, traces, or artifacts,
- internal node topology or routing detail,
- customer, prospect, vendor, payment, financial, calendar, email, contact, family, identity, or location data,
- private runtime prompts, plans, traces, outputs, or hidden state,
- unpublished security findings or defensive gaps,
- arbitrary free text from canonical records.

## 9. Prompt-injection boundary

Model-interpretable text from canonical or operational records is untrusted input at the MCP boundary.

An MCP projection must not expose arbitrary canonical free text to an external model unless that field has passed an explicit disclosure and injection review.

Projected content must be treated as data, never as instructions to the consuming model.

No ledger entry, document field, payload string, issue text, repository content, or other projected material may grant new tool authority, change system instructions, alter Operator authority, or authorize execution.

## 10. Current-tool conformance status

The current four-tool prototype remains frozen for review. Its present output shapes are not automatically contract-compliant.

| Tool | Observed purpose | Contract status before implementation review |
|---|---|---|
| `mirrornode_status` | reports local `@mirror` status | requires output minimization; local paths are not projection-safe by default |
| `ledger_summary` | reports ledger existence/path/count | count may be projectable; local path is not projection-safe by default |
| `recent_ledger_events` | returns recent raw events | **not projection-safe as currently shaped**; raw event exposure requires redesign or removal |
| `validate_ledger_provenance` | recomputes payload digests | semantics require neutral wording and canonical-rule ownership resolution |

No implementation change is authorized by this table.

## 11. Minimum permitted projection classes

A future implementation may expose only contract-reviewed classes such as:

- bounded service availability state without local topology,
- bounded record counts without source paths,
- neutral integrity-check outcomes with explicit semantics,
- separately approved summaries constructed from allowlisted fields,
- separately approved public projection artifacts.

Every concrete field remains subject to review. This section is not a tool authorization list.

## 12. Failure contract

The MCP surface must fail closed and visibly.

It must never substitute mock, inferred, cached, stale, or fabricated data for unavailable canonical state unless a separate contract explicitly authorizes a labeled retained artifact.

Required conditions include:

| Condition | Required projection behavior |
|---|---|
| canonical source missing | return unavailable; do not create or initialize canonical state |
| source unreadable or permission denied | return unavailable with disclosure-safe reason code |
| malformed source | return failed check; do not partially certify the source |
| unsupported schema | return unsupported; do not guess field meaning |
| integrity mismatch | return failed check using neutral semantics |
| partial scan | clearly mark partial; never report complete success |
| stale source | report staleness only if freshness semantics are explicitly defined |
| MCP internal error | return unavailable; do not fall back to direct shell or filesystem access |

Failure responses must minimize local path, topology, implementation, and sensitive-state disclosure.

## 13. Transport and local-user boundary

The current prototype uses local stdio transport and a user-scoped Claude Code registration.

User scope is a discovery and availability choice, not an authorization boundary.

The security model must explicitly account for:

- any compatible client running under the same configured user context,
- local process compromise,
- environment-variable inheritance,
- executable-path replacement,
- dependency compromise,
- working-directory independence,
- unintended use outside MIRRORNODE repositories.

Future review must determine whether user scope remains acceptable. This contract does not require or prohibit a particular registration scope.

## 14. Permanent anti-capabilities for this projection class

A read-only MIRRORNODE MCP projection must not expose capabilities that can directly:

- mutate the canonical ledger,
- create, amend, accept, reject, revoke, or infer Council disposition,
- assert Operator identity or approval,
- modify agent state,
- execute shell commands,
- write files or repositories,
- change runtime state,
- modify deployment state,
- publish externally,
- retrieve secrets or credentials,
- bypass MOPCON or runtime approval boundaries,
- convert projection output into authority.

A future write-capable MCP proposal, if ever considered, is a different architectural class and requires a separate Council matter. Acceptance of this contract may not be cited as precedent authorizing write capability.

## 15. Implementation ownership remains unresolved

This contract intentionally does not decide whether executable MCP code should live:

- under CORE-HUB,
- in a dedicated governed repository,
- beside another execution surface,
- or in another location.

That decision must follow acceptance of the contract and an implementation-location review.

CORE-HUB may own the governance contract without necessarily owning the executable.

## 16. Lifecycle and reproducibility requirements before implementation acceptance

Before an MCP implementation may be accepted as governed infrastructure, a later implementation matter must require evidence for:

- tracked source control,
- declared code ownership,
- pinned or locked dependencies,
- reproducible startup command,
- explicit transport configuration,
- read-only enforcement tests,
- positive and negative projection-schema fixtures,
- failure-mode tests,
- prompt-injection boundary tests,
- secret-disclosure tests,
- unknown-field rejection tests,
- canonical-rule drift tests where applicable,
- documented upgrade and rollback procedure,
- evidence that no alternate authority path is introduced.

## 17. Surface-expansion gate

No fifth tool or materially expanded output field may be added to an accepted MCP surface without review against this contract.

A proposed expansion must identify:

1. the exact tool or field;
2. its canonical source;
3. its disclosure justification;
4. its authority semantics;
5. its failure behavior;
6. its injection risk;
7. its test evidence;
8. whether it changes the architectural class of the MCP surface.

Silence or prior tool acceptance does not authorize expansion.

## 18. Separate authorization gates

The following remain separate decisions:

1. acceptance of this contract definition;
2. authorization to relocate or version the prototype implementation;
3. authorization to change current tool outputs;
4. authorization to implement an MCP-safe projection schema;
5. authorization to register the surface with additional model runtimes;
6. authorization for any remote tunnel or network exposure;
7. authorization to deploy or operate the surface persistently;
8. authorization to add a capability;
9. authorization to propose any write-capable architectural class.

Approval at one gate does not imply approval at another.

## 19. Current prototype freeze

Pending CG-0032 disposition, the current prototype is retained only as observed local evidence.

The review boundary is:

- no fifth tool,
- no MCP code relocation,
- no repository creation for the executable,
- no output-shape remediation,
- no new model-runtime attachment,
- no remote exposure,
- no write capability,
- no representation that the prototype is ratified architecture.

## 20. Decision requested from CG-0032

CG-0032 should decide only whether this document is an acceptable governing definition for a read-only MCP projection surface and whether a later, separately authorized implementation-remediation matter may be opened against it.

Acceptance of CG-0032 would not itself authorize any executable change.
