# Claude / PTAH Lane — Plugin Constellation Implementation Review Request

**Date:** 2026-11-13  
**Status:** PREPARED FOR HANDOFF / NOT TRANSMITTED / NO FORMAL VERDICT  
**Target:** `docs/mcp/CHATGPT_PLUGIN_CONSTELLATION_AND_LATTICE_V0_1_PROPOSED_2026-11-13.md`  
**Authority:** Advisory review request only. A Claude response is not automatically a formal PTAH judgment or approval.

## Read these exact source authorities first
1. `docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md` and CG-0032 disposition.
2. CG-0033 MICC/MIM contract and `PTAH_POSITION.md` / `THOTH_POSITION.md`.
3. `GOVERNANCE.md`, `MASTER_INDEX.md`, `CANONICAL_SOURCES.md`, `AGENTS.md`.
4. `docs/continuity/NAMING_AND_SOURCE_SCOPE_RECONCILIATION_2026-08-13.md`.
5. The proposed constellation architecture in this branch.

## Review assignment
Determine the smallest legitimate way to provide separately valuable THEIA, PTAH and THOTH ChatGPT experiences while keeping the lattice as a private, authorized substrate initially.

Please return:
- Proposed component ownership and execution-repository placement; identify whether a Site-hosted model or independent MCP server can be made contract-conforming without modifying the currently frozen local prototype.
- Exact trust boundaries: client identity, tenant isolation, consent, external model egress, per-product namespaces, key custody, revocation, authorization envelopes and receipts.
- What can be shared across products and what must remain separate; show the failure cases for cross-node impersonation and authority laundering.
- Whether CG-0032 must be amended, expanded by a separate Council matter, or kept untouched while a new external MCP architectural class is separately defined.
- Dependencies on MICC/MIM and the actual evidence needed for adapter conformance, replay resistance, capability scope and credential disclosure.
- A read-only, synthetic-fixture first vertical slice, with concrete endpoint/tool contracts, schemas, deterministic failure outcomes, tests, exact implementation ownership and rollback.
- Explicit blockers for adding ChatGPT runtime attachment, remote exposure, public distribution, customer-data processing or any write path.
- A cost/effort and feasibility assessment for a twelve-hour private pilot that clearly distinguishes runnable evidence from proposals.

## Required return format
1. Exact source/ref reviewed and date.
2. OBSERVED facts vs REPORTED facts vs INFERRED proposals.
3. P0/P1 security or authority findings; P2 implementation issues.
4. Recommended architecture, alternatives and trade-offs.
5. Enforceable invariants and test fixtures.
6. Minimal next authorization needed; no presumed approval.
7. Recommendation: SUPPORT / REVISE / HOLD, with reasons.

**Do not** modify repositories, expose credentials, connect ChatGPT to the existing MCP prototype, deploy, publish or claim a PTAH verdict merely because Claude provided advice. Submit findings for explicit Operator and appropriate PTAH/THOTH review.