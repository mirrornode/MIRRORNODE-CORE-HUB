# Digital Asset & Cryptographic Provenance Horizon — Coordination and Source Reconciliation v0.1

**Prepared:** 2026-11-15 (America/Los_Angeles)  
**Owner of final decisions:** Siseon, Operator  
**Coordinator:** THEIA  
**Status:** PROPOSED / NONCANONICAL / RESEARCH-ONLY / NOT RATIFIED  
**Scope:** NFT, cryptographic evidence, optional blockchain anchoring, wallets, crypto payments and tokenized economics  
**Purpose:** One source-linked, reviewable register of facts, responsibilities, handoff/receipt state, dependencies, and the next decision gates.

> This document is a research coordination candidate in a separate draft PR. It does **not** promote canon, change existing agent authorities, amend CORE-HUB PR #71, resolve Platform PR #56 or issue #61, activate a node, grant wallet/custody authority, or authorize implementation, external execution, minting, deployment, publication, or live payment movement.

## 1. Authority and source-of-truth map

Use the existing precedence documented in CORE-HUB's 2026-08-13 source-scope reconciliation: (1) explicit Operator disposition, (2) ratified CORE-HUB Council/canon record, (3) current merged CORE-HUB governance/source maps, (4) current dedicated-repository evidence, (5) draft workspace records, (6) historical evidence, then (7) conversation summaries. Preserve contradictions and provenance rather than silently overwrite them.

| Domain | Governing source or owner | Boundary |
| --- | --- | --- |
| Enterprise governance / source precedence | CORE-HUB, GOVERNANCE.md, CANONICAL_SOURCES.md; promotion register MASTER_INDEX.md | A draft PR is not canon. Promotion requires Ptah evaluation and explicit Operator ratification. |
| Live code, contracts and test receipts | Source-owning repositories, exact immutable commits, actual run artifacts | Repository code does not prove deployment, current security, or operational authority. |
| Cross-repository discovery | mirrornode-index, REPO_MAP and named reconciliation files | Index/snapshot status does not override CORE-HUB governance. Historical REPO_MAP remains stale until refreshed. |
| Case/event system of record | MIRRORNODE-controlled backend was selected as an intended authoritative record in prior Operator planning; design/implementation not independently verified here | ChatGPT, Lattice, MCP and council summaries are interfaces/projections, not the authoritative event store. Confirm the exact backend, schema, retention and ownership before operational reliance. |
| Provenance validation | The governed @mirror source/rule referenced by CG-0032 | Matching SHA-256 deterministic-JSON digest proves only payload/digest correspondence under the declared algorithm; **not** actor identity, truth, freshness, consent, authority or approval. |
| External assistant and plugin surfaces | CG-0032 read-only MCP projection contract; separate CG-0033 implementation gates | All output classes and fields require prior disclosure review; new attachment, writes or deployment require distinct authorization. |
| Research work tracking | This proposed ledger, a separate versioned handoff/receipt record, and THEIA reconciliation | Acknowledgements, actual dispatch, specialist returns, tests, review, and approval must remain distinguishable. |

For this horizon, the approved activity is **bounded research and documentation**. Production, mainnet minting, live payments, custody/transmission, exposure of customer data, private-key sharing, and external execution of a digital-asset workflow remain excluded. New authorization would be needed even if a design appears feasible.

## 2. Evidence classifications and known technical observations

Use OBSERVED, REPORTED, INFERRED, PROPOSED, BLOCKED, UNKNOWN and DECISION_NEEDED; include timestamp, source, scope and exact revision for each claim. A source file is not an executed test, a simulation is not a live node return, and a historical proposal is not implementation.

**OBSERVED through a connected GitHub read on 2026-11-15:**

- CORE-HUB PR #71 (ChatGPT constellation/Lattice): open, **draft**, unmerged; head **062ad9073991ee34fad5a69ed0aeced0b2a8f4b6**; five proposal/handoff documents; zero submitted reviews at inspection. This is a separate noncanonical product proposal, not a digital-asset implementation approval.
- Platform PR #56 (guest audit purchases schema): open, unmerged; head **e3b4b0abe5379aa1cb136d609a45cecf9666e5ad**; sampled/full returned reviews classified COMMENTED and not APPROVED. Maintain the separate exact-head replay/independent approval and release hold; mergeable flag does not override review gates.
- Platform issue #61 records the controlled Node 20-to-24 transition, with isolated tests and nonproduction runtime proof required before any new release. Issue existence is not successful migration.
- mirrornode/tests/test_agents.py on default branch contains a test_nft_lane_stub() with mocked/comment-only transaction and a trivial always-true assertion. **This is stub scaffolding, not demonstrated minting.**
- mirrornode-platform/app/osiris/rotan_routes.py on default branch implements a SHA-256 linked sequence of ROTAN conversation records with Supabase calls. Its compute_merkle_hash naming does not establish an actual Merkle tree or independently verified ledger runtime.

**REPORTED / historical recovery targets, not verified current implementations:** Mirror Mirror/Reflection, MirrorOracle, VoiceOracle, HederaNFTMint, RayDelegator, the past Hedera testnet design, limited editions and ERC-1155 explorations, IPFS/Arweave options, ROTAN-Q/Attestation Node concepts, prior Ed25519 proof work, and 1-of-1 or limited dossiers. Recover precise repositories, commits, contracts, test receipts and rights documentation before promoting any implementation claim.

**UNKNOWN:** Which historical NFT components are currently implemented, deployed, tested, owned or licensed; key custody; merchant/processor architecture; economic rights; actual customer use; authenticated return from each research assignee; operational @mirror validator connection; present independent THOTH verdict on this proposal.

## 3. Who knows what / who can and should act

These rows are **research assignments and evidence-access summaries**, not declarations of live agent connectivity, newly ratified powers, or receipt of this packet. Separate a named node's standing governance responsibilities from the provider or assistant used to obtain advisory work.

| Seat / interface | Information evidenced in this reconciliation | Can / should do within the research scope | Cannot infer or perform | Receipt / result for **this** horizon |
| --- | --- | --- | --- | --- |
| Siseon / RIO (Operator directive source) | Authorized bounded research charter and five separately judged horizons | Set priorities, resolve cross-role conflicts, decide scope and later gate outcomes | Research authorization is not production or mainnet authorization | Operator charter RECEIVED in this THEIA conversation; final dispositions pending |
| THEIA | Current charter and connected GitHub observations; reconciliation and source maps | Maintain source register, build request packets, track evidence/freshness, compare returns, escalate contradictions, prepare decision options | No self-promotion of canon, fabricated approvals, security verdicts, or funding commitments | This coordination draft PREPARED; specialist receipt not assumed |
| @mirror | CG-0032 narrow digest semantics and planned evidence continuity; actual validator connection not verified | Recover provenance and historical implementation records, annotate source links and confidence, distinguish exact digest matching from truth | Cannot claim to know a missing source, grant permissions, or act as independent security approver | ASSIGNED / NOT CONFIRMED DELIVERED |
| Merlin | CORE-HUB source-scope reconciliation supports planning, dependency mapping, sequencing and orchestration advice | Coordinate architecture alternatives and legal research questions; map dependencies, assignment order, cost and approval gates | Not the dispatcher by name; no canon control, minting, custody or execution authority | ASSIGNED / NOT CONFIRMED DELIVERED |
| Claude (architectural advisor) | Candidate off-chain/Hedera/EVM review scope is defined | Draft ADR, trust boundaries, artifact schema, minimal synthetic prototype, rights and failure model, commercial assumptions | A Claude provider reply is **not automatically** a formal PTAH disposition | ASSIGNED / NOT CONFIRMED DELIVERED |
| PTAH (architecture/custody authority) | Standing structural role and canon-promotion gate documented; no current digital-asset review shown | Independently evaluate candidate architecture and custody implications **when separately submitted/authorized** | No unreviewed keys, mainnet deployment, self-authorization, or automatic adoption of a provider opinion | FUTURE FORMAL REVIEW; NOT RECEIVED |
| Perplexity / HERMES research seat | Hermes advisory evidence/routing scope is documented; previous unrelated suite advisory intake is not a digital-asset legal return | Research Washington/US securities, FinCEN, licensing, tax, copyright, privacy, sanctions, payments, and source dates; route bounded evidence | Not legal counsel, not regulator, not THOTH, not a substitute for licensed professional review; no autonomous dispatch authority inferred | ASSIGNED / NOT CONFIRMED DELIVERED |
| THOTH | Independent security verdict boundary is documented; no horizon-specific decision seen | Review complete trust-boundary/failure model independently, return findings, residual risk, stop conditions and evidence requirements | Must not be collapsed into Hermes research, Claude implementation or THEIA synthesis | DEPENDS ON ARCHITECTURE PACKET; NOT RECEIVED |
| Grok / Gemini | Historical contribution and prospective commercial/UX roles are known from other workstreams | Remain available as **unassigned candidates** for later pricing, UX or adversarial assessment if separately tasked | No automatic participation, access, authority or completed review | NOT ASSIGNED |
| Osiris, ROTAN, House Ramses, Lattice | Business/system context exists; actual integrations are not proved by conceptual linkage | Owners may later furnish bounded interfaces, synthetic scenarios and evidence under separate approval | No automatic customer-data access, marketplace activation or family-wallet features | IMPACT-ANALYSIS ONLY |

**Dispatch discipline:** Preparing or pasting a packet in THEIA's conversation does not prove delivery to @mirror, Merlin, Claude, Hermes, PTAH or THOTH. A returned user-supplied transcript is REPORTED until attributed and source-linked. Never equate node identity, implementation repository, provider account, runtime eligibility, operational instance, received packet, authorized action and formal verdict.

## 4. Requested work and dependency order

1. **THEIA / @mirror recovery:** Collect exact source paths and immutable revisions for historical Hedera/NFT/provenance work, record statuses, compile contradictions and inaccessible sources. Do not update existing PRs while doing this.
2. **Merlin + Claude architecture:** Produce comparative ADR for signed off-chain evidence, Hedera-native anchoring/issuance, and EVM-compatible approach. Specify privacy, canonical artifact record, human-signing/consent boundaries, rights, fees, lifecycle, idempotency, revocation/supersession, failure handling and a synthetic off-chain first slice. Merlin coordinates; Claude authors candidate design; neither supplies final PTAH authorization by default.
3. **Perplexity / HERMES source research:** Produce primary-source, date-stamped issue map on federal/Washington laws and facts, with activity, jurisdiction, source, uncertainty, professional reviewer and release blocker. Research is issue-spotting, not a legal opinion. Explicitly identify counsel and CPA decisions before commercial or financial operation.
4. **THOTH security input:** Once architecture artifacts are frozen to a version, independently inspect identity, privacy/correlation, signature and key custody, wallet recovery, metadata durability, chain outages, duplicate execution, transfer disputes, failed issuance and rollback limitations. Return independent disposition; **no execution**.
5. **PTAH / formal architecture:** A selected candidate goes to PTAH only after a separate Operator decision to commission that formal review. Do not pre-mark a provider report as PTAH-approved.
6. **THEIA / Siseon decision:** Reconcile independently attributable returns against costs, privacy, evidence, revenue potential and existing Osiris gates. Siseon records separate PROCEED / REVISE / DEFER / REJECT outcomes for evidence anchoring, NFT artifacts, wallet integration, crypto payments and tokenized economics.

**First recommended research slice:** a signed, verifiable **off-chain Osiris evidence credential** using synthetic data, without any required wallet or token. A testnet anchoring comparison is conditional research, not a minting authorization.

## 5. Receipt/knowledge contract: prevent false council completion

Every handoff or return should have these fields at minimum:

- **Identity and channel:** packet_id, request_id, sender, intended recipient/seat, actual channel/provider identity, authentication/attribution evidence.
- **Authority:** Operator directive reference, permitted research scope, prohibited actions, classification, consent/data eligibility, expiration.
- **Source and version:** canonical source references, commit SHA or immutable document version, claimed time, retrieved time, freshness limit.
- **Lifecycle:** PREPARED → TRANSMITTED → ACKNOWLEDGED → IN_PROGRESS → RETURNED → INDEPENDENTLY_REVIEWED → DISPOSITIONED. Use BLOCKED/EXPIRED/REVOKED as separate states. Never skip to TRANSMITTED by drafting.
- **Return:** exact artifacts, evidence links, tests personally run versus supplied, assumptions, contradictions, completeness, unresolved questions, reviewer identity and named next gate.
- **Verdict/permissions:** distinguish research recommendation from formal PTAH custody review, independent THOTH security verdict and Siseon authorization. No synthesized text can impersonate any of these.

Cross-provider continuity must be **receipted**, not inferred from an account, open browser tab, shared document, conceptual name or cached memory. Every time a return is ingested, record what that seat demonstrably knows and what remains undisclosed to it.

## 6. Source hierarchy conflicts and related workstream holds

- **Do not modify CORE-HUB PR #71.** This new research record is adjacent to its proposed ChatGPT suite, not an amendment or endorsement.
- **Do not modify Platform PR #56.** Schema-reconciliation approval, exact-head replay, and release gates are independent.
- **Do not modify issue #61/runtime settings or claim Node 24 readiness.**
- **Do not promote into MASTER_INDEX.md** unless the formal Ptah evaluation and explicit Operator ratification are evidenced and recorded.
- **Keep separate workstreams:** public commercial/client experiences; internal canonical/operational systems; family and child-facing worlds; public-service/community work; personal finance; and employment.
- **MCP is read-only by the current accepted CG-0032 definition.** It cannot become a raw private-ledger gateway, source of approvals or vehicle for token transactions by name.
- **Privacy:** do not put client evidence, identities, children’s information, personal financial data, confidential artifacts, secrets, or linkable hashes/identifiers onto an immutable public ledger without separately reviewed design/consent/legal gates. Prefer bounded commitments and off-chain revocable access.
- **Economic realism:** separate cryptographic value (integrity proof) from collectible ownership, legal title, copyright license, resale, financial rights and customer demand. Tokenized profit or revenue claims remain DEFERRED research, not product copy.

## 7. Open decision queue (not approved)

| Horizon | Recommended next step | State |
| --- | --- | --- |
| Off-chain evidence receipt | Architectural specification and synthetic acceptance harness | RESEARCH PROCEED (not implementation approval) |
| Optional blockchain anchoring | Compare against off-chain baseline, including recurring cost, privacy and operational dependence | RESEARCH / DECISION NEEDED |
| NFTs and participant credentials | Clarify tangible use, transfer rights, user experience and commercial interest | RESEARCH / DECISION NEEDED |
| Wallets and custody | Compare wallet-optional and regulated third-party arrangements; identify counsel/security dependencies | DEFER OPERATIONAL DECISION |
| Crypto payments | Legal and provider due diligence before any processing integration | DEFER OPERATIONAL DECISION |
| Fungible tokenomics / revenue participation | Securities/consumer implications and credible buyer-use case first | DEFER OPERATIONAL DECISION |

## 8. Source register (observed or governing at drafting)

- Governance: https://github.com/mirrornode/MIRRORNODE-CORE-HUB/blob/main/GOVERNANCE.md
- Canonical sources: https://github.com/mirrornode/MIRRORNODE-CORE-HUB/blob/main/CANONICAL_SOURCES.md
- Promotion gate: https://github.com/mirrornode/MIRRORNODE-CORE-HUB/blob/main/MASTER_INDEX.md
- Registry caution: https://github.com/mirrornode/MIRRORNODE-CORE-HUB/blob/main/AGENTS.md
- Naming/source precedence: https://github.com/mirrornode/MIRRORNODE-CORE-HUB/blob/main/docs/continuity/NAMING_AND_SOURCE_SCOPE_RECONCILIATION_2026-08-13.md
- Current registry dimensions: https://github.com/mirrornode/MIRRORNODE-CORE-HUB/blob/main/docs/continuity/AGENT_REGISTRY_EVIDENCE_SNAPSHOT_2026-08-13.md
- CG-0032: https://github.com/mirrornode/MIRRORNODE-CORE-HUB/blob/main/docs/mcp/MCP_SURFACE_CONTRACT_V0_1.md
- Suite draft at inspected head: https://github.com/mirrornode/MIRRORNODE-CORE-HUB/pull/71 (head 062ad9073991ee34fad5a69ed0aeced0b2a8f4b6)
- Platform hold: https://github.com/mirrornode/mirrornode-platform/pull/56 (head e3b4b0abe5379aa1cb136d609a45cecf9666e5ad)
- Node transition: https://github.com/mirrornode/mirrornode-platform/issues/61
- NFT stub: https://github.com/mirrornode/mirrornode/blob/main/tests/test_agents.py
- ROTAN hash-chain source: https://github.com/mirrornode/mirrornode-platform/blob/main/app/osiris/rotan_routes.py

**Audit boundary:** These are repository links and snapshot observations, not receipts for execution, runtime health, access to every historical branch, legal approval, outside-specialist knowledge or source-of-truth promotion.

## 9. Next controlled handoff

THEIA: publish this file only as a separate reviewable draft PR. Assign packet IDs for @mirror, Merlin, Claude, Perplexity, and conditional THOTH review. Keep all unacknowledged packets PREPARED. Request source-linked returns; compare evidence freshness and contradictions before escalating. Siseon determines any formal review, canon promotion, implementation, client promise, payment commitment or publication.
