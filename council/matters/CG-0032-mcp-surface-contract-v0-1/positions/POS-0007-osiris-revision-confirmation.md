# POS-0007 — Osiris Revision Confirmation

**Matter:** CG-0032 — MCP Surface Contract v0.1  
**Role:** Osiris — disclosure and authority boundary  
**Review type:** bounded revision confirmation  
**Authority effect:** advisory only

## Confirmation scope

Confirm whether the combined R1/R2 revisions preserve and strengthen disclosure minimization, authority separation, and publication separation identified in POS-0004.

No executable MCP change, publication, remote exposure, or new capability is reviewed or authorized here.

## Result

**confirmed-with-residual-future-conditions**

## Findings

The revised definition preserves the prior disclosure and authority protections and improves them in two relevant ways:

1. Deterministic failure semantics now require bounded machine-readable outcomes, completeness values, and disclosure-safe reason codes, reducing pressure to expose sensitive free-text diagnostics.
2. The projection, prohibited-data, prompt-injection, anti-capability, and expansion rules now apply to the full MCP protocol surface rather than only tools.

The definition still clearly separates:

- projectability from publication approval;
- digest consistency from truth, safety, approval, authorization, actor identity, freshness, or publication permission;
- canonical private state from MCP-safe projection;
- definition acceptance from implementation, remote exposure, deployment, publication, or capability expansion.

No revised section authorizes raw ledger exposure, local-path disclosure, or publication by implication.

## Residual future conditions

A later implementation matter must still define exact field allowlists, response schemas, disclosure-safe diagnostics, cadence/count inference handling, and concrete tests proving that no private data leaks through errors or protocol metadata.

These remain future implementation and publication gates, not definition defects.

## Recommendation

**Combined R1/R2 revisions confirmed. No Osiris definition-level blocker remains.**
