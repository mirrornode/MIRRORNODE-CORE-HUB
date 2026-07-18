# CG-0029 — Continuity Console v0.1 Definition

**Workflow state:** Framing  
**Disposition:** Pending  
**Final authority:** Operator

## Decision question

Should MIRRORNODE repurpose the existing System Integrity Scorecard into a read-only Continuity Console at `/continuity`, with private operational actions remaining exclusively in MOPCON?

## Proposed ruling

- Reuse the scorecard's visual and adapter concepts.
- Implement the canonical route in `mirrornode-platform`.
- Show current system, active work, council matters, and continuity record.
- Require source, verification time, freshness, visibility, and authority metadata for displayed status.
- Keep execution, approval, private traces, and Operator notes inside MOPCON.
- Exclude email, calendar, finances, and other personal integrations from public Continuity v0.1.

## Current artifact

[`CONTINUITY_CONSOLE_V0_1_DEFINITION.md`](../../../docs/continuity/CONTINUITY_CONSOLE_V0_1_DEFINITION.md)

## Why this matter exists

The scorecard already provides a real but detached local status surface. The current Platform is intentionally a static public orientation layer, while MOPCON contains explicit runtime actions and Operator decision controls. This matter defines a safe bridge between those roles without creating another product or exposing private operations.

## Next required step

Review the public/private boundary, data truth model, scorecard reuse plan, and implementation scope before granting implementation authority.