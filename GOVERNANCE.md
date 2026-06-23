# Governance — MIRRORNODE-CORE-HUB

## Decision Authority
This repository holds organization-level governance. Changes require explicit human authorization.

## Branch Model
- main — canonical governance record.
- All structural changes should use pull requests.
- Documentation updates should be reviewable and traceable.

## What Triggers Updates Here
- New repo added to the organization
- Repo role changed
- Agent promoted, retired, or given a new capability class
- Cross-repo interface contract changed
- Deployment canon changed
- Security or payment boundary changed

## Prohibited Actions
- Do not commit secrets or environment-specific credentials.
- Do not remove repo or agent references without a deprecation note.
- Do not let local prototype names override verified production canon.
- Do not describe unverified deployment paths as live.

## Documentation Priority
If repository structure, runtime behavior, deployment configuration, or system contracts differ from documentation, the discrepancy must be corrected.

Documentation describes reality; reality does not change to satisfy documentation.
