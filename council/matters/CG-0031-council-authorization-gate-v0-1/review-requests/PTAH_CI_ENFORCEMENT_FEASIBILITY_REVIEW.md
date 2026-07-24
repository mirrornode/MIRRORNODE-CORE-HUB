# Ptah Review — CG-0031 CI Enforcement Feasibility

Matter: CG-0031 — Council Authorization Gate v0.1  
Reviewer: Ptah  
Review type: implementation-feasibility

## Scope of This Review

This review is limited to whether the proposed Phase 0 gate can be implemented deterministically within the boundary recorded in CG-0031 and `matter.yaml`.

It considers:

- authority input contract
- immutable source pinning
- repository and path-scope matching
- accepting disposition and condition validation
- failure-closed behavior
- fixture testing and scoped CI topology

It does not consider:

- whether CG-0030 or CG-0031 should be accepted
- Operator authority or Council Grounds governance
- required branch-protection activation
- broader repository rollout
- runtime or MOPCON enforcement

## Questions for Ptah

1. **Authority Input Contract**

   - Can a strict checked-in contract identify the exact matter ID, authority repository, immutable commit SHA, record path, implementation repository, and protected path scope?
   - Can unknown fields, mutable refs, and unsupported contract versions be rejected?

2. **Disposition and Condition Semantics**

   - Can the validator distinguish `accepted` and `accepted-with-conditions` from every non-accepting state without interpreting free text?
   - Can conditions be represented and checked in a narrow machine-readable form?
   - Do unknown, ambiguous, or unsatisfied conditions fail closed?

3. **Source and Scope Integrity**

   - Can the gate validate authority from an immutable pinned Council artifact rather than a mutable branch head?
   - Can it prove exact repository, matter, and protected-path alignment without blocking unrelated work?
   - What is the smallest safe cross-repository trust model for the CG-0030 pilot?

4. **Failure-Closed Behavior**

   - Do missing, malformed, mismatched, superseded, revoked, conflicting, or unpinned records fail deterministically?
   - Is any cached or last-known-good authority fallback excluded?

5. **Pilot CI Topology**

   - Can a scoped `mirrornode-platform` CI job run only for the `/continuity` implementation boundary and reference CG-0030?
   - Can the workflow fail as designed without changing branch protection or becoming a required merge check?
   - Can the validator remain reusable without silently expanding the pilot scope?

6. **Evidence and Testability**

   - Are the required positive and negative fixtures sufficient to prove deterministic behavior?
   - Are stable reason codes and disclosure-minimized diagnostics practical?

## Requested Output

Please provide:

- **feasible**, **feasible-with-conditions**, or **not-feasible** under the CG-0031 boundary
- required contract, topology, or test changes
- the recommended implementation location for the validator and pilot workflow
- a clear statement on whether the pilot can remain limited to CG-0030 and `/continuity`

## Advisory Nature of This Review

This review is advisory. It informs the Operator’s disposition but does not grant implementation or CI activation authority.

Authority remains `none-until-operator-disposition`. Required branch-protection activation and broader rollout require later Council action.
