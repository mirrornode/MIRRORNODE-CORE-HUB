# MIRRORNODE Continuity Console v0.1

**Status:** Definition Draft  
**Implementation authority:** Not granted by this document  
**Reference implementation target:** `mirrornode-platform/continuity`

## 1. Purpose

The Continuity Console is the read-only MIRRORNODE orientation surface for answering four questions:

1. Where does the system currently stand?
2. What work is active or blocked?
3. What council matters require review or decision?
4. What changed since the last verified checkpoint?

It repurposes the existing System Integrity Scorecard rather than creating a new product.

## 2. Product boundary

The Continuity Console is not MOPCON.

| Surface | Purpose | Authority |
|---|---|---|
| Continuity Console | Read-only system orientation and source-labeled continuity record | No execution, approval, mutation, or hidden access |
| MOPCON | Private operator workflow and runtime control | Explicit Operator actions behind review boundaries |

Public Continuity must never expose:

- execution prompts,
- Operator notes,
- approval or rejection controls,
- private trace bodies,
- secrets or environment values,
- internal-only infrastructure details,
- raw customer or audit data,
- direct private-console routes unless an authenticated access layer exists.

When action is required, Continuity states that Operator action is required and points to a safe public explanation or authenticated handoff. It does not perform the action.

## 3. MIRRORFRAME declaration

```ts
const continuityFrame: MirrorFrameDeclaration = {
  version: "0.1",
  surface: {
    id: "continuity-console",
    name: "Continuity Console",
    purpose:
      "Presents a read-only, source-labeled view of MIRRORNODE status, active work, council matters, and recent verified change.",
  },
  identity: {
    systemName: "MIRRORNODE",
    frameLabel: "MIRRORFRAME",
    systemHomeHref: "https://mirrornode.xyz",
    mirrorMirrorHref: "/mirror",
  },
  presentation: {
    state: "static",
    description: "Build-generated continuity view",
  },
  boundary: {
    pattern: "no-execution",
    statement: "Read-only orientation; no execution, approval, or hidden system access.",
  },
  primaryAction: {
    mode: "enabled",
    label: "Inspect current matters",
    href: "#council-matters",
    intent: "inspect",
  },
  stewardship: {
    steward: "MIRRORNODE",
    authorityReminder: "Status is limited to the cited sources and generation time.",
    mirrorMirrorHref: "/mirror",
  },
};
```

The surface remains `static` in v0.1. Individual records may be source-verified, but source verification does not convert the page itself into a human-reviewed artifact.

The final Mirror Mirror route remains subject to the MIRRORFRAME ratification decision. `/mirror` is a proposed internal route, not a confirmed production URL.

## 4. Page anatomy

### 4.1 Snapshot header

Required fields:

- snapshot condition,
- generated-at timestamp,
- data source mode,
- stale, partial, or unavailable disclosure,
- return path.

Allowed source modes:

- `source-verified-snapshot`
- `partial-snapshot`
- `static-fallback`
- `unavailable`

The header must not synthesize a single system health score. It describes the completeness and freshness of the snapshot only.

The interface must never silently present fallback data as live or current data.

### 4.2 Current system

Shows safe summaries for:

- Platform,
- agent runtime,
- MOPCON,
- Parallax,
- Osiris,
- Council Grounds,
- other explicitly registered surfaces.

Each item declares:

- surface name,
- current presentation state,
- last verification time,
- evidence link,
- public boundary,
- safe next route or `Operator action required` label.

Do not expose internal hostnames, secrets, trace payloads, private routes, or unsupported live-state claims.

### 4.3 Active work

Shows repository-backed work items such as:

- open pull requests,
- draft pull requests,
- blocked or failing checks,
- recently merged work,
- declared next technical action.

Every work item must distinguish:

- active,
- waiting for verification,
- blocked,
- stale review,
- completed.

A failed check is not automatically a failed product state. The display must identify the exact PR or commit context.

### 4.4 Council matters

Shows registered Council Grounds matters with:

- matter ID,
- decision question,
- workflow state,
- disposition status,
- required reviews received or missing,
- unresolved objections,
- next required step,
- source link.

The page must keep workflow state separate from Operator disposition.

It must not display `ratified` unless an Operator disposition record exists.

### 4.5 Continuity record

Shows a concise chronological record of source-verified changes:

- merges,
- dispositions,
- canon actions,
- handoff receipts,
- deployment verification,
- material state changes.

Each entry requires:

- timestamp,
- event type,
- source reference,
- actor or authority,
- short factual description.

The record is append-oriented. Corrections must preserve the original entry and add a correcting record.

## 5. Data truth model

Every displayed item must include or inherit:

- `source`
- `verifiedAt`
- `freshness`
- `visibility`
- `authority`

Recommended types:

```ts
type ContinuityFreshness = "current" | "aging" | "stale" | "unknown";
type ContinuityVisibility = "public" | "operator-summary-only";
type ContinuityAuthority = "informational" | "source-verified" | "operator-disposition";

type ContinuityEvidence = {
  source: string;
  verifiedAt: string | null;
  freshness: ContinuityFreshness;
  visibility: ContinuityVisibility;
  authority: ContinuityAuthority;
};
```

Rules:

1. No item may claim current status without a timestamp and source.
2. Missing data must render as unavailable, not healthy.
3. Mock data must be labeled and must not contribute to any overall status claim.
4. Public data must be allowlisted before snapshot generation.
5. Operator-only records may be represented by safe summaries, never by copied sensitive content.
6. `source-verified` means the source and timestamp were validated; it does not mean a human approved the underlying system state.
7. `operator-disposition` may only be used for an actual Operator disposition record.

## 6. Source and generation model

### v0.1 generation ruling

Continuity v0.1 uses a build-generated static snapshot.

A controlled generation step gathers allowlisted public data, writes a typed snapshot artifact, and records `generatedAt`. The public page renders that artifact without holding GitHub credentials or calling private systems at request time.

This avoids:

- exposing tokens,
- public rate-limit dependence,
- unstable request-time failures,
- accidental private-data retrieval,
- ambiguous live-state claims.

### v0.1 allowed sources

- GitHub pull requests, commits, and checks,
- Council Grounds matter files in CORE-HUB,
- explicit static surface registry,
- safe runtime health summary captured during a documented verification pass,
- safe MOPCON availability summary captured during a documented verification pass.

Runtime and MOPCON summaries age according to their captured timestamp. A local verification result must not be described as currently live after its freshness window expires.

### Deferred sources

- email,
- calendar,
- finances,
- customer records,
- raw runtime traces,
- autonomous agent status inference,
- request-time GitHub API calls from the public page.

Connected personal services must not enter the public Continuity Console without a separate privacy and authority decision.

## 7. Existing scorecard reuse

Retain from `apps/mirrornode-scorecard`:

- status-band pattern,
- source disclosure,
- last-sync display,
- card-based system overview,
- incident or attention-list pattern,
- adapter concept.

Replace or revise:

- `detached local surface` framing,
- assumed Theia event/state API dependency,
- raw API and WebSocket URL display,
- active-agent count without evidence,
- incident data that is mock or unsupported,
- silent mock fallback behavior,
- request-time live endpoint assumptions.

The old scorecard remains a design and adapter reference. The canonical product route should be implemented in `mirrornode-platform` rather than deployed as a separate public application.

## 8. Route and visibility ruling

Canonical public route:

```text
/continuity
```

Public Continuity contains safe, read-only summaries.

Private operational depth remains in MOPCON, including:

- objective submission,
- plan content,
- approval and rejection,
- execution,
- trace retrieval,
- Operator notes.

In v0.1, public Continuity does not expose a direct MOPCON URL. It may display `Operator action required` and a safe handoff description.

## 9. v0.1 implementation boundary

### In scope

- new `/continuity` route in Platform,
- typed build-generated snapshot contract,
- source and verification labels,
- Current system section,
- Active work section,
- Council matters section,
- Continuity record section,
- safe evidence links,
- responsive and accessible rendering,
- explicit unavailable and stale states,
- a generation script or build step for the allowlisted snapshot.

### Out of scope

- automatic execution,
- automatic PR mutation,
- autonomous council transitions,
- realtime sockets,
- email, calendar, or finance ingestion,
- private trace display,
- direct private-console links without authentication,
- cross-repository write actions,
- automatic health conclusions from incomplete data,
- request-time public GitHub API access.

## 10. Acceptance criteria

The definition is ready for implementation when:

1. public and private fields are explicitly separated,
2. every displayed status has a source and verification rule,
3. mock fallback cannot appear as live truth,
4. Council Grounds state and disposition are represented separately,
5. MOPCON actions remain private and are not duplicated,
6. the page does not create a synthetic overall health score,
7. v0.1 uses a build-generated allowlisted snapshot,
8. the scorecard reuse plan is accepted,
9. the Operator approves the implementation boundary.

## 11. Decision summary

Continuity Console v0.1 should be implemented as a read-only `/continuity` route in `mirrornode-platform`, using the existing scorecard as a design and adapter reference.

It provides orientation, not control.

It reports source-labeled state, active work, council matters, and recent change from a build-generated snapshot. It does not execute, approve, infer hidden state, expose private routes, create a synthetic health score, or silently substitute mock data for evidence.
