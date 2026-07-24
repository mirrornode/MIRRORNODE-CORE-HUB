# POS-0002 — Ptah Implementation Contract Review — CG-0032

## Verified Current Implementation

- CG-0032 is documentation-only and carries no executable authority. The current local MCP prototype remains outside governed source control for purposes of this matter and is recorded only as observed evidence.
- The observed prototype is a local stdio MCP server with user-scoped Claude Code registration and four demonstrated tools: `mirrornode_status`, `ledger_summary`, `recent_ledger_events`, and `validate_ledger_provenance`.
- The observed validation result of 45 events checked with 0 reported errors is properly framed as an observation, not as architecture, approval, or implementation acceptance.
- `tools/@mirror` currently owns the ledger validation behavior used as the reference for the prototype. Its `validate` path invokes `ensure_files` before running deterministic payload-digest checks, so directly exposing that command as a strictly side-effect-free MCP validation primitive would not preserve the intended read-only boundary.
- CORE-HUB declares itself the governed canonical surface for charters, contracts, schemas, promotion records, and source-of-truth decisions while explicitly separating runtime implementation into appropriate execution repositories unless an implementation path actually exists in CORE-HUB.

## Contract Assessment

1. **Single canonical validation rule:** Technically implementable. Section 6 correctly prevents the MCP layer from becoming the permanent owner of duplicated provenance logic and leaves multiple feasible implementation mechanisms open: extract a side-effect-free canonical primitive, expose a governed read-only canonical interface, or adopt another Council-approved single-owner mechanism.
2. **Current duplication:** Correctly characterized as temporary implementation fact rather than architectural precedent. The contract neither blesses the duplicate implementation nor requires it to remain.
3. **Lifecycle and reproducibility:** Substantially sufficient. Tracked source control, code ownership, locked dependencies, reproducible startup, transport declaration, read-only tests, positive/negative projection fixtures, failure tests, injection tests, secret-disclosure tests, unknown-field rejection, drift tests, upgrade/rollback, and alternate-authority checks form a credible minimum acceptance packet.
4. **Failure behavior:** Directionally correct and fail-closed, but not fully deterministic at the contract level. The table specifies semantic outcomes such as `unavailable`, `failed check`, `unsupported`, and `partial`, yet only one row explicitly requires a disclosure-safe reason code. Without a stable machine-readable outcome vocabulary and reason-code requirement across failure classes, independent implementations can satisfy the prose while returning incompatible shapes, making conformance tests weaker than the contract intends.
5. **Repository placement:** Correctly unresolved. The contract should not select CORE-HUB, a dedicated repo, or another execution surface before a later implementation-location review.
6. **Prototype facts:** No material overstatement found. The draft appropriately distinguishes observed facts from governed implementation state. It does not claim the local prototype is tracked, persistent, remotely exposed, or accepted infrastructure.
7. **Expansion gate:** Sufficient for definition stage. It requires exact capability/field scope, canonical source, disclosure justification, authority semantics, failure behavior, injection risk, test evidence, and architectural-class impact before expansion can be proposed.

## Identified Implementation Risks

- **Failure-contract drift:** Without stable machine-readable outcome and reason-code semantics, different implementations could encode identical failure states differently while each claiming compliance.
- **Canonical-rule drift:** Any period in which MCP duplicates the `@mirror` validation algorithm creates a drift window until one canonical side-effect-free primitive exists.
- **Environment reproducibility:** The prototype currently depends on a local Python/`uv` environment and user-scoped registration. Future acceptance must pin both package resolution and startup behavior rather than rely on workstation coincidence.
- **Local executable replacement:** A user-scoped registration pointing at a mutable local path can continue to resolve after the file changes. Future governed operation needs source/version identity and startup evidence tied to the reviewed implementation.
- **Read-only implementation leakage:** A nominally read-only tool can still trigger incidental initialization, metadata writes, cache writes, or setup behavior if it wraps existing commands without inspecting their side effects. Tests must verify actual behavior, not only tool naming.
- **Projection-schema ambiguity:** The contract correctly prohibits raw/private fields but does not yet define the eventual concrete projection schema; that remains a future implementation matter and must not be improvised by tool code.

## Required Revisions

One definition-level revision is required before an accepting disposition:

### Add deterministic failure outcome semantics

Section 12 should require a stable machine-readable failure/result contract across all listed conditions, not only prose labels. At minimum, the definition should require:

- a bounded outcome/status enum for projection operations;
- a stable disclosure-safe reason code for every non-success outcome;
- an explicit completeness indicator where partial scans are possible;
- prohibition on free-text-only failure classification; and
- conformance tests that assert those exact machine-readable semantics.

The contract does **not** need to define a full tool response schema in CG-0032. It does need to make deterministic failure classification a governing requirement so later implementations cannot diverge while claiming the same failure behavior.

No other definition-level revision is required from the implementation-reality position.

## Residual Future Questions

These belong to the later implementation-remediation matter:

- Where should the executable live and which repository should own release/version history?
- What exact canonical side-effect-free validation primitive should replace duplicated digest logic?
- What package-locking strategy and supported Python/runtime version should be required?
- What exact projection schemas replace current path-bearing and raw-event outputs?
- How should executable identity be pinned to prevent registration from silently following unreviewed local edits?
- What startup model is intended: per-client stdio spawn, persistent local process, or another separately authorized lifecycle?
- What test harness proves that read-only tools perform no incidental writes?
- What evidence is required to show rollback restores both executable version and client registration safely?

## Recommendation

**Support with one required definition revision.**

CG-0032 is technically coherent and implementable without creating a second canonical validation authority, but Section 12 should be tightened to require deterministic machine-readable outcome and reason-code semantics before an accepting Operator disposition.

This recommendation authorizes no executable change, relocation, registration change, or output remediation.