# CG-0032 Revision Confirmation Summary

**Matter:** MCP Surface Contract v0.1  
**Recorded disposition:** `revision-required`  
**Revision authority:** R1 and R2 only  
**Executable MCP change authorized:** No  
**Confirmation state:** complete

## Confirmation record

| Position | Result | Definition-level conclusion |
|---|---|---|
| POS-0005 — Ptah Revision Confirmation | confirmed | R1 deterministic failure semantics are resolved; no Ptah definition-level blocker remains. |
| POS-0006 — Thoth Revision Confirmation | confirmed | R2 primitive-independent MCP boundary is resolved; no Thoth definition-level blocker remains. |
| POS-0007 — Osiris Revision Confirmation | confirmed-with-residual-future-conditions | Combined R1/R2 revisions preserve disclosure minimization, authority separation, and publication separation; no Osiris definition-level blocker remains. |

## R1 resolution — deterministic failure semantics

The revised contract now requires:

- bounded machine-readable operation outcomes;
- bounded completeness semantics;
- stable disclosure-safe reason codes for non-success outcomes;
- explicit condition-to-outcome/completeness/reason mappings;
- prohibition on free-text-only failure classification;
- schema rejection of unknown outcome, completeness, and reason-code values;
- later implementation fixtures proving exact failure semantics.

Ptah confirms this is sufficient at the definition level while leaving the complete future response schema to a later implementation matter.

## R2 resolution — primitive-independent MCP boundary

The revised contract now applies its governance boundary to every MCP server primitive, negotiated capability, extension, and output channel, including:

- tools;
- resources;
- prompts;
- templates;
- notifications/subscriptions;
- server instructions;
- extensions;
- future or newly negotiated protocol capabilities.

Projection rules, prohibited-data rules, prompt-injection restrictions, anti-capabilities, and the expansion gate all use this primitive-independent boundary. Unknown/new protocol primitives are denied by default pending separate review.

Thoth confirms the prior tool-specific loophole is closed at the definition level.

## Disclosure and authority confirmation

Osiris confirms the revisions preserve these separations:

- MCP projection is not publication approval;
- digest consistency is not truth, safety, approval, authorization, actor identity, freshness, or publication permission;
- canonical private state is not MCP-safe projection by default;
- failure diagnostics must remain disclosure-minimized;
- definition acceptance does not authorize implementation, remote exposure, deployment, publication, or capability expansion.

## Residual future conditions — not definition blockers

The following remain intentionally deferred to a separately authorized implementation-remediation matter:

- executable repository/location and ownership;
- one side-effect-free canonical validation primitive;
- exact field schemas and allowlists;
- concrete disposition of each current prototype tool;
- registration scope and executable identity pinning;
- dependency/runtime locking and reproducible startup;
- proof of no incidental writes;
- failure, prompt-injection, secret-disclosure, unknown-field, and protocol-capability tests;
- count/cadence inference review;
- remote exposure or additional model-runtime attachment;
- deployment, persistence, rollback, and publication decisions.

These require implementation evidence and separate Operator authority.

## Readiness conclusion

The Operator-authorized R1/R2 revision is complete and confirmed. No definition-level blocker remains in the required confirmation positions.

**CG-0032 is ready for final Operator disposition on the revised governing definition.**

An accepting disposition may authorize finalization/merge of the documentary definition-and-record PR only. It must not, by implication, authorize any MCP executable change, output remediation, relocation, additional primitive/capability, model-runtime attachment, remote exposure, deployment, publication, or write-capable MCP class.
