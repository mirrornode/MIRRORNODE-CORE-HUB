# POS-0004 — Osiris Disclosure and Authority Review — CG-0032

## Verified Current Implementation

- The observed local MCP prototype reads canonical/local continuity state and exposes four tools, but CG-0032 explicitly records those outputs as evidence rather than approved disclosure shapes.
- `recent_ledger_events` is already marked nonconforming as currently shaped because it returns raw event material and model-interpretable text.
- Local path-bearing output in `mirrornode_status` and `ledger_summary` is explicitly flagged for minimization and is not treated as projection-safe by default.
- The current integrity result (`valid: true`, 45 events checked, 0 errors) is recorded as a prototype observation only. The contract explicitly denies any inference from digest consistency to truth, approval, actor identity, authorization, freshness, safety, or publication permission.
- The analogous Continuity Console definition already establishes MIRRORNODE precedent that private-derived material must arrive as a separately approved projection, that public-looking source metadata is not automatically safe, and that publication requires separate authorization. CG-0032 is aligned with that precedent while governing a different surface.

## Contract Assessment

1. **Raw canonical state:** Sufficiently prohibited by default. The contract requires projection before the external-model boundary, explicit field allowlisting, unknown-field rejection, and default prohibition of raw ledger payloads, Council deliberation, Operator rationale, local topology, private runtime state, arbitrary canonical free text, and multiple private-data classes.
2. **Model-side filtering:** Correctly prohibited. The definition does not permit sending private canonical material to a model and asking the model to decide what is safe. Projection must be constructed before crossing the boundary.
3. **Paths, actors, contributors, topology, free text, integrity tokens:** The default-deny allowlist model is sufficient at definition level. Local paths, usernames/identity data, topology, arbitrary free text, and raw ledger payloads are explicitly prohibited by default. Actor/contributor or integrity-token fields are not implicitly safe merely because they are metadata or hashed; they would require separate explicit review and allowlisting.
4. **Authority language:** Strong. `valid`, `provenance`, `authority`, `approved`, `verified`, and `authorized` are identified as controlled semantic terms. The digest section expressly limits what integrity checking means. The current prototype’s `valid: true` wording is not approved as the future projection vocabulary.
5. **Failure disclosure:** Fail-closed and disclosure-minimized in principle. Ptah’s required deterministic outcome/reason-code revision should be incorporated so implementations do not fall back to raw exception text, local paths, or source fragments when reporting failure.
6. **Canonical versus projection state:** Explicit. Canonical private state remains upstream; MCP receives only an approved projection contract/output. The MCP surface is neither the authoritative archive nor a canonical state store.
7. **Publication boundary:** Preserved. MCP-projectability does not authorize publication, remote exposure, deployment, or additional runtime attachment. Section 18 separates those decisions, and the document header independently denies publication authority.

## Identified Disclosure or Authority Risks

- **Count and cadence inference:** Even a bounded record count can reveal operational cadence or change volume. Section 11 correctly treats counts as only potentially projectable; implementation review must justify exact count fields rather than assume aggregation is harmless.
- **Role-label inference:** Generic actor or authority labels may still reveal internal workflow structure. If later allowed, labels should be purpose-built projection values rather than copied canonical actor/contributor fields.
- **Integrity-token leakage:** Raw digests or canonical integrity tokens may become correlatable identifiers or acquire false authority meaning in model reasoning. Neutral outcome projection is preferable to exposing canonical hash values unless a later review specifically justifies them.
- **Failure-detail leakage:** Raw parser errors, permission errors, filesystem exceptions, or schema diagnostics can reveal paths, source shape, dependency details, or record fragments. Stable reason codes and safe summaries are required.
- **Documentation/publication ambiguity:** CG-0032’s authorized public draft PR is a documentary action, while `publication` in the MCP contract refers to publication/exposure of MCP projection output or a product surface. Future records should preserve that scope distinction so documentary review activity is not confused with MCP publication authority.
- **Cross-surface equivalence:** A field approved for local MCP projection is not thereby approved for Continuity, Platform, remote MCP, API, downloadable artifact, or any other public surface.

## Required Revisions

No additional independent disclosure revision is required beyond the revisions already identified by Ptah and Thoth:

1. **Ptah:** deterministic machine-readable outcome/status and disclosure-safe reason-code semantics across failure classes;
2. **Thoth:** primitive-independent projection, anti-capability, and expansion-gate language covering the entire MCP server surface rather than tools alone.

Those revisions materially strengthen disclosure safety by preventing raw failure details and alternate protocol channels from bypassing the projection contract.

The current contract already separates MCP projection approval from publication permission strongly enough for definition-stage acceptance once those shared revisions are incorporated.

## Residual Future Conditions

A later implementation-remediation matter should require:

- an exact MCP-safe projection schema with field-by-field disclosure justification;
- explicit handling of actor/contributor labels, counts, timestamps, freshness, and integrity outcomes;
- prohibition or separate justification for raw canonical hashes/tokens;
- fixtures proving local paths, raw ledger text, private topology, arbitrary free text, and sensitive fields cannot cross the boundary;
- disclosure-safe error fixtures with no raw exception or source-fragment leakage;
- review of enumeration and cadence inference for counts/history windows;
- separate authorization for any remote exposure or additional model runtime;
- independent publication review for any later public-facing surface, even if the same field is approved for local MCP projection.

## Recommendation

**Support with incorporation of the Ptah and Thoth required revisions.**

No further Osiris-specific definition blocker is identified. The contract correctly distinguishes canonical private state, MCP-safe projection state, integrity checking, authority, and publication.

This recommendation does not approve the current prototype output shapes, remote exposure, additional runtime attachment, or publication.