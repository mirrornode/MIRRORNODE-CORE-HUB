# POS-0003 — Thoth Security Boundary Review — CG-0032

## Verified Current Implementation

- The current observed prototype is local, stdio-based, user-scoped in Claude Code, and exposes four demonstrated tools. No write-capable MCP tool is recorded in CG-0032.
- The contract does not treat absence of write tools as sufficient proof of safety. It separately governs disclosure, prompt injection, integrity semantics, transport/user scope, and anti-capabilities.
- `recent_ledger_events` is explicitly marked nonconforming as currently shaped because it exposes raw ledger data and model-interpretable text.
- Local filesystem paths in `mirrornode_status` and `ledger_summary` are explicitly not approved as projection-safe by default.
- `validate_ledger_provenance` is not approved as an authority assertion; the contract narrows digest consistency to payload/digest correspondence and denies truth, safety, approval, authorization, freshness, identity, and publication implications.
- `@mirror` itself includes probable-secret rejection on write-oriented ledger operations, but the MCP contract correctly does not infer that canonical secret filtering makes arbitrary canonical content safe for projection.

## Contract Assessment

1. **Raw canonical text and prompt injection:** Strong. Sections 7–9 correctly require projection before the external-model boundary, field allowlisting, unknown-field rejection, treatment of model-interpretable canonical text as untrusted input, and the rule that projected content is data rather than instruction or authority.
2. **Prohibited data:** Strong for this architectural class. Raw ledger payloads, Council deliberation, Operator rationale, local topology, credentials, private repository state, runtime traces, private prompts/plans, security findings, arbitrary canonical free text, and multiple personal/private data classes are denied by default.
3. **User scope:** Correctly framed. User-scoped registration is identified as a discovery/availability choice rather than an authorization boundary. The contract appropriately requires analysis of local-user context, process compromise, environment inheritance, executable replacement, dependency compromise, working-directory independence, and unintended use outside MIRRORNODE repositories.
4. **Local-process threat model:** Adequately represented for a definition. It does not claim stdio is authenticated merely because it is local, and it does not treat registration scope as process isolation.
5. **Failure behavior:** Fail-closed and disclosure-minimized in principle. Ptah’s requested deterministic reason-code revision should be incorporated because stable machine-readable failure semantics also reduce the temptation to emit raw exceptions, paths, or sensitive diagnostic text.
6. **Integrity language:** Strong. The contract explicitly blocks the most dangerous semantic collapse: digest match → truth/approval/authorization/safety. Current prototype wording such as `valid: true` is recorded as evidence and not approved as the future projection vocabulary.
7. **Anti-capabilities:** Substantively strong, but the surface-expansion gate has one protocol-level loophole described below.

## Identified Security Risks

- **Primitive-bypass risk:** Section 17 currently says no fifth *tool* or materially expanded output field may be added without review. MCP servers can expose more than tools. Current official MCP SDK documentation describes server primitives including tools, resources, and prompts, with additional negotiated capabilities. A future implementation could therefore add a resource, prompt, or another protocol output channel without literally adding a fifth tool, creating an avoidable governance bypass.
- **Cross-tool composition risk:** The external model runtime may separately possess shell, repository, browser, deployment, or other operative tools. Read-only MCP data can influence those tools even when MCP itself cannot execute. The contract correctly denies authority transfer, but implementation testing must verify that projected content cannot be interpreted as permission by surrounding orchestration.
- **Resource leakage risk:** A read-only MCP resource could expose canonical files or raw ledger content without violating a tool-only anti-write rule. Projection constraints must apply equally regardless of whether data is returned from a tool, resource, prompt, template, notification, extension, or other server capability.
- **Instruction-channel risk:** MCP prompt templates or server-supplied instructional metadata can influence model behavior without mutating canonical state. A projection-class server must not gain an instruction channel that can alter authority interpretation or bypass the data-only boundary.
- **Error-channel disclosure:** Implementation-generated exception strings can leak local paths, dependency versions, environment details, and source fragments unless the failure contract requires stable disclosure-safe outcomes.
- **Mutable local executable risk:** User-scoped configuration that launches a mutable local executable can continue to expose changed code without a separate registration change. Governed implementation must tie executable identity and version evidence to the reviewed artifact.

## Required Revisions

Two definition-level revisions are required before an accepting disposition:

### 1. Broaden the surface-expansion gate beyond tools

Section 17 must apply to **any new or materially expanded MCP server primitive, capability, or output channel**, not only a fifth tool or expanded tool field.

The contract should state, in protocol-neutral language, that adding or materially expanding any tool, resource, prompt, template, subscription/notification surface, server instruction, extension, or other negotiated capability that can expose data or influence model behavior requires review against the same expansion gate.

This wording should remain capability-generic so protocol evolution cannot create a new ungated channel.

### 2. Make the data/authority boundary primitive-independent

The anti-capability and projection rules should explicitly state that their restrictions apply **regardless of MCP primitive or transport mechanism**. Raw canonical data, authority-bearing language, model instructions, secrets, and operative capability may not be reintroduced through a resource, prompt, metadata channel, notification, extension, or other protocol feature merely because it is not a tool result.

Ptah’s separate deterministic failure/reason-code revision should also be incorporated; Thoth treats that as a shared requirement rather than a third independent revision.

## Permanent Anti-Capabilities

For the read-only projection architectural class, the following must remain impossible regardless of which MCP primitive or transport could technically express them:

- canonical ledger mutation;
- Council matter creation, amendment, acceptance, rejection, revocation, or inferred disposition;
- Operator identity or approval assertion;
- agent-state or runtime-state mutation;
- shell/process execution;
- filesystem or repository writes;
- deployment or publication changes;
- secret, credential, token, cookie, header, or environment-value retrieval;
- direct exposure of raw canonical/private state outside an explicitly approved projection schema;
- projected text or prompt content that grants authority, changes governing instructions, or authorizes execution;
- server-initiated model execution or user-input collection used to evade the read-only projection boundary;
- any alternate protocol primitive, extension, metadata field, or notification path used to bypass the surface-expansion gate;
- conversion of MCP integrity/status output into Operator, Council, security, publication, or runtime authority.

A future write-capable MCP design remains a different architectural class and cannot inherit authorization from CG-0032.

## Recommendation

**Support with required revision.**

The contract has the right security model for a read-only projection surface, including a strong injection boundary and authority-semantics separation. Before acceptance, the expansion and anti-capability language must be made primitive-independent so the governance boundary covers the full MCP server surface rather than only tools.

No executable MCP change, registration change, remote exposure, or output remediation is authorized by this recommendation.