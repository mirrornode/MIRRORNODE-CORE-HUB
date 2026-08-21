# Delegation Architecture

Draft artifacts under CG-0036:

- `DELEGATION_BOUNDARY_V0_1.md` — normative draft semantics.
- `CANONICALIZATION_V0_1.md` — RFC 8785 hash/authenticated-payload profile.
- `CANONICALIZATION_VECTORS_V0_1.json` — fixed canonicalization and snapshot-hash vectors.
- `ISSUER_PROOF_V0_1.md` — protected-header proof metadata; schema hints are untrusted; credential maps to `logical_issuer_id`.
- `ISSUER_AUTHORITY_RECORD_V0_1.schema.json` — hash-bound root-issuer delegable scope (authentication ≠ authorization).
- `REFERENCE_INTEGRITY_PROFILE_V0_1.md` — governed-reference hash binding, resolver behavior, and preimage retention.
- `DECISION_PRECONDITIONS_V0_1.schema.json` — closed typed precondition language.
- `AGGREGATE_AUTHORITY_POLICY_V0_1.schema.json` — deterministic aggregation ceilings and combiners.
- `MICC_INVOCATION_BINDING_V0_1.schema.json` — exact MIM, adapter, capability, lifecycle, scope, requester, executor, class, and nonce binding.
- `REVOCATION_STATE_V0_1.schema.json` — authenticated monotonic revocation state.
- `RESOURCE_REGISTRY_SNAPSHOT_V0_1.schema.json` — authenticated canonical resource mapping and target anchors.
- `EXECUTION_RECEIPT_V0_1.schema.json` — authenticated authorization/consumption/dispatch/effect evidence.
- `DELEGATION_AUDIT_MAPPING_V0_1.md` — additive mapping into the repaired locked AUDIT_EMISSION envelope.
- `DELEGATION_VALIDATOR_CONTRACT_V0_1.md` — provider-neutral cross-document validation contract.
- `END_TO_END_CONFORMANCE_VECTORS_V0_1.json` — compromise-path and evidence fixture index.
- `DELEGATION_ENVELOPE_V0_1.schema.json` — machine-readable delegation grant shape (includes `delegate_logical_issuer_id` identity binding).
- `DELEGATION_DECISION_V0_1.schema.json` — PDP decision / PEP enforcement binding shape (authenticated; Council ALLOW unreachable).
- `OPERATOR_APPROVAL_V0_1.schema.json` — authenticated, request-bound Operator approval object.
- `COUNCIL_APPROVAL_V0_1.schema.json` — authenticated Council evidence object; cannot unlock v0.1 `ALLOW`.
- `AGGREGATE_AUTHORITY_SNAPSHOT_V0_1.schema.json` — closed aggregate-authority snapshot hashed into decisions.
- `EFFECT_CONSUMPTION_COMMIT_V0_1.md` — effect/consumption durable commit protocol.
- `EFFECT_CONSUMPTION_COMMIT_VECTORS_V0_1.json` — crash-boundary expected outcomes.
- `AUTHORIZATION_EVALUATION_PROFILE_V0_1.md` — deterministic authorization evaluation order and aggregate-authority profile.
- `RESOURCE_IDENTITY_V0_1.md` — canonical resource identity, URI mapping, and registry-snapshot binding.
- `DELEGATION_CONFORMANCE_V0_1.md` — cross-document, provenance, consumption, TOCTOU, and commissioning checks.
- `STANDARDS_CROSSWALK_V0_1.md` — informative crosswalk to current standards and practices.

These artifacts are pre-canon and do not grant implementation authority.
