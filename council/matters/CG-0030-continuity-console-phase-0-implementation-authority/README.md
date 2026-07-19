# CG-0030 — Continuity Console v0.1 Phase 0 Implementation Authority

## Purpose

CG-0030 is a **proposed** governance matter. It does not grant authority by itself.

Its purpose is to decide whether to authorize a **bounded Phase 0 implementation** of the public, read-only `/continuity` route in `mirrornode-platform`, using a **validated, build-generated public snapshot artifact** with a strict, typed contract. Implementation and local validation are the only authorities requested by this matter. Deployment, publication, and populated production snapshots require separate Council matters and recorded Operator disposition.

## Anchors

This matter stands on MIRRORNODE's own recorded authority:

- **CG-0029** — Continuity Console definition and public `/continuity` surface design.
- **Merged PR #29** — Recorded Platform definition of the Continuity Console.
- **CL-0000** — Purpose and invariant of the Operator Continuity Ledger: it records, and does not decide, execute, publish, or infer authority.
- **Merged PR #30** — Operator Continuity Ledger v0.1, including CL-0000 and the non-operative boundary.
- **Platform vs MOPCON boundary** — The `/continuity` route is a public Platform surface; MOPCON remains a separate, private governance console.

CG-0030 may only be accepted once all anchor requirements in `matter.yaml` are satisfied.

## Phase 0 Scope

Phase 0 is deliberately small. It requests **implementation and local validation only**, under a strict public boundary.

### Authorized (Requested)

If CG-0030 is accepted, Phase 0 may implement:

- An implementation branch in `mirrornode/mirrornode-platform` for `/continuity`.
- A **static, read-only** `/continuity` route that renders from a validated, build-generated public snapshot artifact.
- A narrow, typed public snapshot contract with strict schema validation and checked-in allowlists for sources, fields, paths, enums, and evidence links.
- Fixture-only development data; no live continuity data and no production data.
- Calculated freshness and source-class freshness windows, with explicit `as of` metadata and retained last-valid snapshot behavior.
- Failure-closed production build validation: if no valid snapshot artifact exists, the production build must fail. An invalid or newly generated artifact must never replace the retained last-valid artifact.
- Accessibility, responsive layout, lint, type-check, tests, and production build validation.
- Preparation of an implementation evidence packet: diff, schema, allowlists, fixture snapshot, validation and freshness tests, retained-valid behavior tests, build results, and Platform/MOPCON boundary confirmation.

### Not Authorized

Phase 0 does **not** authorize:

- Any populated production snapshot or live continuity data.
- Deployment of `/continuity` to production or public environments.
- Publication or external announcement of continuity information via the Platform route.
- Private Ledger ingestion or direct use of Council, GitHub, runtime, or MOPCON state at request time.
- Use of customer data, personal data, secrets, or private operational material.
- Operator controls, dashboards, or actions in `/continuity`.
- Editing or authoring of continuity records (CL) or governance records (CG) via the Platform route.
- Autonomous Librarian behavior, background agents, or automatic generation of CL/CG records.
- Any language that implies approval or authority merely because material is source-checked.

## Data, Rendering, and Language Boundaries

Phase 0 is bounded by three structural constraints:

- **Data boundary:** development data is fixture-only; production data, private sources, and request-time sources are prohibited. Any private-derived material must pass through an approved public projection before it can appear in a snapshot.
- **Rendering boundary:** `/continuity` is public, read-only, and snapshot-driven. It does not support operator actions, editing, decision generation, execution, publication authority, or authority inference.
- **Language constraints:** the route may use status language such as `source-checked`, `current`, `stale`, and `unavailable`. Authority terms such as `source-verified`, `approved`, `authorized`, and `ratified` are prohibited. Source checking does **not** constitute approval, authorization, ratification, or publication authority.

These boundaries keep Phase 0 firmly in a presentation-of-governed-material posture.

## Platform vs MOPCON

CG-0030 applies only to the **Platform** `/continuity` route:

- Platform: public, read-only, snapshot-driven.
- MOPCON: unmodified by this matter; private record access, searching, and correlation remain **not authorized** by CG-0030 and require separate governance.

No MOPCON behavior is changed or permitted by accepting this Phase 0 implementation authority.

## Reviews, Evidence, and Post-Implementation Gates

CG-0030 requests:

- **Ptah** — Implementation feasibility review limited to the typed snapshot contract, checked-in allowlists, generation/validation separation, fixture-only data, retained last-valid behavior, and failure-closed build behavior.
- **Osiris** — Privacy, authority, and disclosure review limited to public/private field boundaries, publication candidacy, freshness, non-approving language, retained last-valid behavior, and nondisclosure on failure.

Acceptance requires an evidence packet as enumerated in `acceptanceEvidence` in `matter.yaml`. Even after implementation is complete, the following gates remain:

- Populated snapshot review.
- Deployment authority.
- Publication authority.
- Disclosure review.
- A separate Council matter to grant any of these.

## Operator Disposition

CG-0030 encodes that **authority remains latent**:

- `workflowState: proposed` and `authorityEffect: none-until-operator-disposition` must remain in place while the matter is under review.
- Operator disposition and rationale must be recorded before any implementation becomes effective.

Creating CG-0030 records a proposal. Only the Operator's recorded disposition can turn that proposal into a live implementation authority.

## Constitutional Boundary

CG-0030 authorizes only a bounded implementation effort.

It does not modify the authority order established by the Operator Continuity Ledger, does not alter Council Grounds governance, and does not create new authority for the Platform.

The `/continuity` route remains a presentation surface whose authority derives entirely from previously approved governance artifacts.
