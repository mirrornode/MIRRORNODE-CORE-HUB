# Critical Function Acceptance Contract v0.1

**Status:** PROPOSAL  
**Parent:** Capability Continuity Invariant v0.1  
**Authority effect:** NONE

## Purpose

Make `same capability` testable.

A substrate cannot be called a valid replacement merely because it accepts the same prompt or produces plausible output. MIRRORNODE needs a function-level contract that survives model/provider replacement and can be evaluated independently of the substrate.

## Function identity

Each critical function should have a durable identity that is not the provider/model name.

Minimum fields:

- `function_id`
- `function_version`
- `purpose`
- `criticality`
- `owner`
- `authority_ceiling`
- `input_contract`
- `output_contract`
- `tool_contract`
- `side_effect_contract`
- `evidence_contract`
- `failure_contract`
- `acceptance_suite_ref`
- `acceptance_threshold`
- `provenance_requirements`
- `independence_requirements`

A model/provider identifier belongs in an eligibility record, not in the function identity.

## Criticality

Proposed values:

- `NON_CRITICAL`
- `IMPORTANT`
- `CRITICAL`

A `CRITICAL` function is subject to the Capability Continuity Invariant.

Criticality must be justified by business/operational consequence, not by prestige of the role.

## Input contract

The input contract should state what the function is allowed and required to receive.

Examples:

- exact repository and immutable target;
- bounded artifact packet;
- declared user/customer context;
- tool availability;
- policy/instruction version;
- prior findings/review memory;
- prohibited data classes.

A replacement substrate that needs materially broader sensitive context is not automatically equivalent.

## Output contract

The output contract should specify machine- and human-consumable requirements.

Examples:

- schema-valid finding records;
- severity vocabulary;
- evidence references;
- explicit unknowns;
- bounded claims;
- confidence/uncertainty representation;
- no unsupported authority language.

Semantic quality must still be tested; schema validity alone is insufficient.

## Tool contract

Define:

- tools the function may use;
- tools it must be able to use;
- tools it must not use;
- read/write posture;
- network boundary;
- credential class;
- timeout/retry limits.

Tool availability is part of capability. A model that reasons well but cannot perform required evidence acquisition may not be eligible for the same function.

## Side-effect contract

Define allowed effects independently of model capability.

Examples:

- `NONE`
- `READ_ONLY_EXTERNAL`
- `LOCAL_EPHEMERAL_WRITE`
- `PROPOSED_MUTATION_ONLY`

Consequential mutation, approval, deployment, publication, or financial action should remain separately governed and never be inferred from model eligibility.

## Authority ceiling

The function contract must state the maximum authority a substrate can exercise while performing the function.

Model quality cannot raise this ceiling.

A more capable model does not become more authorized.

The machine-readable function contract binds the authority ceiling to an external source reference and SHA-256 digest. A substrate eligibility record separately binds the exact same authority-ceiling digest. A deterministic verifier must establish that equality from immutable evidence rather than trusting a model or caller assertion.

## Evidence contract

State what must be durable after the function completes.

Examples:

- immutable target identity;
- input packet digest;
- substrate/model identity;
- instruction/policy digest;
- tool/evidence observations;
- findings and supporting references;
- failure state;
- start/end timestamps;
- verifier version;
- acceptance-suite version.

Evidence should be sufficient to explain what was run and what was claimed without relying on the model session remaining available.

## Failure contract

Define explicit failure states.

Examples:

- `SUBSTRATE_UNAVAILABLE`
- `INPUT_INCOMPLETE`
- `TOOL_UNAVAILABLE`
- `TARGET_UNVERIFIED`
- `ACCEPTANCE_THRESHOLD_NOT_MET`
- `POLICY_MISMATCH`
- `EVIDENCE_INCOMPLETE`
- `OUTPUT_INVALID`
- `HOLD`

A failover system must not convert one of these into success merely because another model returned text.

## Acceptance suite

The acceptance suite should include both known and novel tests appropriate to the function.

A substrate eligibility run should bind:

- function version;
- substrate/model version;
- inference configuration;
- suite version;
- tool environment;
- score/results;
- known failures;
- eligibility disposition;
- validity window or re-evaluation trigger.

## Replacement eligibility

Proposed dispositions:

- `ELIGIBLE`
- `ELIGIBLE_WITH_LIMITS`
- `INELIGIBLE`
- `STALE_REEVALUATION_REQUIRED`
- `UNVERIFIED`

`ELIGIBLE_WITH_LIMITS` cannot be silently routed into cases exceeding the recorded limits.

An eligibility record also carries `ACTIVE`, `REVOKED`, or `SUPERSEDED` status. A technically qualifying historical evaluation is not current eligibility when its record is revoked, superseded, expired, outside its recorded limits, or subject to a fired re-evaluation trigger.

## Re-evaluation triggers

Eligibility should be reconsidered when materially relevant conditions change, including:

- model version or weights;
- system prompt/instruction contract;
- quantization or inference configuration;
- tool environment;
- acceptance suite;
- safety layer/provider wrapper;
- function contract;
- material observed regression;
- expiry of the eligibility window.

## Machine-readable proof chain

This proposal now includes a bounded machine-contract package:

- `schemas/critical-function-contract.schema.json`
- `schemas/substrate-eligibility-record.schema.json`
- `schemas/capability-continuity-assessment.schema.json`
- synthetic conformance fixtures under `examples/`
- `CAPABILITY_CONTINUITY_MACHINE_CONTRACT_V0_1.md`, which defines the mandatory semantic verification obligations.

The proof chain is:

```text
Critical Function Contract
        ↓
Substrate Eligibility Record
        ↓
Capability Continuity Assessment
```

For a critical function, the assessment schema allows `CAPABILITY_AVAILABLE` / `capability_loss: NONE` only when at least one path is recorded as active, eligible, within limits, function-bound, authority-ceiling-bound, within its validity window, clear of re-evaluation triggers, tool-available, substrate-available, and evidence-complete.

It allows `CAPABILITY_UNAVAILABLE` only when no path satisfies all of those conditions.

The schema does not make caller-supplied verification booleans trustworthy. A deterministic verifier must compute them from immutable referenced evidence. Failure to prove any required condition makes that path non-qualifying.

## Example — adversarial exact-target review

Illustrative only.

`function_id`: `mirrornode.review.adversarial_exact_target`

Potential requirements:

- exact immutable target must be established before substantive review;
- detect authority escalation and provenance mismatch;
- distinguish representational consistency from denotational safety;
- exercise known escaped-defect corpus;
- produce at least one novel probe class when warranted;
- refuse unsupported clearance;
- emit structured P1/P2 findings with evidence references;
- preserve independence/provenance status separately from technical quality;
- authority ceiling `NONE`.

A local or hosted model that cannot meet those requirements is not a valid substitute for that function, regardless of general benchmark rank.

## Continuity consequence

For a critical function, `CAPABILITY LOSS: NONE` is a valid system claim only when at least one currently eligible execution path exists and the required surrounding tools/evidence mechanisms are available.

The model alone is not the capability.

The governed function stack is the capability.

Technical eligibility does not establish independent-review provenance, approval, execution authority, deployment authority, or constitutional clearance.

## Non-claims

This proposal now defines **proposal-stage machine schemas and conformance fixtures**. It does not claim those schemas are ratified canon, that a production semantic verifier exists in CORE-HUB, that any real model/substrate has qualified, or that any current production continuity assessment has been emitted.

It does not define final benchmark weights, qualifying models, production routing policy, or automatic failover behavior.

It does not authorize model procurement, cloud GPU spend, deployment, runtime implementation, publication, or automated failover.
