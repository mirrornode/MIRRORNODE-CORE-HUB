# CM-SOURCE-001 — Source & Custody Model Candidate

**Status:** Candidate / not canonical  
**Vocabulary:** `TERMINOLOGY_STANDARD_CANDIDATE.md`  
**Purpose:** Make it immediately clear what governs, what is current, what executes, what proves a claim, and what is merely projected for another audience.

## 1. CANON — ratified governance state

Primary governed surface: `MIRRORNODE-CORE-HUB` and its explicit promotion records.

Canon contains ratified governance, authority boundaries, contracts, schemas, promotion records, and supersession relationships. A canonical statement may become stale relative to implementation; staleness is recorded as a discrepancy until a successor is explicitly promoted.

## 2. OPERATIONAL STATE — current, provenance-backed state

Operational state answers “what is happening now?” It is assembled from current owning sources and MUST retain provenance. It does not silently override canon and it does not substitute for implementation evidence.

`mirrornode-workspace` is a current operating synthesis surface for business development, continuity, advisor preparation, and working records. Its role is synthesis/custody, not governance ratification.

## 3. IMPLEMENTATION STATE — code and services that actually exist or execute

Implementation state belongs to the repository, deployment, or authenticated service implementing the surface.

| Surface | Current owning source / custody |
|---|---|
| Agent runtime | `mirrornode-agent-runtime` |
| Operator console / MOPCON | `mirrornode-operator-console` |
| Public/product implementation | `mirrornode-platform` |
| Governance canon and promotion records | `MIRRORNODE-CORE-HUB` |
| Business/continuity operating synthesis | `mirrornode-workspace` |

An implementation repository proves what is implemented only to the extent that the relevant branch, commit, deployment, or service state is verified.

## 4. EVIDENCE — attributable support for a claim

Evidence may include:

- commits and pull requests;
- review threads and reviewer verdicts;
- authenticated permission records;
- tests and CI results;
- deployment/service state;
- decision and disposition records;
- action receipts and traces;
- external correspondence that proves a permission, event, or commitment.

A green CI result is evidence for the checks that actually ran. It is not evidence that every semantic defect has been excluded. PR #35 and PR #36 are explicit examples: configured checks passed while later Codex review identified verifier bypasses.

## 5. PROJECTION — derived views for another audience

A projection is a bounded view generated from other source classes. Examples include MOPCON, `@mirror` handoffs, advisor packets, dashboards, and public status pages.

Projection rules:

1. retain source/provenance;
2. state freshness and verification level;
3. do not invent authority;
4. do not become a competing manual truth set;
5. separate verified facts from candidate interpretation.

## 6. AUTHORITY — a separate dimension, not a source class

Authority describes who may decide, approve, ratify, veto, or direct within a defined envelope. It is intentionally separated from repository custody and technical capability.

Examples:

- Siseon holds final governance disposition.
- Ptah has an evaluation/promotion role under current CORE-HUB governance.
- Thoth security verdicts are a distinct review boundary.
- `SYSTEM_CONTRACT.md` uses **execution authority** for LUCIAN; in this workstream that is interpreted as contract-scoped **runtime execution authority**, not final governance authority.

## Conflict rule

When records conflict:

1. Name each record's class: canon, operational state, implementation state, evidence, or projection.
2. Name the owning source/custodian.
3. Name the relevant authority or review lane separately.
4. Mark the discrepancy and its verification state.
5. Prefer direct implementation/evidence sources for claims about what currently executes, while preserving canon as the governing record until formally superseded.
6. Resolve through the appropriate review/promotion path.
7. Preserve superseded history and link the successor.

## Current high-value discrepancy

The April 28 `SYSTEM_CONTRACT.md` says it is “the operational truth until the runtimes change,” declares LUCIAN on port 7700 and `POST /dispatch`, while later `mirrornode-agent-runtime` history includes an Operator-approval execution change dated July 22. That is sufficient to classify the April contract's implementation-freshness claim as **requiring reconciliation**, not sufficient by itself to rewrite the contract.

## MOPCON rule

MOPCON should project verified canon, operational state, implementation state, evidence freshness, discrepancy state, and permitted actions. It should not maintain a separate manually curated authority model.
