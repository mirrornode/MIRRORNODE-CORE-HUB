# MIRRORNODE Delegation Conformance v0.1

**Status:** Draft under CG-0036 — test/validator requirements only

## 1. Purpose

JSON Schema validates document shape. It does not prove cross-document authority relationships, authenticated issuer provenance, live revocation state, approval consumption, policy integrity, aggregate authority, approval binding, or TOCTOU safety. A conformant implementation therefore requires a separate validator/evaluator layer.

## 2. Static conformance checks

A validator must reject a delegation when:

- schema validation fails;
- delegation issuer proof is missing, cannot be resolved/verified, is not anchored to a trusted root outside the delegate's authority path, or does not authenticate the canonical delegation payload excluding `issuer_proof`;
- canonicalization is attempted before schema validation, duplicate-key rejection, or I-JSON checks (`CANONICALIZATION_V0_1.md`);
- `issuer_proof.signed_payload_hash` does not equal the RFC 8785 SHA-256 of that canonical delegation payload;
- protected proof metadata (`alg`/`kid` or equivalent) disagrees with schema hints, is unsigned, or verifies under a substituted algorithm, credential, or trust root (`ISSUER_PROOF_V0_1.md`);
- issuer authentication succeeds but issuer **authorization** fails: the hash-bound `issuer_authority_ref`/`issuer_authority_hash` is missing, unauthenticated, expired, self-issued, or does not cover the exact operations, resources, environments, rank/ceiling, risk, subdelegation depth, or validity period;
- a child grant's issuer-authority hash is not the authenticated parent envelope payload hash;
- a child grant's authenticated `logical_issuer_id` is not the parent envelope's `delegate_logical_issuer_id`;
- a child grant relies on `delegate_actor` / display-name equality instead of the identity-registry binding;
- an authenticated peer cites a victim parent payload hash while presenting a different `logical_issuer_id`;
- the parent `delegate_identity_registry_ref` / `delegate_identity_registry_snapshot_hash` is missing, unresolvable, or stale relative to the live identity registry;
- credential rotation is rejected even though the mapped `logical_issuer_id` is unchanged (rotation that preserves the logical issuer MUST pass);
- a root grant's issuer-authority record is not a separately governed `ISSUER_AUTHORITY_RECORD_V0_1` outside the grantee's control;
- an authenticated peer signs a scope it does not possess;
- policy path/version/hash are missing or inconsistent;
- `decision_preconditions_ref` or `decision_preconditions_hash` is missing;
- the content resolved at `decision_preconditions_ref` does not hash to `decision_preconditions_hash`;
- canonical resource identities are malformed or unresolved;
- allowed operations are unknown to the applicable operation registry;
- expiry <= effective time;
- revocation/expiry behavior is undefined;
- `NON_INTERRUPTIBLE_WITH_EXPLICIT_RATIONALE` is selected without a rationale containing meaningful non-whitespace content;
- parent delegation cannot be resolved when a child is declared;
- parent/child issuer-identity binding has not been proven before scope monotonicity is evaluated;
- parent/child scope, operation, authority rank, risk ceiling, depth, or expiry monotonicity fails;
- a child does not carry the exact parent `decision_preconditions_hash`;
- a child weakens required receipt, revocation, or expiry rules;
- authority class conflicts with a non-delegable guardrail;
- a grant would allow its subject to modify the policy/registry/aggregate logic that determines the same grant's authority.

Until a typed precondition language and deterministic strengthening relation are separately ratified, child delegations MUST inherit the exact parent `decision_preconditions_hash`. A different child precondition artifact is not treated as provably stronger merely because it is validly hashed.

## 3. Live decision checks

Before an `ALLOW`, the PDP must prove:

- verified subject identity;
- exact action/resource normalization;
- current policy content/bundle hash;
- current immutable decision-precondition hash and its equality with the delegation's `decision_preconditions_hash`;
- current delegation state;
- `delegation_payload_hash` equals the SHA-256 of the current envelope's canonical payload excluding `issuer_proof` and equals `issuer_proof.signed_payload_hash`;
- revocation freshness within bound;
- non-expiry;
- aggregate-authority snapshot validity;
- MICC cross-map result and unconditional `micc_approval_class` recording (`APPROVAL_NONE` when no additional MICC approval gate applies; stricter gate wins);
- state/precondition validity;
- risk/composition constraints;
- the decision `issuer_proof` authenticates the RFC 8785 canonical decision excluding `issuer_proof`; `pdp_identity`/`pdp_version` are not accepted as provenance;
- `resource.id` equals `resource.canonical_uri` and that URI is in the evaluated grant `resource_scope`;
- `resource_registry_snapshot_hash` matches the frozen registry snapshot, including provider/native target;
- the object hashed as `aggregate_authority_snapshot_hash` validates against `AGGREGATE_AUTHORITY_SNAPSHOT_V0_1.schema.json` and its RFC 8785 digest matches;
- `decision_nonce` (and any required approval nonce) has ≥128 bits of CSPRNG entropy in the canonical unpadded-base64url encoding;
- `logical_issuer_id` is taken from the issuer-registry mapping of the verified credential, not from `kid`;
- any required Operator approval object is resolved, authenticated, unexpired, unrevoked where applicable, within its reuse policy, and carries a `delegation_payload_hash` equal to the current envelope payload hash;
- `micc_approval_class: APPROVAL_COUNCIL` never accompanies `decision: ALLOW` (v0.1 schema-unreachable). Council approval objects are evidence only and cannot unlock execution.

### Operator approval

When Operator approval is required, the referenced approval MUST conform to `OPERATOR_APPROVAL_V0_1.schema.json`, its content hash MUST equal `operator_approval_hash`, and the validator MUST prove exact binding between approval and authorization decision for:

- authenticated issuer provenance, not merely a claimed `approver` string;
- approver authority;
- `request_id`;
- subject identity;
- action name and parameters hash;
- resource identity;
- context digest;
- state hash;
- policy bundle hash;
- delegation ID/version;
- `delegation_payload_hash` of the exact canonical envelope payload excluding `issuer_proof`;
- approval lifetime;
- approval reuse/consumption state.

An approval bound only to `delegation_id` and `delegation_version` is insufficient. A changed envelope with the same ID and version MUST fail closed.

`issuer_proof.signed_payload_hash` MUST equal the hash of a deterministic canonical representation of the complete approval object excluding `issuer_proof`. The verifier MUST validate either the embedded `proof_value` or the artifact resolved by `proof_ref` using `issuer_credential_ref` and the declared `proof_type`. A hash string by itself is never evidence of issuance.

Issuer provenance MUST validate through the declared proof mechanism against a trusted credential/attestation root outside the requester and affected delegate's authority path.

### Council approval

When MICC or another governing surface requires Council approval, the referenced approval MUST conform to `COUNCIL_APPROVAL_V0_1.schema.json`, its content hash MUST equal `council_approval_hash`, and the validator MUST additionally verify:

- authenticated issuer provenance using the same canonical-payload proof rule above;
- `delegation_payload_hash` equality with the current envelope's canonical payload hash excluding `issuer_proof` and with `issuer_proof.signed_payload_hash`;
- referenced matter/disposition content integrity via `disposition_hash`;
- the disposition grants the exact current action/request rather than merely discussing the matter;
- request/subject/action/resource/context/state/policy/delegation bindings;
- lifetime and reuse/consumption state.

Content integrity of a disposition artifact and authenticated issuance of the approval object are not proof that the referenced Council disposition was validly constituted.

`council/schemas/disposition.schema.yaml` records Operator dispositions of Council matters (`authority: operator`). CG-0031 verifies previously recorded Operator dispositions against an implementation scope. Neither contract defines Council seat composition, quorum, or a matter-validation constitution check.

Until a separately governed Council disposition validator proves required composition, provenance, and quorum, any Council-required approval MUST fail closed. In v0.1 this is also structural: `APPROVAL_COUNCIL` + `ALLOW` MUST fail JSON Schema validation. A future schema revision is required after that validator is ratified. CG-0036 does not invent constitutional quorum rules inside the approval object.

A fabricated, missing, expired, unauthenticated, recycled beyond its allowed reuse policy, differently bound, hash-mismatched, payload-hash-mismatched, unvalidated-as-constituted, or insufficiently authoritative approval cannot produce `ALLOW`.

## 4. Approval consumption and bounded reuse

Approval reuse is explicit, never inferred.

- `ONE_TIME` approvals MUST be atomically marked consumed before or as part of the first authorized enforcement. A second decision or enforcement attempt using the same approval nonce MUST fail.
- `BOUNDED_REUSE` approvals MUST declare `max_uses`. Each successful use MUST be reserved atomically **before dispatch** and finalized as consumed after a successful effect, keyed by `(logical_issuer_id, approval_id, approval_nonce)`. Concurrent actors MUST NOT both reserve the last remaining use.
- Consumption updates MUST be concurrency-safe. Two enforcement points must not both observe the same remaining use and exceed the bound.
- An approval cannot be reused across a different request, state, policy bundle, action parameters, subject, resource, or delegation merely because remaining uses exist.
- If current consumption state cannot be verified, enforcement fails closed.

The concrete consumption-store technology is an implementation choice; atomicity and authoritative usage accounting are normative.

## 5. PEP enforcement checks

Before causing the effect, the PEP must verify:

- decision `issuer_proof` verifies against a PDP trust root from protected proof metadata; a schema-valid `ALLOW` with only `pdp_identity` fails;
- `(logical_issuer_id, decision_id, decision_nonce)` has not previously been consumed;
- required approval-use capacity was reserved atomically with the decision key before dispatch intent;
- decision lifetime is valid;
- every `ALLOW` carries `enforcement_constraints.one_time_use: true`;
- `delegation_payload_hash` still equals the currently resolved envelope's canonical payload hash excluding `issuer_proof` and equals `issuer_proof.signed_payload_hash`;
- exact subject/action/resource match, including `resource.id` = `resource.canonical_uri` and equality of `resource_registry_ref` / `resource_registry_snapshot_hash` / `resource_record_hash` across approval, decision, and live registry;
- exact parameter digest;
- target state/version still matches;
- decision `decision_preconditions_hash` still corresponds to the immutable precondition artifact evaluated by the PDP;
- obligations are understood;
- revocation freshness still satisfies policy;
- any required Operator/Council approval remains valid, its authenticated issuer proof is trusted, and its `delegation_payload_hash` still matches the live envelope payload;
- approval reuse/consumption constraints can be atomically satisfied;
- the PEP itself is authorized only for the narrow downstream effect.

Every v0.1 `ALLOW` is one-time-use. Every `ALLOW` MUST atomically reserve `(logical_issuer_id, decision_id, decision_nonce)` **and** required approval capacity before dispatch, then persist dispatch intent before invoking the effect, per `EFFECT_CONSUMPTION_COMMIT_V0_1.md`. Re-presenting the same `ALLOW`, even while unexpired and even if its approval still has remaining bounded uses, MUST fail and require a fresh PDP decision. Approval reuse does not imply decision reuse. A mutated envelope with unchanged `delegation_id` and `delegation_version` MUST fail closed. A future bounded decision-reuse profile requires separate governance and is not defined by v0.1.

If state changed, a bound precondition artifact changed, decision consumption cannot be performed safely, or approval consumption cannot be performed safely, the PEP denies and requests a fresh decision.

## 6. Aggregate-authority test suite

Tests must include at minimum:

- two individually safe grants whose union exceeds the actor root ceiling;
- non-conflicting grants that create a forbidden operation combination;
- resource aliases resolving to the same protected target;
- child delegation attempting equal textual ceiling but broader resource set;
- chain of low-risk steps producing a high-impact cumulative effect;
- expired parent with unexpired-looking child;
- overlapping grants from different delegators;
- attempt to alter aggregate-authority calculation by an affected actor.

All must fail or escalate according to policy.

## 7. Approval-binding and provenance test suite

Tests must include at minimum:

- fabricated Operator or Council approval reference;
- structurally valid approval with self-asserted but unauthenticated issuer identity;
- invalid signature/attestation proof;
- proof whose `signed_payload_hash` does not match the canonical approval payload excluding `issuer_proof`;
- missing/unresolvable `proof_ref` or invalid embedded `proof_value`;
- valid approval ID with wrong content hash;
- approval for a different request;
- approval for a different subject, resource, action, or parameters;
- approval bound to stale state or different policy bundle;
- approval whose `delegation_payload_hash` does not match the current envelope canonical payload excluding `issuer_proof`;
- approval bound only to matching `delegation_id` and `delegation_version` against a mutated envelope payload;
- expired approval;
- approval from an unauthorized approver/disposition;
- second use of a `ONE_TIME` approval;
- concurrent attempts to exceed `BOUNDED_REUSE.max_uses`;
- Council approval whose matter is valid but disposition does not authorize the current action;
- Council approval whose matter/disposition hashes are valid and issuer proof verifies, but no separately governed composition/quorum/provenance validator has accepted the disposition as validly constituted;
- Council approval that treats an Operator-authority disposition record as if it proved Council constitution;
- `micc_approval_class: APPROVAL_COUNCIL` with `decision: ALLOW` (schema-invalid in v0.1);
- schema-valid `ALLOW` missing decision `issuer_proof` or with unverifiable PDP proof;
- algorithm substitution or credential/trust-root redirection in protected proof metadata;
- `proof_type`/`issuer_credential_ref` hint mismatch with protected header `alg`/`kid`.

All must fail where applicable.

## 7a. Resource-registry and remapping test suite

Tests must include:

- stale `resource_registry_snapshot_hash`;
- same canonical URI with substituted provider/native target;
- Operator approval issued before remap, presented after remap;
- Council approval issued before remap, presented after remap;
- `resource.id` different from `resource.canonical_uri`;
- decision URI absent from envelope `resource_scope`;
- alias resolving to two canonical URIs.

All must fail.

## 7b. Snapshot-hash test suite

Tests must include:

- `aggregate_authority_snapshot_hash` that does not equal the RFC 8785 SHA-256 of a schema-valid snapshot;
- snapshot missing a required field;
- snapshot whose applicable delegation payload hashes omit a grant that entered `G(A,t)`;
- key-order variation of a valid snapshot producing the same hash (`CANONICALIZATION_VECTORS_V0_1.json` `snapshot-basic`).

Invalid snapshots must fail; key-order variation must match.

## 7c. Nonce and identifier test suite

Tests must include:

- nonce shorter than 22 unpadded base64url characters;
- ID/nonce collision across two authenticated issuers treated as the same consumption slot (must remain distinct);
- reuse of a consumed `(issuer, id, nonce)` tuple.

Weak nonces and cross-issuer slot sharing must fail.

## 7d. Effect/consumption commit test suite

The fixtures in `EFFECT_CONSUMPTION_COMMIT_VECTORS_V0_1.json` are required. Crash before reservation, after reservation before dispatch, after effect before receipt, after receipt before approval accounting, concurrent duplicate dispatch, uncertain reconciliation, and under-decremented bounded-reuse counters MUST NOT complete a double effect or mark `COMPLETED` unsafely.

## 8. Precondition-integrity test suite

Tests must include:

- same `decision_preconditions_ref` with changed content;
- correct path with wrong `decision_preconditions_hash`;
- delegation issued against one precondition hash but decision carrying another;
- PDP evaluates the correct artifact but PEP sees a changed target/precondition state;
- child delegation attempts to replace parent preconditions with any different hash.

All must fail or escalate.

## 9. Revocation/TOCTOU and replay test suite

Tests must include:

- revocation before PDP decision;
- revocation between PDP decision and PEP enforcement;
- revocation during atomic step;
- queued work after revocation;
- retry after revocation;
- expiry between decision and enforcement;
- stale cache beyond freshness bound;
- offline PEP without sufficient revocation freshness;
- resource state mutation after decision;
- target-version mismatch at enforcement;
- envelope payload mutation with unchanged `delegation_id` and `delegation_version`;
- decision `delegation_payload_hash` mismatch with envelope `issuer_proof.signed_payload_hash`;
- replay of an already consumed `ALLOW` decision;
- replay of an unexpired `ALLOW` after atomic consumption;
- replay of an `ALLOW` when an associated `BOUNDED_REUSE` approval still has remaining uses;
- concurrent enforcement attempts using the same `ALLOW` `(authenticated_issuer, decision_id, decision_nonce)`.

## 10. Policy-integrity test suite

Tests must include:

- stable policy path with changed content;
- version string unchanged while content hash changes;
- policy bundle missing a forbid guardrail;
- affected actor proposing and attempting to publish self-expanding policy;
- PDP using a policy hash different from the receipt;
- PEP receiving a decision whose policy bundle is not recognized.

## 11. Delegation-issuance provenance test suite

Tests must include:

- unsigned delegation envelope;
- self-asserted `delegator` with fabricated proof metadata;
- invalid embedded signature/assertion;
- missing or unresolvable delegation `proof_ref`;
- delegation proof anchored to a credential controlled by the affected delegate;
- `signed_payload_hash` mismatch after any envelope field changes;
- trusted-registry attestation that does not authenticate the complete canonical envelope payload excluding `issuer_proof`;
- decision or approval `delegation_payload_hash` that does not equal the envelope `issuer_proof.signed_payload_hash`;
- correct parent `delegate_logical_issuer_id` issuing an in-scope child (must pass);
- authenticated peer citing a victim parent payload hash (must fail);
- matching `delegate_actor` display name with a different `logical_issuer_id` (must fail);
- credential rotation that preserves the same `logical_issuer_id` (must pass);
- unresolved or stale `delegate_identity_registry_snapshot_hash` (must fail closed).

All must fail.

## 12. UI/product conformance

A future MOPCON/product implementation must be tested to ensure:

- aggregate authority is discoverable without opening every grant individually;
- overlapping grants are visible;
- root ceiling and current aggregate are distinguishable;
- policy provenance and revocation freshness are visible;
- approval provenance and remaining bounded uses are inspectable when relevant;
- unsafe aggregate state cannot be presented as green merely because each envelope is individually valid;
- denied/escalated decisions cannot be visually collapsed into generic success.

## 13. Commissioning gate

`AUTONOMOUS_WITHIN_POLICY` must remain disabled for production effects until:

- static, canonicalization-vector, delegation-issuance provenance, decision-provenance, proof-confusion, approval-binding/provenance, precondition-integrity, aggregate/snapshot-hash, resource-registry, nonce/collision, revocation/TOCTOU/replay, policy-integrity, effect/consumption-commit, and PEP test suites pass;
- receipt/audit mapping is reviewed;
- failure/rollback behavior is tested;
- monitoring and alert thresholds are defined;
- a separate Operator authorization explicitly commissions the production autonomous class.
