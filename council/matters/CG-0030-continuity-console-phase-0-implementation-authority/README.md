# CG-0030 — Continuity Console v0.1 Phase 0 Implementation Authority

## Final State

**Workflow state:** Closed  
**Operator disposition:** `accepted`  
**Authority effect:** bounded Phase 0 implementation and local validation only

CG-0030 authorizes a **bounded Phase 0 implementation** of the public, read-only `/continuity` route in `mirrornode-platform`, using a validated, build-generated public snapshot artifact with a strict typed contract.

It does **not** authorize deployment, publication, a populated production snapshot, private-data ingestion, MOPCON modification, runtime modification, or inferred authority.

## Anchors

This authority stands on:

- **CG-0029** — merged Continuity Console definition.
- **PR #29** — merged definition-and-record action.
- **CL-0000** — Operator Continuity Ledger invariant: the ledger records and does not decide, execute, publish, or infer authority.
- **PR #30** — merged Operator Continuity Ledger v0.1.
- **Platform/MOPCON boundary** — `/continuity` is a public Platform presentation surface; MOPCON remains separate and private.

## Authorized Phase 0 Scope

Phase 0 may implement and locally validate:

- an implementation branch in `mirrornode/mirrornode-platform` for `/continuity`;
- a static, read-only `/continuity` route rendered from a validated build-generated public snapshot;
- a narrow typed snapshot schema with strict validation;
- checked-in allowlists for sources, fields, paths, enums, and evidence links;
- fixture-only development data;
- calculated freshness and source-class freshness windows;
- atomic snapshot replacement and retained last-valid behavior;
- failure-closed production-build validation;
- accessibility and responsive-layout validation;
- lint, type-check, tests, and production-build validation;
- an implementation evidence packet.

## Explicitly Not Authorized

CG-0030 does not authorize:

- a populated production snapshot or live continuity data;
- deployment;
- publication or external announcement;
- private ledger ingestion;
- request-time GitHub, Council, runtime, or MOPCON access;
- customer, personal, secret, or private operational data;
- MOPCON modification;
- runtime modification;
- Operator controls or dashboards;
- CL or CG record writes;
- autonomous Librarian or background-agent behavior;
- inferred approval or authority from `source-checked` status.

## Required Reviews

The required advisory reviews are recorded:

- **POS-0001 — Ptah:** `feasible-with-conditions`; no definition revision required.
- **POS-0002 — Osiris:** `safe-with-conditions`; no additional definition-level privacy or authority control required.

Their conditions are already encoded in this matter and the merged Continuity definition.

## Post-Implementation Gates

Even after Phase 0 implementation and local validation succeed, the following remain separate future decisions:

- populated snapshot review;
- disclosure review;
- deployment authority;
- publication authority;
- any expansion beyond the authorized Phase 0 boundary.

## Operator Disposition

The Operator accepted CG-0030 on 2026-07-24 after the required Ptah and Osiris reviews.

The recorded disposition authorizes only the bounded Phase 0 implementation and local-validation scope described above. All later exposure, production-data, deployment, and publication decisions remain separately governed.
