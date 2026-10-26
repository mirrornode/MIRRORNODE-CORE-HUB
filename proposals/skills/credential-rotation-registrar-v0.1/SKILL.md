# Credential Rotation Registrar v0.1
Status: OPERATOR-APPROVED; implementation proposed for review. No live credentials inventoried or rotated.

## Mission
Track ownership, scope, expiry, rotation and revocation evidence for API keys, OAuth tokens, signing secrets, certificates, service accounts and recovery credentials. Never collect or store secret values.

## Minimum record
credential_id; provider; system; environment; purpose; owner; custodian; risk_tier; scopes; secure_store_pointer; issued_at; expires_at; last_rotated_at; next_review_at; dependent_services; replacement_validation; old_credential_revoked_at; evidence_refs; approval_ref; status.
Pointers must be non-sensitive; do not store raw secrets, partial secret strings, recovery codes, private keys or access tokens.

## Lifecycle
DISCOVER → CLASSIFY → PLAN → APPROVE → CREATE_NEW → DISTRIBUTE_SECURELY → VALIDATE → CUTOVER → REVOKE_OLD → VERIFY → CLOSE.
Record actor, UTC timestamp, provenance and evidence pointer for every transition. Failure or missing evidence means not complete.

## Safeguards
Metadata-only read and inventory by default. No autonomous issuance, privilege change, deployment, rotation, revocation, or bulk action. THOTH reviews security implications; Siseon authorizes consequential changes. Least privilege, dual-control for critical keys, rollback planning and provider-specific overlap constraints. Exposed or suspected compromised credentials are escalated for incident handling, not silently rotated.

## Reports
Due in 7/30/60 days, overdue, orphaned, overprivileged, expired, cutover unverified, old credential not revoked, dependency gaps and emergency exceptions.

## Implementation gates
Provider-specific inventories and secure-store integrations require separate scope and access review. This document does not grant access to vaults or production systems.
