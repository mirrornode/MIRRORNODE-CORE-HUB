# Copilot Instructions — MIRRORNODE-CORE-HUB

## Repo Context
This is a governance and documentation repository. It contains organization-level records, canonical source mappings, and cross-repo coordination documents.

## Rules
- Prefer Markdown, YAML, and JSON contract edits.
- Do not generate application code in this repo.
- Do not invent runtime surfaces.
- Do not reference secrets, API keys, or environment-specific values.
- When documentation and implementation conflict, inspect implementation before proposing changes.
- Do not assume documentation is current.

## Commit Convention
type(scope): description

Examples:
- docs(canon): add production platform source map
- governance(agents): update agent capability registry
