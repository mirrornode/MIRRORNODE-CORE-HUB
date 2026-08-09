# CM-SOURCE-001 — Source Model Candidate

**Status:** Candidate / not canonical  
**Purpose:** Shared model for reconciliation and review.

## 1. CANON — what governs

Primary authority surface: `MIRRORNODE-CORE-HUB`.

Canon contains ratified governance, authority boundaries, contracts, schemas, promotion records, and supersession relationships. Canon changes require the established promotion gate.

## 2. OPERATIONAL STATE — what is true now

Operational state is a provenance-preserving synthesis of current records. It MUST identify its owning sources and MUST NOT override canon or implementation truth.

`mirrornode-workspace` is a current operating synthesis surface for business development, continuity, advisor preparation, and working records.

## 3. IMPLEMENTATION TRUTH — what exists and executes

Implementation truth belongs to the owning repository, deployment, or authenticated service surface.

Initial ownership map:

| Surface | Owning source |
|---|---|
| Agent runtime | `mirrornode-agent-runtime` |
| Operator console | `mirrornode-operator-console` |
| Public/product implementation | `mirrornode-platform` |
| Governance canon | `MIRRORNODE-CORE-HUB` |
| Business/continuity operating synthesis | `mirrornode-workspace` |

## 4. EVIDENCE — what proves a claim

Evidence may include:

- Git commits and signed/attributable changes;
- pull requests and review records;
- permission grants and authenticated principal records;
- tests and CI results;
- deployment state;
- decision records;
- action receipts;
- service-generated audit trails;
- external correspondence when it evidences a real permission or event.

Evidence must retain provenance and should be referenced rather than recopied when possible.

## 5. REFERENCE — what another principal receives

A reference is a bounded, versioned projection of source material for a specific principal or task. `@mirror` is proposed as the standard handoff envelope for this purpose.

Reference material does not become authoritative merely because it is convenient or current-looking.

## 6. PUBLIC — what outsiders may rely upon

Public material is a deliberate projection from verified source and approved disclosure rules. It must avoid exposing credentials, private reasoning, security-sensitive implementation detail, or claims that have not cleared the appropriate authority/evidence gate.

## Conflict rule

When sources conflict:

1. Do not silently choose.
2. Identify the type of each source: canon, state, implementation, evidence, reference, public.
3. Identify the owning authority.
4. Mark the discrepancy.
5. Resolve through the appropriate gate.
6. Preserve the superseded record and link the successor.

## Maintenance rule

MOPCON should project this model rather than maintain a competing manual truth set. The console should surface source, authority, evidence freshness, discrepancy state, and permitted actions for every material claim or principal.
