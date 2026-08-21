# Delegation Boundary v0.1 — Standards and Practice Crosswalk

**Status:** Informative draft under CG-0036  
**Purpose:** Show which established authorization, identity, AI-governance, and agent-security practices informed the v0.1 design. This document does not claim certification or formal conformance.

## Current reference set

| Reference | Relevant practice | CG-0036 application |
|---|---|---|
| OpenID AuthZEN Authorization API 1.0 (Final, Jan 2026) | Separates Policy Decision Point (PDP) from Policy Enforcement Point (PEP); standardizes Subject, Action, Resource, Context, Decision. | CG-0036 adopts PDP/PEP separation and the same five-object authorization information model. |
| NIST SP 800-207 / SP 800-207A | No implicit trust; identity- and resource-focused authorization; policy decisions enforced at explicit control points. | No action is allowed merely because an actor is local, known, or already participating. Decisions are re-evaluated against identity/resource/state. |
| NIST SP 800-53 Rev.5 Release 5.2.0 | Access control, least privilege, audit/accountability, authorization/monitoring, configuration integrity. | Least authority, separate receipts, policy integrity hashes, non-delegable guardrails, revocation and continuous verification. |
| RFC 8707 | Explicit target-resource identity and audience restriction; scope should not stand in for resource identity. | Resource scope uses canonical target identifiers; aliases normalize before authorization; grants are not portable to unrelated resources. |
| SPIFFE | First-class verifiable workload identity across heterogeneous distributed systems. | PDP/PEP/executor identities should be independently attestable; production implementation should support verifiable workload identity rather than process-name trust. |
| Cedar authorization semantics | Default deny; forbid-overrides-permit; policy schema validation. | CG-0036 uses default deny and explicit non-delegable/forbid guardrails. A future policy engine may use Cedar or equivalent semantics; v0.1 does not mandate a language. |
| NIST AI RMF 1.0 + revision program | Govern/Map/Measure/Manage, risk tolerance, independent review, TEVV, monitoring, go/no-go decisions. | Delegation limits are governed artifacts; autonomous execution requires measurable thresholds, testing, monitoring, review, and explicit commissioning. |
| ISO/IEC 42001:2023 | AI management-system governance, traceability, performance evaluation, continual improvement. | Policy/delegation lifecycle, auditability, review, change control, and product governance should be managed continuously, not frozen at launch. |
| ISO/IEC 23894:2023 | Integrates AI-specific risk management into organizational risk practice. | Risk ceilings and escalation must be tied to an explicit risk process rather than an agent-generated confidence score. |
| OWASP LLM06:2025 Excessive Agency | Minimize extensions/permissions; execute in user context; require human approval for high-impact actions. | Cognition cannot grant action authority; delegated effects use least privilege and human approval for higher-impact classes. |
| OWASP Agentic AI guidance (2026) | Least-privilege agency, human approval for high-impact actions, context validation, agent identity/message integrity, resource budgets/circuit breakers. | Adds aggregate-authority review, identity integrity expectations, chain/composition controls, risk ceilings, and future runtime budget/circuit-breaker requirements. |

## Design gaps explicitly closed in draft.2

### 1. Hidden classifier sovereignty

**Previous gap:** authority classes existed without a bounded owner/process for classification.

**Correction:** policy authorship, PDP/classifier, authorizer, PEP/executor, and verifier are separate roles. The PDP evaluates immutable policy; it does not legislate policy. Unmatched/ambiguous/error states default to deny/non-delegable.

### 2. Mutable policy references

**Previous gap:** `governing_policy_ref` and `policy_version` could point to content that changed underneath them.

**Correction:** every grant and decision binds `policy_content_hash` and `policy_bundle_hash`; enforcement requires the exact evaluated policy content.

### 3. Resource aliasing

**Previous gap:** arbitrary strings could represent resource scope.

**Correction:** authorization uses canonical resource identifiers before evaluation, borrowing the same separation of scope/action from target-resource identity reflected in RFC 8707.

### 4. Aggregate authority multiplication

**Previous gap:** individually safe delegations could combine into excessive effective authority.

**Correction:** autonomous decisions require an aggregate-authority snapshot covering all applicable active grants, with separately governed actor/root ceilings and action-chain composition checks.

### 5. Subdelegation monotonicity

**Previous gap:** prose required monotonic narrowing but JSON Schema could not compare child with parent.

**Correction:** the schema carries explicit ranks/parent references; the specification candidly requires a conformance validator for cross-document subset/rank/expiry checks. JSON Schema is not misrepresented as sufficient.

### 6. Revocation, expiry, and stale enforcement

**Previous gap:** no bounded revocation latency and no independent expiry behavior.

**Correction:** grants carry maximum revocation-propagation time, separate expiry behavior, queued-work rules, offline enforcement restrictions, and fresh authorization on retry.

### 7. TOCTOU

**Previous gap:** stale-state protection was normative only.

**Correction:** decisions bind state/resource/parameter/policy digests and PEPs must reject changed state; compare-and-swap, target-version preconditions, locks, or transactions are named enforcement patterns.

### 8. Cognition naming collision

**Previous gap:** `PROPOSAL_ONLY` meant both cognition side-effect ceiling and delegation class.

**Correction:** delegation class is `ADVISORY_ONLY`; cognition retains `PROPOSAL_ONLY` as its separate side-effect term.

### 9. MICC taxonomy mismatch

**Previous gap:** CG-0036 and MICC could produce unsynchronized authorization classes.

**Correction:** explicit cross-map states that both apply and the stricter gate wins. Delegation can only add restriction; it cannot downgrade MICC `APPROVAL_OPERATOR` or `APPROVAL_COUNCIL`.

### 10. False safety in UI

**Previous gap:** a UI could show one safe delegation while hiding aggregate control.

**Correction:** product requirements include aggregate authority, overlaps, root ceiling, provenance, freshness, action-chain warnings, and unresolved classifier/policy errors.

## Remaining work before implementation

Standards alignment does not make the draft executable. Before production autonomous execution, CG-0036 still needs:

1. bounded Ptah, Thoth, Osiris, and Theia reviews;
2. a provider-neutral conformance-validator contract for cross-document and aggregate checks;
3. a canonical resource-identity registry/normalization contract;
4. an aggregate-authority policy/profile with test fixtures;
5. a revocation-state distribution/freshness mechanism;
6. a PDP/PEP decision protocol profile (AuthZEN-compatible where practical);
7. execution and authorization receipt mapping to a repaired and reviewed audit contract;
8. threat-model fixtures for policy manipulation, grant composition, stale state, retry, aliasing, and compromised PDP/PEP;
9. a product/HUD test proving aggregate authority cannot be hidden by per-envelope presentation;
10. explicit commissioning/go-no-go criteria and monitoring thresholds;
11. a separately governed Council disposition validator that proves required composition, provenance, and quorum before Council-required `ALLOW` (existing `disposition.schema.yaml` and CG-0031 verify Operator dispositions, not Council constitution). v0.1 keeps `APPROVAL_COUNCIL` + `ALLOW` schema-invalid until that validator is ratified and a later schema revision is authorized.

## Primary references

- https://openid.net/specs/authorization-api-1_0.html
- https://csrc.nist.gov/pubs/sp/800/207/final
- https://csrc.nist.gov/pubs/sp/800/207/a/final
- https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- https://www.rfc-editor.org/info/rfc8707
- https://spiffe.io/docs/latest/spiffe-specs/
- https://docs.cedarpolicy.com/auth/authorization.html
- https://airc.nist.gov/airmf-resources/
- https://www.iso.org/standard/42001
- https://www.iso.org/standard/77304.html
- https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
- https://cornucopia.owasp.org/edition/companion/AAIA/1.0/en
