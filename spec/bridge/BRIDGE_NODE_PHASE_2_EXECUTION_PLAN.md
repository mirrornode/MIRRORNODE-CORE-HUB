---
title: Bridge Node Phase 2 Execution Plan
status: draft
claim_class: spec
verification_status: implementation_pending
date: 2026-05-29
owner: Siseon
prepared_by: THEIA
source_receipt: canon/status/MIRRORNODE_PHASE_2_STATE_RECEIPT_2026-05-29.md
---

# Bridge Node Phase 2 Execution Plan

## Purpose

Bridge Node v0.1 is the governed interop layer for MIRRORNODE multi-AI handoffs.

It is not another personality agent. It is a protocol boundary that classifies, routes, validates, and records cross-node communication.

## Operating Law

```text
No cross-node handoff bypasses Hermes or Bridge.
No canon proposal bypasses Judge.
No memory/archive write bypasses Librarian.
No verified-state claim is promoted without evidence.
Operator approval is required for canon promotion.
```

## Core Questions

Every Bridge event must answer:

1. Who is speaking?
2. What claim class is being asserted?
3. What event type is being emitted?
4. What node receives it?
5. What validation gate applies?
6. What write target is allowed?
7. What provenance supports the payload?

## BridgeEnvelope v0.1

Bridge events must conform to `schemas/bridge/bridge-envelope.schema.json`.

Required top-level fields:

```text
id
timestamp
source_node
target_node
event_type
claim_class
payload
routing
provenance
```

## Event Types

| Event Type | Purpose |
| --- | --- |
| handoff | Transfer task/state from one node to another |
| reflection | Mirror-style interpretive response or synthesis |
| canon_proposal | Candidate material for canon/spec/codex promotion |
| research_result | External information returned by research node |
| contradiction | Detected conflict between claims, sources, or states |
| operator_directive | Explicit command from Siseon |
| security_verdict | Thoth/TESLA-LAW9/Ptah-style security or enforcement output |

## Claim Classes

| Claim Class | Handling |
| --- | --- |
| verified | Requires direct evidence and verification record |
| spec | May enter spec layer pending implementation |
| spec_behavioral | Requires test reference before promotion |
| symbolic | Must remain in codex/symbolic or clearly marked symbolic sections |
| session | May be archived; not canon by default |

## Routing Rules

### Hermes

Hermes remains mandatory ingress/egress.

Hermes may emit:

- `operator_directive`
- `handoff`
- `security_verdict`

Hermes must not write canon directly.

### Bridge

Bridge classifies and routes envelopes.

Bridge may decide:

- whether Judge is required;
- whether Librarian is required;
- whether Operator approval is required;
- which write target is allowed.

Bridge must not override Judge denial.

### Judge

Judge validates canon proposals, contradiction events, and claim-class correctness.

Judge receives events when:

```text
routing.requires_judge = true
```

Judge may return:

```text
allow
reject
revise
escalate_to_operator
```

### Librarian

Librarian handles archive, memory, versioning, historical decisions, and agent-specific overlays.

Librarian receives events when:

```text
routing.requires_librarian = true
```

Librarian may write to:

```text
archive
session
spec
codex
```

Librarian must not promote to verified canon without Judge pass and Operator approval.

### HARPA

HARPA is an ingestion/collection surface.

HARPA may emit:

- `research_result`
- `canon_proposal`
- `handoff`

HARPA output must include provenance.

### Mirror / Grok / External Model Nodes

External model reflections may emit:

- `reflection`
- `contradiction`
- `canon_proposal`
- `research_result`

These events default to `claim_class: session` unless evidence supports stronger classification.

## Minimal Test Flow

The first full Bridge loop must prove this sequence:

```text
HARPA ingestion
  -> Hermes event
  -> Bridge classification
  -> Mirror reflection
  -> Judge validation
  -> Librarian archive/spec/canon decision
  -> Operator receipt
```

## Acceptance Criteria

Bridge Node v0.1 is acceptable when:

- every cross-node event is wrapped in BridgeEnvelope v0.1;
- every event has provenance;
- symbolic/session/spec/verified claims are separated;
- canon proposals require Judge;
- archive or memory writes require Librarian;
- canon promotion requires Operator approval;
- unverified repo, deployment, and endpoint claims remain marked pending verification;
- failure paths are explicit and default-deny.

## Failure Modes

| Failure | Required Response |
| --- | --- |
| Missing provenance | reject or request revision |
| Unknown source node | route to security review |
| Symbolic content aimed at engineering canon | reclassify to symbolic or reject |
| Verified claim without evidence | downgrade to session/spec or reject |
| Judge denial | default deny; no write to canon |
| Conflicting claims | emit contradiction event |
| Operator approval missing | hold in pending state |

## Implementation Steps

1. Add BridgeEnvelope schema.
2. Add a minimal Bridge classifier function.
3. Add fixture events for HARPA, Mirror, Judge, Librarian, and Operator.
4. Add tests for successful routing and default-deny cases.
5. Add a smoke run that emits an Operator receipt.
6. Connect to HUD only after test harness passes.

## Phase 2 Locked Objective

```text
Build the smallest Bridge that prevents drift.
```

Do not expand the node roster until BridgeEnvelope, routing, and default-deny behavior are proven.
