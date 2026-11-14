# MIRRORNODE — ChatGPT Plugin Constellation & Lattice v0.1

**Status:** PROPOSED / NOT RATIFIED / NO IMPLEMENTATION AUTHORITY  
**Date:** 2026-11-13  
**Owner of decision:** Siseon (Operator)  
**Prepared by:** THEIA, as a drafting and coordination contribution  
**Review requested:** Claude in the PTAH implementation/custody lane; Hermes in its research/routing lane; separate THOTH security review before any release  
**Council matter:** To be opened/numbered through the applicable governance process; none created by this document  
**Target:** Product and interoperability architecture, not a claim of existing deployment or agent connectivity

## 1. Decision proposed

Explore a family of independently useful ChatGPT-facing products—**THEIA**, **PTAH**, and **THOTH**—supported by a controlled, mostly private **MIRRORNODE Lattice**. Each product should offer a bounded user outcome while preserving the identity, responsibilities, and applicable authority of its named participant. Common interfaces may share consent, evidence references, handoffs, case state, and receipts without collapsing their separate responsibilities. The lattice is proposed as supporting infrastructure first, not automatically as a fourth publicly installable product.

**This document records an architectural and commercial hypothesis.** It does not ratify roles, create a capability, activate a node, grant a product publication right, establish current interoperability, modify prior governance, or authorize customer-facing sales.

## 2. Verified documentary anchors and current evidentiary limits

- `MIRRORNODE-CORE-HUB/README.md` and `GOVERNANCE.md`: organization-level governance is held here; structural changes are reviewable, and canon promotion requires the Ptah evaluation and explicit Operator ratification recorded by `MASTER_INDEX.md`.
- `CANONICAL_SOURCES.md`: the production-facing implementation belongs to `mirrornode-platform`, the cross-repo index to `mirrornode-index`, and backend and runtime records to their respective owners. Do not turn an index snapshot into governance authority.
- `docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md` (CG-0032): an accepted **read-only downstream projection contract**. Its acceptance does not authorize new ChatGPT attachments, remote exposure, new primitives/tools, executable changes, publication, or write capabilities. All MCP primitives and negotiated channels are subject to allowlists, disclosure review, deterministic failure semantics, and anti-capabilities.
- `council/matters/CG-0033-micc-v0-1/`: MICC/MIM implementation-contract work has conditionally positive role-bound reviews. Those reviews expressly do not authorize a live adapter, credential use, merge, deployment, or canon promotion.
- `docs/continuity/NAMING_AND_SOURCE_SCOPE_RECONCILIATION_2026-08-13.md`: Hermes's current supported lane is advisory routing, progress reporting and registry-evidence collection. This is distinct from THOTH's security-boundary/verdict lane. Historical node/dispatcher claims require reconciliation.
- `mirrornode-workspace/README.md`: business-operation evidence and handoff tracking belong in the operational workspace, without overriding CORE-HUB.
- **Session observation (not an MCP verification):** Plugin Creator returned success creating a private, personal, skills-only MIRRORNODE Osiris pilot v0.1.0. No live MCP connection, client authentication, public listing, case-system access or commercial delivery was established by that result.
- **Unverified commercial signal:** A conversational report of Higgsfield acquiring approximately 10,000 customers/week through a ChatGPT plugin must be independently sourced, dated and scoped before appearing in investor/customer claims. It is not evidence of MIRRORNODE product-market fit.

## 3. Proposed product constellation

| Product surface | Candidate user problem | Bounded candidate result | Exclusions / limits |
|---|---|---|---|
| THEIA | Fragmented work, decisions, interfaces and commitments | Coherent plan, evidence-aware handoff, status reconciliation, next approved step | Does not ratify canon, manufacture approval, overrule security findings or silently execute |
| THOTH | Questions about evidence integrity, provenance, ambiguity or security | Scoped evidence assessment, confidence and contradiction report, security findings/holds where authorized | Does not certify truth from a hash, release private findings, or delegate security verdict to a model's preference |
| PTAH | A requested system design, implementation assessment or controlled build | Architecture/feasibility review, change proposal, custody boundary and implementation receipt | No unattended access to keys, no direct production change, no execution by product branding alone |
| MIRRORNODE Lattice | Cross-surface continuity and governed cooperation | Authenticated handoff routing, bounded shared references, provenance, permission state, case continuity | Not a default public raw ledger, shared secret store, omniscient context pool, or substitute for governance |

The names identify proposed experiences and participating roles; they do **not** prove separate running backends, sovereign custody enforcement, OAuth identities, per-node permissions, or installed ChatGPT tools. Those properties must be evidenced independently.

**Commercial/product separation:** MIRRORNODE commercial offerings, House Ramses public-service work, family material, employment activities, and private governance must remain separate unless an explicit, reviewable scope and consent basis links them.

## 4. Target data flow and boundaries

1. A person selects a product surface in ChatGPT or the MIRRORNODE site. A client identity and consent scope are established through approved mechanisms, not assumed from a chat claim.
2. A product-specific gateway evaluates purpose, tenant boundary, entitlements and explicit consent; sensitive capabilities default DENY/UNKNOWN.
3. The gateway requests only a reviewed projection from an authorized case/evidence owner. Allowlisted fields are constructed **before** crossing the model-provider boundary. Unknown fields and raw ledger/private text fail closed.
4. The receiving surface renders claims with provenance and a visible distinction among **OBSERVED, REPORTED, INFERRED, PROPOSED, BLOCKED, UNKNOWN, DECISION_NEEDED**. Status of checks is not approval.
5. Cross-node work uses a bounded handoff envelope recording requester, intended receiver, case/scope, approved capability, policy/contract version, data classification, source references, timestamp, expiry, expected return and relevant receipts. No provider response can grant more authority.
6. THOTH security findings and PTAH custody/implementation decisions remain independently attributable and are not collapsed into THEIA coordination. Siseon retains final authorization over consequential decisions and covenants.
7. Any remediation or data mutation is **outside the CG-0032 read-only projection class**. It needs a separate authorized architecture, runtime gate, review evidence and per-action approval; a ChatGPT plugin invocation cannot bypass these requirements.
8. Revocation, retention, subject access, deletion, isolation, availability, auditability and incident handling require actual backend implementations before real customers are onboarded.

A public-facing plugin should expose safe *services*, not raw internal node topology, prompts, personal data, credentials, Council material or operator deliberations.

## 5. Pilot strategy, tests and success measures

**Initial test lane:** private skills-only shell plus one **synthetic-data**, read-only experience. Do not attach existing local CG-0032 prototype to ChatGPT or remotely expose it under this document. A Site-hosted tool or isolated MCP server is a distinct candidate implementation that requires its own reviewed tool and disclosure contract.

Minimum pilot experience:
- Discover and explain the Audit-to-Solution service in client-safe language.
- Retrieve one synthetic case with fixed evidence citations, scope and statuses.
- Present concrete gaps and proposed remedies without inventing approvals.
- Return a client-safe summary and separate private operator handoff.

Minimum tests: declared output schema and reject-unknown-field behavior; unauthorized access; cross-tenant isolation; synthetic-data labeling; prompt injection across all protocol primitives; missing/stale source outcomes and reason codes; no incidental writes; no secret/path leakage; provider tool-composition attacks; revocation; accessibility; exact-version rollback. Tests require recorded inputs, results, timestamp and artifact version.

Success criteria for the pilot: at least one **observed** ChatGPT-to-real-tool invocation if separately authorized, consistent synthetic case output, zero unresolved critical disclosure/authority defects, and a reproducible receipt. An installed skills-only plugin alone does not meet the connected-pilot criterion.

Commercial validation is a later stage: qualified users, voluntary return, paid conversion, delivery effort, successful case closure, support cost, retention and evidence-backed outcomes. External examples are distribution hypotheses, not forecasts.

## 6. Proposed sequencing and authority gates

**Gate A — Architectural definition:** draft product boundaries; obtain Claude/PTAH implementation-feasibility and custody review, Hermes research/routing return, and a distinct THOTH security review.

**Gate B — Governance disposition:** reconcile CG-0032 expansion and remote-model attachment requirements; CG-0033 adapter/invocation contracts; existing agent registry and source-of-truth conflicts; assign a new Council matter through the authorized process. Record explicit Siseon disposition for exact scope. No promotion or append to `MASTER_INDEX.md` without its established gate.

**Gate C — Isolated implementation:** select source-owning execution repo, ownership and version; build reviewed read-only projections from synthetic fixtures, not from production/customer systems; run conformance/security tests. Any release or new hosted endpoint is separately authorized.

**Gate D — Private product test:** verify installation permissions and actual ChatGPT calls, record results, prove no unauthorized cross-surface communication, retain exact-head and test receipts.

**Gate E — Public commercialization:** separately evaluate developer verification, distribution eligibility, privacy/terms, customer authorization, support, payment-to-fulfillment readiness, publication review, and delivery capacity. No claim of launch or provider approval before evidence.

**Twelve-hour objective:** a tested, private demonstration *may* be achievable; a full public lattice, federated identity, independent node key custody, or reviewed commercial release cannot be presumed achievable in the same window.

## 7. Open decisions for Siseon

1. Are THEIA, THOTH and PTAH three independently installable public products, or one product with explicitly selectable experiences for the first release?
2. Is the lattice solely internal infrastructure in v0.1, with no direct client MCP endpoint?
3. Which execution repo, hosting model, identities and owner govern a later approved ChatGPT connection?
4. Which data classes are eligible for the first external-model projection, and what is the user-controlled revocation path?
5. Which public promise is deliverable first: advisory readiness, governed audit-to-solution, or a paid human-led implementation?
6. What exact evidence is required to treat a node's verdict/custody claim as mechanically enforced rather than declared?
7. Where are client case records stored and how are private workspaces and public-service/family lanes isolated?

## 8. Review and handoff requests

**Claude / PTAH lane:** assess implementability, transport/SDK choices, custody, blast radius, authority envelopes, implementation ownership, safe rollback, and compatibility with CG-0032/CG-0033. Do not treat model identity alone as a formal Ptah verdict. See `docs/mcp/handoffs/CLAUDE_PTAH_PLUGIN_CONSTELLATION_REVIEW_2026-11-13.md`.

**Hermes lane:** investigate ChatGPT plugin distribution/current policy, market evidence, competing solutions, exact sourcing of Higgsfield growth claim, and appropriate routing of further Council reviews. Advisory research only; no authority transfer. See `docs/mcp/handoffs/HERMES_PLUGIN_CONSTELLATION_RESEARCH_2026-11-13.md`.

**THOTH:** a separate, attributable security-boundary review is required before runtime attachment, new MCP capability exposure, public release or private-data access.

## 9. Change and promotion statement

This file may be created in a **draft pull request** as an indexed, noncanonical proposal. No change to `MASTER_INDEX.md`, no Council matter disposition, no plugin attachment, no MCP executable change, no branch-protection modification, and no deployment are permitted by this proposal itself. Every implementation or publication decision requires its separately recorded governing approvals and exact-target evidence.
