# CORE-HUB Modular Orchestrator Review Packet

Status: Draft for CORE-HUB review  
Generated: 2026-07-04  
Authority: Advisory only

## Purpose

This packet introduces a modular adaptive orchestrator concept for MIRRORNODE review.

The orchestrator is intended to route work to the right advisory path based on service area, risk, evidence needs, family/privacy context, and execution sensitivity.

## Review Boundary

This packet does not implement runtime automation.

It does not:

- ratify agent authority
- approve execution
- promote agents
- deploy code
- change secrets
- alter payment configuration
- write production registry records
- authorize customer-facing claims

## Core Principle

Adaptive path. Governed authority.

The orchestrator may recommend a route, but it may not approve the action.

## Proposed Routing Model

A routing request describes:

- requested action
- service area
- operator intent
- sensitivity flags
- required output
- known blocked actions

A routing decision returns:

- selected advisory path
- required reviewers
- blocked actions triggered
- approvals needed before execution
- deferred actions
- confidence
- review boundary

## Initial Trial Set

Two manual trials are included:

1. Osiris fulfillment automation
2. Arvid prototype polish

The Osiris trial intentionally triggers security, evidence, integration, and operator review before material execution.

The Arvid trial intentionally remains in a family/private prototype lane unless public release, analytics, monetization, or identifying child context enters scope.

## Ratification Questions

1. Should the orchestrator remain advisory-only for v0.1?
2. Should `approval_state` be added to routing decisions in v0.2?
3. Should service-area maps be separate schema files?
4. Should family/private work always require an explicit public-release checkpoint?
5. Should commercial/payment work always require Ptah review before implementation?

## Current Recommendation

Accept as a documentation-only review packet.

Do not implement runtime routing until the schema, authority boundary, and reviewer requirements are separately ratified.
