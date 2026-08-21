# CG-0036 — Draft.2 Review Packet

**Scope:** Delegation Boundary v0.1 draft.2 only.  
**Reviewed target:** `1a3d92ea9f69e5ea0d631b0d19a9a9b5ee942312`  
**No implementation, deployment, canon promotion, credential access, or merge authority is requested.**

## Shared question

Does draft.2 define a sound, non-self-referential delegation architecture in which routine actions can proceed under bounded policy without allowing delegates, classifiers, policy authors, approval references, approval issuers, or enforcement points to manufacture authority?

Review the **complete profile set**:

- `docs/delegation/DELEGATION_BOUNDARY_V0_1.md`
- `docs/delegation/CANONICALIZATION_V0_1.md`
- `docs/delegation/CANONICALIZATION_VECTORS_V0_1.json`
- `docs/delegation/ISSUER_PROOF_V0_1.md`
- `docs/delegation/REFERENCE_INTEGRITY_PROFILE_V0_1.md`
- `docs/delegation/ISSUER_AUTHORITY_RECORD_V0_1.schema.json`
- `docs/delegation/DELEGATION_ENVELOPE_V0_1.schema.json`
- `docs/delegation/DELEGATION_DECISION_V0_1.schema.json`
- `docs/delegation/OPERATOR_APPROVAL_V0_1.schema.json`
- `docs/delegation/COUNCIL_APPROVAL_V0_1.schema.json`
- `docs/delegation/AGGREGATE_AUTHORITY_SNAPSHOT_V0_1.schema.json`
- `docs/delegation/EFFECT_CONSUMPTION_COMMIT_V0_1.md`
- `docs/delegation/EFFECT_CONSUMPTION_COMMIT_VECTORS_V0_1.json`
- `docs/delegation/AUTHORIZATION_EVALUATION_PROFILE_V0_1.md`
- `docs/delegation/RESOURCE_IDENTITY_V0_1.md`
- `docs/delegation/DELEGATION_CONFORMANCE_V0_1.md`
- `docs/delegation/STANDARDS_CROSSWALK_V0_1.md`
- `council/matters/CG-0036-delegation-boundary-v0-1/analysis/STANDARDS_AND_EXTERNAL_REVIEW_RESPONSE.md`

## Ptah

Attack implementability and conformance. Focus on RFC 8785 canonicalization, authenticated decision `issuer_proof`, protected proof-header semantics, PDP/PEP contracts, consumption/effect commit protocol, immutable precondition binding, `delegation_payload_hash` binding, structurally unreachable Council `ALLOW`, closed aggregate-authority snapshots, resource-registry snapshot binding, identifier/nonce semantics, and whether the schemas contain enough information to implement without hidden semantics.

## Thoth

Attack authority escalation and compromise paths. Focus on malicious/compromised PDP, PEP, policy publisher, approval resolver/issuer, resource registry, revocation source, consumption store, aggregate evaluator, stale caches, multi-grant composition, and whether any single component can become a hidden sovereign.

## Osiris

Attack receipt/evidence claims. Determine the minimum evidence needed to prove authorization, authenticated approval provenance, approval consumption state, correct classification, policy/precondition integrity, enforcement-time compliance, and successful effect separately. Confirm whether the current locked audit contract can safely receive this mapping only after its separate repair/review. Confirm that `council_matter_ref`, `disposition_ref`, `disposition_hash`, and `issuer_proof` cannot, by themselves, prove that a Council disposition was validly constituted.

## Theia

Attack integration coherence. Determine whether CG-0036 can coexist cleanly with MICC and the Cognition Contract without taxonomy drift, whether Operator and Council approvals remain bounded to current state and authenticated authority, whether Council approval remains fail-closed until a separately governed disposition validator proves composition, provenance, and quorum, and whether the future Room/HUD can surface aggregate authority and approval provenance without turning relevance/presentation into an authority layer.

## Synthesis constraints

- Do not call the four files "independent reviews" unless independent execution provenance is separately evidenced.
- Preserve material disagreement.
- State any invariant that still exists only in prose rather than enforceable/conformance-testable form.
- No Operator disposition until all four role-bounded positions are filed and synthesized.
- Preserve the Council-constitution validator as an open, blocking implementation dependency. Do not treat Operator-authority disposition records or CG-0031 as that validator.
- Treat this packet as the corrected successor to packet v1 reviewed by Osiris; packet v1 carried a superseded embedded target citation. The Osiris position remains filed against the exact target shown above.
