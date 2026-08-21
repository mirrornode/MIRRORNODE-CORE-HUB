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
3. the value is I-JSON: no `NaN`, `Infinity`, `-Infinity`, non-UTF-8, or out-of-range integers beyond IEEE 754 binary64 exact integers used by RFC 8785/I-JSON;
4. the applicable closed JSON Schema (`additionalProperties: false`) has accepted the object.

Absent members and JSON `null` are not interchangeable. Omitting a field is not equivalent to setting it to `null`. A schema that rejects `null` for a field continues to reject `null` after this profile.

## 2. Excluding `issuer_proof`

When a hash or signature is specified as covering “the canonical payload excluding `issuer_proof`”:

1. validate the complete object, including `issuer_proof`, against the applicable schema first;
2. then remove the `issuer_proof` member from the object (do not replace it with `null`);
3. canonicalize and hash the remaining object.

`proof_type` and `issuer_credential_ref` therefore do not enter `signed_payload_hash`. They are untrusted hints until authenticated by protected proof metadata. See `ISSUER_PROOF_V0_1.md`.

## 3. RFC 8785 procedure

Apply RFC 8785:

- object properties are serialized in lexicographic order of Unicode code points of the names;
- array order is preserved exactly;
- strings use RFC 8785 JSON string escaping (no extra escaping of solidus or non-ASCII);
- numbers use RFC 8785 / ES6 / I-JSON number formatting;
- output is UTF-8 with no insignificant whitespace;
- the hash is `SHA-256(canonical_utf8_bytes)` rendered as `sha256:` plus 64 lowercase hex characters.

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

A conformant implementation MUST produce the recorded canonical strings and SHA-256 values, MUST treat key-order variation as equal, MUST treat material string variation as unequal, MUST leave the excluded-proof payload hash unchanged when only `issuer_proof` changes, and MUST fail proof verification when protected proof metadata is substituted.

## 6. Non-authorization

This profile does not select a cryptographic library, JSON parser, or runtime. It does not authorize implementation beyond specifying the hash input.
