# MIRRORNODE Issuer Proof Profile v0.1

**Status:** Draft under CG-0036 — architecture/conformance profile only  
**Cryptography:** use existing JOSE/COSE/WebAuthn (or equivalent hardware-assertion) protected-header semantics. CG-0036 does not invent algorithms, encodings, or custom signature schemes.

## 1. What `issuer_proof` is

`issuer_proof` authenticates a RFC 8785 canonical payload excluding the `issuer_proof` member, hashed as `sha256:` lowercase hex per `CANONICALIZATION_V0_1.md`.

A content hash proves integrity of bytes. It does not prove issuer identity. `pdp_identity`, `pdp_version`, `delegator`, `approver`, `proof_type`, and `issuer_credential_ref` are not self-authenticating authority claims.

## 2. Untrusted schema hints

The schema fields:

- `proof_type`
- `issuer_credential_ref`

are **untrusted hints** until authenticated. They MUST NOT be used as the sole source of algorithm or credential identity.

## 3. Protected proof metadata

The actual proof mechanism MUST cryptographically protect at least:

- the algorithm / mechanism identifier;
- the credential / key identifier;
- the signed payload hash (`signed_payload_hash`, which MUST equal the RFC 8785 SHA-256 of the payload excluding `issuer_proof`).

Where the mechanism is a digital signature, use standard **protected-header** semantics:

- **JOSE JWS** (RFC 7515): compact or flattened JWS. Protected header MUST include `alg` and a key identifier (`kid` or an equivalent credential identifier recognized by the trust root). The JWS payload MUST be the ASCII `signed_payload_hash` string or the raw canonical payload bytes; the verifier documents which of those two JOSE payloads is in use and MUST NOT accept both for the same credential.
- **COSE** (RFC 9052): protected headers analogously carry algorithm and key identifiers.
- **Hardware-backed assertion / WebAuthn**: authenticator data and attested credential identifiers are the protected metadata.
- **Trusted resolver/registry attestation**: the attestation statement’s signed attributes MUST bind algorithm, resolver/credential identity, and payload hash.

The verifier MUST derive or confirm algorithm and credential from that protected metadata, then validate the credential against a trust root outside the requester and affected delegate’s authority path.

The verified credential MUST then be mapped through a hash-bound issuer registry (`issuer_registry_ref` + `issuer_registry_snapshot_hash`) to a stable `logical_issuer_id`. `kid` and `issuer_credential_ref` MUST NOT be used as consumption-namespace issuers. Rotation of a credential that remains bound to the same logical issuer preserves the namespace; unrelated or revoked credentials MUST NOT.

Credential authentication is not issuer **authorization**. Grant envelopes additionally require a hash-bound `issuer_authority_ref` / `issuer_authority_hash` proving the logical issuer may delegate the exact operations, resources, environments, rank/ceiling, risk, subdelegation depth, and validity period (`ISSUER_AUTHORITY_RECORD_V0_1.schema.json` for root records; parent envelope payload hash for children).

## 4. Fail-closed mismatches

The following MUST fail:

- schema `proof_type` / `issuer_credential_ref` disagree with protected `alg` / `kid` (or equivalent);
- algorithm substitution (hint or header names one algorithm, bytes verify under another, or `alg` is `none` / empty);
- credential redirection (`kid` or credential identifier does not match the trust-rooted credential used to verify);
- trust-root substitution (proof verifies only under a root the affected delegate or requester controls);
- `signed_payload_hash` mismatch with the RFC 8785 payload hash;
- missing, unresolvable, or truncated `proof_value` / `proof_ref`.

A fabricated, schema-valid object with an untrusted or absent proof never becomes an active grant, approval, or `ALLOW` decision.

## 5. Decision provenance

Authorization decisions carry required `issuer_proof` over the complete canonical decision object excluding `issuer_proof`. PEP enforcement MUST verify that proof against a PDP trust root. `pdp_identity` and `pdp_version` are correlating labels only.

## 6. Non-authorization

This profile does not select JOSE libraries, key-management systems, or production trust roots.
