# MIRRORNODE Governance & Evidence Index

**Status:** NON-CANONICAL OPERATIONAL INDEX

## Purpose

This directory is a source-linked routing and status layer. It helps locate and reconcile governance, legal/issued, client-scoped, technical, and evidentiary records without becoming a parallel authority plane.

## The Index may

- locate source records;
- record evidence states;
- link decisions, risks, releases, incidents, access, dependencies, and evidence packs;
- expose review status and stale state;
- identify unresolved gaps.

## The Index may not

- create authority;
- establish canonical status;
- upgrade evidence state without source-backed evidence;
- overwrite or silently supersede a legal or canonical source record;
- infer governance authority from technical capability or provider permission;
- treat file location as promotion.

## Source roles

Each index entry must identify one of:

- `OPERATIONAL_RECORD`
- `CANONICAL_POINTER`
- `LEGAL_ISSUED_POINTER`
- `CLIENT_SCOPED_RECORD`
- `UNRESOLVED_UNKNOWN`

## Required shared metadata

Every structured record MUST inherit `docs/records-architecture/schemas/shared-record.schema.json` and use `record_id` as its sole durable primary identifier.

Domain-specific IDs are aliases only.

## Review semantics

For any record requiring periodic review:

- missing or invalid `next_required_review` => `STALE_FOR_USE`;
- unverified/unavailable trusted time => `STALE_FOR_USE`;
- trusted time after review deadline => `STALE`;
- scheduler/write failure cannot preserve an expired record as current.

The effective review state is evaluated at read time by consuming software.

## Canonical boundary

CORE-HUB promotion establishes MIRRORNODE canonical-governance status only for the promoted scope. Canonical status, legal authority, contractual authority, provider permission, runtime capability, and evidence state remain distinct.

External canonical artifacts must use immutable revision anchors described by `canonical-anchor.schema.json`.
