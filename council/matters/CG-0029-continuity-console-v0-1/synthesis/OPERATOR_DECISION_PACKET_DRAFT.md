# CG-0029 Operator Decision Packet

**Matter:** Continuity Console v0.1 Definition  
**Workflow state:** Synthesis-ready  
**Disposition:** Pending  
**Decision authority:** Operator  
**Packet status:** Complete for disposition

## 1. Decision required

Choose whether MIRRORNODE should proceed toward implementation of a public, read-only Continuity Console at `/continuity` in `mirrornode-platform`.

The proposed surface would reuse the existing System Integrity Scorecard as a design and adapter reference, render a build-generated allowlisted snapshot, and leave all execution and approval controls inside private MOPCON.

## 2. Positions received

| Position | Stance | Core finding |
|---|---|---|
| Theia — POS-0001 | Support with conditions | Public orientation and private action must remain separate; use a static build snapshot; expose no direct MOPCON route; create no synthetic health score |
| Ptah — POS-0002 | Support with conditions | Implementation is feasible as a static Next.js server route reading a strict local artifact; generation and build validation must remain separate |
| Osiris — POS-0003 | Support with conditions | The artifact must be an intentionally approved public disclosure product, not an automatically sanitized projection of private systems |

All required reviewers support the direction conditionally. No reviewer opposes the Continuity concept or identifies an architectural blocker.

## 3. Areas of agreement

The positions converge on the following:

1. `/continuity` belongs in `mirrornode-platform` as a static, read-only route.
2. The detached Vite scorecard should not be imported wholesale.
3. Scorecard presentation patterns may be selectively reused.
4. The page should consume one strict, locally stored, build-generated snapshot artifact.
5. The deployed route should perform no request-time GitHub or private-system calls.
6. Generation must use explicit source, field, record-type, and URL allowlists.
7. Unknown fields and schema drift must fail closed.
8. Missing data must render unavailable rather than healthy.
9. `generatedAt` and source `verifiedAt` are distinct facts.
10. Freshness must be computed from source-specific windows and recalculated when rendered.
11. Workflow state, review completion, Operator disposition, merge state, deployment state, and product approval must remain separate.
12. MOPCON actions, routes, prompts, plans, notes, traces, topology, and private health details remain private.
13. Email, calendar, finance, customer, payment, and personal data remain outside public v0.1.
14. No mock fallback, synthetic active-agent count, or inferred overall health score is permitted.
15. Implementation authorization and first-snapshot publication authorization are separate decisions.

## 4. Reconciled implementation shape

### Route

```text
app/continuity/page.tsx
```

Static server component. No fetch calls. No client state required for v0.1.

### Artifact

```text
content/continuity/snapshot.generated.json
```

The artifact remains outside `public/` and is imported through a validating reader.

### Supporting boundary

```text
lib/continuity/contract.ts
lib/continuity/schema.ts
lib/continuity/readSnapshot.ts
lib/continuity/freshness.ts
scripts/generate-continuity-snapshot.mts
scripts/validate-continuity-snapshot.mts
```

### Build behavior

```text
continuity:generate
```

runs manually or in a credential-scoped preparation workflow.

```text
continuity:validate && next build
```

validates the existing artifact without source credentials or network access.

Generation writes to a temporary artifact, validates it, then atomically replaces the previous valid artifact. A failed generation does not overwrite the last valid artifact. With no valid initial artifact, production build fails.

## 5. Conflict and tension analysis

### Retained stale artifact versus failure-closed withdrawal

Ptah permits retaining the last valid artifact and rendering it according to its actual age. Osiris requires failure-closed behavior and warns against silently retaining plausible-looking content.

These positions are compatible if the rule is:

- retained content never receives a new generation or verification timestamp;
- each retained record is visibly stale;
- the page header states that refresh failed;
- sensitive or withdrawn records are removed from the public projection through tombstones;
- no retained snapshot may be presented as current or complete.

### `source-verified` terminology

Ptah uses `source-verified` as a machine authority value. Osiris identifies likely public misinterpretation.

Reconciled rule:

- internal machine value may be `source-checked`;
- visible text states that the source and timestamp were checked;
- the label does not imply product, security, implementation, deployment, or Operator approval.

### Operator-action wording

The current definition permits `Operator action required`. Osiris finds this unsafe by default.

Reconciled rule:

- default public wording: `Further status is not publicly available`;
- an action-required label appears only when the existence and description of that action have separate disclosure approval.

### Append-only continuity versus protective withdrawal

The authoritative repository record remains append-oriented. The public projection may tombstone or withdraw unsafe content without deleting the authoritative source record.

The public artifact must not preserve prohibited content inside client-readable JSON merely to demonstrate immutability.

## 6. Required definition revision

Before implementation authority is granted, the definition must add or change the following:

1. Define source-specific freshness windows.
2. Rename `static-fallback` to `retained-checked-snapshot` or equivalent and prohibit mock or synthetic fallback.
3. Require atomic artifact replacement and preservation of the prior valid artifact on generation failure.
4. Require production-build failure when no valid initial artifact exists.
5. Require strict Zod validation and rejection of unknown fields.
6. Require checked-in source, repository, path, field, record-type, enumeration, and evidence-origin allowlists.
7. Separate source generation from build-time validation.
8. Recalculate freshness during rendering.
9. Exclude private-derived material unless it arrives as a separately approved public projection.
10. Replace the public `source-verified` label with `source checked` and an explicit non-approval explanation.
11. Replace default `Operator action required` wording with `Further status is not publicly available`.
12. Add `disputed`, `corrected`, and `withdrawn` record conditions.
13. Define disagreement behavior without automatic reconciliation.
14. Define a bounded public-history display and retention policy.
15. Prohibit enumerable internal identifiers in public output.
16. Distinguish authoritative append-only preservation from public tombstoning.
17. Validate public HTTPS evidence origins and redirects.
18. Extend prohibited-data inspection across the complete deployable output, including JSON, bundles, source maps, metadata, comments, and published build artifacts.
19. Require content hash and source-revision provenance for the generated artifact.
20. Require human disclosure review of the first populated snapshot.
21. Require separate Operator authorization to publish the first snapshot after route implementation.

## 7. Explicitly prohibited scope

No approval under CG-0029 may authorize:

- runtime execution;
- PR creation, merging, closing, labeling, or mutation;
- autonomous Council transitions or consensus claims;
- private MOPCON URLs or access instructions;
- objectives, prompts, plans, approvals, rejections, notes, results, or traces;
- private health detail, topology, agent availability, model configuration, or routing data;
- email, calendar, contacts, location, family, finance, payment, customer, audit-client, vendor, contract, or personal identity data;
- unpublished vulnerabilities, incidents, severity, remediation, or defensive gaps;
- private repository metadata or strategy-bearing public aggregation;
- arbitrary URLs or source text;
- mock incidents, synthetic counts, or inferred system health;
- request-time GitHub or private-system access;
- publication of the first populated snapshot without separate authorization.

## 8. Remaining Operator-policy questions

The technical and boundary reviews leave four policy values to be set during the revision:

1. Exact freshness windows by source class.
2. Public continuity-history display horizon.
3. Final Platform navigation placement.
4. Final canonical Mirror Mirror route.

These do not invalidate the concept, but they prevent the present definition from being implementation-ready.

## 9. Decision options

### Option A — Ratify for implementation now

Not recommended. The current definition does not yet contain the required failure, freshness, disclosure, history, and publication rules.

### Option B — Revision required

Recommended.

Effect:

- preserve all three attributed positions;
- revise the definition with the reconciled requirements in Section 6;
- keep PR #29 draft;
- grant no Platform implementation or deployment authority yet;
- return the revised definition for a narrow confirmation pass;
- then present a ratification decision.

### Option C — Park

Use only if current business or competition priorities make the work premature.

### Option D — Reject

Not supported by the evidence. No required reviewer recommends rejection.

## 10. Final recommendation

**Select Option B — Revision required.**

The product direction is coherent, useful, and technically feasible. The remaining defects are not reasons to abandon it; they are exactly the kind of disclosure and failure-boundary details that must be settled before a public continuity surface exists.

The revision should be tightly bounded to the requirements in Section 6. It should not reopen the governing purpose, move actions into Continuity, add personal integrations, or expand the product scope.

After the revision, Ptah and Osiris need only confirm that their requested conditions were incorporated. A new broad deliberation is unnecessary unless the revision changes the product boundary.

## 11. Operator disposition block

```yaml
matterId: CG-0029
status: revision-required
authority: operator
decidedAt: <timestamp>
selectedOption: B
rationale: >-
  The Continuity Console direction is accepted in principle, but the definition
  requires the reconciled freshness, generation-failure, disclosure,
  public-history, evidence-link, and first-publication controls identified by
  the required Ptah and Osiris reviews before implementation authority may be
  granted.
approvedScope:
  - revise the definition using the bounded requirements in the decision packet
  - preserve all attributed positions and disagreement context
  - prepare the revised definition for narrow confirmation review
prohibitedScope:
  - Platform implementation
  - deployment
  - publication of a populated snapshot
  - MOPCON or runtime changes
  - personal integration ingestion
  - private data projection
nextAction: >-
  Revise CONTINUITY_CONSOLE_V0_1_DEFINITION.md according to Section 6 and return
  the revision for Ptah and Osiris confirmation.
canonAction: none
```

## 12. Authority note

This synthesis does not itself select Option B. Only the Operator may record the disposition.