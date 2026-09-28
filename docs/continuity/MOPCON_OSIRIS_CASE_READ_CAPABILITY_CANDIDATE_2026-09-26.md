# MOPCON ↔ Osiris case read capability — candidate record

**Status:** IN_REVIEW / candidate operational evidence; authority effect NONE  
**Recorded:** 2026-09-26  
**Implementation subject:** `mirrornode/mirrornode-platform` PR #53, head `8ca41410785f4af316e38d30a9cac25dfc7dcf34`  
**Schema prerequisite:** draft Platform PR #56, head `ace95524609246dcb0cdce16021fe949ce494d6e`; still unmerged. The reviewed local test/documentation correction is not a new remote head.
**Scope:** one read-only Osiris case projection for the private MOPCON operator surface.

## Capability boundary

- Intended caller: the MOPCON server, using a separately provisioned server-to-server bearer secret. The consumer integration and live authentication have not been re-attested at the implementation head above.
- Entry point: `GET /api/internal/mopcon/cases` on Platform. The read secret is `MOPCON_CASES_READ_SECRET`, server-only, never `NEXT_PUBLIC_*`.
- Platform uses its server-side Supabase service-role credential for one `public.mopcon_case_projection()` RPC. MOPCON receives neither the credential nor direct database access.
- The SQL function is `SECURITY INVOKER`; `EXECUTE` is revoked from `PUBLIC`, `anon`, and `authenticated`, and granted to `service_role`. Its source is `public.guest_audit_purchases` for flow `osiris-audit-v1`. SQL scopes by flow and status, but provides no caller-specific or tenant-specific authorization. The service role bypasses RLS; the route bearer-secret check protects this server-owned read.
- Selection contract: all rows in `intake_pending`, `intake_complete`, `fulfillment_started`, or `paused`, plus the latest 100 `delivered` or `refunded` rows, read in one PostgreSQL statement snapshot. The terminal branch has a partial order index at the implementation head above. A local correction under review adds an actionable partial order index with the exact actionable predicate; it does not cap actionable rows or confer additional authority.
- Response fields: internal case UUID, masked customer email, flow, payment and fulfillment statuses, timestamps for creation/update/intake/review/start/delivery, intake-presence flag, and artifact count. It omits Stripe identifiers, raw intake text, artifact URLs, and secrets. The Platform process temporarily receives source email and artifact-link JSON to derive the masked email and count.
- `mutation: disabled` is a response declaration. The route implements GET only; it grants no fulfillment, approval, release, delivery, refund, command, or governance authority. A read can inform an Operator, but cannot itself decide or advance state.

## Verification and release boundary

At the recorded implementation head, the SQL correction has passed a rollback-only PostgreSQL 17.6 fixture replay with 501 actionable and 150 terminal rows: the RPC returned 501 actionable plus the latest 100 terminal rows, with the expected function privileges. The disposable project retained its prior table shape and row count after rollback. A second historical rollback-only replay applied the draft baseline migration SQL from Platform PR #56 at `6b8e52699bcd14b1a2a04c7caae9950ecde5af22` followed by the corrected #53 projection migration to a staged legacy Stripe-primary-key fixture; it verified UUID primary key, unique session identifier, 601-row projection, and RPC privileges. That historical replay predates the session-identifier type guard and does not validate current #56. It is a combined relevant-migration replay, not a pristine replay of every repository migration. It does not establish performance at production scale, live E2E, or secret provisioning.

### Local correction evidence — 2026-09-27 (not a new PR head)

A fresh network-disabled disposable PostgreSQL 17.6 test applied the selected creation/intake migrations, the unchanged UUID migration from #56 at `ace95524609246dcb0cdce16021fe949ce494d6e`, and the projection correction based on `8ca41410785f4af316e38d30a9cac25dfc7dcf34`. Corrected projection SQL SHA-256: `9dd1d3d74ef65bab7ea3425fae4ae053b083f96e0e79e0df3f404654f04f738b`. With 501 actionable, 100,000 terminal and 100 other-flow synthetic rows, original and corrected RPC results were identical (601 rows); all actionable and latest 100 terminal selection, flow isolation, EXECUTE privileges, service-role invocation and migration rerun passed. The temporary database was removed.

An EXPLAIN ANALYZE probe of the exact extracted SQL body used the actionable partial index after correction; the original body used a sequential scan filtering 100,100 rows. This is a single synthetic distribution, not a production RPC plan, concurrency/load benchmark, or a guaranteed index choice. The planner may choose a sequential scan for other distributions. All actionable rows and associated payload still need retrieval and ordering; no capacity limit or latency commitment is established. Index creation has deployment-time locking/build cost requiring separate evaluation.

This selected-migration test is neither full integrated-tree replay nor pristine bootstrap. `20260813212729_harden_guest_audit_purchase_privileges.sql` still references a legacy function absent from repository creation migrations. Its bootstrap repair remains separate; documented legacy-state compatibility cannot waive pristine-replay debt. Neither this local correction nor its evidence changes the immutable implementation head stated above. A published correction requires its own exact-head review and checks.

The earlier Codex review on Platform head `d92caeb98ee3a9fb93290964127186b726523b9f` raised P1 CORE-HUB recording and P2 full-ledger materialization. The new Platform head needs fresh independent exact-head review, CI/Canon Gate, and a full disposable migration replay with its schema prerequisite. Neither this record nor ordinary review promotes canon. Any canon promotion follows Ptah evaluation, explicit Operator ratification, and a promotion record under `MASTER_INDEX.md`.

**HOLD:** No merge, deployment, production migration, credential provisioning, live customer read, publication, or operational promotion is authorized by this candidate record.
