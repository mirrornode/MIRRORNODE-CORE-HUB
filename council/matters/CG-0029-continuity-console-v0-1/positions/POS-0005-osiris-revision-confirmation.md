---
schemaVersion: "0.1"
id: POS-0005
matterId: CG-0029
author: osiris
role: disclosure-boundary-confirmation
kind: condition
createdAt: 2026-07-19T09:42:00Z
source:
  form: agent-response
  reference: PR-29-revision-confirmation
  capturedBy: operator
  receipt: null
contentPath: council/matters/CG-0029-continuity-console-v0-1/positions/POS-0005-osiris-revision-confirmation.md
respondsTo:
  - POS-0003
supersedes: null
stance: support-with-conditions
claims:
  - All Osiris definition-level conditions are resolved.
  - Remaining conditions are future implementation and authorization gates.
requestedChanges: []
provenanceNotes:
  - The fuller of two substantively duplicate Osiris confirmation responses supplied by the Operator was registered as the canonical supplemental position.
  - This confirmation does not authorize implementation, populated-snapshot generation, deployment, or publication.
immutableOriginal: true
---

# Osiris revision confirmation

## Result

confirmed-with-residual-conditions

## Conditions resolved

The revised `CONTINUITY_CONSOLE_V0_1_DEFINITION.md` resolves the definition-level conditions recorded in POS-0003:

1. Private-derived material is excluded unless supplied as a separately approved public projection. The generator is prohibited from inspecting private payloads and deciding what excerpt is safe.

2. Freshness windows are defined for each permitted source class. Freshness is calculated from `verifiedAt`, rendering time, and source class during generation and independently recalculated during rendering.

3. Visible `source-verified` language is replaced with `source checked` and `source-checked`. The definition requires the clarification:

   > Source and timestamp checked; underlying state not approved by this label.

4. Default `Operator action required` wording is replaced with:

   > Further status is not publicly available.

   Action-required wording is permitted only after separate affirmative publication approval.

5. Public GitHub records, evidence links, and Council data are explicitly treated as publication candidates requiring review and allowlisting. Public visibility alone does not authorize aggregation.

6. `disputed`, `corrected`, and `withdrawn` conditions are defined for public records. The snapshot model also distinguishes partial and unavailable conditions.
