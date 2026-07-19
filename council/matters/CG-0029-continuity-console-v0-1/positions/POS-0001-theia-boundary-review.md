---
schemaVersion: "0.1"
id: POS-0001
matterId: CG-0029
author: theia
role: synthesis-and-authority-review
kind: condition
createdAt: 2026-07-18T16:10:00Z
source:
  form: agent-response
  reference: PR-29-review-round-1
  capturedBy: theia
  receipt: null
contentPath: council/matters/CG-0029-continuity-console-v0-1/positions/POS-0001-theia-boundary-review.md
respondsTo: []
supersedes: null
stance: support-with-conditions
claims:
  - Continuity should remain a public read-only orientation surface.
  - MOPCON should remain the private action surface.
  - The existing scorecard is a valid design and adapter reference.
requestedChanges:
  - Use static rather than reviewed for the v0.1 MIRRORFRAME surface state.
  - Generate a build-time allowlisted snapshot rather than calling GitHub at request time.
  - Do not expose a direct private MOPCON route in public v0.1.
  - Replace overall health language with snapshot completeness and freshness.
provenanceNotes:
  - Review grounded in the scorecard source, Platform public-boundary metadata, MOPCON PR #3, and the MIRRORFRAME state rules.
immutableOriginal: true
---

# Theia boundary review

## Position

Support the Continuity Console v0.1 direction with the conditions listed below.

## Conditions resolved in the current revision

1. **Surface state** — The page is `static`; individual records may be source-verified. Source verification is not equivalent to human review.
2. **Generation model** — v0.1 uses a build-generated, allowlisted snapshot. The public page does not hold GitHub credentials or depend on request-time private-system calls.
3. **Private routing** — public Continuity does not expose a direct MOPCON URL without an authenticated handoff layer.
4. **No synthetic score** — the header reports snapshot condition, completeness, and freshness rather than inventing an overall system-health score.

## Remaining questions

- exact freshness windows by source class,
- final Mirror Mirror route,
- whether snapshot generation requires a signed manifest,
- Platform navigation placement.

## Recommendation

Advance CG-0029 from framing to assembled after the revised definition and this attributed position are registered. Implementation authority should wait for Ptah feasibility review and Osiris boundary review.