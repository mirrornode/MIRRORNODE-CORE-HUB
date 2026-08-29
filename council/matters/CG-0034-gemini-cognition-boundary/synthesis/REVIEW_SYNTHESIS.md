# CG-0034 — Review Synthesis

**Status:** synthesis filed; superseded by Operator disposition on 2026-08-14  
**Scope:** cognition capability classification only

## Position summary

| Reviewer | Classification | Core reason |
|---|---|---|
| Ptah | Option B — sibling cognition contract | Avoid semantic overloading; cognition requires different machine-readable invariants from infrastructure capabilities. |
| Thoth | Option B — sibling cognition contract, hard security boundaries | Cognition introduces prompt/context/tool-call attack surfaces that must remain non-executing and separately authorized. |
| Osiris | Option B — sibling cognition contract | Generated output must remain distinct from verified evidence; provenance and disclosure require separate semantics. |
| Theia | Option B — sibling cognition contract | Provider invocation and Room presence are different architectural identities; separation preserves contestability and Operator access. |

All four filed positions reject convenience-classification of Gemini under `EVIDENCE` or `EXECUTION`. They are governance inputs; this synthesis does not claim that they constitute independent exact-head reviews of this pull request.

## Shared invariants

The positions converge on the following requirements:

1. **Provider non-authority:** Gemini/Google cannot grant MIRRORNODE authority.
2. **Non-executing first slice:** initial cognition has a side-effect ceiling of `NONE`.
3. **Tool proposals are inert:** function/tool calls are generated data until a distinct authorized execution path handles them.
4. **Attribution and provenance:** provider, effective model/version, cognition declaration, requesting principal, governing policy/context references, completion state, and preserved output remain attributable.
5. **Generated output is not verified truth:** a receipt may prove that Gemini generated an output; it does not prove the output's claims.
6. **Context boundaries:** outbound context is explicitly scoped, provenance-aware, and disclosure-governed.
7. **Failure visibility:** refusal, truncation, safety block, parse/schema failure, timeout, provider error, and model substitution remain distinct states.
8. **MCP boundary preserved:** no Gemini remote-MCP path may create inbound/write/execution authority.
9. **Provider/presence separation:** provider adapter and later Room participant are distinct machine-readable identities.
10. **Contestability:** competing positions, dissent, uncertainty, and source evidence remain navigable; no model output becomes the exclusive representation layer.

## Classification decision recommended to Operator

**Recommended: Option B.** Define a provider-neutral sibling cognition contract that interoperates with MICC rather than expanding MICC v0.1 with a ninth capability family.

MICC remains responsible for infrastructure dependencies such as credentials, transport, evidence/telemetry, metering, state, and execution. The cognition contract defines model invocation and generated-position semantics. Any later Room/presence contract remains a separate layer again.

Recommended conceptual chain:

`MICC infrastructure -> cognition invocation -> attributed generated position -> optional Room presence/participation -> Operator decision -> separately authorized execution`

## Explicit rejection under current state

A bounded Gemini cognition declaration **should not be authored as a MIM instance under current MICC v0.1**. There is no honest primitive-family fit, and provider extensions cannot create a ninth family.

## Contract artifacts required if Operator accepts Option B

A subsequent separately authorized drafting matter should create, at minimum:

- cognition contract specification v0.1;
- machine-readable cognition declaration schema v0.1;
- provider-neutral input/context envelope schema;
- generated-position/output envelope schema;
- cognition invocation receipt mapping/additive AUDIT_EMISSION relationship;
- failure-state vocabulary;
- context/disclosure policy hooks;
- tool-proposal boundary semantics;
- provider-adapter reference semantics;
- model/version attribution rules;
- conformance fixture(s), beginning with the Gemini epistemic-capture inquiry.

The drafting matter must determine names and exact fields; this synthesis does not canonize them.

## Preserved unresolved questions

The reviewers agree on classification but leave material details unresolved:

- whether the contract should be called a Cognition Contract, Inference Contract, Model Invocation Contract, or another provider-neutral term;
- exact requirements for pinning model revisions where providers expose aliases rather than immutable revisions;
- which cognition provenance fields belong directly under existing `AUDIT_EMISSION.evidence` versus a new nested additive object;
- how context manifests reference protected material without leaking it;
- the machine-readable boundary between an attributed generated position and a persistent Room presence;
- when, if ever, cognition may propose tools/actions and which approval class governs that proposal stage;
- how replay/reproducibility should be described for stochastic model outputs.

These are not blockers to the classification decision, but they are blockers to implementation.

## Gate

**Historical gate satisfied:** The Operator selected Option B on 2026-08-14.

This synthesis remains a pre-disposition review artifact. The disposition grants no implementation, credential access, runtime change, Room/HUD implementation, deployment, publication, canon promotion, or merge authority.