---
schemaVersion: "0.1"
id: POS-0002
matterId: CG-0029
author: ptah
role: implementation-feasibility-review
kind: condition
createdAt: 2026-07-19T09:00:00Z
source:
  form: agent-response
  reference: operator-provided-session-response
  capturedBy: operator
  receipt: null
contentPath: council/matters/CG-0029-continuity-console-v0-1/positions/POS-0002-ptah-implementation-review.md
respondsTo:
  - POS-0001
supersedes: null
stance: support-with-conditions
immutableOriginal: true
---

# Ptah implementation review

## Stance

support-with-conditions

## Feasibility finding

Platform can implement `/continuity` without importing the detached Vite scorecard application wholesale.

The current `mirrornode-platform` structure already supports the required implementation:

* Next.js App Router
* strict TypeScript
* JSON module imports
* Zod for runtime validation
* Vitest for contract and transformation tests
* static server-component rendering
* existing public-orientation components and styling patterns

The scorecard’s Vite shell, client-side fetch lifecycle, environment configuration, and silent mock fallback should not be migrated. The useful portion is its presentation vocabulary and adapter concept.

MOPCON PR #3 confirms a technically distinct private action boundary: runtime proxying, objective submission, approval/rejection, execution, and trace retrieval remain in MOPCON. None of those facilities are required by `/continuity`.

The implementation is feasible as a static route consuming a validated local artifact. It requires no runtime GitHub credentials, request-time network calls, cross-repository writes, private MOPCON access, or client-side state synchronization.

## Proposed file and route structure

```text
mirrornode-platform/
├── app/
│   └── continuity/
│       ├── page.tsx
│       ├── loading.tsx              # optional; unnecessary if fully static
│       └── _components/
│           ├── SnapshotHeader.tsx
│           ├── CurrentSystem.tsx
│           ├── ActiveWork.tsx
│           ├── CouncilMatters.tsx
│           ├── ContinuityRecord.tsx
│           ├── EvidenceLabel.tsx
│           └── UnavailableState.tsx
├── content/
│   └── continuity/
│       └── snapshot.generated.json
├── lib/
│   └── continuity/
│       ├── contract.ts
│       ├── schema.ts
│       ├── readSnapshot.ts
│       └── freshness.ts
├── scripts/
│   ├── generate-continuity-snapshot.mts
│   └── validate-continuity-snapshot.mts
└── tests/
    └── continuity/
        ├── contract.test.ts
        ├── freshness.test.ts
        ├── generator.test.ts
        ├── allowlist.test.ts
        └── rendering.test.tsx
```

`snapshot.generated.json` should live under `content/continuity/`, not `public/`.

Keeping it outside `public/` prevents the raw artifact from automatically becoming a separately addressable endpoint. The server component should import it through `readSnapshot.ts`, validate it, and render only the intended fields.

`page.tsx` should remain a server component with no fetch calls and no `"use client"` directive unless a purely presentational interaction later requires one.

## Minimal snapshot contract

```ts
type Freshness = "current" | "aging" | "stale" | "unknown";
type Visibility = "public" | "operator-summary-only";
type Authority =
  | "informational"
  | "source-verified"
  | "operator-disposition";

type Evidence = {
  source: {
    label: string;
    href: string | null;
  };
  verifiedAt: string | null;
  freshness: Freshness;
  visibility: Visibility;
  authority: Authority;
};

type SystemItem = Evidence & {
  id: string;
  name: string;
  presentationState: string;
  boundary: string;
  nextRoute: string | null;
  actionRequired: boolean;
};

type WorkItem = Evidence & {
  id: string;
  title: string;
  status:
    | "active"
    | "waiting-verification"
    | "blocked"
    | "stale-review"
    | "completed";
  context: string;
};

type CouncilMatter = Evidence & {
  id: string;
  decisionQuestion: string;
  workflowState: string;
  disposition: "pending" | "ratified" | "revision-required" | "parked" | "rejected";
  reviewsReceived: string[];
  reviewsMissing: string[];
  unresolvedObjections: string[];
  nextRequiredStep: string | null;
};

type ContinuityEvent = Evidence & {
  id: string;
  occurredAt: string;
  eventType:
    | "merge"
    | "disposition"
    | "canon-action"
    | "handoff"
    | "deployment-verification"
    | "state-change"
    | "correction";
  actor: string;
  description: string;
  corrects: string | null;
};

type ContinuitySnapshot = {
  schemaVersion: "0.1";
  generatedAt: string;
  condition: "complete" | "partial" | "stale" | "unavailable";
  sourceMode:
    | "source-verified-snapshot"
    | "partial-snapshot"
    | "static-fallback"
    | "unavailable";
  generation: {
    succeeded: boolean;
    attemptedAt: string;
    lastSuccessfulAt: string | null;
    failureCode: string | null;
  };
  sections: {
    currentSystem: SystemItem[];
    activeWork: WorkItem[];
    councilMatters: CouncilMatter[];
    continuityRecord: ContinuityEvent[];
  };
};
```

The contract should not include arbitrary metadata bags. Open-ended fields weaken the allowlist and create an accidental disclosure channel.

Freshness should be calculated during generation from explicit source-class thresholds, then independently checked during rendering against the current time. This prevents an artifact generated as `current` from remaining visually current indefinitely.

## Generation and failure behavior

Use a controlled command:

```text
npm run continuity:generate
```

mapped to:

```text
tsx scripts/generate-continuity-snapshot.mts
```

or an equivalent checked-in TypeScript runner.

The generator should:

1. Read a checked-in source allowlist.
2. Read only approved public sources and explicitly supplied safe verification summaries.
3. Normalize them into the snapshot contract.
4. Reject unknown fields and unsupported authority values.
5. calculate freshness using declared source-class thresholds.
6. Write to a temporary file.
7. Validate the complete temporary artifact.
8. Atomically replace `snapshot.generated.json` only after successful validation.

`next build` should not implicitly contact GitHub or private systems. Its prebuild responsibility should be validation only:

```text
npm run continuity:validate && next build
```

Generation should occur manually or in a credential-scoped preparation workflow before the Platform build. That workflow may read other repositories but must write only the Platform snapshot artifact or a CI handoff artifact. It must not mutate source repositories.

On generation failure:

* Do not overwrite or delete the last valid snapshot.
* Do not update `generatedAt` or `lastSuccessfulAt`.
* Record the failed attempt separately in CI output or a controlled generation receipt.
* Render the retained snapshot according to its actual age.
* Promote the page-level condition to `stale` when its freshness window expires.
* If no previously valid artifact exists, fail the production build rather than generate mock content.
* If the artifact is valid but partial, render available sections and explicitly mark missing sections unavailable.
* Never infer success from the generator process merely completing; schema and allowlist validation must pass.

A failed refresh therefore leaves visible old evidence with an old timestamp. It cannot manufacture the appearance of a newer snapshot.

## Reuse versus rewrite

Reusable from the scorecard:

* status-band layout pattern
* source badges
* last-sync/generated-at presentation
* card-based system overview
* incident/attention-list visual hierarchy
* adapter boundary between source material and rendered records
* degraded-state visual treatment

These should be reused as patterns or selectively ported presentational markup—not imported as a Vite application dependency.

Rewrite for Next.js:

* the application shell
* `useEffect` loading flow
* `getSystemSnapshot()`
* Vite `import.meta.env` configuration
* API and WebSocket URL display
* live-endpoint health inference
* active-agent count
* incident mock data
* silent catch-to-mock fallback
* `live endpoint | mock fallback` source model
* global scorecard types derived from `typeof mockSystem`

The new contract must be defined independently of sample data. Types derived from a mock object are not acceptable for this boundary.

## Required tests

Implementation verification requires:

1. **Contract validation**

   * Valid complete, partial, stale, and unavailable fixtures pass.
   * Missing evidence metadata fails.
   * Invalid authority or visibility values fail.
   * Unknown fields fail under a strict Zod schema.
   * `operator-disposition` without a disposition record fails.

2. **Allowlist enforcement**

   * Only approved repositories, paths, fields, and evidence-link origins are accepted.
   * Private MOPCON URLs, trace bodies, Operator notes, secrets, hostnames, and arbitrary payload fields are rejected.
   * Generator input cannot introduce cross-repository write targets.

3. **Freshness behavior**

   * Current records age into `aging` and `stale` at defined thresholds.
   * `verifiedAt: null` renders `unknown` or unavailable.
   * An old artifact cannot continue rendering as current.
   * Page-level condition correctly reflects partial or stale sections.

4. **Generation failure**

   * A failed fetch does not replace the last valid artifact.
   * A malformed source does not replace the artifact.
   * A failed schema validation does not replace the artifact.
   * No prior artifact plus failed generation causes build failure.
   * Partial permitted input produces an explicitly partial artifact.

5. **Council semantics**

   * Workflow state and disposition render separately.
   * `ratified` cannot render without an Operator disposition record.
   * Missing required reviews remain visible.
   * Positions are not rewritten into apparent consensus.

6. **Rendering**

   * All four required sections render.
   * Empty sections render unavailable states rather than success states.
   * Evidence labels and timestamps are visible.
   * No operational controls, mutation forms, private links, or runtime proxy calls exist.
   * The page works without JavaScript hydration if no interactive enhancement is added.

7. **Repository verification**

   * Type-check passes.
   * ESLint passes.
   * Vitest passes.
   * Production build passes.
   * Static output contains no GitHub token, private hostname, MOPCON route, trace content, or Operator note.
   * Responsive and keyboard-accessibility checks pass.

## Risks and blockers

There is no architectural blocker requiring abandonment of the current definition.

The following are implementation blockers until resolved:

* Freshness thresholds are not yet defined by source class.
* Generator failure semantics are not explicit enough in the definition.
* The definition does not state whether the last valid artifact is retained after generation failure.
* The allowed evidence-link origins and source-path allowlist are not yet enumerated.
* The behavior for an absent initial snapshot must be explicit.
* `static-fallback` is ambiguous and could recreate the scorecard’s mock-fallback defect unless tightly defined.
* Safe runtime and MOPCON summaries need an explicit handoff format; the generator must not scrape private responses and decide what is safe.
* The definition does not yet distinguish build validation from source generation. Combining them would risk deployment builds acquiring unnecessary credentials or network dependencies.

A signed manifest is not necessary for v0.1 if the artifact is generated in controlled CI, schema-validated, committed or transferred with provenance, and covered by repository integrity controls. A content hash and source revision list are sufficient for v0.1. Signing can remain deferred.

## Requested definition changes

Add the following requirements before implementation verification:

1. Define freshness thresholds for each allowed source class.
2. State that generation uses atomic replacement and never overwrites the last valid artifact on failure.
3. State that an absent valid artifact causes the production build to fail.
4. Define `static-fallback` as a previously validated snapshot retained after generation failure—not mock or synthetic data. Prefer renaming it `retained-verified-snapshot`.
5. Require strict schema validation with rejection of unknown fields.
6. Require a checked-in source and field allowlist, including permitted evidence-link origins.
7. Separate `continuity:generate` from `continuity:validate`; production build runs validation but does not require source credentials or network access.
8. Require rendering-time freshness recalculation so an old artifact cannot preserve a historical `current` label.
9. Require safe runtime and MOPCON summaries to arrive as explicitly prepared public records, not as generator-selected excerpts from private payloads.
10. Require artifact provenance containing source revisions or references and a content hash.

## Recommendation

Proceed with implementation after the requested definition changes are incorporated.

The smallest sound implementation is a static Next.js server route reading one strict, locally stored snapshot artifact. The generator operates before deployment under controlled credentials; the deployed application performs no GitHub access, private-system access, runtime mutation, or cross-repository write.

The scorecard should remain a design and adapter reference. Its Vite runtime, live endpoint assumptions, mock-derived types, and silent fallback behavior should not cross into Platform.

This is Ptah’s implementation-feasibility position only. It does not ratify CG-0029, alter its governing purpose, or extend the supplied Operator and Theia approval beyond its recorded scope.