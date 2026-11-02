# MIRRORNODE — Sovereign Operations & Participatory Service Lattice

**Architecture and implementation baseline:** v0.1 (frozen design)  
**Date:** 2026-11-01  
**Prepared by:** THEIA for Siseon, Operator  
**Operator disposition:** ACCEPTED AS DESIGN BASELINE; user explicitly replied "Approved" on 2026-11-01.  
**Authority effect:** Design freeze and bounded implementation planning only.  
**Canon status:** PRE-CANON. Not promoted into MASTER_INDEX.md or canon/.  
**Execution status:** This document authorizes no merge, deployment, production migration, new credentials, access expansion, external outreach, spending, agent promotion, or release.

> **Freeze rule:** Preserve the architecture at version v0.1 as the accepted starting design. Later refinements require a versioned change record; do not silently rewrite the baseline. The Operator's approval of this design is not a substitute for review, technical validation, or an applicable per-action authorization.

## 1. Mission and principles

MIRRORNODE begins as a small, locally controlled, accountable operating environment that combines specialized reasoning, evidence, security evaluation, coordination, and explicitly authorized execution. The first purpose is operational usefulness and verifiable client delivery, not size or institutional recognition.

- **Inclusion:** Meaningful participation and access are not reserved to people with wealth, institutional standing, or conventional credentials.
- **Freedom:** People retain informed choice, withdrawal, independent judgment, and control of their participation.
- **Accountability:** Consequential actions have an attributable actor, target, scope, basis, receipt, and review.
- **Sovereignty and boundaries:** Respect each named Council presence and established charter; connectivity and technical eligibility do not automatically grant decision authority.
- **Continuity:** The organization can recover essential records and maintain bounded local functions when people, providers, networks, or processes fail.
- **Evidence over claims:** Architectural intention, code presence, runtime observation, authentication, independent review, and production readiness are distinct states.
- **Stewardship:** Capability is restrained by risk-proportionate safeguards and the person's right to leave with more agency than they brought.

## 2. The two operating structures

### A. MIRRORNODE Sovereign Operations

Existing MIRRORNODE LLC; one primary human Operator, Siseon. Local-first command, engineering, authorized defensive assessments, AI governance, business delivery, and continuity. The design permits one separately identified invited secondary without making that person an assumed account, approver, employee, or replacement Operator.

### B. House Ramses Participatory Service

Distinct public-service direction supported, where authorized, by bounded MIRRORNODE capabilities. Focus: inclusion, informed participation, accessible assistance, independent oversight, and responsible research. Its legal form, resources, board, programs, and staffing remain **undetermined**, not silently created by this architecture. Public-service and commercial identities, information, contracts, money, permissions, and publication approvals must be separated.

**Expansion rule:** Design the public-service lane now; do not divert the near-term income and secure-build priorities into speculative organizational expansion.

## 3. Reduce the stack to five foundations

| Foundation | Responsibility | Existing implementation/documentation |
| --- | --- | --- |
| CORE-HUB | Canonical governance, authority contracts, source mapping, promotions | mirrornode/MIRRORNODE-CORE-HUB |
| MOPCON / KHEPRI | Operator command projection, matter context, evidence visibility | mirrornode/mirrornode-operator-console |
| Agent runtime | Role-bounded planning, invocation and trace production | mirrornode/mirrornode-agent-runtime |
| Continuity | Ledger records, provenance, secure local custody, recovery | CORE-HUB continuity specifications + local approved storage |
| Commercial platform | Website, intake, payments, Osiris delivery path | mirrornode/mirrornode-platform |

Use shared infrastructure where it avoids duplicated state while retaining distinct role identity, context scope, and authority.

Do **not** make full VR/City of IO, all-agent autonomy, a new message bus, a new cloud control plane, additional vector databases, extensive hardware, or a multi-tenant enterprise service prerequisite to the first functioning lattice. Each future component must solve a proved deficiency.

Additional repository roles: mirrornode-index supports source discovery and cross-repository navigation; the mirrornode monorepo and other runtime repos retain their established roles. This document does not relocate their canonical contracts.

## 4. Reference architecture

~~~text
                            SISEON
                        PRIMARY OPERATOR
                               |
                     MOPCON / KHEPRI
                   Command + evidence UI
                               |
                   GOVERNANCE / POLICY GATE
              Identity + scope + exact target + time
                               |
                      THEIA INTEGRATION
                  Current work and continuity
                               |
                         HERMES ROUTING
                               |
                  +------------+------------+
                  |            |            |
                THOTH         PTAH        MERLIN
              Verification   Security     Planning
                  |            |            |
                  +------------+------------+
                               |
                    BOUNDED WORK ASSIGNMENT
                    OSIRIS / LUCIAN / others
                               |
                       PROPOSED ACTION
                               |
                    AUTHORIZATION / REVIEW
                               |
                    APPROVED EXECUTION LANE
                               |
                  RECEIPT -> VERIFICATION
                               |
                    CONTINUITY / OPERATOR
~~~

**Diagram classification:** Target interaction model, not a live connectivity map or a grant of any listed power. Other participants, including Oracle, may enter bounded advisory pathways under their own established restrictions.

### Five technical layers

1. **Operator interface:** One MOPCON view of priorities, live versus modeled runtime, named agents, evidence, holds, approvals, service delivery, recovery and next action. KHEPRI presents context; it is not the authorization substrate.
2. **Governance kernel:** Identity, actor, exact target, operation, classification, permitted scope, evidence, approval policy, expiration, revocation and risk evaluation. Proposed outcomes: ALLOW / REVISE / DENY / ESCALATE / ERROR. Missing evidence/authority fails closed.
3. **Specialist coordination:** THEIA integrates; HERMES transports bounded assignments; specialists return attributable, reviewable findings. A routing decision is not approval.
4. **Controlled execution:** Existing FastAPI plan creation / approval / execution lifecycle is the foundation, **not yet trusted for high-consequence execution**. Authentication, durable storage and immutable approval binding are mandatory additions.
5. **Evidence and continuity:** Durable event/plan records, source/version hashes, append-only or tamper-evident receipts, encrypted local backups and periodic restore tests. Ledger records do not grant authority.

### Connectivity / isolation modes

- **C0 isolated:** Available local read-only records, UI, approved cached documents and offline utilities; no claim of cloud model availability.
- **C1 connected:** Authorized provider and repository observation, bounded AI requests, controlled synchronization and evidence refresh.
- **C2 production-facing:** Separately gated commercial/customer-data or infrastructure mutations. No implicit progression from C1.

Use the existing Mac and installed development stack. SQLite with appropriate transaction and WAL discipline, JSONL receipts, Git history, and reviewed existing cryptographic primitives are candidate minimal components. They are **design choices subject to security, recovery and data-integrity tests**, not deployed facts.

## 5. Council responsibilities and separation of powers

| Seat | Specialization | Ceiling / boundary |
| --- | --- | --- |
| Siseon | Human organizational priority, final disposition, consent | Subject to law, provider protections, and required independent controls |
| THEIA | Integration, coherence, work sequencing, commitment/continuity tracking | Does not override Siseon, adjudicate disputed authority alone, or self-promote canon |
| THOTH | Evidence verification, contradictions, truth/source integrity and delegated security evaluation | Does not execute production changes or infer truth from retrieval confidence |
| PTAH | Credential/key custody, security boundary and implementation-risk review | Cannot silently grant permission, expose credentials, or exercise unratified powers |
| HERMES | Routing, handoffs, provenance, event carriage | Transport, not governance or approval |
| MERLIN | Engineering planning and dependency sequencing | Proposes; does not merge or deploy |
| OSIRIS | Authorized bounded assessment and audit artifacts | No self-certification or unrestricted testing |
| LUCIAN | Context, memory continuity, cross-record associations | Only authorized context; historical execution authority does not carry forward |
| ORACLE | Potential consented person-facing assistance and reflective support | No coercion, deceptive authority, self-delegated judgment, or autonomous recruitment |
| WITNESS | Incident/evidence preservation and scoped examination | No presumption of guilt, surveillance license, or final adjudication |

**Status caution:** These are planned work lanes and do not replace individual charters or prove a currently active dedicated runtime. THOTH and PTAH have distinct security/evidence mandates; the exact binding force of a verdict must come from the applicable current ratified record. Existing draft manifests remain draft until formally promoted. Shared model provider, runtime, or prompts do not establish independent reviewers.

## 6. Human authority and invited secondary

### Primary Operator mode

The Operator can assign bounded work, inspect findings, authorize acts within their own legitimate powers, suspend activity, and record final disposition. Standing permission for low-risk, reversible local work is possible only through an actual policy with traceable scope; high-risk acts remain per-action gated.

### One invited secondary — three permission tiers

- **Observer:** Read an explicitly approved subset; comment without changing decisions or records.
- **Reviewer:** Issue attributable review on assigned exact matters. Counts as independent only when actual eligibility, conflicts and native provider requirements are satisfied.
- **Delegated Operator:** Complete narrowly scoped time-limited tasks with individualized identity; cannot self-elevate, confer forbidden permissions, or access unrelated private data.

No shared accounts or master credentials. Participant-specific revocation, access expiry and audit trail. Protected branch approvals, consequential credential changes and defined high-risk production actions require genuine separation when policy requires it. Absence of an eligible second person is a **HOLD**, not an excuse to simulate independence with another model.

## 7. One matter, one operating contract

Every consequential unit of work must capture:

~~~yaml
matter_id:
owner:
purpose:
classification:
target:
exact_target_version:
source_references:
evidence_state:
assigned_seats:
source_and_model_provenance:
permitted_actions:
blocked_actions:
review_requirements:
security_findings:
operator_disposition:
authorization_source:
authorization_state:
expiration:
execution_receipt:
verification_evidence:
recovery_or_rollback:
next_checkpoint:
~~~

Lifecycle: **intake -> classify -> assign -> investigate -> specialist review -> human disposition -> authorization -> bounded execution -> verification -> receipt -> closure**. For a read-only advisory workflow, later steps may be inapplicable and must be labeled as such.

Preserve disagreements, missing sources, failed review, expired authority, and exact-head drift rather than flattening them. A successful check, visible button, plan status, model output, or connector token is not itself authorization.

## 8. Capability portfolio and immediate service lanes

1. **AI governance and assurance:** Agent permissions, tool boundaries, human approvals, evidence provenance, traceability, revocation, and recovery. Deliver bounded findings and prioritized remediation.
2. **Defensive security review:** Authorized repository/configuration and credential-handling review, access-control inspection, security architecture, and incident evidence. No penetration testing without specific written scope.
3. **Continuity and recovery design:** Dependencies, provider outages, backup/restoration, operational handoff, incident exercises.
4. **Public-source institutional research:** Sourced, non-deceptive research into technology, risks, organizations, policy and procurement requirements, with explicit uncertainties.
5. **Commercial delivery:** Existing Osiris Audit intake, evidence-backed service fulfillment, cost/time accounting, communication and quality review.

Do not represent proposed capability as independently tested, certified, clearance-bearing, deployable for military use, or already contracted.

## 9. High-consequence / active-duty dual-use analysis

The aggregation of AI reasoning, records, access and execution can produce significant risk. Capability exploration is **not** an authorization to operationalize it.

| Potential capability | Permitted study/application | Principal misuse risk | Initial posture |
| --- | --- | --- | --- |
| Information correlation | Authorized reconstruction and defensive research | Invasive profiling | Restrict input and subjects |
| Vulnerability identification | Written-scope defensive assessment | Unauthorized exploitation | Require authorization |
| Automated infrastructure control | Reversible operations and recovery | Cascading changes | Exact-action human gate |
| Behavior analysis | Consented accessibility/service research | Psychological manipulation | Restricted + ethical review |
| Influence/communications analysis | Education, clarity and accessibility | Covert persuasion | No covert influence operations |
| Threat/incident monitoring | Owned/authorized infrastructure | Unauthorized surveillance | Target/asset controls |
| Autonomous coordination | Bounded low-risk administrative work | Authority drift | Strict scopes, expiry and halt |
| Sensitive-data recovery | Authorized restoration | Exposure of protected material | Segregated custody |
| Emergency decision support | Verified logistics/continuity support | Overconfident high-stakes advice | Human domain review |

Potential legitimate government, defense, emergency-management or critical-infrastructure uses: **non-weaponized readiness**, defensive AI assurance, incident records, continuity exercises, vendor/supply-chain dependency assessment, and human-controlled research. These are target sectors, not evidence of recruitment, clearance, operational readiness or institutional endorsement.

**Excluded from the initial operating lattice:** autonomous weapons targeting or engagement; covert monitoring of private citizens; unauthorized access; deceptive recruitment or impersonation; political manipulation; uncontrolled identification/tracking; private intelligence collection outside lawful authorized scope; agent-only high-stakes determinations.

Reviewing risk does not mean undertaking a mission. Future high-consequence changes require lawful scope, accountable sponsorship, qualified independent review and a new explicit authorization process.

## 10. Information classes and safeguarding

- **Public:** Approved releases and general non-sensitive material.
- **Internal:** Ordinary operations and non-public development.
- **Confidential:** Customer, commercial, proprietary, legal and financial material.
- **Restricted:** Credentials, incident evidence and especially private personal or family records.

Restricted material does not belong in public repos, generalized agent context, open demonstrations, recruitment material, or public-service research by default. Connector reachability does not imply permission to copy. Need-to-know, retention, disposal and provenance must be explicitly governed.

## 11. House Ramses participatory development

Develop the secondary institution around consent, human agency, inclusion and accountable research. Possible services: public education, decision-literacy and accessibility support, consented research and feedback, independent evaluation, and resource-light assistance.

Before a pilot, define: responsible human; non-exploitative participant terms; plain-language notice; refusal/withdrawal route; minimally necessary data collection; grievance mechanism; independent review where warranted; separation from sales and sensitive records; crisis/high-stakes referrals where applicable.

Oracle may contribute only through an explicit consented, carefully evaluated person-facing lane. Avoid emotional dependency, misleading authority claims, diagnostic or therapeutic impersonation, and coercive participation. No public launch is established by this blueprint.

Participation must not demand surrender of agency, private data, or independent judgment.

## 12. Phased implementation

### Phase 0 — Source-of-truth and operating-state reconciliation

- Refresh CORE-HUB/cross-repo source mapping; note any unresolved canon conflict.
- Inspect the exact installed/local state of MOPCON, FastAPI runtime, GitHub access and provider bindings.
- Register deployed/available/eligible/advisory/dormant/unknown separately.
- Preserve existing PR/CI/review and release holds.
- Identify one first acceptance matter and safe local fixture.

**Done when:** Another reviewer can reproduce the inventory; no missing observation is mislabeled as live.

### Phase 1 — Secure single-Operator local lattice

- Reuse MOPCON/KHEPRI read-only view and existing terminal entrypoint.
- Authenticate Operator-to-runtime calls and replace unauthenticated plan approvals.
- Persist plans, decisions, traces and rejected actions across restart.
- Bind plan approvals to exact target, digest, actor, policy/version, scope, expiration and nonce.
- Reject unknown node identifiers and mismatched targets; guard replay and duplicate execution.
- Implement safe local pause, revocation, backup and restore exercises.
- Add one governed read-only GitHub assessment-to-report demonstration.

**Done when:** One bounded task is traced from intake through Operator decision, safe execution (if needed), verification and durable receipt without uncontrolled permissions.

### Phase 2 — Revenue-backed operation

- Protect current Osiris $149 offer and delivery terms.
- Validate an authorized, real end-to-end case before claiming fulfillment readiness.
- Keep database, application release, independent PR review and production approval separate.
- Collect actual costs, delivery effort, receipts and customer outcomes.
- Package the first repeatable governance/continuity report and sanitized case study.

**Done when:** Verified revenue-producing service delivery requires no undocumented manual reconstruction.

### Phase 3 — Invited secondary

- Add one individual identity with Observer/Reviewer/Delegated Operator projection.
- Demonstrate restricted-data separation, reviewer independence and revocation.
- Validate separation of duties against actual GitHub/provider controls.

**Done when:** A secondary participates with an attributable trail and without acquiring general Operator power.

### Phase 4 — Participatory service and research

- Establish appropriate program governance and funding separation.
- Run a genuinely optional, consented small pilot with feedback and complaint paths.
- Independently assess outcomes, publish only appropriately reviewed aggregate evidence.

**Done when:** Observed beneficiary value and retained participant agency justify expansion.

## 13. Cashflow and team-supported R&D projection

Expand against **collected** cashflow, verified obligations and reserve policy—not speculative contracts. First hires may be fractional contractors. No permanent staffing commitments prior to sustainable receipts.

A purely illustrative mature-month envelope at **$75,000 gross collected revenue**:

| Planned use | Allocation | Amount/month |
| --- | ---: | ---: |
| Delivery specialists and contractors | 35% | $26,250 |
| Research and development | 15% | $11,250 |
| Independent review/accountability | 10% | $7,500 |
| Infrastructure, security and compliance | 10% | $7,500 |
| Operator compensation, taxes, capital and reserves | 30% | $22,500 |

**Not a forecast or profit calculation.** The last category must be broken into separate tax, payroll, cash and reserve budgets before obligations are incurred. Staffing only after unit economics, obligations, insurance, legal/contract terms and recovery readiness are evidenced.

Suggested funded disciplines: runtime engineering; security/infrastructure; operations/delivery; research/evaluation; independent governance/audit. Priority R&D: verifiable action authorization, provenance, independent review, resilient local continuity, privacy, consent and explainable operator interfaces.

## 14. Acceptance and failure tests

| Test | Minimum required observation |
| --- | --- |
| A1 Restart | Approved durable matter/receipts survive process restart |
| A2 Caller | Unknown or unauthenticated actor cannot approve/execute |
| A3 Separation | Specialist cannot exceed scope or access restricted data |
| A4 Integrity | Changed SHA/digest invalidates dependent authorization |
| A5 Independence | Shared-model output never counts as eligible human approval |
| A6 Isolation | C0 retains only expressly supported local functions |
| A7 Revocation | Withdrawn capability/secondary access stops functioning |
| A8 Privacy | Restricted records do not leak into public/client artifacts |
| A9 Production | Local action cannot bypass platform/GitHub release gates |
| A10 Recovery | Backup restore verifies integrity and preserves conflict evidence |
| A11 Delivery | One real authorized intake-to-delivery trail is reproducible |
| A12 Stop | Expired, revoked or invalid authorization fails closed with receipt |

Do not represent these tests as passing until execution evidence exists.

## 15. Stop conditions

HOLD or block affected operations for unclear authority; wrong/unverified target; missing mandatory independent review; unauthorized sensitive data; leaked secrets; stale, altered or replayed authorization; unverified production isolation; unsupported deployment path; evidence-integrity failure; or self-promoted agent authority. Record the reason, affected scope and smallest legitimate recovery action. A hold is not an accusation.

## 16. Live state and implementation evidence at design freeze

This design is informed by **repository inspection on 2026-11-01**; it is not a complete local runtime or deployment audit.

- CORE-HUB CANONICAL_SOURCES.md establishes governance and implementation repository roles.
- CORE-HUB ARCHITECTURE.md and MASTER_INDEX.md distinguish governance promotion from runtime implementation.
- CORE-HUB INTER/OUTER draft materials describe exact-target, review, and permission boundaries.
- MOPCON README and T-044/T-045 materials show read-only coordination and a proposal-only local terminal; they expressly do not grant execution, merge or deployment powers.
- Current mirrornode-agent-runtime/app/main.py supports proposed/approved/executed plans; direct agent execution is disabled; plan records are in-memory; the approval routes in inspected code do not authenticate the caller. Operational security therefore remains incomplete.
- Platform governance documentation separates preview/production risk, database migration, and release; published status snapshots may be stale.
- Observed repository state: platform PR #54 merged at f9365b801ecf0fdb7c4bb94758a5d7e99e334d31; platform PR #56 open at e3b4b0abe5379aa1cb136d609a45cecf9666e5ad with review/release HOLD; platform PR #58 open/draft at 4dee2a54ba0800e59a83ccfb6570fa459affcbb9; CORE-HUB PR #68 open/draft at 04c2294b0ee4ac974d7c53ead6ef7d5aed7d96e7.
- Local process health, current Vercel state, current GitHub approvals/checks, actual second-person eligibility, full provider reachability and a complete Council integration demonstration were **not** independently established by this design review.

## 17. Immediate execution order

1. Preserve v0.1 as an accepted **pre-canon** design baseline.
2. Reconcile local/runtime/evidence state against CORE-HUB source rules.
3. Develop MOPCON -> runtime authenticated proposal/decision/receipt path on an isolated branch.
4. Demonstrate a read-only, authorized GitHub review-to-report workflow.
5. Protect outstanding Osiris delivery, employment/income and existing release holds.
6. Send the implemented slice through the applicable THOTH/PTAH and eligible independent review.
7. Seek separate explicit approvals for any canon promotion, execution permission, PR merge, production change or public service activation.

## 18. Immutable disposition boundary

**Operator decision on 2026-11-01:** Freeze the design baseline as accepted for planning and controlled future engineering work.

**Not decided here:** Final governance ratification; named node promotions; execution authority expansion; credential custody changes; incorporation of House Ramses; customer/participant consent; public release; institutional engagement; independent reviewer eligibility; merge; deploy; production migration.

**Change-control rule:** Subsequent designs must identify this exact version, carry a rationale and delta, preserve the original, and pass the relevant review gates. Approval of the design is never retroactive authorization for a downstream action.

---

## Source index (repository-native)

- MIRRORNODE-CORE-HUB: CANONICAL_SOURCES.md; ARCHITECTURE.md; GOVERNANCE.md; MASTER_INDEX.md; docs/continuity/OPERATOR_CONTINUITY_LEDGER_V0_1.md; docs/governance/INTER_OPERATOR_HUMAN_OVERSIGHT_COMMAND_MANUAL_V0_1.md; docs/governance/OUTER_AGENT_LATTICE_OPERATIONS_CHARTER_V0_1.md; docs/integration/MICC_V0_1.md.
- mirrornode-operator-console: README.md; docs/T-044_COUNCIL_REVIEW_ORCHESTRATION.md; docs/MOPCON_FOUNDATIONAL_NODE_TERMINAL_V0_1.md; docs/KHEPRI_PRODUCT_SPINE_V1.md.
- mirrornode-agent-runtime: app/main.py and agents role prompts.
- mirrornode-platform: GOVERNANCE.md; ARCHITECTURE.md; docs/operations/DEPLOYMENT_GATES_AND_RELEASE_SEQUENCE.md.
- mirrornode-workspace: MIRRORNODE_AGENT_STACK_MANIFEST_v0_1.md; PTAH_SECURITY_AUTHORITY_MANIFEST_v0_1.md; THOTH_VALIDATION_MANIFEST_v0_1.md; THEIA_INTEGRATION_MANIFEST_v0_1.md.

The document is a frozen **design**, not a fabricated record of all components running or all risks resolved.
