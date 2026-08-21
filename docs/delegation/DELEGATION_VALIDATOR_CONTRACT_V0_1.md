# Delegation Validator Contract v0.1

**Status:** Draft architecture under CG-0036; not commissioned runtime code.  
**Purpose:** Define provider-neutral cross-document checks that JSON Schema alone
cannot express.

## Required inputs

The validator receives the exact envelope, decision, applicable approval,
precondition artifact and evaluation, aggregate policy and snapshot, resource
registry snapshot and record, revocation state, MICC invocation binding, receipt
policy, and—after dispatch—the execution receipt and effect receipt.

Every input is parsed and hash-verified under
`REFERENCE_INTEGRITY_PROFILE_V0_1.md` before semantic evaluation. Unknown inputs,
missing preimages, ambiguous identities, and unsupported versions fail closed.

## Identity roles

The validator MUST keep these roles distinct and record each explicitly:

- envelope issuer (`envelope.logical_issuer_id`);
- authority holder (`envelope.delegate_logical_issuer_id`);
- request subject and MICC requester;
- PDP/decision issuer (`decision.logical_issuer_id`);
- approval issuer, when applicable;
- MICC executor; and
- execution-receipt issuer (the accountable PEP/evidence service).

Equality is required only where a named invariant requires it. In particular,
`decision.authority_holder_logical_issuer_id` and
`aggregate_snapshot.authority_holder_logical_issuer_id` MUST equal the envelope
delegate logical issuer. The PDP issuer MUST NOT be substituted for that holder
in aggregation or consumption attribution.

## Deterministic checks

In order, the validator MUST:

1. validate all closed schemas and authenticated payload hashes;
2. authenticate each issuer and authorize its role using the bound registries;
3. verify delegation lineage and monotonic non-weakening;
4. verify every governed reference and retained preimage;
5. evaluate all typed preconditions with `ALL_MUST_PASS`, recording a canonical
   evaluation artifact and hash;
6. resolve the exact MICC invocation binding and require its approval class to
   equal the decision and any applicable approval binding;
7. resolve the canonical resource record and verify the PEP target and any
   identity anchors at dispatch;
8. reject a revocation state whose authenticated sequence is not greater than
   the highest previously accepted sequence for that revocation issuer, or whose
   age exceeds the envelope bound;
9. compute aggregation with `CG0036_AGGREGATE_V0_1`, keyed to the authority
   holder, using intersection-only scope and most-restrictive grant combination;
10. enforce Council fail-closed behavior: v0.1 never returns `ALLOW` for
    `APPROVAL_COUNCIL`;
11. atomically reserve decision and applicable approval consumption before
    dispatch; and
12. authenticate the execution receipt and cross-check its decision, delegation,
    holder, MICC, resource, precondition, revocation, aggregate, consumption,
    dispatch, effect, and audit bindings.

## Required reason codes

At minimum: `SCHEMA_INVALID`, `HASH_MISMATCH`, `PREIMAGE_UNAVAILABLE`,
`ISSUER_UNAUTHORIZED`, `IDENTITY_BINDING_MISMATCH`, `PRECONDITION_FAILED`,
`MICC_BINDING_MISMATCH`, `RESOURCE_TARGET_MISMATCH`, `REVOCATION_STALE`,
`REVOCATION_SEQUENCE_REPLAY`, `AGGREGATE_CEILING_EXCEEDED`,
`COUNCIL_ALLOW_FORBIDDEN`, `CONSUMPTION_CONFLICT`, `RECEIPT_INVALID`, and
`EFFECT_UNCERTAIN`.

## Commissioning block

This contract is not a validator implementation. Autonomous commissioning
remains blocked until a provider-neutral implementation passes the end-to-end
vectors, compromise fixtures, crash-boundary vectors, and an exact-head review.
Future Council `ALLOW` additionally requires a separately governed and ratified
Council-constitution validator; this contract does not supply one.
