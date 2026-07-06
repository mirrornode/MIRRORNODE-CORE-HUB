# MIRRORNODE Visual Direction v0.1

Status: Draft visual direction  
Generated: 2026-07-05  
Scope: CORE-HUB console, Osiris Audit public sequence, future operator surfaces  
Authority: Design/documentation only; no runtime automation, deployment, execution authority, or live-data claim

## 1. Direction Statement

MIRRORNODE should feel like a governed command surface, not a generic SaaS dashboard.

The visual language should communicate:

- state awareness
- causal trace
- intervention readiness
- review gates
- evidence discipline
- adaptive routing
- governed authority

Primary frame:

> Adaptive path. Governed authority.

## 2. Current Reference Surface

The first successful direction is represented by:

- `mirrornode-command-console.html`
- `core-hub-architecture.html`

The console works because it has the right balance:

| Quality | Why It Matters |
| --- | --- |
| Command-center density | Makes the system feel operational, not theoretical. |
| CORE-HUB center of gravity | Keeps canon/control visually central. |
| Gated intervention controls | Shows power without implying reckless execution. |
| Agent lanes | Makes the stack legible as roles, not a blur of names. |
| Timeline and nexus | Shows state, causality, and intervention as a sequence. |
| Osiris split visible | Prevents commercial, execution, and agent authority from collapsing. |
| Evidence and drift panels | Makes review and validation visible as first-class functions. |

## 3. Visual Principles

### 3.1 Make Authority Visible

Every surface should show what is:

- allowed
- blocked
- pending review
- ratified
- advisory
- commercial-limited
- execution-gated

Do not hide governance in tooltips or backend logic.

### 3.2 Make Movement Traceable

The user should be able to see work moving through:

```text
State -> Causality -> Intervention
```

This should apply to:

- CORE-HUB review
- Osiris Audit sequence
- manual routing trials
- future operator console
- Arvid continuity prototype

### 3.3 Make Execution Feel Powerful But Gated

Buttons may look serious.

They must not imply unauthorized capability.

Correct:

```text
EXECUTION REQUIRES RATIFICATION
```

Correct:

```text
PREPARE REVIEW PACKET
```

Wrong:

```text
EXECUTE REMEDIATION
```

unless the action is truly authorized, scoped, traceable, and approved.

### 3.4 Show Review As A System Function

Review should not feel like a footnote.

It should appear as live system structure:

- Ptah security review
- THOTH evidence review
- THEIA integration
- Merlin sequencing
- Hermes routing evidence
- Librarian placement recommendation

### 3.5 Preserve Human Readability

The console can look advanced, but the text must stay plain.

Avoid:

- over-symbolic labels
- invented metrics with no source
- fake live claims
- spiritual claims in product surfaces
- words that imply certification or legal/security certainty

## 4. Surface Taxonomy

| Surface | Audience | Visual Mode | Authority Boundary |
| --- | --- | --- | --- |
| CORE-HUB console | internal/operator | dense command center | may show governance, review, blocked execution |
| Osiris Audit page | customer/public | guided sequence | must not imply MIRRORNODE certification or canon authority |
| Operator HUD | internal/operator | split terminal/browser command surface | may show task routing and traces |
| Arvid prototype | family/game | playable continuity surface | avoid governance pressure unless needed |
| Repo visualization | internal/operator | architecture map | evidence-bound, not speculative |

## 5. CORE-HUB Console Requirements

The CORE-HUB console should show:

- current review packet status
- registry records
- agent lanes
- blocked material actions
- evidence packet state
- adaptive routing status
- manual routing trial status
- ratification questions
- execution gate state

It should not show:

- fake production telemetry
- fake customer counts
- fake live deployment status
- fake security clearance
- automatic remediation controls

## 6. Osiris Audit Public Adaptation

The public page may borrow the visual language, but it must simplify the authority layer.

Customer-facing sequence:

```text
Intake -> Structural Review -> Evidence Pass -> Findings -> Delivery
```

Optional deeper label:

```text
State -> Causality -> Intervention
```

Public page should emphasize:

- what the customer gets
- how the review proceeds
- why the process is traceable
- what is not being promised

Public page must avoid:

- canon authority claims
- governance certification claims
- security certification claims
- compliance guarantees
- legal certainty
- autonomous remediation

Approved boundary sentence:

> Osiris Audit is a commercial review service. It does not certify MIRRORNODE governance status, grant registry authority, or create canon approval.

## 7. Design Motifs

Use:

- dark operational field
- neon blue/teal accents
- restrained red for blocked/gated states
- timeline linework
- causal nexus/orb visual
- compact agent rows
- evidence progress lanes
- gated intervention panel

Avoid:

- generic marketing hero
- decorative-only symbols
- excessive mythic language on public offer pages
- fake terminal claims
- fake "online" claims unless live
- unapproved execute buttons

## 8. Implementation Notes

The current visual files are mock surfaces.

Before runtime wiring:

1. identify source data
2. define update cadence
3. define allowed actions
4. define blocked actions
5. define trace fields
6. define review gates
7. define empty/error states

Until then, label the surface as:

```text
Static visual direction / review mock
```

or keep it in docs/internal preview only.

## 9. Next Recommended Work

1. Place `mirrornode-command-console.html` in CORE-HUB docs as visual direction v0.1.
2. Create a public Osiris Audit sequence component inspired by the console, but simplified.
3. Keep execution actions disabled until ratified.
4. Use the console as the future operator HUD north star.

## 10. Holding Statement

The visual language is now strong enough to guide product design.

It is not yet a live operations console.

Preserve the difference.
