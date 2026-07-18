# MIRRORFRAME v0.1
## Content Schema and Validation Specification

**Status:** Ratification Draft  
**Scope:** MIRRORNODE public and internal surfaces  
**Authority:** Proposed governance contract; not yet canonical  
**Implementation status:** No implementation authority granted by this document

---

## 1. Purpose

MIRRORFRAME is the shared trust, orientation, and authority-disclosure layer used across MIRRORNODE surfaces.

It is not a standalone product, destination, runtime, or shell application.

MIRRORFRAME standardizes how each surface declares:

1. identity,
2. purpose,
3. the condition of the material currently being presented,
4. the authority limits governing that material, and
5. the next legitimate action available to the user.

Its purpose is to reduce fragmentation across MIRRORNODE without forcing every surface into the same visual or operational character.

> The frame carries continuity. The surface carries character. The authority model governs claims and actions.

## 2. Governing Principle

MIRRORFRAME is a governance contract, not merely a visual wrapper.

It does not standardize what each MIRRORNODE surface does. It standardizes how each surface:

- identifies itself,
- explains its function,
- describes the material currently being shown,
- discloses authority limits,
- exposes the next legitimate action,
- preserves reviewability before material execution.

Where surface-specific language conflicts with MIRRORFRAME state, boundary, or action language, the MIRRORFRAME declaration governs interpretation.

## 3. Layer Model

| Layer | Function |
|---|---|
| Surface layer | Product-specific content, behavior, interaction, and presentation |
| Frame layer | Identity, orientation, state, boundary, stewardship, and next action |
| Authority layer | Permitted claims, transitions, approvals, and execution boundaries |

MIRRORFRAME belongs to the frame layer but must accurately represent the authority layer. It must not create authority that the underlying surface does not possess.

## 4. User-Facing Five-Field Contract

Every conforming surface must communicate five user-facing concepts.

### 4.1 Identity

Answers:

- Where am I?
- Which MIRRORNODE surface is active?

Required display content:

- MIRRORNODE identity,
- MIRRORFRAME label,
- current surface name,
- return path to Mirror Mirror.

### 4.2 Purpose

Answers:

- What is this surface for?

Required display content:

- one stable, plain-language purpose statement.

The purpose must describe the actual function of the surface. It must not use unsupported promotional or authority language.

### 4.3 State and boundary

Answers:

- What kind of material am I seeing?
- What may this surface not claim or do?

Required display content:

- one approved state,
- one explicit boundary statement.

State and boundary must remain separate.

### 4.4 Governed next action

Answers:

- What is the next legitimate step?

Required display content:

- one enabled primary action, or
- one explicit unavailable-action condition.

A surface must not invent an actionable CTA when no legitimate forward action exists.

### 4.5 Stewardship and closure

Answers:

- Who maintains this surface?
- Where is the canonical source or return path?
- What authority reminder applies?

Required display content:

- steward,
- authority reminder,
- canonical link where applicable,
- return path to Mirror Mirror.

## 5. Terminology

### 5.1 Surface

A named MIRRORNODE experience, product interface, service interface, model, report, or operational environment.

Examples: Mirror Mirror, MIRRORNODE Platform, Parallax, Osiris, MopCon.

### 5.2 Frame

The consistent orientation and disclosure structure surrounding a surface.

The frame does not control the surface's internal logic unless a separate implementation contract grants that authority.

### 5.3 State

A finite label describing the condition or evidence class of the material currently presented inside the frame.

State does not describe:

- the quality of the product,
- the maturity of the company,
- the permanent condition of the repository,
- the authority of the entire MIRRORNODE system,
- a marketing category.

### 5.4 Presentation description

A short optional description explaining how the current state appears in a particular surface.

Examples:

- Interactive declared model
- Public service and intake page
- Human-reviewed audit report
- Staging deployment preview

Presentation description may clarify state but must not replace or modify the approved state value.

### 5.5 Boundary

A plain-language authority limit describing what the surface or presented material is not authorized to claim, decide, diagnose, execute, imply, or access.

### 5.6 Primary action

The single most legitimate next step available in the current state and boundary.

A primary action may be enabled or unavailable.

### 5.7 Stewardship

Metadata identifying the maintainer or governing party responsible for the surface declaration and canonical reference.

### 5.8 Material change

Any action that may alter:

- production behavior,
- canonical records,
- financial state,
- customer data,
- infrastructure,
- permissions,
- external communications,
- system authority,
- deployment state.

Material changes must preserve a reviewable step before final execution unless an explicitly ratified authority contract permits otherwise.

## 6. Approved State Vocabulary

```ts
type MirrorFrameState =
  | "static"
  | "modeled"
  | "reviewed"
  | "live-preview"
  | "deferred"
  | "internal-only";
```

### 6.1 Static

Informational or explanatory material with no active model, live preview, or represented human-reviewed output.

Examples: public product overview, service intake page, explanatory documentation.

### 6.2 Modeled

A structured, calculated, simulated, or generated representation is being presented.

Modeled material must not be interpreted as runtime observation, verified production truth, or a guaranteed forecast unless separately established.

Examples: Parallax architecture scenario, deterministic risk model, interactive declared-system representation.

### 6.3 Reviewed

The specific material currently presented has completed a declared human review.

Reviewed does not mean certified, permanently correct, automatically approved, or authorized for execution.

The responsible reviewer or review class should be traceable where appropriate.

### 6.4 Live Preview

An active preview or staging representation is being shown.

Live Preview does not imply production authority, canonical status, final approval, or stable availability.

### 6.5 Deferred

The surface or action exists conceptually or structurally, but activation, publication, conclusion, or entry is intentionally postponed.

Deferred surfaces fail closed.

### 6.6 Internal-only

The surface is not intended for public or external-facing use.

Internal-only surfaces fail closed for public entry and must not expose public execution paths.

## 7. State Rules

1. A surface must use exactly one approved state at a time.
2. State applies only to the material currently presented inside the frame.
3. State must be derived from actual presentation condition.
4. State must not be selected for branding or promotional value.
5. State must not imply authority beyond the underlying evidence.
6. A change in material presentation condition must trigger a corresponding state review.
7. Custom state values are prohibited in v0.1.
8. Presentation description may vary by surface but must not contradict state.
9. Deferred and Internal-only states must not expose an enabled public forward-action CTA.
10. Reviewed must only be used where an identifiable human-review event has occurred for the displayed material.

## 8. Boundary Model

```ts
type BoundaryPattern =
  | "not-runtime-monitoring"
  | "findings-not-remediation"
  | "no-diagnosis"
  | "no-execution"
  | "no-hidden-access"
  | "preview-only"
  | "internal-use-only"
  | "not-canonical"
  | "review-required"
  | "custom-reviewed";
```

### 8.1 Approved default statements

| Pattern | Default statement |
|---|---|
| `not-runtime-monitoring` | Not runtime monitoring. |
| `findings-not-remediation` | Findings, not autonomous remediation. |
| `no-diagnosis` | No diagnosis. |
| `no-execution` | No execution authority. |
| `no-hidden-access` | No hidden system access. |
| `preview-only` | Preview only; not production authority. |
| `internal-use-only` | Internal use only. |
| `not-canonical` | Not a canonical record. |
| `review-required` | Requires review before action. |

### 8.2 Custom reviewed boundaries

A surface may use `custom-reviewed` when the approved patterns do not accurately describe its authority limit.

Custom text must:

- remain restrictive,
- use plain language,
- identify the authority limit,
- avoid legalistic caution theater,
- avoid promotional claims,
- receive human copy review before public promotion.

### 8.3 Boundary rules

1. Every surface must declare at least one boundary statement.
2. Boundary must describe an authority limit, not a feature list.
3. Boundary must not contradict the current state.
4. Boundary must not imply hidden capabilities.
5. Boundary must remain visible where a user could mistake modeled, reviewed, or preview material for execution authority.
6. Boundary framing must remain visible after acknowledgement.
7. Boundary acknowledgement does not remove or supersede the boundary.
8. Material change paths must preserve review before final execution unless separately authorized.

## 9. Primary Action Model

```ts
type MirrorFramePrimaryAction =
  | {
      mode: "enabled";
      label: string;
      href: string;
      intent:
        | "request"
        | "begin-intake"
        | "prepare"
        | "submit-for-review"
        | "return"
        | "inspect"
        | "view-model";
    }
  | {
      mode: "unavailable";
      reason: string;
      returnHref?: string;
    };
```

### 9.1 Enabled action

An enabled action must:

- align with surface purpose,
- fit the current state,
- respect the boundary,
- reflect actual authority,
- present the next legitimate step,
- preserve reviewability where material change may follow.

### 9.2 Unavailable action

Unavailable mode must be used when:

- the surface is Deferred,
- the surface is Internal-only for a public user,
- required review has not occurred,
- no legitimate forward action exists,
- action would imply unsupported authority.

Unavailable mode must include a plain-language reason.

A return path may still be offered.

### 9.3 Approved action intents

| Intent | Typical use |
|---|---|
| `request` | Request a human-governed service or review |
| `begin-intake` | Begin a bounded intake process |
| `prepare` | Prepare material without executing it |
| `submit-for-review` | Route material to a human or governed review |
| `return` | Return to Mirror Mirror or another safe origin |
| `inspect` | Inspect evidence, structure, or explanatory material |
| `view-model` | Open a modeled representation |

### 9.4 Preferred verbs

Request, Begin intake, Prepare, Submit for review, Return, Inspect, View model.

### 9.5 Restricted verbs

The following verbs must not be used unless the surface has explicit, ratified authority:

Deploy, Execute, Fix now, Resolve automatically, Diagnose, Remediate, Complete, Approve, Publish.

## 10. Stewardship Model

```ts
type MirrorFrameStewardship = {
  steward: string;
  authorityReminder: string;
  canonicalHref?: string;
  mirrorMirrorHref: string;
};
```

### 10.1 Steward

The party responsible for maintaining the surface declaration.

Default public value: `MIRRORNODE`.

A more specific steward may be used where operationally useful, provided it does not imply unsupported authority.

### 10.2 Authority reminder

A short closure statement reinforcing the governing boundary.

Examples:

- Human-governed public surface.
- Review required before material action.
- Modeled output; not production observation.
- Internal operator surface.

### 10.3 Canonical link

Where a canonical document, repository, report, or source exists, the frame should provide a stable reference.

Absence of a canonical link must not be concealed through ambiguous wording.

## 11. Implementation-Grade Schema

```ts
type MirrorFrameDeclaration = {
  version: "0.1";

  surface: {
    id: string;
    name: string;
    purpose: string;
  };

  identity: {
    systemName: "MIRRORNODE";
    frameLabel: "MIRRORFRAME";
    systemHomeHref: string;
    mirrorMirrorHref: string;
  };

  presentation: {
    state: MirrorFrameState;
    description?: string;
  };

  boundary: {
    pattern: BoundaryPattern;
    statement: string;
    acknowledgementRequired?: boolean;
  };

  primaryAction: MirrorFramePrimaryAction;

  stewardship: MirrorFrameStewardship;
};
```

## 12. Field Validation Rules

### 12.1 `version`

- Required.
- Must equal `"0.1"`.

### 12.2 `surface.id`

- Required.
- Stable machine-readable identifier.
- Lowercase kebab case.
- Must not change for visual or marketing reasons.

Examples: `mirrornode-platform`, `mirror-mirror`, `parallax`, `osiris-audit`.

### 12.3 `surface.name`

- Required.
- Human-readable canonical surface name.
- Must not include temporary state language.

### 12.4 `surface.purpose`

- Required.
- One sentence.
- Plain language.
- Must describe actual function.
- Must not contain unsupported superlatives or authority claims.

### 12.5 `identity.systemName`

- Required.
- Must equal `MIRRORNODE`.

### 12.6 `identity.frameLabel`

- Required.
- Must equal `MIRRORFRAME`.

### 12.7 `identity.systemHomeHref`

- Required.
- Must resolve to the canonical MIRRORNODE public orientation surface.

### 12.8 `identity.mirrorMirrorHref`

- Required.
- Must resolve to the canonical Mirror Mirror entry surface.

### 12.9 `presentation.state`

- Required.
- Must use the approved finite vocabulary.

### 12.10 `presentation.description`

- Optional.
- Must clarify, not replace, state.
- Must not introduce an unapproved state value.
- Must not imply runtime or execution authority.

### 12.11 `boundary.pattern`

- Required.
- Must use an approved pattern.

### 12.12 `boundary.statement`

- Required.
- Must be explicit and restrictive.
- Must match or refine the selected pattern.
- Custom text requires `custom-reviewed`.

### 12.13 `boundary.acknowledgementRequired`

- Optional.
- May only gate an otherwise legitimate action.
- Must not convert Deferred or Internal-only into an enabled state.
- Acknowledgement must not remove boundary framing.

### 12.14 `primaryAction`

- Required.
- Must use either `enabled` or `unavailable`.
- Only one primary action may be emphasized.

### 12.15 `stewardship.steward`

- Required.
- Must identify a real maintainer or governing party.

### 12.16 `stewardship.authorityReminder`

- Required.
- Must reinforce the boundary or review model.

### 12.17 `stewardship.canonicalHref`

- Optional.
- Required where the surface presents itself as derived from or governed by a canonical artifact.

### 12.18 `stewardship.mirrorMirrorHref`

- Required.
- Must match the identity-level Mirror Mirror return path.

## 13. Cross-Field Validation Rules

1. `deferred` must use `primaryAction.mode = "unavailable"`.
2. `internal-only` must use `primaryAction.mode = "unavailable"` for public contexts.
3. `reviewed` requires traceable evidence that the displayed material received human review.
4. `modeled` must not use language implying live observation or verified production truth.
5. `live-preview` must include a preview or non-production boundary.
6. An acknowledgement requirement may not override a fail-closed state.
7. An enabled action must use an approved intent.
8. An enabled action must not conflict with the boundary.
9. A material-change action must route through review unless separately authorized by a ratified authority contract.
10. A custom boundary must use `custom-reviewed`.
11. Mirror Mirror return paths must be present in both identity and stewardship.
12. Surface purpose, state, boundary, and action must describe the same actual operating condition.
13. The frame must not imply runtime connectivity where none exists.
14. The frame must not expose raw secrets, private system state, or hidden authority metadata.

## 14. Publishability Enforcement

A MIRRORNODE surface is not eligible for promotion to a public production domain unless:

1. a complete MIRRORFRAME declaration exists,
2. the declaration passes schema validation,
3. all cross-field rules pass,
4. the boundary statement receives human copy review,
5. the primary action is confirmed to match actual authority,
6. the return path to Mirror Mirror is verified,
7. public presentation is visually reviewed,
8. required repository and deployment checks pass.

### 14.1 Enforcement classes

| Class | Requirement |
|---|---|
| Schema validation | Automated |
| Cross-field conformance | Automated where possible |
| Boundary copy review | Human |
| Authority and CTA review | Human |
| Visual and interaction review | Human |
| Repository checks | Automated |
| Production promotion | Operator-authorized |

### 14.2 Failure behavior

A declaration failure must:

- block production promotion,
- identify the failing field or rule,
- fail closed,
- avoid silently selecting replacement state or action values.

No surface may default to an enabled CTA when declaration validation fails.

## 15. Canonical Examples

### 15.1 MIRRORNODE Platform

```ts
const platformFrame: MirrorFrameDeclaration = {
  version: "0.1",
  surface: {
    id: "mirrornode-platform",
    name: "MIRRORNODE Platform",
    purpose:
      "Provides public orientation, governed lane selection, and explicit system boundaries.",
  },
  identity: {
    systemName: "MIRRORNODE",
    frameLabel: "MIRRORFRAME",
    systemHomeHref: "https://mirrornode.xyz",
    mirrorMirrorHref: "https://mirrornode.xyz/mirror",
  },
  presentation: {
    state: "static",
    description: "Public orientation and lane-routing surface",
  },
  boundary: {
    pattern: "no-execution",
    statement: "No execution authority.",
  },
  primaryAction: {
    mode: "enabled",
    label: "Choose a lane",
    href: "#lanes",
    intent: "inspect",
  },
  stewardship: {
    steward: "MIRRORNODE",
    authorityReminder: "Human-governed public orientation surface.",
    mirrorMirrorHref: "https://mirrornode.xyz/mirror",
  },
};
```

### 15.2 Mirror Mirror

```ts
const mirrorMirrorFrame: MirrorFrameDeclaration = {
  version: "0.1",
  surface: {
    id: "mirror-mirror",
    name: "Mirror Mirror",
    purpose:
      "Reflects the visitor's stated concern and routes them toward an appropriate governed MIRRORNODE surface.",
  },
  identity: {
    systemName: "MIRRORNODE",
    frameLabel: "MIRRORFRAME",
    systemHomeHref: "https://mirrornode.xyz",
    mirrorMirrorHref: "https://mirrornode.xyz/mirror",
  },
  presentation: {
    state: "modeled",
    description: "Interactive public reflection and routing experience",
  },
  boundary: {
    pattern: "no-hidden-access",
    statement: "No diagnosis, execution, or hidden system access.",
  },
  primaryAction: {
    mode: "enabled",
    label: "Choose what you need to see clearly",
    href: "#reflection",
    intent: "inspect",
  },
  stewardship: {
    steward: "MIRRORNODE",
    authorityReminder: "Reflection and routing only; no diagnosis or execution.",
    mirrorMirrorHref: "https://mirrornode.xyz/mirror",
  },
};
```

### 15.3 Parallax

```ts
const parallaxFrame: MirrorFrameDeclaration = {
  version: "0.1",
  surface: {
    id: "parallax",
    name: "Parallax",
    purpose:
      "Models declared architecture assumptions, dependencies, stress conditions, and directional tradeoffs.",
  },
  identity: {
    systemName: "MIRRORNODE",
    frameLabel: "MIRRORFRAME",
    systemHomeHref: "https://mirrornode.xyz",
    mirrorMirrorHref: "https://mirrornode.xyz/mirror",
  },
  presentation: {
    state: "modeled",
    description: "Interactive declared architecture model",
  },
  boundary: {
    pattern: "not-runtime-monitoring",
    statement:
      "Not runtime monitoring; modeled outputs are directional and require human review.",
  },
  primaryAction: {
    mode: "enabled",
    label: "Request Osiris Audit",
    href: "https://mirrornode.xyz/audit",
    intent: "request",
  },
  stewardship: {
    steward: "MIRRORNODE",
    authorityReminder: "Modeled output; not production observation.",
    canonicalHref: "https://parallax.mirrornode.xyz",
    mirrorMirrorHref: "https://mirrornode.xyz/mirror",
  },
};
```

### 15.4 Osiris public service page

```ts
const osirisServiceFrame: MirrorFrameDeclaration = {
  version: "0.1",
  surface: {
    id: "osiris-audit",
    name: "Osiris Audit",
    purpose:
      "Provides a bounded human structural review of an AI system and delivers documented findings.",
  },
  identity: {
    systemName: "MIRRORNODE",
    frameLabel: "MIRRORFRAME",
    systemHomeHref: "https://mirrornode.xyz",
    mirrorMirrorHref: "https://mirrornode.xyz/mirror",
  },
  presentation: {
    state: "static",
    description: "Public service and intake page",
  },
  boundary: {
    pattern: "findings-not-remediation",
    statement: "Findings, not autonomous remediation.",
    acknowledgementRequired: true,
  },
  primaryAction: {
    mode: "enabled",
    label: "Begin audit intake",
    href: "https://mirrornode.xyz/audit",
    intent: "begin-intake",
  },
  stewardship: {
    steward: "MIRRORNODE",
    authorityReminder: "Human-reviewed service; no autonomous remediation.",
    mirrorMirrorHref: "https://mirrornode.xyz/mirror",
  },
};
```

### 15.5 Osiris delivered report

A delivered audit report may use `reviewed` only after the specific report has completed human review.

```ts
const osirisReportFrame: MirrorFrameDeclaration = {
  version: "0.1",
  surface: {
    id: "osiris-audit-report",
    name: "Osiris Audit Report",
    purpose:
      "Presents human-reviewed structural findings and prioritized recommendations for a defined audit scope.",
  },
  identity: {
    systemName: "MIRRORNODE",
    frameLabel: "MIRRORFRAME",
    systemHomeHref: "https://mirrornode.xyz",
    mirrorMirrorHref: "https://mirrornode.xyz/mirror",
  },
  presentation: {
    state: "reviewed",
    description: "Human-reviewed audit report",
  },
  boundary: {
    pattern: "findings-not-remediation",
    statement:
      "Findings and recommendations only; execution requires separate authorization and review.",
  },
  primaryAction: {
    mode: "enabled",
    label: "Submit next steps for review",
    href: "#next-steps",
    intent: "submit-for-review",
  },
  stewardship: {
    steward: "MIRRORNODE",
    authorityReminder: "Reviewed findings do not grant execution authority.",
    mirrorMirrorHref: "https://mirrornode.xyz/mirror",
  },
};
```

## 16. Nonconforming Examples

### 16.1 Invalid state description used as state

Invalid:

```ts
state: "public interactive orientation";
```

Reason:

- not in approved vocabulary,
- combines state and presentation description.

Correct:

```ts
state: "modeled";
description: "Interactive public orientation";
```

### 16.2 Reviewed used as a product category

Invalid:

```ts
state: "reviewed";
description: "Paid human audit service";
```

Reason:

- the service page itself has not necessarily undergone the represented review event,
- human review is part of the service, not necessarily the state of the current material.

Correct:

```ts
state: "static";
description: "Public service and intake page";
```

### 16.3 Deferred surface with enabled CTA

Invalid:

```ts
state: "deferred";
primaryAction: {
  mode: "enabled",
  label: "Launch now",
  href: "/launch",
  intent: "view-model",
};
```

Reason: Deferred must fail closed.

### 16.4 Boundary hidden after acknowledgement

Reason:

- acknowledgement permits continuation,
- it does not erase authority limits.

## 17. Conformance Requirements

A surface conforms to MIRRORFRAME v0.1 only when:

- all required schema fields are present,
- state uses the approved finite vocabulary,
- state accurately describes current presented material,
- presentation description does not replace state,
- boundary uses an approved pattern or reviewed custom text,
- boundary remains explicit and non-promotional,
- the primary action is enabled or explicitly unavailable,
- the action aligns with state and boundary,
- a return path to Mirror Mirror exists,
- stewardship is declared,
- material changes preserve reviewability,
- frame language matches actual system authority,
- validation failures fail closed.

## 18. Ratification Notes

The following changes were made from the initial MIRRORFRAME draft:

1. Separated finite state from presentation description.
2. Defined state as applying only to material currently presented inside the frame.
3. Prevented Reviewed from being used as a product or service category.
4. Added enabled and unavailable primary-action modes.
5. Defined controlled boundary patterns with reviewed custom text permitted.
6. Defined stewardship fields and clarified ownership language.
7. Converted the five user-facing concepts into an implementation-grade schema.
8. Added cross-field validation rules.
9. Defined public-production publishability enforcement.
10. Added automated, human-review, and Operator-authorization enforcement classes.
11. Corrected Platform, Mirror Mirror, Parallax, and Osiris examples.
12. Added a separate reviewed Osiris report example.
13. Required fail-closed behavior for Deferred, Internal-only, and invalid declarations.
14. Preserved reviewable boundaries before material execution.

## 19. Ratification Questions

Before canonical adoption, reviewers must resolve:

1. Is `https://mirrornode.xyz/mirror` the intended canonical Mirror Mirror route?
2. Should MIRRORFRAME declarations live in code, content files, or a shared package?
3. Should `reviewed` require reviewer identity, review timestamp, or evidence reference in v0.1?
4. Should boundary acknowledgement be part of the base declaration or a separate interaction contract?
5. Which repository owns the canonical state and boundary vocabulary?
6. Which checks block production promotion: CI, Canon Gate, a dedicated MIRRORFRAME gate, or all three?
7. Does MopCon conform to the same schema internally, or require a later operator extension?

## 20. Decision Status

MIRRORFRAME v0.1 remains a ratification draft until:

- the ratification questions are resolved,
- the schema receives formal internal review,
- canonical ownership is assigned,
- implementation authority is explicitly granted.

No runtime, deployment, route, or product behavior changes are authorized by this document.
