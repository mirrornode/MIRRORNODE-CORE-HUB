# MIRRORNODE Delegation Canonicalization Profile v0.1

**Status:** Draft under CG-0036 — architecture/conformance profile only  
**Normative algorithm:** RFC 8785 JSON Canonicalization Scheme (JCS)  
**Hash:** SHA-256 over UTF-8 JCS bytes, encoded `sha256:` + lowercase hexadecimal

This profile defines the single canonicalization and hashing procedure for every CG-0036 content hash and authenticated payload, including:

- `issuer_proof.signed_payload_hash` on envelopes, decisions, and approvals;
- `delegation_payload_hash`;
- `decision_preconditions_hash`, `policy_content_hash`, `policy_bundle_hash`;
- `aggregate_authority_snapshot_hash`;
- `resource_registry_snapshot_hash`;
- `disposition_hash` and approval content hashes referenced by decisions.

No application-specific string normalization is applied. Unicode NFC/NFKC, case-folding, whitespace collapsing, URI rewriting, and locale-dependent comparison are forbidden at this layer. Alias resolution and resource canonicalization happen **before** an object is presented to this profile.

## 1. Preconditions (validation before canonicalization)

Canonicalization MUST NOT be attempted until:

1. the input is UTF-8 JSON text or an in-memory JSON value produced from such text;
2. a duplicate-key-rejecting parser has accepted the text (duplicate object keys fail closed);
3. the value is I-JSON: no `NaN`, `Infinity`, `-Infinity`, non-UTF-8, or integers outside the IEEE-754 binary64 exact range `-(2^53-1) … 2^53-1` inclusive (`-9007199254740991` … `9007199254740991`). Oversized integers MUST be rejected recursively (objects, arrays, nested values). They MUST NOT be rounded, coerced, or converted to strings.
4. the applicable closed JSON Schema (`additionalProperties: false`) has accepted the object.

Absent members and JSON `null` are not interchangeable. Omitting a field is not equivalent to setting it to `null`. A schema that rejects `null` for a field continues to reject `null` after this profile.

## 2. Excluding `issuer_proof`

When a hash or signature is specified as covering “the canonical payload excluding `issuer_proof`”:

1. validate the complete object, including `issuer_proof`, against the applicable schema first;
2. then remove the `issuer_proof` member from the object (do not replace it with `null`);
3. canonicalize and hash the remaining object.

`proof_type` and `issuer_credential_ref` therefore do not enter `signed_payload_hash`. They are untrusted hints until authenticated by protected proof metadata. See `ISSUER_PROOF_V0_1.md`.

Authenticated aggregate-authority, revocation-state, resource-registry, and
execution-receipt payloads follow the same procedure: validate the complete
object, remove only the top-level `issuer_proof`, then canonicalize and hash the
remaining payload. The proof's `signed_payload_hash` MUST equal that digest.

## 3. RFC 8785 procedure

Apply RFC 8785, including §3.2.3 name ordering:

- object properties are serialized in lexicographic order of the **UTF-16 code units** of the names, not Unicode code points;
- Python `json.dumps(..., sort_keys=True)` is **not** an RFC 8785 implementation;
- array order is preserved exactly **after** any required set-like preprocessing (below);
- strings use RFC 8785 JSON string escaping (no extra escaping of solidus or non-ASCII);
- numbers use RFC 8785 / ES6 / I-JSON number formatting; integers outside `±(2^53-1)` fail before serialization;
- output is UTF-8 with no insignificant whitespace;
- the hash is `SHA-256(canonical_utf8_bytes)` rendered as `sha256:` plus 64 lowercase hex characters.

A non-BMP name versus a BMP name MUST distinguish UTF-16 ordering from code-point ordering. Vector: `canon-utf16-name-order`.

## 3a. Set-like array preprocessing

RFC 8785 preserves array order. Semantically set-like arrays MUST therefore be preprocessed **after schema validation and before** hashing the enclosing object:

1. reject duplicate items (fail closed);
2. sort items by the UTF-8 bytes of each item’s RFC 8785 canonical representation;
3. then canonicalize the enclosing object.

**Set-like** (must preprocess): `allowed_operations`, `resource_scope`, `environment_scope`, `eligible_operations`, `applicable_delegation_payload_hashes`.

**Sequence-bearing** (must **not** reorder): `obligations`, `notes`.

Permutation of a set-like array MUST NOT change the hash. Vector: `snapshot-set-permutation`.

## 4. Rejection set

Fail closed on:

- schema failure;
- duplicate keys;
- non-I-JSON numbers or values;
- invalid UTF-8;
- attempt to canonicalize before validation;
- any transformation other than RFC 8785.

## 5. Fixed vectors

Normative fixtures: `CANONICALIZATION_VECTORS_V0_1.json`.

A conformant implementation MUST produce the recorded canonical strings and SHA-256 values, MUST treat BMP key-order variation as equal, MUST treat UTF-16 name order as distinct from code-point order, MUST treat material string variation as unequal, MUST schema-validate complete objects before excluding `issuer_proof`, MUST leave the excluded-proof payload hash unchanged when only `issuer_proof` changes, MUST fail proof verification when protected proof metadata is substituted, and MUST hash equal semantic sets identically after set-like preprocessing.

## 6. Non-authorization

This profile does not select a cryptographic library, JSON parser, or runtime. It does not authorize implementation beyond specifying the hash input.
