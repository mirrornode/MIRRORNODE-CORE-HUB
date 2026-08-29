# Hermes Transport Truth Slice — Acceptance Criteria

**Status:** PROPOSED / NON-CANONICAL  
**Scope:** First corrective slice only. No durable provider implementation is authorized here.

This slice is complete only when the current prototype stops manufacturing stronger success semantics than the runtime can prove.

## Required corrections

- Hermes `/route` must not return `routed=true` for an in-memory append.
- Hermes route audit evidence must not emit `message_routed` before consumer delivery occurs.
- Hermes `/ingest` and `/route` responses must identify process-local volatile buffering and must not reuse a canonical transport state before governed invocation context is resolved.
- Administrative queue flush must require an explicit authorization boundary or be unavailable.
- Canon `invoke()` must not return `success=true` when a command has no handler.
- An unimplemented command must return a machine-readable non-success outcome.
- The focused truth-semantics gate must execute these assertions as a blocking PR check.

## Explicit non-goals

- No Redis/Inngest/QStash/Supabase selection.
- No durable queue implementation.
- No production deployment claim.
- No canon promotion.
- No autonomous approval or release.

## Exit condition

After this slice, the legacy prototype may still be incomplete, but its observable API and audit semantics must be honest about that incompleteness. The next slice may then introduce governed invocation context and durable transport behind the provider-neutral Hermes Transport Contract v0.1.
