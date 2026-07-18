# Council Matter Template

Copy this directory to `council/matters/CG-####-slug/` when opening a matter.

## Required structure

```text
CG-####-slug/
  matter.yaml
  README.md
  sources/
  positions/
  synthesis/
  receipts/
  history/
  disposition/
  canon-links/
```

## Rules

- `matter.yaml` is the current machine-readable snapshot.
- `history/` is append-only and records every workflow transition.
- `positions/` preserves immutable attributed submissions. Revisions create new position records; originals remain.
- `synthesis/` contains derivative assemblies and must declare its source position IDs.
- `receipts/` records transport, ingestion, registration, and dispatch evidence. Hermes operates here as courier and receipt layer only.
- `disposition/` is written only after an explicit Operator decision.
- `canon-links/` records downstream canon actions; deliberation and canon movement remain separate.

Automation may scaffold, validate, index, route, and assemble. It may not ratify, infer consensus, rewrite positions silently, or merge canon.