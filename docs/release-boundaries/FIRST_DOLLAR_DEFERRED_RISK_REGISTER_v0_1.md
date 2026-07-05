# FIRST_DOLLAR_DEFERRED_RISK_REGISTER_v0_1

Status: Draft
Authority Class: Deferred Risk Register
Canonical Home: MIRRORNODE-CORE-HUB
Applies To:
- FIRST_DOLLAR_RELEASE_LANE_v0_1.md
- CANON_TO_PLATFORM_PROMOTION_BOUNDARY_v0_1.md
- mirrornode-platform first-dollar implementation work
Oversight:
- Theia: risk visibility and scope coherence
- Ptah / Operator: release hold, waiver, or escalation authority
- execution surfaces: may not retire deferred risks without review

## Purpose

Record known risks that do not automatically block narrow first-dollar build work,
but must remain visible before launch, expansion, or public production claims.

This register exists so deferred work remains explicit, reviewable, and bounded.

## Deferred Risk Rule

Deferred means:
- known
- named
- bounded
- assigned a review trigger
- prevented from silently expanding scope

Deferred does not mean:
- solved
- safe by default
- irrelevant
- approved for launch
- approved for scale
- retired from governance review

## Risk Table

| Risk | Current Holding | Build Impact | Launch Impact | Review Trigger |
| --- | --- | --- | --- | --- |
| Legacy JWT disablement | Deferred technical/security cleanup | May proceed only if the first-dollar lane does not depend on broad auth trust assumptions | Must be reviewed before account-bearing or identity-sensitive launch expansion | Any auth-dependent flow, customer account behavior, or identity-bearing record |
| Entity-path clarification | Deferred business/legal structure decision | Narrow implementation planning may proceed | Live public monetization, tax handling, ownership claims, and public business language need explicit review | Before accepting public money beyond controlled test/payment validation |
| Automated fulfillment | Deferred operational expansion | Manual fulfillment should be used first | Automation requires separate approval, trace, and rollback design | Any attempt to auto-generate, auto-send, or auto-complete audit delivery |
| Full customer portal | Deferred product maturity | Not required for first-dollar proof if fulfillment records remain traceable | Required only if customer self-service becomes part of the launch promise | Any public claim that customers can log in, track, manage, or retrieve audit history |
| Generalized agent activation | Deferred system expansion | Not required for Osiris Audit v1 manual fulfillment | Must not be implied by first-dollar release | Any work that routes live customer data to named agents or autonomous seats |
| Registry automation | Deferred canon/platform bridge automation | Manual promotion records are sufficient for the first lane | Automation requires CORE-HUB review and explicit authority model | Any script, workflow, or service that writes or mutates registry/promotion state |
| Broad public marketing launch | Deferred go-to-market expansion | Offer copy may be drafted within approved boundary language | Public campaign language requires boundary review | Any broad announcement, paid campaign, or claim of platform-wide readiness |
| Payment-to-fulfillment data mismatch | Active operational risk until verified | Build must include enough state to connect payment to fulfillment | Launch blocked if purchase records cannot be fulfilled reliably | Checkout test, webhook change, schema change, or first live payment |
| Refund and pause procedure | Required before launch | May be drafted during build | Launch blocked without a practical pause/refund path | Before live payment acceptance |
| Boundary-language drift | Active governance risk | Build docs and UI copy must avoid certification language | Launch blocked if public claims exceed approved scope | Any customer-facing copy, README, route, or product claim change |

## Required Review Before Retirement

A deferred risk may be retired only when:

1. The corrective work is named.
2. Evidence of completion is recorded.
3. The affected scope is identified.
4. Theia reviews the governance impact.
5. Ptah / Operator accepts retirement or reclassification.

## Required Review Before Expansion

Any expansion beyond the first-dollar lane must review this register first.

Expansion includes:
- new offers
- new customer-facing dashboards
- automated fulfillment
- agent-mediated customer processing
- account-bearing flows
- schema changes that affect runtime behavior
- broader public claims
- launch beyond controlled validation

## Initial Operating Interpretation

Until superseded:
- deferred risks may not be used as reasons to stall narrow build work unless they
  directly affect the bounded lane
- deferred risks may not be ignored during launch review
- a risk that becomes active must be reclassified before continuation
- unresolved authority language is a launch blocker, not a polish issue
