# MOPCON ↔ Osiris case read capability — candidate record

**Status:** IN_REVIEW / candidate operational evidence; authority effect NONE  
**Recorded:** 2026-09-26  
**Implementation subject:** `mirrornode/mirrornode-platform` PR #53, head `8ca41410785f4af316e38d30a9cac25dfc7dcf34`  
**Schema prerequisite:** draft Platform PR #56, head `bf22464fe51a6a4637c31bef589bac0508aa8b02`  
**Scope:** one read-only Osiris case projection for the private MOPCON operator surface.

## Capability boundary

- Intended caller: the MOPCON server, using a separately provisioned server-to-server bearer secret. The consumer integration and live authentication have not been re-attested at the implementation head above.
- Entry point: `GET /api/internal/mopcon/cases` on Platform. The read secret is `MOPCON_CASES_READ_SECRET`, server-only, never `NEXT_PUBLIC_*`.
- Platform uses its server-side Supabase service-role credential for one `public.mopcon_case_projection()` RPC. MOPCON receives neither the credential nor direct database access.
- The SQL function is `SECURITY INVOKER`; `EXECUTE` is revoked from `PUBLIC`, `anon`, and `authenticated`, and granted to `service_role`. Its source is `public.guest_audit_purchases` for flow `osiris-audit-v1`.
- Selection contract: all rows in `intake_pending`, `intake_complete`, `fulfillment_started`, or `paused`, plus the latest 100 `delivered` or `refunded` rows, read in one PostgreSQL statement snapshot. The terminal branch has a partial order index in the candidate migration.
- Response fields: internal case UUID, masked customer email, flow, payment and fulfillment statuses, timestamps for creation/update/intake/review/start/delivery, intake-presence flag, and artifact count. It omits Stripe identifiers, raw intake text, artifact URLs, and secrets. The Platform process temporarily receives source email and artifact-link JSON to derive the masked email and count.
- `mutation: disabled` is a response declaration. The route implements GET only; it grants no fulfillment, approval, release, delivery, refund, command, or governance authority. A read can inform an Operator, but cannot itself decide or advance state.

## Verification and release boundary

At the recorded implementation head, the SQL correction has passed a rollback-only PostgreSQL 17.6 fixture replay with 501 actionable and 150 terminal rows: the RPC returned 501 actionable plus the latest 100 terminal rows, with the expected function privileges. The disposable project retained its prior table shape and row count after rollback. This fixture does not establish a full repository migration replay, performance at production scale, live E2E, or secret provisioning.

The earlier Codex review on Platform head `d92caeb98ee3a9fb93290964127186b726523b9f` raised P1 CORE-HUB recording and P2 full-ledger materialization. The new Platform head needs fresh independent exact-head review, CI/Canon Gate, and a full disposable migration replay with its schema prerequisite. Neither this record nor ordinary review promotes canon. Any canon promotion follows Ptah evaluation, explicit Operator ratification, and a promotion record under `MASTER_INDEX.md`.

**HOLD:** No merge, deployment, production migration, credential provisioning, live customer read, publication, or operational promotion is authorized by this candidate record.
