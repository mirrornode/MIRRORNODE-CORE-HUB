# Capability Continuity Machine Contract v0.1

**Status:** PROPOSAL — machine-contract companion to the Capability Continuity Invariant v0.1  
**Authority effect:** NONE  
**Runtime/deployment effect:** NONE

## Purpose

Turn the sentence **“a critical MIRRORNODE function has at least one currently eligible execution path”** into a bounded proof obligation without pretending that JSON Schema alone can establish runtime truth.

The proof chain is:

```text
Critical Function Contract
        ↓ exact function/version/digest binding
Substrate Eligibility Record
        ↓ current-status / limits / time / evidence checks
Capability Continuity Assessment
        ↓
CAPABILITY_AVAILABLE | CAPABILITY_UNAVAILABLE | HOLD
```

The model/provider is not the durable function identity. Eligibility is a separate evidence-bearing statement about whether a particular substrate may presently perform a particular function contract.

## Machine-readable artifacts

### Function contract

`schemas/critical-function-contract.schema.json`

Binds:

- function identity and version;
- criticality and owner;
- authority-ceiling source and digest;
- input/output/tool/side-effect/evidence/failure contract references and digests;
- acceptance-suite identity, version, digest, and threshold;
- provenance and independence requirements.

A model/provider identifier does not appear in the function identity.

### Substrate eligibility record

`schemas/substrate-eligibility-record.schema.json`

Binds:

- exact function identity/version and function-contract digest;
- exact authority-ceiling digest;
- substrate identity, class, revision, and inference-configuration digest;
- acceptance-suite identity/version/digest;
- evaluation provenance and result digest;
- tool-environment digest;
- evidence-pack reference/digest;
- disposition, limits, effective time, expiry, and reevaluation triggers;
- active/revoked/superseded status.

`ELIGIBLE` and `ELIGIBLE_WITH_LIMITS` require the recorded acceptance threshold to have been met. `ELIGIBLE_WITH_LIMITS` requires at least one explicit limit.

### Capability continuity assessment

`schemas/capability-continuity-assessment.schema.json`

For a `CRITICAL` function, each candidate path records fail-closed verification results for:

- active eligibility status;
- eligible disposition;
- case falling within recorded limits;
- exact function binding;
- authority-ceiling binding;
- current validity window;
- absence of a fired reevaluation trigger;
- required tool-environment availability;
- substrate availability;
- evidence completeness.

The schema permits `CAPABILITY_AVAILABLE` / `capability_loss: NONE` only when at least one path satisfies every required condition.

The schema permits `CAPABILITY_UNAVAILABLE` / `CRITICAL_FUNCTION_UNAVAILABLE` only when no path satisfies every required condition.

`HOLD` maps to `capability_loss: UNKNOWN`.

## Semantic verification is mandatory

Schema validity is necessary but not sufficient.

A deterministic verifier consuming these records MUST compute the path verification booleans from referenced evidence. It must not accept caller-supplied booleans as proof.

At minimum it must fail closed unless it can establish:

1. the function record itself is schema-valid;
2. the eligibility record itself is schema-valid;
3. the eligibility record's `function_id`, `function_version`, and `function_contract_sha256` match the exact function contract under assessment;
4. the eligibility record's `authority_ceiling_sha256` matches the exact external authority-ceiling source bound by the function contract;
5. the acceptance-suite identity/version/digest matches the function contract;
6. the evaluation result and evidence-pack references are present and digest-bound;
7. the eligibility record is `ACTIVE`;
8. the disposition is `ELIGIBLE` or `ELIGIBLE_WITH_LIMITS`;
9. the requested case falls within any recorded limits;
10. trusted time establishes `effective_at <= evaluated_at <= valid_until`;
11. no recorded reevaluation trigger has fired;
12. the required tool environment matches and is available;
13. the substrate itself is available;
14. required continuity evidence is complete.

Failure to prove any required condition makes that path non-qualifying.

If no path qualifies, the verifier must not emit `CAPABILITY_AVAILABLE`.

## Authority boundary

Capability eligibility and continuity availability do not create or enlarge authority.

A substrate that meets every capability benchmark remains bounded by the externally sourced authority ceiling. Independent-review provenance is also separate from technical eligibility and must not be manufactured by model substitution.

A continuity assessment is evidence about function availability. It is not approval, constitutional clearance, merge authority, execution authority, deployment authority, or procurement authority.

## Example fixtures

The files under `examples/` are synthetic conformance fixtures. Their `example://` references and repeated-character hashes are placeholders and MUST NOT be interpreted as evidence of deployed infrastructure, actual model qualification, or present production availability.

- `critical-function-contract.example.json` — synthetic critical review function.
- `substrate-eligibility-record.example.json` — synthetic bounded eligibility record.
- `capability-continuity.available.example.json` — one hosted path unavailable, one controlled path qualifies; result is `CAPABILITY_AVAILABLE`.
- `capability-continuity.unavailable.example.json` — hosted path unavailable and controlled path stale; result is `CAPABILITY_UNAVAILABLE`.

## Validation performed for this proposal slice

Before repository write, the three schemas were checked as Draft 2020-12 schemas and the example records were validated against them.

Two adversarial state checks were also exercised:

- changing the unavailable fixture to claim `CAPABILITY_AVAILABLE` was rejected because no fully qualifying path exists;
- changing the available fixture to claim `CAPABILITY_UNAVAILABLE` was rejected because a fully qualifying path exists.

This is proposal-level conformance evidence only. It is not an independent exact-head review and does not authorize merge or runtime implementation.

## Next implementation boundary

The next implementation step belongs in an owning verifier/runtime repository, not CORE-HUB: consume these contracts, recompute the semantic bindings above from immutable evidence, and emit the assessment record.

That implementation must remain fail-closed and separately reviewed before any routing or automatic failover is enabled.
