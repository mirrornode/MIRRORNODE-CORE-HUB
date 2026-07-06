# CORE-HUB Modular Orchestrator Ratification Appendix

Status: Draft appendix for CORE-HUB review  
Generated: 2026-07-04  
Related spec: `MODULAR_ADAPTIVE_ORCHESTRATOR_SPEC_v0_1.md`  
Authority: Documentation-only; no implementation, automation, deployment, registry promotion, or agent activation authorized

## Purpose

This appendix converts the modular adaptive orchestrator concept into ratification-ready governance decisions.

The aim is to let MIRRORNODE route work adaptively by capability and service area while keeping approval, canon, security, and material execution governed.

## Ratification Thesis

CORE-HUB may ratify adaptive routing as a coordination method without granting autonomous execution authority.

Ratified routing would mean:

- work can be classified by service area
- eligible agents or services can be recommended by capability
- required reviews can be identified automatically
- handoff packets can be assembled consistently

Ratified routing would not mean:

- work is approved
- execution is authorized
- agents are promoted
- canon is changed
- commercial claims become governance claims
- provider availability becomes permission

## Proposed CORE-HUB Rules

| Rule | Proposed Ratification |
| --- | --- |
| Adaptive routing is allowed | Yes, as advisory coordination only. |
| Routing by capability is allowed | Yes, if agent status and blocked actions are checked. |
| Routing by provider availability is allowed | No, provider availability is only an adapter signal. |
| Routing can approve execution | No. |
| Routing can promote agents | No. |
| Routing can define required reviews | Yes, as a recommendation or policy check. |
| Routing can produce handoff packets | Yes, provided outputs remain reviewable. |
| Routing can bypass CORE-HUB | No. |
| Routing can bypass Ptah where security/material execution risk appears | No. |
| Routing can bypass THOTH where source/evidence claims appear | No. |

## Required Registry Fields

Every routable agent or service must eventually expose:

```yaml
id:
display_name:
kind: agent | service | provider_adapter | execution_surface
status:
lane:
evidence_class:
capabilities:
service_areas:
allowed_actions:
blocked_actions:
requires_review_for:
handoff_outputs:
authority_boundary:
source_refs:
last_reviewed:
```

## Required Routing Request Fields

```yaml
trace_id:
operator_intent:
task_summary:
service_area:
required_capabilities:
sensitivity:
source_inputs:
expected_output:
blocked_actions:
desired_reviewers:
```

## Required Routing Decision Fields

```yaml
trace_id:
service_area:
selected_path:
required_reviews:
blocked_actions_triggered:
approval_needed_before:
deferred_actions:
confidence:
review_boundary:
```

## Sensitivity Flags

These flags must be evaluated before routing:

| Flag | Meaning | Default Effect |
| --- | --- | --- |
| `secrets` | Credentials, tokens, private keys, or secret material may be involved. | Require Ptah/security review before material action. |
| `payments` | Checkout, Stripe, invoices, refunds, or billing may be involved. | Require Ptah and operator approval before material action. |
| `legal` | Legal records, filings, claims, or court-related materials may be involved. | Require operator review and professional-context caution. |
| `private_context` | Personal, family, health, legal, financial, or identity-sensitive context may be involved. | Restrict sources and prevent unsupported inference. |
| `production` | Live app, deployment, database, workflow, or customer-facing system may be involved. | Require material execution checkpoint. |
| `canon` | Governance, registry, authority, protected namespace, or ratification may be involved. | Require CORE-HUB review. |

## Service Area Starter Map

| Service Area | Default Authority | Required Review |
| --- | --- | --- |
| `canon_control` | CORE-HUB | THEIA, THOTH, Ptah if security/authority risk appears |
| `security_authority` | Pending Ptah ratification | Ptah advisory until ratified; CORE-HUB for binding force |
| `evidence_validation` | Advisory until THOTH ratification | THOTH, CORE-HUB for canon implications |
| `commercial_offer` | Operator review | Ptah for authority/payment risk; THOTH for factual claims |
| `operational_execution` | Prepare-and-submit | Ptah for material execution; THEIA integration; operator approval |
| `memory_curation` | Recommendation only | Librarian, THOTH for evidence claims, CORE-HUB for canon placement |
| `family_game` | Operator review | THEIA for continuity; Ptah only if public/deploy/privacy/payment risk appears |
| `repo_management` | Repo rules and operator approval | Ptah for protected branches/secrets/deploys; THOTH for source claims |
| `deployment` | Blocked until approved | Ptah and operator approval |

## Eligibility Rule

An agent or service is eligible for routing only when all are true:

1. Its status permits the requested use.
2. Its capabilities match the task.
3. Its service areas include the task service area.
4. Its blocked actions do not conflict with the request.
5. Its required review gates are known.
6. Its output contract matches the expected output.
7. Its use does not imply authority beyond its boundary.

If any condition fails, the route must return `no_eligible_route` or `needs_review`.

## Recommended Holding Decision

Ratify the concept, not the automation.

Recommended CORE-HUB holding:

```yaml
modular_adaptive_orchestrator:
  status: concept_ready_pending_schema_review
  allowed_now:
    - documentation
    - schema drafting
    - examples
    - advisory routing analysis
  blocked_now:
    - autonomous execution
    - production automation
    - registry writes
    - agent promotion
    - deployment
    - payment changes
    - secret handling
```

## Ratification Questions

1. Does CORE-HUB accept adaptive routing as advisory coordination?
2. Which statuses permit advisory routing?
3. Which statuses permit operational routing?
4. Can providers be routed directly, or only through adapter records?
5. Who owns the service area map?
6. Who owns the capability map?
7. Who can change sensitivity flag policy?
8. What route decisions must be logged?
9. Where should routing schemas live?
10. What must be true before runtime implementation begins?

## Final Boundary

The orchestrator may make the path adaptive.

It may not make authority automatic.
