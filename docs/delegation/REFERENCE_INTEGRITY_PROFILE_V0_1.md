# Governed Reference Integrity Profile v0.1

**Status:** Draft under CG-0036; no implementation or canon authority.  
**Purpose:** Make every authority-relevant repository reference immutable,
retrievable, and independently verifiable.

## 1. Reference classes

A field is a **governed reference** when the resolved artifact can change whether
an action is authorized, how authority ends, or what evidence is required after
an effect. Every governed reference MUST be paired in the same authenticated
object with the RFC 8785 SHA-256 digest of the exact resolved artifact.

This rule includes policy, preconditions, issuer authority, identity and resource
registry snapshots, revocation sources, receipt policies, and aggregate-authority
policies. A reference is not exempt merely because it governs enforcement or
evidence after a PDP decision. Navigation-only links that cannot affect an
authorization result MUST be explicitly labelled informative and MUST NOT be
consumed by a PDP or PEP.

## 2. Resolution and verification

For each `(ref, hash)` pair, the consumer MUST:

1. resolve the reference without path traversal or ambient branch movement;
2. retrieve the exact byte preimage identified by the reference;
3. parse with duplicate-key rejection and the I-JSON restrictions in
   `CANONICALIZATION_V0_1.md` when the artifact is JSON;
4. canonicalize JSON artifacts with RFC 8785 and compute SHA-256;
5. compare the result to the authenticated hash before using the artifact; and
6. fail closed on absence, ambiguity, unsupported media type, parse failure,
   hash mismatch, or unavailable preimage.

Resolvers MUST NOT substitute the current contents of a mutable symbolic path
for a previously evaluated preimage. Repository paths therefore require a
separately retained content-addressed preimage or an immutable commit/object
binding.

## 3. Retention and retrievability

The issuer, PDP, PEP, and evidence custodian MUST retain or be able to retrieve
every governed-reference preimage for at least the longer of:

- the envelope and decision validity periods plus the applicable receipt-policy
  retention interval; or
- the unresolved investigation, contest, or audit period for an effect.

The receipt policy MUST state the retention interval and evidence locator rules.
A receipt is incomplete when an auditor cannot retrieve and hash-verify the
preimages that controlled its authorization and enforcement.

## 4. v0.1 envelope pairs

The envelope schema requires these pairs:

| Reference | Integrity field |
|---|---|
| `issuer_registry_ref` | `issuer_registry_snapshot_hash` |
| `issuer_authority_ref` | `issuer_authority_hash` |
| `delegate_identity_registry_ref` | `delegate_identity_registry_snapshot_hash` |
| `governing_policy_ref` | `policy_content_hash` and `policy_bundle_hash` |
| `decision_preconditions_ref` | `decision_preconditions_hash` |
| `revocation_ref` | `revocation_source_hash` |
| `receipt_policy_ref` | `receipt_policy_hash` |
| `aggregate_authority_policy_ref` | `aggregate_authority_policy_hash` |

Static conformance MUST enumerate every `repoRef`-typed field in every CG-0036
schema and fail if an authority-relevant reference lacks a same-object integrity
binding. This is a sweep invariant, not a two-field allowlist.
