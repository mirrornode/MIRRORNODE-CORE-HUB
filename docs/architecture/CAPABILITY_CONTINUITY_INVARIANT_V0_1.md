# Capability Continuity Invariant v0.1

**Status:** PROPOSAL — architecture source; not canon, not deployment authority  
**Date:** 2026-08-22  
**Authority effect:** NONE

## Purpose

Define the stronger MIRRORNODE continuity requirement that emerged from the owned-inference discussion:

> Loss of an external provider token, model session, context window, or single compute host must not be treated as an acceptable loss of a critical MIRRORNODE capability.

This proposal distinguishes continuity of **capability** from continuity of a particular model, vendor, credential, device, or conversation.

## Terminology and novelty boundary

`Capability Continuity` is used here as a descriptive name for this MIRRORNODE invariant. It is **not** a claim that MIRRORNODE coined the phrase or uniquely identified the wider enterprise continuity problem.

Current market research shows overlapping public language around capability continuity, AI continuity, model-change management, portable governance, model-agnostic control planes, and behavioral continuity. MIRRORNODE's proposition must therefore be evaluated on its mechanism and evidence, not terminology ownership.

The mechanism this proposal intends to make testable is the combination of:

- function identity outside the model;
- replacement-substrate eligibility against the same acceptance contract;
- authority ceilings external to model capability;
- durable evidence outside model memory;
- retained failure lineage for future verification;
- fail-closed refusal to call an ineligible substrate a valid fallback.

## Core invariant

**Capability Continuity Invariant**

A MIRRORNODE function classified as critical must have at least one independently operable execution path under MIRRORNODE control that can meet the function's acceptance contract without depending exclusively on a metered third-party cognition API.

The loss of any single external provider, API token, model session, context window, or compute host must not eliminate the critical function.

A replacement substrate is not considered equivalent merely because it runs. Eligibility is demonstrated against the role/function acceptance suite.

## Three-layer execution model

### 1. Optional frontier cognition

Examples may include hosted OpenAI, Anthropic, Perplexity, Gemini, or later providers.

These services can provide high-value cognition, comparison, or independent review. Their availability must not constitute the sole continuity mechanism for a critical MIRRORNODE function.

### 2. MIRRORNODE-controlled inference

Open or otherwise deployable model weights may run on GPU compute provisioned by MIRRORNODE while the underlying hardware is rented from an infrastructure provider.

The replaceable infrastructure provider supplies compute capacity. MIRRORNODE retains control of the serving configuration, model eligibility decision, deployment specification, access policy, evidence/receipt policy, routing, and shutdown/reprovision procedure.

This layer is the principal path for preserving high-capability inference without per-request cognition-token dependence.

### 3. Local control and deterministic continuity

The trusted local/operator layer retains system state, authority records, exact targets, evidence, receipts, review memory, deterministic Thea verification, continuity packets, and the ability to recover or reprovision the higher-capability inference layer.

Locality by itself is not the governing objective. The governing objective is that authoritative state and critical operating control remain recoverable and portable.

## Provider independence

Provider independence means that a MIRRORNODE role or function is defined by:

- required inputs;
- required outputs;
- tool and side-effect boundaries;
- evidence requirements;
- authority ceiling;
- failure behavior;
- acceptance tests.

It does **not** mean that Claude, Gemini, Copilot, OpenAI, Perplexity, or a local/open model are interchangeable by declaration.

Substrates are candidates for a role. The role survives substrate replacement.

## Capability parity

Each critical function should eventually have a capability suite appropriate to that function.

A review role may be tested for, among other things:

- exact-target discipline;
- authority-escalation detection;
- representational-versus-denotational analysis;
- provenance and independence reasoning;
- known-regression discovery;
- novel adversarial probe generation;
- unsupported-clearance refusal;
- structured finding emission.

A substrate becomes eligible only when it meets the governed threshold for the function it is asked to perform.

## Failure semantics

Provider unavailability should be represented as substrate state, not automatically as capability loss.

Example:

```text
OpenAI substrate ........ unavailable
MIRRORNODE reasoner ..... ready
Reasoning capability .... ready
Capability loss ......... none
```

If no eligible substrate remains, MIRRORNODE must report the function unavailable rather than silently lowering its acceptance contract.

## Deterministic layer

Thea remains below model interpretation where possible.

The model may generate hypotheses, attacks, classifications, or proposed findings. Deterministic machinery should establish machine-checkable facts and refuse known-invalid states.

No model substrate gains authority merely by satisfying a capability benchmark.

## Oracle implication

Oracle should be treated as a MIRRORNODE service/function contract rather than as one permanently bound model endpoint.

The Oracle role may change eligible model substrate while preserving its governed prompt/role contract, tools, evidence requirements, review-memory access, and authority ceiling.

A model swap does not itself establish equivalent quality; the replacement must satisfy the relevant benchmark and provenance requirements.

## Commercial implication

The first production-facing application of this principle is Osiris Audit v1.

The audit may examine, where supported by supplied evidence:

- single-provider or single-token dependency;
- model/session dependency;
- authority that accidentally lives in a provider rather than the governed system;
- evidence that disappears with a context window or account;
- functions that could move to controlled inference or deterministic enforcement;
- missing recovery or substrate-replacement paths.

The audit remains a bounded structural review and does not certify portability, compliance, security, or production readiness.

## Public positioning implication

A truthful public positioning may say that MIRRORNODE is **building control infrastructure for AI systems that must remain governable through model and provider change**.

A concise external formulation may center three durable concerns:

1. **Control** — explicit bounded consequential authority.
2. **Continuity** — preservation of required capability across model/provider/compute changes.
3. **Evidence** — durable reconstructable observations, decisions, reviews, and receipts.

Public language must not imply that MIRRORNODE uniquely owns the general continuity/control problem or that `Capability Continuity` is an uncontested category term.

Until an owned cloud-GPU inference path is actually deployed and verified, public language must describe it as architecture direction rather than current production fact.

## Infrastructure portability target

A mature MIRRORNODE inference deployment should be reproducibly provisionable from controlled deployment specifications on more than one acceptable GPU infrastructure provider.

The infrastructure host should be replaceable without rewriting MIRRORNODE's role contracts, evidence format, authority model, or continuity record.

## Local laptop implications

This proposal intentionally does **not** settle the protected-laptop architecture.

It changes that problem materially: the laptop may become the trusted Operator endpoint, root-of-control surface, local deterministic/evidence layer, and recovery point rather than the sole location of high-capability inference.

Credential custody, device identity, remote-inference authentication, local service supervision, secure logging, backup, incident evidence preservation, and three-seat stop/review authority require a separate bounded design pass.

## Non-claims

This proposal does not claim:

- a production MIRRORNODE cloud-GPU inference fabric currently exists;
- local/open models presently match every hosted frontier model;
- model substitution establishes independent review provenance;
- provider-independent operation eliminates infrastructure-provider risk;
- an eligible model gains governance or execution authority;
- the protected-laptop control design is complete;
- MIRRORNODE originated the general capability-continuity concept or phrase;
- publication, deployment, procurement, credential issuance, or expenditure is authorized.

## Next proposed slices

1. Define the critical-function inventory and acceptance suites.
2. Benchmark candidate owned inference substrates against the adversarial corpus and function-specific tests.
3. Define a portable inference deployment specification and two-provider recovery test.
4. Define the protected-laptop control/security/evidence architecture separately.
5. Reconcile MIRRORNODE-00 and public positioning after Operator disposition on this proposal.
