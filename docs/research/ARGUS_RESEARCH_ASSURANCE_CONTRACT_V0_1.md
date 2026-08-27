# MIRRORNODE / ARGUS — Research Assurance Contract v0.1

**Status:** PROPOSED / UNEVALUATED

## 1. Core rule

ARGUS is an **evidence-production pipeline**, not an authority pipeline.

Providers, models, agents, repositories, search systems, documents, and external sources may contribute evidence, claims, interpretations, and recommendations. None may self-certify truth, policy, canon, reconciliation eligibility, implementation authorization, or governance disposition.

Research output remains a working record until a separately governed reconciliation path accepts a bounded claim or disposition.

## 2. Primary failure mode

ARGUS MUST defend against **authority laundering**: the transformation of an articulate or apparently well-supported provider output into an implicit truth claim, recommendation, approval, or canonical fact without an explicit evidence and governance boundary.

The system MUST preserve four non-interchangeable artifact classes:

1. **ResearchEvidence** — attributable record of what a source says or what an instrument observed.
2. **Interpretation** — reasoned synthesis of evidence, assumptions, ambiguity, alternatives, and uncertainty.
3. **Recommendation** — proposed action or option ranking with rationale, tradeoffs, reversibility, and confidence.
4. **GovernanceDisposition** — accept, reject, defer, request-more-evidence, promote, or otherwise govern a claim. This class is produced only by an authorized governance path.

A transition between classes requires an explicit derivation event. No object may silently change class.

## 3. Minimum pipeline

`INTAKE -> ACQUIRE -> EXTRACT -> CORROBORATE -> INTERPRET -> RECOMMEND -> ADVERSARIAL_REVIEW -> RECONCILIATION_SUBMISSION`

### 3.1 Intake

Required: research question, scope, decision context, risk class, cutoff time, exclusions, source policy version, disagreement-policy version, and declared poisoning surface.

Intake may not assert the answer or choose policy.

### 3.2 Acquisition

Acquisition MUST produce immutable or content-addressed captures with retrieval metadata. Search rank, vendor status, provider identity, or model confidence MUST NOT be treated as source quality or authority.

### 3.3 Atomic claim extraction

Material factual assertions MUST be decomposed into atomic claims with exact evidence references. Fact and inference MUST remain distinct.

### 3.4 Corroboration

ARGUS MUST build a claim-to-source graph and group shared-origin material into independence clusters. Syndicated articles, wire copies, shared datasets, common press releases, shared analyst notes, or provider paraphrases MUST NOT be counted as independent corroboration.

### 3.5 Interpretation

Interpretation MUST identify assumptions, causal or semantic model, alternatives, uncertainty, and evidence boundaries. It may not present inference as evidence.

### 3.6 Recommendation

Recommendations MUST identify objectives, constraints, tradeoffs, reversibility, blast radius, rollback path, monitoring signals, and a non-recommendation alternative where meaningful. A recommendation cannot bind governance.

### 3.7 Adversarial review

The review stage MUST challenge provenance completeness, claim support, source independence, contradiction handling, injection resistance, poisoning resistance, and authority leakage. Suspicious evidence remains inspectable but quarantined from synthesis until cleared.

### 3.8 Reconciliation submission

The output is a frozen packet and review record. Submission does not promote the packet into canon. The reconciliation authority may reject, defer, request evidence, accept a bounded claim, or refuse promotion.

## 4. Evidence record requirements

Every evidence-bearing artifact MUST include, where applicable:

- stable `evidence_id`, `packet_id`, version, immutable content hash, and canonical serialization identifier;
- original URI or source identifier;
- publisher/author where known;
- publication time, retrieval time, jurisdiction, and access conditions;
- exact locator: page, section, paragraph, table, timestamp, repository commit/path/line range, or dataset row range;
- raw capture identifier, MIME type, normalization procedure, raw hash, and normalized hash;
- acquisition activity: tool/provider/model/version, query or prompt hash, system/policy version, permissions, acting identity, and execution time;
- transformation lineage: OCR, translation, summarization, chunking, embeddings, extraction prompts, and parent hashes;
- source classification, volatility, adversarial-risk level, licensing, and retention restrictions;
- validation state: capture verified, locator verified, quote verified, duplicate-cluster assignment, integrity result, reviewer identity, and review timestamp;
- redaction map when sensitive material is removed.

Corrections MUST create successor records. Evidence records are append-only.

## 5. Source-quality model

ARGUS MUST use a vector profile rather than one opaque trust score. At minimum:

- proximity;
- verifiability;
- specificity;
- integrity;
- competence;
- incentive exposure;
- independence;
- recency;
- contestability;
- attack surface.

A tiering overlay MAY classify source types for operational convenience, but provider/model identity MUST remain metadata rather than a truth predicate.

Primary sources can prove that an actor made a statement or performed an action; they do not automatically prove every broader claim contained within the source.

## 6. Independence rules

ARGUS MUST compute evidence diversity by origin and dependency, not source count.

Different providers are not independent evidence when they rely on the same source corpus, upstream analyst conclusion, retrieval channel, prompt template, dataset, or common origin.

For high-impact material claims, require either:

- two provenance-independent corroborating paths; or
- one directly inspectable primary artifact with an explicit single-source limitation.

If neither is available, the claim remains provisional or contested.

## 7. Disagreement protocol

Disagreement is a first-class artifact.

For material conflicts:

1. freeze competing atomic claims and evidence sets;
2. classify the conflict as factual, definitional, temporal, methodological, normative, forecast, recommendation-level, or scope-related;
3. determine whether the conflict is genuine contradiction or differing scope/time/model;
4. compare evidence-quality vectors and provenance independence rather than provider status, eloquence, confidence score, or vote count;
5. emit a `DisagreementRecord` with strongest case for each position, missing discriminating evidence, materiality, and affected decision;
6. assign one disposition: `resolved`, `bounded-divergence`, `insufficient-evidence`, `escalate-human-review`, or `blocked`;
7. preserve minority and rejected interpretations with reasons.

No materially contested claim may be rendered as settled.

## 8. Injection and poisoning controls

All retrieved or uploaded content is **untrusted evidence payload**, never executable instruction.

Required controls:

- strict separation of instruction channels and evidence channels;
- non-executable rendering of quoted evidence;
- quarantine of content attempting to alter system instructions, authorization, browsing behavior, tool use, secrets, memory, records, or publication state;
- deny-by-default tool actions during acquisition and analysis;
- fetch-and-freeze capture before synthesis on material claims;
- hashes for raw capture, extracted claim set, prompt/policy versions, and packet outputs;
- duplicate-narrative and common-origin detection;
- domain impersonation, citation-loop, hidden-Unicode, prompt-like payload, and anomaly checks;
- adversarial review attempting to induce instruction following, citation fabrication, source-independence collapse, or certainty inflation;
- credential compartmentalization;
- human review for sensitive, irreversible, legal, financial, safety, reputational, or canonical-impact conclusions.

Research agents MUST NOT receive standing write access to canon, governance registries, system prompts, or authority policy merely because they participate in research.

## 9. Provider independence

No provider has standing epistemic or governance authority by identity alone.

Provider-specific metadata MUST be recorded for reproducibility and may inform competence, incentives, or failure analysis. It MUST NOT elevate evidence tier or grant authority.

Retrieval and interpretation providers SHOULD be swappable. The evidence graph MUST remain interpretable when one provider's model-generated outputs are removed.

Unavailable capability MUST be represented as unavailable rather than silently substituted.

## 10. Submission gate

A packet is eligible for canonical reconciliation only when all applicable conditions are satisfied:

- question, scope, decision class, and evidence cutoff are frozen;
- all material factual assertions map to exact evidence records;
- unsupported assertions are removed or explicitly typed as assumptions;
- raw captures, extracts, transformations, and packet artifacts have verified immutable identifiers and hashes;
- each material source has a source-quality profile and independence-cluster membership;
- corroboration requirements are met or an explicit provisional/single-source limitation exists;
- evidence, interpretation, recommendation, limitation, disagreement, and governance disposition are separately typed and rendered;
- all material disagreements have records and non-misleading dispositions;
- injection/poisoning screening passes, with suspicious material quarantined and documented;
- the packet is reproducible from frozen inputs and recorded method/tool/prompt/policy versions;
- at least one reviewer who did not author the synthesis validates material source locators, claim mapping, scope, and independence classification;
- no implied authority grant, implementation authorization, canon promotion, or merge authority appears in the packet;
- the exact frozen packet and review record are submitted together.

Absence of proof for a required condition is a failed gate, not a warning.

## 11. Agent topology

ARGUS coordinates the research contract. Provider/model lanes are assignments, not permanent authority classes.

Recommended v0.1 roles:

- discovery/retrieval lanes produce candidate evidence and leads;
- extraction lanes produce atomic claim candidates;
- a graph coordinator maintains claim/evidence relationships and independence clusters;
- adversarial lanes challenge contradiction, poisoning, and common-mode failure;
- a reconciliation coordinator packages, but does not promote, the frozen record.

No lane may self-certify the result it materially authored.

## 12. ResearchReadinessAttestation

The final machine attestation MUST say only whether a frozen research packet is **eligible for reconciliation** under the named contract version. It MUST NOT state that the recommendation is adopted, the claim is canonical, or the research lane has governance authority.

## 13. v0.1 acceptance tests

ARGUS v0.1 MUST pass:

1. **Typed-artifact test** — evidence, interpretation, recommendation, and governance disposition remain structurally distinct.
2. **Claim-traceability test** — 100% of material factual claims resolve to exact locators and evidence hashes.
3. **Reproducibility test** — a separate reviewer regenerates the evidence manifest/claim ledger from frozen inputs with matching identifiers.
4. **Provider-neutrality test** — removing one provider's model outputs does not collapse the evidence logic.
5. **Independence test** — shared-origin materials collapse into one corroboration cluster.
6. **Single-source test** — material single-source claims remain visibly provisional unless policy explicitly permits otherwise.
7. **Conflict test** — credible contradiction generates a disagreement record rather than silent selection or averaging.
8. **Injection test** — hostile instructions inside evidence have no control effect and are quarantined.
9. **Poisoning test** — coordinated near-duplicate sources do not inflate corroboration without independent origin.
10. **Mutation test** — changing source capture, extraction rule, model version, prompt, or policy version invalidates downstream packet identity as required and triggers re-review.
11. **Boundary test** — a recommendation cannot create a governance disposition, authorize implementation, publish a canonical record, or modify canon.
12. **Exact-subject test** — reconciliation blocks when the reviewed packet differs from the submitted immutable packet.
13. **Fail-closed test** — missing provenance, failed validation, unresolved material conflict, or incomplete review blocks submission.

## 14. Non-grants

This contract grants no governance-registry membership, dispatch authority, merge authority, repository permissions, constitutional standing, credential access, financial authority, legal authority, canon-write authority, or autonomous release authority.
