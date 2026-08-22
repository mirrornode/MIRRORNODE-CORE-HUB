# Thea / Oracle Verification Architecture v0.1

**Status:** proposal; not canon, not runtime-enforced  
**Authority effect:** `NONE`  
**Date:** 2026-08-22  
**Implementation repo:** `mirrornode/theia-core`  
**Operator projection:** `mirrornode/mirrornode-operator-console` / MOPCON  

## 1. Purpose

This proposal records the system-level place of Thea and Oracle after the PR #53 specialized-terminal-agent review cycle exposed a recurring failure mode: tests, digests, schemas, reviewers, and green CI can each be individually valid while the combined authority claim remains false or incomplete.

The solution is not to designate another model as infallible. It is to separate:

1. deterministic verification;
2. adversarial hypothesis generation;
3. reviewer provenance and independence;
4. constitutional/Operator disposition.

## 2. Thea

Thea is the owned deterministic verification kernel.

Its responsibilities are to:

- validate bounded, machine-checkable invariants;
- fail closed on malformed or contradictory review evidence;
- execute permanent adversarial regression probes;
- preserve finding lineage and confidence withdrawals;
- emit bounded review claims;
- remain available independently of external code-review quota.

Thea is evidence infrastructure, not an authority source.

A Thea result cannot itself grant repository mutation, merge, canon promotion, deployment, runtime execution, Council clearance, or Operator authority.

### Current v0.1 proof surface

The implementation proposal currently verifies supplied-manifest semantics such as strict input types, path denotation, bounded operation classes, positive artifact containment, write-target collisions, verification-specific authorization presence, effect separation, path-set agreement, and limited lineage references.

The current implementation does **not yet** independently prove the live repository checkout is at the supplied SHA, parse raw Git status itself, or recompute handoff authorization-scope digests. Those are explicit next slices, not implied current capabilities.

## 3. Oracle

Oracle is the interpretive/adversarial layer above Thea.

Oracle receives Thea's deterministic evidence and asks a locally controlled model to:

- generate counterexamples;
- identify missing probe classes;
- attack inverse privilege surfaces;
- compare prose guarantees to executable guarantees;
- look for self-modification of validators, CI, policy, instructions, and audit evidence;
- explain uncertainty and additional risk.

Oracle may add findings. It may not erase a deterministic P1/P2 or convert evidence into authorization.

The initial model boundary is loopback-only with no cloud fallback. A remote Oracle provider would require a separately governed adapter/disclosure boundary.

## 4. Review provenance

Technical usefulness and independence are separate dimensions.

Every review record should preserve at least:

- implementer provenance;
- correction provenance;
- adversarial self-review provenance;
- independent review provenance;
- synthesis provenance;
- immutable target head;
- applicable prior findings by head.

A correction author may provide technically decisive self-review while remaining ineligible to supply independent closure.

## 5. Claim ladder

No lower claim implies a higher claim:

`SCHEMA_VALID`
→ `SEMANTIC_VALID`
→ `TEST_SUITE_PASS`
→ `ADVERSARIAL_PROBES_PASS`
→ `EXACT_HEAD_REVIEWED`
→ `INDEPENDENT_EXACT_HEAD_REVIEWED`
→ `CONSTITUTIONALLY_CLEARED`
→ `MERGE_AUTHORIZED`

This ladder is deliberately stricter than a single PASS/FAIL field.

## 6. Review lenses

Authority-bearing changes should be attacked through orthogonal lenses rather than several reviewers repeating the same inspection:

1. structural/schema;
2. semantic-invariant;
3. denotational/resource;
4. authorization-lifecycle;
5. adversarial state-transition;
6. provenance;
7. human-audit versus machine-consumption divergence;
8. self-modification/gate-modification.

Denotational and self-modification review are mandatory for scope/authority changes.

## 7. Permanent review memory

Serious escaped defects become permanent probes.

The seed corpus comes from PR #53 and includes:

- traversal and normalized path aliases;
- protected `.git` / `.github` targets;
- positive artifact-root containment and inverse privilege;
- validator/CI/agent-instruction self-modification;
- duplicate destination and source/destination collisions;
- raw-versus-parsed evidence divergence;
- verification external effects;
- verification-specific authorization;
- handoff scope lineage;
- working-directory binding;
- authorization expiry/revocation/supersession;
- legitimate accept baselines.

The intended rule is: once an escaped defect is understood, repeating that exact mistake should become cheap to detect.

## 8. Relationship to MOPCON / KHEPRI

MOPCON is the operator projection surface, not the source of Thea's facts or governing authority.

Conceptually:

`repository target → Thea deterministic evidence → Oracle adversarial interpretation → MOPCON/KHEPRI projection → independent/constitutional review → Operator disposition`

The first MOPCON slice is read-only and UNKNOWN-safe.

MOPCON may show target identity, claim limit, findings, probe coverage, Oracle status, provenance, constitutional state, and the next lawful action. It must not infer authorization from a green Thea run.

## 9. Relationship to CG-0036 and PR #53

### CG-0036 / PR #48

Delegation-boundary work addresses who may hold, grant, delegate, revoke, and consume authority. Thea does not redefine that architecture. It should eventually verify implementation/evidence artifacts against the ratified delegation semantics in force.

### Specialized terminal-agent proposal / PR #53

PR #53 is the primary failure-learning case for Thea. Its exact reviewed head `05d83494527a7318139d5255dd75fb4ff740600c` remains immutable evidence. The review cycle demonstrated that a passing 47-test suite did not cover path denotation, positive artifact scope, destination collision, evidence agreement, or handoff lineage.

The learning was moved into Thea rather than appended to the #53 branch so the review target remained unchanged.

## 10. Standards alignment

The architecture is intended to support—not claim automatic compliance with—current NIST-aligned practices:

- NIST AI 100-1, AI RMF 1.0 (`GOVERN`, `MAP`, `MEASURE`, `MANAGE`);
- NIST AI 600-1, Generative AI Profile;
- NIST SP 800-218, SSDF v1.1 (final);
- NIST SP 800-218A, AI/dual-use foundation-model SSDF Community Profile (final);
- NIST SP 800-218 Rev. 1, SSDF v1.2 (initial public draft, 2025-12-17) as a forward reference;
- NIST CSF 2.0 governance/risk communication principles.

NIST AI RMF 1.0 is itself under revision as of 2026; MIRRORNODE should track the revision rather than freeze a future compliance claim to the current version.

## 11. Non-authority statement

This document does not:

- ratify Thea;
- designate a default Oracle model;
- authorize MOPCON integration;
- clear PR #48 or PR #53;
- authorize merge, deployment, provider connection, or runtime action;
- replace existing Council or Operator gates.

Its purpose is to establish a coherent review architecture proposal and a shared vocabulary for the next implementation and review passes.
