# Solo Operator Mode Receipt

Date: 2026-05-27
Repository: mirrornode/MIRRORNODE-CORE-HUB
Ruleset: Main Branch Protection

## Decision

The repository is operating in Solo Operator Mode.

## Active controls

- Pull request path required.
- Direct deletion blocked.
- Non-fast-forward updates blocked.
- Required status check remains enforced: Contract Compliance Check.
- Required approving review count is set to 0.
- Bypass actors are empty.

## Rationale

The prior configuration required one approving write-access review while the repository currently has no second write-access reviewer available. That created a governance deadlock.

Solo Operator Mode keeps the canonical verification gate active while removing the fictional second-key requirement.

## Future upgrade condition

When a second trusted write-access reviewer exists, the approval count may be restored to 1.
