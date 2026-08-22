# CG-0036 — Exact-Target Successor Review Packet

**Scope:** Delegation Boundary v0.1 draft.2 only.  
**Normative correction target (immutable):** `299c24a70dda0e2f21c00b23be3bf52a60376435`  
**Packet publication note:** this packet is published in the immediately following administrative commit and does not alter the normative target above. Reviewers MUST attest to `299c24a70dda0e2f21c00b23be3bf52a60376435`, not to an ancestor and not to the packet-publication commit.  
**Historical correction target (preserved, superseded):** `e4ab25a128eb5b76312765eb9ba2d29a2e7ad796`  
**Original historical packet target (preserved, not rewritten):** `1a3d92ea9f69e5ea0d631b0d19a9a9b5ee942312`  
**No implementation, deployment, canon promotion, credential access, or merge authority is requested.**

This is the successor exact-target packet after the bounded Codex correction pass. Prior council positions remain positions against their original immutable targets and are not silently re-attributed to this target.

## Shared question

Does draft.2 at `299c24a70dda0e2f21c00b23be3bf52a60376435` define a sound, non-self-referential delegation architecture in which routine actions can proceed under bounded policy without allowing delegates, classifiers, policy authors, approval references, approval issuers, aggregate evaluators, registries, or enforcement points to manufacture authority?

Review the **complete profile set at the immutable normative target**:

- `docs/delegation/DELEGATION_BOUNDARY_V0_1.md`
- `docs/delegation/CANONICALIZATION_V0_1.md`
- `docs/delegation/CANONICALIZATION_VECTORS_V0_1.json`
- `docs/delegation/ISSUER_PROOF_V0_1.md`
- `docs/delegation/REFERENCE_INTEGRITY_PROFILE_V0_1.md`
- `docs/delegation/DECISION_PRECONDITIONS_V0_1.schema.json`
- `docs/delegation/ACTIVE_GRANT_INVENTORY_V0_1.schema.json`
- `docs/delegation/AGGREGATE_AUTHORITY_POLICY_V0_1.schema.json`
- `docs/delegation/AGGREGATE_AUTHORITY_SNAPSHOT_V0_1.schema.json`
- `docs/delegation/MICC_INVOCATION_BINDING_V0_1.schema.json`
- `docs/delegation/REVOCATION_STATE_V0_1.schema.json`
- `docs/delegation/RESOURCE_REGISTRY_SNAPSHOT_V0_1.schema.json`
- `docs/delegation/EXECUTION_RECEIPT_V0_1.schema.json`
- `docs/delegation/DELEGATION_AUDIT_MAPPING_V0_1.md`
- `docs/delegation/DELEGATION_VALIDATOR_CONTRACT_V0_1.md`
- `docs/delegation/END_TO_END_CONFORMANCE_VECTORS_V0_1.json`
- `docs/delegation/ISSUER_AUTHORITY_RECORD_V0_1.schema.json`
- `docs/delegation/DELEGATION_ENVELOPE_V0_1.schema.json`
- `docs/delegation/DELEGATION_DECISION_V0_1.schema.json`
- `docs/delegation/OPERATOR_APPROVAL_V0_1.schema.json`
- `docs/delegation/COUNCIL_APPROVAL_V0_1.schema.json`
- `docs/delegation/EFFECT_CONSUMPTION_COMMIT_V0_1.md`
- `docs/delegation/EFFECT_CONSUMPTION_COMMIT_VECTORS_V0_1.json`
- `docs/delegation/AUTHORIZATION_EVALUATION_PROFILE_V0_1.md`
- `docs/delegation/RESOURCE_IDENTITY_V0_1.md`
- `docs/delegation/DELEGATION_CONFORMANCE_V0_1.md`
- `docs/delegation/STANDARDS_CROSSWALK_V0_1.md`
- `council/matters/CG-0036-delegation-boundary-v0-1/matter.yaml`
- `council/matters/CG-0036-delegation-boundary-v0-1/analysis/STANDARDS_AND_EXTERNAL_REVIEW_RESPONSE.md`

## Exact-head correction surfaces

The bounded correction pass after `397e0f51bd224ae0cc19c7baf2c51212669d79c9` addresses only the five Codex findings from that head:

1. Complete active-grant inventory is now independently authenticated and hash-bound through `ACTIVE_GRANT_INVENTORY_V0_1`.
2. `CG0036_AGGREGATE_V0_1` now has deterministic formulas and authenticated metric inputs, including per-grant `budget_ceiling` and policy `budget_unit`.
3. String `RESOURCE_VERSION` values permit equality/inequality only; ordered comparisons are restricted to safe integers.
4. `UNCERTAIN` execution receipts require at least durable dispatch intent and may not claim finalized approval consumption.
5. This successor packet is bound to the immutable normative correction target above.

## Final bounded conformance follow-up

The follow-up pass after `d46ff9844a84e19b8c6d756262046d065807f3d1` closes the five findings from review `4999368577`:

1. Root issuer-authority records now bind unit-aware budget ceilings independently of the envelope.
2. v0.1 requires every active grant to bind one identical aggregate-policy reference and hash; mismatches fail closed.
3. `RESOURCE_VERSION.expected` rejects booleans and permits only strings or safe integers under the defined operator matrix.
4. All envelope, decision, approval, and aggregate-snapshot canonicalization fixtures carry the required fields and independently recomputed RFC 8785/SHA-256 hashes.
5. Active-grant inventory reference/hash integrity is registered in both the normative profile and the conformance sweep.

## Final semantic closure addendum

The final bounded pass also rejects undocumented numeric `DEPENDENCY_STATE` expectations and records released approval reservations only as `approval_consumption: RELEASED` with a confirmed `effect_outcome: NO_EFFECT`. These changes close the two P2 findings from review `4999786411` without altering the authority model.

## Ptah

Attack implementability and conformance. In addition to existing surfaces, verify that active-grant inventory completeness, aggregate formulas, safe-integer arithmetic, budget-unit handling, ordering rules, and independent recomputation are implementable without hidden semantics.

## Thoth

Attack authority escalation and compromise paths. In addition to existing surfaces, assume the aggregate evaluator is stale or compromised and determine whether omission of an active grant can still convert a denial into `ALLOW`. Verify that the grant-registry authority is distinct from the evaluator authority path.

## Osiris

Attack receipt/evidence claims. Verify that the active-grant inventory, aggregate snapshot, and independent recomputation evidence establish completeness rather than merely evaluator assertion. Confirm that `UNCERTAIN` receipts cannot claim no dispatch intent or finalized approval consumption.

## Theia

Attack integration coherence. Verify that the new grant-inventory and aggregate-budget bindings do not create taxonomy drift or an unintended authority source, and that the Room/HUD can present these records as evidence without becoming the source of authority.

## Synthesis constraints

- Every position MUST name the immutable normative target `384ff115f21497c096d09051cbc0d63155c76e7b`.
- Do not call the four files "independent reviews" unless independent execution provenance is separately evidenced.
- Preserve material disagreement.
- State any invariant that still exists only in prose rather than enforceable/conformance-testable form.
- No Operator disposition until all four role-bounded positions are filed and synthesized.
- Preserve the Council-constitution validator as an open, blocking implementation dependency. Do not treat Operator-authority disposition records or CG-0031 as that validator.
