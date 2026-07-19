# CG-0029 — Continuity Console v0.1 Definition

**Workflow state:** Closed  
**Disposition:** Revision required  
**Revision confirmation:** Complete  
**Final authority:** Operator

## Decision question

Should MIRRORNODE repurpose the existing System Integrity Scorecard into a read-only Continuity Console at `/continuity`, with private operational actions remaining exclusively in MOPCON?

## Recorded disposition

The Operator accepted the direction in principle and authorized revision of the definition against the reconciled Ptah and Osiris conditions.

The disposition did not authorize:

- Platform implementation,
- populated-snapshot generation,
- deployment,
- publication,
- MOPCON or runtime changes,
- personal or private data projection.

## Revised ruling

- Reuse the scorecard's visual and adapter concepts rather than importing the detached Vite application.
- Implement the canonical route in `mirrornode-platform` only after separate implementation authorization.
- Render a strict, build-generated, allowlisted snapshot with no request-time private-system access.
- Show current system, active work, Council matters, and a bounded continuity record.
- Require source references, verification time, calculated freshness, visibility, authority, and artifact provenance.
- Keep execution, approval, private traces, Operator notes, and private routes inside MOPCON.
- Exclude email, calendar, finances, customer data, and other personal integrations from public Continuity v0.1.
- Require separate first-snapshot disclosure review and later publication authorization.

## Confirmation positions

- `POS-0004` — Ptah: **confirmed**; no remaining definition-level implementation blockers.
- `POS-0005` — Osiris: **confirmed with residual conditions**; no remaining definition defects, with implementation and publication gates preserved.

## Current artifact

[`CONTINUITY_CONSOLE_V0_1_DEFINITION.md`](../../../docs/continuity/CONTINUITY_CONSOLE_V0_1_DEFINITION.md)

## Why this matter exists

The scorecard already provides a real but detached local status surface. Platform is intentionally a static public orientation layer, while MOPCON contains explicit runtime actions and Operator decision controls. This matter defines a safe bridge between those roles without creating another product or exposing private operations.

## Next required step

The Operator decides whether PR #29 may be finalized and merged as a documentary definition-and-record action only. A separate Council matter must authorize any Platform implementation.