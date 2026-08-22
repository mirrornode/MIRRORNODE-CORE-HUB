# MIRRORNODE System Review — 2026-08-22

**Status:** review artifact / proposal branch  
**Branch:** `proposal/mirrornode-00-dossier-v0-1`  
**Authority effect:** `NONE`  
**Companion dossier:** `canon/dossiers/2026-08/MIRRORNODE-00-2026-08-22.md`  

## Review objective

Assess whether MIRRORNODE's current documentation, verification, governance, and operator surfaces can support a coherent system dossier without silently promoting historical records, test results, model opinions, or repository metadata into stronger claims than the evidence supports.

This review is broad but not exhaustive across every repository. Repositories not inspected beyond inventory are explicitly marked as such in MIRRORNODE-00.

## Overall disposition

**SYSTEM COHERENT / MATERIAL OPEN CONDITIONS REMAIN.**

The architecture is substantially more legible than earlier generations because current records increasingly separate governance, runtime, evidence, review, interpretation, projection, and Operator disposition.

No system-wide merge/deployment/canon clearance is implied by this review.

---

## SR-01 — Historical runtime truth is now correctly marked historical

**Severity:** informational / previously high drift risk  
**State:** CLOSED AT DOCUMENTATION LEVEL

`SYSTEM_CONTRACT.md` still contains the April 28 Lucian-centered runtime registry and `/dispatch` execution model, but it now opens with an explicit historical-runtime notice dated 2026-08-13 explaining that the runtimes changed and the embedded registry must not be used as current governance without reconciliation.

This is the correct pattern: preserve historical evidence without deleting it, but block silent inheritance into present authority.

**Carry-forward rule:** all similar historical “ground truth” documents should acquire equivalent supersession/reconciliation notices when their runtime assumptions cease to be current.

---

## SR-02 — Canon index contains stale authority/presentation language

**Severity:** P2 documentation/governance ambiguity  
**State:** OPEN

`canon/INDEX.md` is last updated 2026-06-01 and still declares `Authority: Desktop Commander + Oracle`, while current governance and review architecture are materially more nuanced.

It also describes canon as uniformly “enforced reality,” which is too strong for a repository that now deliberately preserves historical artifacts, pre-canon proposals, and evolving governance matters.

**Recommendation:** do not patch this opportunistically inside the MIRRORNODE-00 proposal. Open a bounded canon-index reconciliation after the new dossier and current governance authority are reviewed, so the index can be corrected against an approved source rather than another ad hoc summary.

---

## SR-03 — Review claim semantics are now explicit enough to prevent common clearance drift

**Severity:** positive control  
**State:** ESTABLISHED AS PROPOSED DOCTRINE

The current review-memory work distinguishes:

`SCHEMA_VALID → SEMANTIC_VALID → TEST_SUITE_PASS → ADVERSARIAL_PROBES_PASS → EXACT_HEAD_REVIEWED → INDEPENDENT_EXACT_HEAD_REVIEWED → CONSTITUTIONALLY_CLEARED → MERGE_AUTHORIZED`.

This directly addresses repeated historical drift where “green,” “reviewed,” or “mergeable” could be read too strongly.

**Recommendation:** this ladder should become a shared vocabulary across Thea, MOPCON, Council packets, and future review templates after governance review.

---

## SR-04 — PR #53 remains the primary proof that test completeness cannot be inferred from test success

**Severity:** P1 learning case  
**State:** RETAINED / HOLD

PR #53 remains open at exact retained head `05d83494527a7318139d5255dd75fb4ff740600c`.

Its repository record reports 47/47 tests passing. Later adversarial self-review found ten missing probe classes whose unsafe examples were accepted.

The correct reconciliation is now preserved:

- `47/47 passing` = true test-suite evidence;
- `therefore adversarially complete` = withdrawn inference.

The branch was not modified merely to store the later learning. That preserves the target as immutable evidence.

---

## SR-05 — CG-0036 review evidence must be reconciled to its live head, not historical heads

**Severity:** P1 governance/review binding  
**State:** OPEN

PR #48 currently points to `3b3dd302b6a4816314a4710385d735ed3959bc40` and its own body states that the current head is not cleared and requires rereview.

Earlier CG-0036 council/reviewer artifacts remain valid historical evidence for the immutable heads they actually reviewed, but they cannot be silently applied to `3b3dd302...`.

**Recommendation:** when Thea's observed-checkout slice exists, CG-0036 should become one of its first real governance targets because the matter already has rich historical review lineage.

---

## SR-06 — Thea is useful, but v0.1 initially overstated several proof claims

**Severity:** P1/P2 verifier integrity  
**State:** CORRECTED WITH OPEN PROOF-DEPTH ITEMS

The full internal review of `mirrornode/theia-core` PR #1 found that the first implementation described some supplied-manifest checks as if they were observed exact-head proof.

Corrections made include:

- `EXACT_HEAD` language narrowed to immutable SHA-form unless checkout is actually observed;
- raw/parsed status language narrowed to supplied path-set agreement;
- strict manifest typing added;
- file-operation vocabulary bounded;
- verification artifact root separated from implementation write scope;
- Oracle endpoint restricted to loopback in v0.1;
- probe-harness error precedence corrected;
- result claim limit made explicit: `SUPPLIED_MANIFEST_SEMANTICS_ONLY`.

Open proof-depth items remain:

1. observed Git checkout/head/base/diff binding;
2. raw Git status parsing inside Thea;
3. cryptographic handoff-scope recomputation/path reconciliation;
4. symlink/tree escape detection;
5. independent exact-head review.

At exact proposal head `1d100d4cfec6153978e8bd3d3af6f78d42d5a1c2`, Thea's own verifier workflow passed. The repository's separate Canon Gate remains failed on the inherited missing-`REPO_MAP.md` baseline.

---

## SR-07 — Thea repository Canon Gate baseline is unresolved, not a Thea test failure

**Severity:** P2 repository-integrity condition  
**State:** OPEN

`theia-core`'s pre-existing Canon Gate requires `REPO_MAP.md`, which is absent from the repository.

The Thea proposal did not delete the file, manufacture a replacement, or weaken the gate.

The failure should be disposed separately as a repository-baseline matter.

**Recommendation:** reconcile whether `REPO_MAP.md` is still normatively required. If yes, reconstruct it from current approved topology rather than historical assumptions. If no, revise the gate through a separately reviewed change.

---

## SR-08 — MOPCON/KHEPRI remains correctly positioned as projection, not authority

**Severity:** positive architectural control  
**State:** PROPOSED THEA PROJECTION / EXISTING KHEPRI PRINCIPLE

MOPCON's KHEPRI direction already states that visibility, presentation gravity, and displayed gates are not authorization.

The new Thea projection proposal extends that by separating:

- observed target state;
- deterministic verification;
- adversarial probe state;
- Oracle interpretation;
- reviewer provenance;
- constitutional state;
- Operator-authorized action.

The first slice is documentation-only and read-only.

**Recommendation:** keep it that way until Thea's response schema and observed-checkout semantics stabilize.

---

## SR-09 — Workflow naming can overstate effect even when job behavior is validation-only

**Severity:** P3 human-interface / operational interpretation risk  
**State:** OPEN LOW-PRIORITY

CORE-HUB documentation PR #54 triggered workflows named `MIRRORNODE Platform Release` and `Lucian Release`.

Inspection of the jobs showed validation steps such as `Verify Charters & Integrity`, `Validate Runtime Release Surface`, and `Validate Lucian Release Surface`; no deployment action was observed in those jobs.

The current behavior does not establish an unauthorized deployment.

However, workflow names can create an incorrect human interpretation of effect.

**Recommendation:** later distinguish validation-only workflows from effect-bearing release/deploy workflows by naming, job summary, or explicit authority-effect metadata.

---

## SR-10 — Repository inventory is broader than reviewed active topology

**Severity:** P2 documentation/inventory risk  
**State:** OPEN / CONTROLLED BY DOSSIER CLASSIFICATION

The GitHub account contains many active, historical, experimental, private-node, product, workspace, and incubation repositories.

Repository names and descriptions are not enough to prove current runtime activation, governance membership, provider identity, or authority.

MIRRORNODE-00 therefore marks uninspected surfaces as `INVENTORIED / NOT REVIEWED`.

**Recommendation:** resist rebuilding a single omniscient repo map from names alone. Update active topology only when a role/repo relationship is evidenced from current governance or observed runtime state.

---

## SR-11 — NIST alignment is useful only when kept as evidence mapping, not certification rhetoric

**Severity:** positive control / external-claims risk  
**State:** CONTROLLED

The current documentation correctly treats NIST AI RMF, the GenAI Profile, SSDF v1.1, SP 800-218A, the v1.2 draft, and CSF 2.0 as engineering/risk references.

It does not claim that Thea or MIRRORNODE is NIST-certified merely because its controls map naturally to those frameworks.

**Recommendation:** future security/NIST packets should use a control-evidence-gap matrix and name which claims are design intent, implemented control, observed evidence, or remaining gap.

---

## SR-12 — Packet generation needs one source spine plus fresh evidence

**Severity:** architectural documentation control  
**State:** PROPOSED IN MIRRORNODE-00

Previous long review cycles repeatedly reconstructed system context independently for different agents/providers. That creates drift even when each packet is individually careful.

MIRRORNODE-00 introduces the rule:

`Packet = MIRRORNODE-00 + fresh target evidence + audience purpose + disclosure boundary + authority question`

This allows tailored packets without pretending the system dossier itself is immutable truth forever.

**Recommendation:** every future packet should declare the source dossier version and its target-specific freshness anchors.

---

# Priority findings

## Immediate / before merge of current proposals

1. Keep Thea PR #1 draft and unmerged pending its open proof-depth slices or explicit scope decision.
2. Keep MIRRORNODE-00 PR proposal-only until its authority/status language is reviewed.
3. Do not use PR #53's 47/47 suite as clearance.
4. Do not apply older CG-0036 reviews to the current PR #48 head without reconciliation.

## Next engineering priority

1. Thea observed checkout binding.
2. Raw Git-status parsing.
3. Handoff scope cryptographic reconciliation.
4. Thea self-run / permanent corpus replay.
5. Independent Thea review.
6. Read-only MOPCON integration.

## Next documentation/governance priority

1. Canon index reconciliation.
2. `theia-core` `REPO_MAP.md` requirement disposition.
3. Active topology inventory based on evidence rather than repository naming.
4. Workflow effect naming/metadata cleanup.

---

# Final assessment

MIRRORNODE does not currently need another broad redesign.

The dominant work is now **proof depth, reconciliation, and controlled projection**.

That is a better problem to have.

The system's most valuable recent change is methodological: contradictions and failed confidence claims are increasingly being retained as first-class evidence rather than rewritten out of the story. Thea's own review defects reinforce that pattern rather than undermine it.

The appropriate posture is therefore neither emergency nor victory lap:

**coherent architecture, material open conditions, bounded next steps.**
