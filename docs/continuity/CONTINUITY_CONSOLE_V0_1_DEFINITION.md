# MIRRORNODE Continuity Console v0.1

**Status:** Revised Definition Draft  
**Revision authority:** CG-0029 Operator disposition — revision required  
**Implementation authority:** Not granted by this document  
**Publication authority:** Not granted by this document  
**Reference implementation target:** `mirrornode-platform/continuity`

## 1. Purpose

The Continuity Console is the read-only MIRRORNODE orientation surface for answering four questions:

1. Where does the publicly disclosable system record currently stand?
2. What publicly disclosable work is active, blocked, stale, or completed?
3. What publicly disclosable council matters require review or decision?
4. What publicly disclosable changes occurred within the defined display horizon?

It repurposes the existing System Integrity Scorecard as a design and adapter reference rather than creating or deploying a separate product.

Continuity publishes intentionally approved public facts. It is not a filtered projection of MOPCON, the agent runtime, connected services, or private repositories.

## 2. Product and authority boundary

The Continuity Console is not MOPCON.

| Surface | Purpose | Authority |
|---|---|---|
| Continuity Console | Read-only public orientation and source-labeled continuity record | No execution, approval, mutation, hidden access, or inferred authority |
| MOPCON | Private operator workflow and runtime control | Explicit Operator actions behind private review and approval boundaries |

Public Continuity must never expose or reproduce:

- execution objectives, prompts, plans, rationales, results, or routing,
- Operator notes or approval and rejection activity,
- trace, session, request, correlation, or internal sequential identifiers,
- private runtime health detail, model configuration, agent availability, or topology,
- secrets, credentials, environment values, connection strings, cookies, or headers,
- private or local URLs, hostnames, IP addresses, ports, sockets, preview deployments, or authenticated routes,
- customer, audit-client, prospect, vendor, payment, financial, contractual, calendar, email, contact, family, identity, or location data,
- unpublished vulnerabilities, security incidents, exploit detail, defensive gaps, or remediation status,
- private repository names, branches, commits, pull requests, checks, artifacts, logs, or file paths,
- raw Council positions, objections, rationale, missing-review details, or next actions unless separately approved for public disclosure,
- generated summaries of private records,
- mock incidents, unsupported counts, or inferred system health.

Nothing becomes safe for publication merely because it has a source, type, timestamp, or public-looking label.

When further status cannot be disclosed, the default public wording is:

> Further status is not publicly available.

`Operator action required` may appear only when the existence and description of the action have received separate affirmative publication approval.

## 3. Separate authorization gates

The following are distinct decisions:

1. approval of this definition,
2. authorization to implement the route,
3. authorization to generate a populated snapshot,
4. human approval of the first populated public snapshot,
5. authorization to deploy or publish,
6. later approval of material source, field, retention, or visibility changes.

Approval at one gate does not imply approval at another.

## 4. MIRRORFRAME declaration

```ts
const continuityFrame: MirrorFrameDeclaration = {
  version: "0.1",
  surface: {
    id: "continuity-console",
    name: "Continuity Console",
    purpose:
      "Presents a read-only, source-labeled view of intentionally approved public MIRRORNODE status, work, matters, and recent change.",
  },
  identity: {
    systemName: "MIRRORNODE",
    frameLabel: "MIRRORFRAME",
    systemHomeHref: "https://mirrornode.xyz",
    mirrorMirrorHref: null,
  },
  presentation: {
    state: "static",
    description: "Build-generated continuity view",
  },
  boundary: {
    pattern: "no-execution",
    statement:
      "Read-only public orientation; no execution, approval, hidden-system access, or publication of unapproved private-derived material.",
  },
  primaryAction: {
    mode: "enabled",
    label: "Inspect public matters",
    href: "#council-matters",
    intent: "inspect",
  },
  stewardship: {
    steward: "MIRRORNODE",
    authorityReminder:
      "Source checking does not approve the underlying system, decision, security state, or publication scope.",
    mirrorMirrorHref: null,
  },
};
```

The surface remains `static` in v0.1. Individual records may display `source checked`, but that label means only that the cited public source and verification time were checked.

Visible source-check wording must include or link to this clarification:

> Source and timestamp checked; underlying state not approved by this label.

The final Mirror Mirror route remains unresolved and must not be fabricated in this definition or implementation.

## 5. Page anatomy

### 5.1 Snapshot header

Required fields:

- snapshot condition,
- generated-at timestamp,
- last successful generation timestamp,
- data source mode,
- partial, stale, disputed, withdrawn, or unavailable disclosure,
- safe return path.

Allowed snapshot conditions:

- `complete`
- `partial`
- `stale`
- `disputed`
- `unavailable`

Allowed source modes:

- `source-checked-snapshot`
- `partial-snapshot`
- `retained-validated-snapshot`
- `unavailable`

`retained-validated-snapshot` means a previously schema-valid and publication-approved artifact retained after a later generation failure. It never means mock, synthetic, regenerated, or silently refreshed content.

The header must not synthesize a single system-health score. It describes snapshot completeness, age, and disclosure condition only.

`generatedAt` is the artifact-generation time. It must never be presented as the time the underlying facts were verified.

### 5.2 Current system

The section may show only separately approved public projection records for registered surfaces such as:

- Platform,
- agent runtime,
- MOPCON,
- Parallax,
- Osiris,
- Council Grounds,
- other explicitly registered public surfaces.

Private-system observations may enter only as pre-approved public projection records. The generator must not inspect a private payload and decide what excerpt is safe.

Each public system item declares:

- public item identifier that does not expose an internal sequential identifier,
- surface name,
- public presentation state,
- verification time,
- record condition,
- approved evidence link or no link,
- public boundary statement,
- safe next route or nondisclosure wording.

Static verification must not be labeled `live`, `online now`, or equivalent.

### 5.3 Active work

The section may show only work records explicitly approved for public aggregation.

Candidate records include:

- public pull requests,
- public check results,
- public recently merged work,
- public declared next technical action.

Public repository visibility alone does not authorize aggregation.

Every work item must distinguish:

- `active`
- `waiting-verification`
- `blocked`
- `stale-review`
- `completed`
- `disputed`
- `corrected`
- `withdrawn`

A failed check is not automatically a failed product state. The display must identify the exact approved public context without exposing private strategy, security detail, staffing cadence, or launch timing.

### 5.4 Council matters

Council data requires a separate public projection. The raw matter file is not automatically the public record.

A public Council projection may include only fields explicitly marked for publication, such as:

- public matter label,
- approved decision question,
- workflow state,
- disposition status,
- approved next-step summary,
- approved public source link.

Raw positions, objections, reviewer gaps, detailed rationale, and internal next actions remain excluded unless separately approved.

Workflow state and Operator disposition must remain separate.

`ratified` may appear only when an attributable Operator disposition record exists and the public projection accurately describes the scope of that disposition.

### 5.5 Continuity record

The public continuity record is a bounded display projection, not the authoritative archive.

Allowed event classes:

- merge,
- disposition,
- canon action,
- handoff receipt,
- deployment verification,
- material state change,
- correction,
- withdrawal.

Each public entry requires:

- non-enumerable public identifier,
- event time,
- record condition,
- approved source reference or no link,
- actor or authority label appropriate for publication,
- short factual description,
- correction target where applicable.

The authoritative source remains append-oriented. The public projection may tombstone unsafe material.

A public tombstone states that a record was corrected or withdrawn without repeating the prohibited content. Sensitive originals must not remain inside client-readable JSON, HTML, source maps, assets, or downloadable static artifacts.

### 5.6 Public history horizon

v0.1 displays at most the most recent 90 days or 50 public events, whichever is smaller.

Older authoritative records remain in their source repositories but are not automatically aggregated into the public route.

Any change to this horizon requires a separate review of scraping, inference, operational-cadence, and enumeration risk.

## 6. Data truth and record-condition model

```ts
type ContinuityFreshness = "current" | "aging" | "stale" | "unknown";

type ContinuityRecordCondition =
  | "normal"
  | "partial"
  | "disputed"
  | "corrected"
  | "withdrawn"
  | "unavailable";

type ContinuityAuthority =
  | "informational"
  | "source-checked"
  | "operator-disposition";

type ContinuitySourceClass =
  | "github-pr"
  | "github-check"
  | "council-projection"
  | "deployment-verification"
  | "runtime-public-projection"
  | "mopcon-public-projection"
  | "surface-registry";

type ContinuityEvidence = {
  sourceClass: ContinuitySourceClass;
  sourceLabel: string;
  sourceHref: string | null;
  verifiedAt: string | null;
  freshness: ContinuityFreshness;
  condition: ContinuityRecordCondition;
  authority: ContinuityAuthority;
};
```

Rules:

1. No item may claim current status without a valid `verifiedAt` and approved public source.
2. Missing data renders as unavailable, never healthy.
3. Mock or synthetic data is prohibited from populated production snapshots.
4. Public data is allowlisted before generation; denylist filtering is insufficient.
5. Private-derived material is excluded unless it arrives as a separately approved public projection record.
6. `source-checked` does not imply product, security, implementation, deployment, or publication approval.
7. `operator-disposition` means only that an attributable Operator disposition record exists within the cited scope.
8. Unknown fields are rejected.
9. Arbitrary metadata bags are prohibited.
10. Sources that disagree produce a `disputed` record; the generator does not select a winner.
11. A disputed derived status is suppressed.
12. A record whose public description becomes unsafe may be tombstoned as `withdrawn` while the authoritative source preserves the original.

## 7. Freshness windows

Freshness is calculated from `verifiedAt`, the current rendering time, and the source class. It is never accepted as an unsupported editorial assertion.

Default v0.1 windows:

| Source class | Current | Aging | Stale |
|---|---:|---:|---:|
| GitHub pull request or check | 0–24 hours | >24–72 hours | >72 hours |
| Council public projection | 0–72 hours | >72 hours–7 days | >7 days |
| Deployment verification | 0–24 hours | >24–48 hours | >48 hours |
| Runtime public projection | 0–4 hours | >4–12 hours | >12 hours |
| MOPCON public projection | 0–4 hours | >4–12 hours | >12 hours |
| Static surface registry | 0–30 days | >30–90 days | >90 days |

`verifiedAt: null` always produces `unknown` and cannot contribute to a current page-level condition.

Freshness is calculated during generation and independently recalculated during rendering. A historically current artifact cannot remain visually current indefinitely.

Snapshot-level status never overrides stale, disputed, or unavailable records.

## 8. Source, field, and link allowlists

The generator uses checked-in allowlists for:

- permitted repositories and source locations,
- permitted public projection files,
- permitted record types,
- permitted fields,
- permitted enum values,
- permitted evidence-link origins,
- permitted redirect destinations.

Public evidence links must:

- use HTTPS,
- resolve to an approved public origin,
- resolve to a public resource,
- reject authentication redirects,
- reject private repositories and expiring artifact links,
- reject local, preview, CI-artifact, raw-log, and private-console destinations.

No arbitrary source text or URL is copied into a display field without validation.

## 9. Snapshot generation and validation

### 9.1 Artifact location

The proposed generated artifact lives inside Platform at:

```text
content/continuity/snapshot.generated.json
```

It does not live under `public/` and is not automatically exposed as a raw endpoint.

### 9.2 Separate commands

```text
npm run continuity:generate
npm run continuity:validate
```

Generation and build validation remain separate.

The production build may run:

```text
npm run continuity:validate && next build
```

The production build must not require source credentials or network access.

### 9.3 Generator behavior

The controlled generator:

1. reads checked-in source, field, and link allowlists;
2. reads only approved public sources and prepared public projection records;
3. normalizes records into the strict contract;
4. rejects unknown fields, unsupported enums, unapproved sources, and unsafe links;
5. calculates freshness from source-class thresholds;
6. records source revisions or references;
7. calculates a content hash;
8. writes a temporary artifact;
9. validates the complete temporary artifact;
10. atomically replaces the prior valid artifact only after all checks pass.

The generator must not:

- write to source repositories,
- create, modify, merge, close, label, or comment on pull requests,
- mutate Council matters,
- access broader private data than required,
- summarize private payloads into allegedly safe output,
- create mock fallback data.

### 9.4 Failure-closed behavior

On generation or validation failure:

- do not overwrite or delete the last valid artifact;
- do not update `generatedAt` or `lastSuccessfulAt`;
- record the failed attempt only in controlled CI or generation receipts;
- render a retained artifact only with its original timestamps and actual age;
- mark retained content stale when its freshness window expires;
- display `Snapshot unavailable` when no valid artifact exists;
- fail the production build when no valid artifact exists;
- never produce plausible-looking mock content;
- never imply that retention equals renewed verification.

A partial permitted input may produce a partial snapshot only when missing sections are explicitly unavailable and the header reports `partial`.

### 9.5 Source disagreement

When approved sources disagree:

- preserve attributable public references and verification times,
- mark the affected record `disputed`,
- suppress derived conclusions,
- do not automatically select a winner,
- withhold the dispute from public display when describing it would cross a privacy boundary.

## 10. Minimal provenance

A v0.1 snapshot requires:

- schema version,
- generated-at time,
- generation attempt time,
- last successful generation time,
- source revision or reference list,
- content hash,
- generator version,
- record counts by section,
- snapshot condition.

A signed manifest is deferred for v0.1 while generation and deployment remain inside one controlled CI trust boundary. Signing becomes required before snapshots cross trust domains or are generated outside the deployment chain.

## 11. Existing scorecard reuse

Retain as patterns:

- status-band layout,
- source disclosure,
- last-sync or generated-at display,
- card-based system overview,
- attention-list hierarchy,
- degraded and unavailable-state treatment,
- adapter separation between source records and presentation.

Rewrite for Next.js and the new contract:

- the Vite application shell,
- client-side `useEffect` loading flow,
- live endpoint adapter,
- Vite environment configuration,
- API and WebSocket URL display,
- active-agent count,
- incident mock data,
- silent catch-to-mock fallback,
- live-versus-mock source model,
- types derived from sample or mock data.

The canonical route is implemented in Platform as a static server component. The detached Vite app is not imported wholesale.

## 12. Route and private-surface boundary

Canonical proposed public route:

```text
/continuity
```

Private operational depth remains in MOPCON, including:

- objective submission,
- plan content,
- approval and rejection,
- execution,
- trace retrieval,
- Operator notes,
- private health and topology detail.

Public v0.1 exposes no direct MOPCON URL or access instruction.

## 13. Deployment and artifact inspection conditions

Before first public deployment:

1. all source-class freshness windows are implemented and tested;
2. `verifiedAt` and `generatedAt` are visibly and semantically distinct;
3. source, field, enum, repository, path, and outbound-link allowlists are checked in;
4. unknown fields and schema drift fail closed;
5. private-derived summaries are absent unless supplied as approved public projections;
6. no request-time GitHub or private-system calls exist;
7. no credentials exist in the deployed route or build output;
8. MOPCON-derived objectives, plans, decisions, traces, notes, topology, and routes are absent;
9. visible source-check wording cannot reasonably imply approval;
10. stale, partial, disputed, corrected, withdrawn, and unavailable displays are verified;
11. public-history horizon and non-enumerable identifiers are enforced;
12. evidence links and redirects are validated;
13. fixtures contain no production or private records;
14. built HTML, JavaScript, JSON, source maps, metadata, comments, static assets, and published build artifacts are scanned for prohibited fields and strings;
15. type-check, lint, contract tests, freshness tests, generator tests, rendering tests, production build, accessibility, and responsive checks pass;
16. a human disclosure review approves the first populated snapshot;
17. the Operator separately authorizes implementation and later publication.

## 14. v0.1 implementation boundary

### In scope only after separate authorization

- `/continuity` static server route in Platform,
- strict typed snapshot contract,
- checked-in source, field, and link allowlists,
- separate generation and validation commands,
- Current system public projection section,
- Active work public projection section,
- Council public projection section,
- bounded Continuity record section,
- evidence and timestamp labels,
- stale, partial, disputed, corrected, withdrawn, and unavailable states,
- content hash and source-reference provenance,
- build-output disclosure scan,
- accessibility and responsive verification.

### Out of scope

- runtime execution,
- automatic repository mutation,
- autonomous Council transitions,
- realtime sockets,
- request-time GitHub or private-system access,
- private trace display,
- direct private-console linking,
- email, calendar, finance, contact, customer, payment, or contractual ingestion,
- automatic health conclusions,
- mock fallback,
- aggregation of public data without affirmative publication approval,
- publication of the first populated snapshot without human disclosure review and Operator authorization.

## 15. Acceptance criteria for later implementation authorization

A later confirmation matter may recommend implementation authorization only when:

1. Ptah confirms that the revised definition is implementable in current Platform without importing the Vite app wholesale;
2. Osiris confirms that the revised definition satisfies the required disclosure, freshness, history, correction, and failure boundaries;
3. source-class freshness windows are accepted;
4. failure-closed and atomic replacement semantics are accepted;
5. strict allowlists and URL validation are accepted;
6. public projection, tombstone, history-horizon, and non-enumeration rules are accepted;
7. implementation and publication remain separately authorized;
8. the Operator issues a new explicit disposition granting implementation authority.

## 16. Revision summary

This revision incorporates the conditions recorded by Ptah and Osiris under CG-0029.

The route remains feasible and directionally supported, but implementation is not yet authorized.

The governing rule is:

> Continuity publishes intentionally approved public facts. It does not automatically sanitize, summarize, or expose private operations.
