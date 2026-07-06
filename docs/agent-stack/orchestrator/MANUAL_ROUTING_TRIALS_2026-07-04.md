# Manual Routing Trials

Status: Draft for CORE-HUB review  
Generated: 2026-07-04  
Scope: Manual validation of adaptive routing examples only

## Purpose

These trials test whether the modular adaptive orchestrator can produce useful routing recommendations without granting authority, approving execution, promoting agents, or crossing into automation.

## Trial Results

| Trial | Request | Decision | Result |
| --- | --- | --- | --- |
| Osiris fulfillment automation | `examples/osiris-fulfillment-routing-request.json` | `examples/osiris-fulfillment-routing-decision.example.json` | Correctly triggers Merlin, Ptah, THOTH, THEIA, and operator approval before material action. |
| Arvid prototype polish | `examples/arvid-prototype-routing-request.json` | `examples/arvid-prototype-routing-decision.example.json` | Correctly stays in the family game lane, with THEIA continuity review and operator approval before public movement. |

## Holding Rules

1. Routing decisions are recommendations, not approvals.
2. Sensitive flags must trigger review requirements before material execution.
3. Blocked actions remain blocked even when a routing path is available.
4. Private or family-context work must not be converted into public, commercial, or data-collecting surfaces without explicit review.
5. Osiris fulfillment automation remains deferred until payment, secret, connector, deployment, and execution checkpoint rules are accepted.

## Review Questions

1. Are the selected paths correct for each service area?
2. Are any required reviewers missing?
3. Are the blocked actions specific enough to prevent authority drift?
4. Should confidence describe routing fit only, or also evidence quality?
5. Should routing decisions include a separate `approval_state` field in the next schema revision?

## Current Verdict

The manual trials support the orchestrator concept as an advisory router. They do not support runtime automation yet.
