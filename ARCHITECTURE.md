# Architecture — MIRRORNODE-CORE-HUB

## Role
MIRRORNODE-CORE-HUB is the governance and coordination hub for the MIRRORNODE organization. It records cross-repo decisions, canonical source mappings, repo roles, agent registry posture, and governance contracts.

## What Lives Here
- Canonical source mapping
- Cross-repo governance contracts
- Org-wide audit and readiness notes
- Agent registry references
- Operational coordination documents

## What Does Not Live Here
- Production application code
- Agent runtime implementations
- Secrets or environment-specific credentials
- Database migrations unless explicitly designated

## Canonical Function
Repository roles, agent registry entries, and cross-repo interface contracts are canonical here unless superseded by an explicit governance document.

## Dependencies
This repo has no runtime dependency. Other repos reference it for governance and coordination.
