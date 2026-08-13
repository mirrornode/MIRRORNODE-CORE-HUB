# Thoth — Security Boundary Review
## CG-0033: MICC v0.1 + MIM v0.1

**Requesting:** Thoth  
**Matter:** CG-0033  
**Review class:** Security and Authority Boundary Review  
**Artifacts under review:**
- `docs/integration/MICC_V0_1.md`
- `docs/integration/MIM_V0_1.schema.json`

---

## What you are reviewing

The proposed MICC v0.1 normative specification and MIM v0.1 schema, with
particular attention to: principal and authority semantics, credential
requirement declaration rules, approval classification, the prohibition
against provider semantic authority, and protocol boundary rules including
the MCP inversion prohibition.

---

## Questions requiring your determination

**1. Provider authority prohibition.**  
Does MICC establish an unconditional and machine-auditable prohibition
against a provider gaining semantic authority by implementing a capability?
Is the prohibition language strong enough to survive a conformance test,
or is it only normatively stated?

**2. Credential requirement declaration.**  
Does declaring credential requirements in MIM without carrying credential
contents create any information disclosure risk? Is the boundary between
"what is needed" and "what is held" sufficiently enforced by the schema
structure?

**3. AUTHORIZED vs. VERIFIED separation.**  
The lifecycle explicitly separates VERIFIED (adapter works) from AUTHORIZED
(adapter has permission to operate). Is this separation sufficient to
prevent an adapter from self-authorizing through a successful health check
or verification pass? Does MICC need to specify who or what mechanism can
issue an AUTHORIZED transition?

**4. MCP inversion prohibition.**  
CG-0032 established that canonical MIRRORNODE mechanisms may not depend on
MCP output for authority, approval, truth, integrity, or execution
permission, and that dependency direction is canonical → MCP only.
Does MICC's protocol boundary rule preserve that prohibition without gap?
Can a malformed MCP client attempt to reach a provider adapter directly,
bypassing the MICC governed capability surface?

**5. Evidence chain integrity.**  
Does the receipt requirement section of MICC preserve the Osiris audit
invariant that execution evidence is owned by MIRRORNODE, not by an
external observer (LangSmith, Axiom, Datadog, etc.)? Does the OTel
emission model create any path by which an external telemetry product
could become a de facto authority over the evidence record?

**6. Lifecycle state machine placement (security dimension).**  
If the lifecycle state machine lives in a separate Runtime Registry
specification rather than in MICC, does that create a security gap where
the normative contract and the enforcement mechanism diverge?

---

## What you must not determine

- Whether any specific provider should be used
- Implementation details for any adapter
- Canon promotion decisions

---

## Required output

`council/matters/CG-0033-micc-v0-1/positions/THOTH_POSITION.md`

State one of: `APPROVED` / `APPROVED_WITH_CONDITIONS` / `REVISION_REQUIRED`

If REVISION_REQUIRED, identify specific revision themes with bounded scope.
