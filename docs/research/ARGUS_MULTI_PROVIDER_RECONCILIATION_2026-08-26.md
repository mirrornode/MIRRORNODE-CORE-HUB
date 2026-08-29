# ARGUS Multi-Provider Reconciliation — 2026-08-26

**Status:** TWO-LANE RECONCILIATION COMPLETE / THIRD-LANE REVIEW PENDING

## Inputs

Independent adversarial architecture reviews were supplied from:

- Perplexity
- Grok

Claude review is not yet incorporated and remains an independent pending lane.

## Convergent findings

Both lanes independently converge on the following required architecture:

1. Research is an **evidence-production pipeline**, not an authority pipeline.
2. Evidence, interpretation, recommendation, and governance disposition must remain structurally distinct.
3. Provenance must be immutable, reconstructible, and exact-source bound.
4. Provider identity does not create epistemic or governance authority.
5. Corroboration must account for common origin and shared dependency rather than count sources or providers.
6. Disagreement must be preserved explicitly rather than averaged or silently resolved.
7. Retrieved content is untrusted data and must be isolated from instruction authority.
8. Prompt injection, poisoning, duplicate narratives, and citation loops are first-class research threats.
9. Research agents must not directly write canon or self-promote findings.
10. Submission for reconciliation must fail closed when provenance, validation, contradiction handling, or independent review is incomplete.

## Preserved differences

The two reviews are not identical and their differences are retained:

### Source-quality representation

Perplexity argues for a multidimensional vector profile and warns against reducing quality to a single trust score. Grok adds an operational Tier 0-4 overlay.

**Reconciliation:** use the vector profile as the canonical quality representation. A tier overlay may exist for routing or display, but must be derived, versioned, auditable, and must never replace the vector dimensions.

### Graph-write topology

Grok proposes a Navigator-style sole writer to the shared evidence graph. Perplexity emphasizes immutable evidence objects and typed derivations but does not require one privileged writer.

**Reconciliation:** v0.1 requires a single logical graph-coordination contract but does not yet canonize one named agent as permanent sole writer. Search/retrieval lanes are evidence producers; graph mutation must pass the coordinator contract and adversarial checks. Provider or agent naming remains replaceable.

### Corroboration threshold

Perplexity proposes two provenance-independent paths or one directly inspectable primary artifact with an explicit single-source limitation for high-impact claims. Grok proposes Tier-0/1 support or explicit low-confidence/contested status.

**Reconciliation:** both constraints apply: material claims require independent corroboration when available; a single directly inspectable primary source may support a provisional bounded claim only with explicit limitation. Source type alone cannot make a contested claim settled.

### Contradiction scanner

Grok proposes a mandatory Grok contradiction scanner on every graph mutation. Perplexity defines adversarial review functionally rather than binding it to one provider.

**Reconciliation:** contradiction/adversarial screening is mandatory; Grok may serve that lane initially, but the contract remains provider-independent. No provider receives permanent constitutional or governance standing from this assignment.

### Promotion language

Grok references existing Ptah + Operator promotion semantics; Perplexity states a separately governed reconciliation process.

**Reconciliation:** ARGUS does not define or expand constitutional promotion authority. It submits only to the currently valid reconciliation/governance path. Any named authority must be resolved from the canonical governance substrate at the time of disposition rather than hard-coded into the research contract.

## Adopted v0.1 boundary

The common denominator has been encoded in:

- `ARGUS_RESEARCH_ASSURANCE_CONTRACT_V0_1.md`
- `ARGUS_RESEARCH_PACKET_V0_1.schema.json`

These artifacts are **PROPOSED / UNEVALUATED** and grant no governance-registry membership, dispatch authority, merge authority, repository permission, constitutional standing, autonomous execution, or canon-write authority.

## Remaining review

Claude should receive the exact same underlying architecture problem without being shown the conclusions above if an independent third lane is still desired. Its response should then be compared against this frozen two-lane reconciliation rather than used to silently rewrite the record.

## Promotion condition

No ARGUS contract should be treated as ratified until:

- the current exact proposal head passes repository checks;
- independent exact-head review finds no unresolved P1/P2 boundary defect;
- the remaining third-lane review is either completed or explicitly waived by the appropriate human governance disposition;
- any proposed changes to canonical runtime/event schemas are separately reviewed as implementation work rather than implied by this documentation proposal.
