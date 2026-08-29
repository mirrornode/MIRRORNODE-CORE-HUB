# CG-0036 — External Review Response + Standards Check

**Status:** drafting evidence; not a disposition  
**Date:** 2026-08-14

## External-review findings accepted

The drafting pass accepts the following material findings from the independent Perplexity repository analysis:

1. The v0.1 filing described delegation vocabulary but did not yet define a binding decision/enforcement architecture.
2. Classifier ownership was the load-bearing unresolved authority question.
3. Multiple valid grants could compose into excessive aggregate authority.
4. Subdelegation monotonicity could not be established by the initial JSON Schema alone.
5. Resource scope lacked canonicalization.
6. Mutable policy references needed content integrity binding.
7. Revocation propagation, expiry behavior, retries, and TOCTOU required explicit enforcement semantics.
8. `PROPOSAL_ONLY` collided semantically with the Cognition Contract.
9. CG-0036 authority classes were not mapped to MICC approval classes.
10. Per-envelope UI could conceal aggregate effective authority.

## Draft.2 response

The revised specification and schemas address those findings by adding:

- PDP/PEP separation and a bounded Authority Classification Boundary;
- Subject/Action/Resource/Context/Decision information model;
- default deny and explicit forbid/non-delegable guardrails;
- policy content and bundle hashes;
- canonical resource identifiers;
- aggregate-authority snapshots and root ceilings;
- explicit cross-document conformance-validator obligations;
- separate revocation and expiry behavior plus freshness limits;
- fresh authorization on retries and TOCTOU enforcement requirements;
- `ADVISORY_ONLY` delegation terminology;
- MICC cross-map with stricter-gate-wins semantics;
- decision receipt schema;
- aggregate-authority visibility requirements for future HUD/product surfaces.

## Current standards/practice check

The revised architecture was compared against current primary-source guidance and standards, including OpenID AuthZEN Authorization API 1.0 (Final, January 2026), NIST SP 800-207/207A, NIST SP 800-53 Rev.5 Release 5.2.0, RFC 8707, SPIFFE, NIST AI RMF resources, ISO/IEC 42001:2023, ISO/IEC 23894:2023, Cedar authorization semantics, and OWASP guidance on excessive/agentic agency.

The standards check supports the architectural direction but also confirms that CG-0036 should not claim implementation readiness. The key remaining implementation-layer artifacts are listed in `docs/delegation/STANDARDS_CROSSWALK_V0_1.md`.

## Additional repository integrity finding

The external review reported corruption in `canon/contracts/AUDIT_EMISSION.md`. Direct inspection confirmed the file contains an embedded shell/heredoc used to write itself. Because CG-0036 must not modify locked canon as a side effect of delegation drafting, that defect is being handled as a separate, semantics-preserving repair lane rather than silently corrected in this matter.

## Review posture

The Ptah, Thoth, Osiris, and Theia positions required by CG-0036 should evaluate **draft.2**, not the superseded initial filing. Position provenance must be described accurately as role-bounded analyses unless independent reviewer execution is separately evidenced.
