# MIRRORNODE Delegation Conformance v0.1

**Status:** Draft under CG-0036 — test/validator requirements only

## 1. Purpose

JSON Schema validates document shape. It does not prove cross-document authority relationships, authenticated issuer provenance, live revocation state, approval consumption, policy integrity, aggregate authority, approval binding, or TOCTOU safety. A conformant implementation therefore requires a separate validator/evaluator layer.

## 2. Static conformance checks

A validator must reject a delegation when:

- schema validation fails;
- delegation issuer proof is missing, cannot be resolved/verified, is not anchored to a trusted root outside the delegate's authority path, or does not authenticate the canonical delegation payload excluding `issuer_proof`;
- `issuer_proof.signed_payload_hash` does not equal the SHA-256 of that canonical delegation payload;
- policy path/version/hash are missing or inconsistent;
- `decision_preconditions_ref` or `decision_preconditions_hash` is missing;
- the content resolved at `decision_preconditions_ref` does not hash to `decision_preconditions_hash`;
- canonical resource identities are malformed or unresolved;
- allowed operations are unknown to the applicable operation registry;
- expiry <= effective time;
- revocation/expiry behavior is undefined;
- `NON_INTERRUPTIBLE_WITH_EXPLICIT_RATIONALE` is selected without a rationale containing meaningful non-whitespace content;
- parent delegation cannot be resolved when a child is declared;
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
- any required Operator/Council approval object is resolved, authenticated, unexpired, unrevoked where applicable, within its reuse policy, and carries a `delegation_payload_hash` equal to the current envelope payload hash.

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

Until a separately governed Council disposition validator proves required composition, provenance, and quorum, any Council-required approval MUST fail closed. CG-0036 does not invent constitutional quorum rules inside the approval object.

A fabricated, missing, expired, unauthenticated, recycled beyond its allowed reuse policy, differently bound, hash-mismatched, payload-hash-mismatched, unvalidated-as-constituted, or insufficiently authoritative approval cannot produce `ALLOW`.

## 4. Approval consumption and bounded reuse

Approval reuse is explicit, never inferred.

- `ONE_TIME` approvals MUST be atomically marked consumed before or as part of the first authorized enforcement. A second decision or enforcement attempt using the same approval nonce MUST fail.
- `BOUNDED_REUSE` approvals MUST declare `max_uses`. Each successful use MUST be recorded in an authoritative consumption store/counter keyed by `approval_id` and `approval_nonce`.
- Consumption updates MUST be concurrency-safe. Two enforcement points must not both observe the same remaining use and exceed the bound.
- An approval cannot be reused across a different request, state, policy bundle, action parameters, subject, resource, or delegation merely because remaining uses exist.
- If current consumption state cannot be verified, enforcement fails closed.

The concrete consumption-store technology is an implementation choice; atomicity and authoritative usage accounting are normative.

## 5. PEP enforcement checks

Before causing the effect, the PEP must verify:

- decision issuer/integrity;
- `decision_id` and `decision_nonce` have not previously been consumed;
- decision lifetime is valid;
- every `ALLOW` carries `enforcement_constraints.one_time_use: true`;
- `delegation_payload_hash` still equals the currently resolved envelope's canonical payload hash excluding `issuer_proof` and equals `issuer_proof.signed_payload_hash`;
- exact subject/action/resource match;
- exact parameter digest;
- target state/version still matches;
- decision `decision_preconditions_hash` still corresponds to the immutable precondition artifact evaluated by the PDP;
- obligations are understood;
- revocation freshness still satisfies policy;
- any required Operator/Council approval remains valid, its authenticated issuer proof is trusted, and its `delegation_payload_hash` still matches the live envelope payload;
- approval reuse/consumption constraints can be atomically satisfied;
- the PEP itself is authorized only for the narrow downstream effect.

Every v0.1 `ALLOW` is one-time-use. Every `ALLOW` MUST be atomically consumed by `decision_id` and `decision_nonce` before or as part of enforcement. Re-presenting the same `ALLOW`, even while unexpired and even if its approval still has remaining bounded uses, MUST fail and require a fresh PDP decision. Approval reuse does not imply decision reuse. A mutated envelope with unchanged `delegation_id` and `delegation_version` MUST fail closed. A future bounded decision-reuse profile requires separate governance and is not defined by v0.1.

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
- Council approval that treats an Operator-authority disposition record as if it proved Council constitution.

All must fail where applicable.

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
- concurrent enforcement attempts using the same `ALLOW` `decision_nonce`.

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
- decision or approval `delegation_payload_hash` that does not equal the envelope `issuer_proof.signed_payload_hash`.

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

- static, delegation-issuance provenance, approval-binding/provenance, precondition-integrity, aggregate, revocation/TOCTOU/replay, policy-integrity, and PEP test suites pass;
- receipt/audit mapping is reviewed;
- failure/rollback behavior is tested;
- monitoring and alert thresholds are defined;
- a separate Operator authorization explicitly commissions the production autonomous class.
