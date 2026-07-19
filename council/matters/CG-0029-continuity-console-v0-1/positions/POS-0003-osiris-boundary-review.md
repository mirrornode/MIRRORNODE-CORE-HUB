---
schemaVersion: "0.1"
id: POS-0003
matterId: CG-0029
author: osiris
role: privacy-authority-boundary-review
kind: condition
createdAt: 2026-07-19T09:00:00Z
source:
  form: agent-response
  reference: operator-provided-session-response
  capturedBy: operator
  receipt: null
contentPath: council/matters/CG-0029-continuity-console-v0-1/positions/POS-0003-osiris-boundary-review.md
respondsTo:
  - POS-0001
supersedes: null
stance: support-with-conditions
immutableOriginal: true
---

# Osiris boundary review

## Stance

support-with-conditions

## Boundary finding

The proposed separation is sound only if the build artifact is treated as a deliberately published disclosure product—not as a filtered projection of MOPCON or other private systems.

The typed and build-generated model reduces request-time exposure but does not itself make data safe. Types validate shape; they do not establish publication authority. Every record must pass an explicit field-level and source-level public allowlist before entering the artifact.

The MOPCON boundary is decisive. The following remain private even when summarized elsewhere: objectives, execution prompts, plan content, approval or rejection activity, operator notes, trace identifiers and bodies, runtime routing, private health detail, and authenticated console locations.

No Continuity state may create or imply authority to act.

## Public-data risks

Public repository data is not automatically safe to aggregate. Aggregation can reveal more than the individual sources reveal conveniently, including:

* internal topology and dependencies between repositories, services, agents, and surfaces;
* operational cadence, maintenance windows, staffing patterns, and periods of reduced attention;
* unresolved security weaknesses through check failures, incident titles, correction patterns, or blocked work;
* customer or commercial activity embedded in branch names, PR titles, commits, evidence, or issue text;
* private-system existence through MOPCON summaries and action-required labels;
* sequential identifiers that permit enumeration of incidents, matters, customers, traces, or internal records;
* deployment timing and version correlation useful for targeted probing;
* disagreement patterns or pending decisions that expose internal strategy.

Evidence links are not safe by default. Each link must resolve to an explicitly approved public origin and public resource. Links to private repositories, authenticated consoles, expiring URLs, CI artifacts, raw logs, local addresses, branch previews, or redirects into private infrastructure are prohibited.

Council summaries require a separate publication projection. Decision questions, objections, missing reviewers, next steps, and history may contain sensitive strategy even when the matter schema itself is public. Only fields expressly marked for public disclosure may be emitted.

A public continuity history should be bounded. An unlimited append-only history becomes a high-quality scraping and inference dataset. v0.1 should use a defined retention or display horizon, while the authoritative record remains in its source repository.

`Operator action required` is unsafe as a general-purpose label. It can disclose that a private decision, incident, security response, commercial act, or customer matter exists. Public output should default to a neutral statement such as `Further status is not publicly available`. An action label may appear only when the existence and public description of that action have been separately approved for disclosure.

## Freshness and authority risks

The current freshness model is incomplete because its source-specific windows remain unresolved. A timestamp plus a manually assigned `current` value does not prevent old verification from appearing live.

Freshness must be calculated from `verifiedAt`, the source class, and a defined maximum age. It must not be supplied as an unsupported editorial claim. At minimum:

* each record has its own `verifiedAt`;
* each source class has an explicit freshness window;
* snapshot-level freshness never overrides a stale record;
* `generatedAt` is never presented as the time the underlying fact was verified;
* an expired record automatically renders as stale or unavailable;
* unknown verification time cannot render as current;
* partial currency is disclosed per section and per affected record.

Runtime and MOPCON observations are point-in-time verification only. They must never be labeled `live`, `online now`, or equivalent when rendered from a static artifact.

`source-verified` remains vulnerable to misreading. It may imply that the underlying system, decision, security state, or product has been approved. If retained as a machine value, its visible label must say:

> Source and timestamp checked; underlying state not approved by this label.

Prefer a less authoritative public label such as `source checked`. `operator-disposition` must mean only that an attributable Operator disposition record exists. It must not mean that implementation, deployment, security, or publication was approved unless the cited disposition says so expressly.

Workflow progression, review completion, merge state, deployment verification, and product approval are distinct facts and must not be collapsed.

## Failure and disagreement behavior

Generation failure must fail closed.

The public route must not silently retain or regenerate plausible-looking content. It should display:

* `Snapshot unavailable`;
* the last successful generation time, if safe and known;
* whether previously published content has been withdrawn from current display;
* a neutral instruction to consult the cited public record, when one exists.

A previous snapshot may remain visible only if every record retains its original verification time and is visibly marked stale. It must not receive a new `generatedAt` that implies renewed verification.

When only part of the snapshot is current:

* each section and record shows its own condition;
* stale or unavailable sections cannot inherit a current page-level presentation;
* the header states `partial snapshot`;
* no overall nominal, healthy, operational, or verified conclusion is produced.

When sources disagree:

* do not choose a winner automatically;
* display `disputed` or `sources disagree`;
* preserve attributable source references and their verification times;
* suppress any derived status dependent on the disagreement;
* do not expose the dispute publicly if describing it would cross a privacy boundary.

Corrections must be append-oriented, but append-only does not forbid protective redaction. The original record should remain preserved in the authoritative source. If an entry contains personal data, secrets, customer information, or unsafe operational detail, the public projection must replace it with a tombstone stating that the public record was withdrawn or corrected. The sensitive original must not remain downloadable merely to demonstrate immutability.

A correction record must identify what public assertion it corrects without repeating prohibited content. Disputed records must not be silently overwritten, reordered to disguise the dispute, or presented as settled before an authorized disposition exists.

## Explicitly prohibited fields

The build artifact must explicitly prohibit:

* secrets, tokens, credentials, cookies, authorization headers, environment values, and connection strings;
* private or local URLs, hostnames, IP addresses, ports, WebSocket addresses, preview deployments, authenticated routes, and internal API paths;
* MOPCON URLs or access instructions;
* objectives, prompts, plans, plan rationales, preferred-agent selections, approval or rejection activity, operator notes, and execution results;
* trace IDs, session IDs, request IDs, correlation IDs, raw logs, stack traces, payloads, and trace bodies;
* private runtime health details, routing data, agent availability, internal model configuration, and topology;
* customer, prospect, audit-client, vendor, payment, billing, financial, or contractual data;
* personal email, calendar, contact, location, family, identity, or connected-service data;
* unpublished vulnerabilities, exploit details, security incidents, severity labels, remediation status, or defensive gaps;
* private repository names, branch names, commit messages, PR content, issue content, checks, artifacts, or file paths;
* author email addresses and unnecessary personal identifiers;
* raw Council positions, objections, decision rationale, missing-review details, or next actions unless separately marked public;
* sequential internal identifiers that enable enumeration;
* draft commercial strategy, competition work, launch timing, staffing signals, or confidential roadmaps;
* generated summaries of private records;
* mock incidents, synthetic counts, unsupported active-agent counts, or inferred system health;
* arbitrary source text or URLs copied into display fields without validation;
* deleted, corrected, disputed, or withdrawn content preserved inside client-accessible JSON;
* source timestamps or metadata that reveal sensitive operational cadence when coarser disclosure is sufficient.

The prohibition applies to the entire deployable artifact, including JSON, source maps, static assets, page metadata, HTML comments, build logs published as artifacts, and client-side bundles—not only visible UI.

## Deployment conditions

Before public deployment:

1. Source-specific freshness windows are defined and automatically enforced.
2. `verifiedAt` and `generatedAt` are visibly and semantically distinct.
3. Every source, record type, field, enumeration, and outbound link has an explicit public allowlist.
4. Private-derived summaries require affirmative publication approval; absence from a denylist is insufficient.
5. The generator rejects unknown fields and fails closed on schema drift.
6. The generator cannot access more private data than required. Prefer inputs already prepared as public projections.
7. No private credentials or request-time private-system calls exist in the deployed route.
8. MOPCON-derived objectives, plans, decisions, traces, notes, topology, and routes are absent from both rendered output and deployable assets.
9. The public label for source verification cannot reasonably be read as approval.
10. Action-required wording defaults to nondisclosure.
11. Partial, stale, unavailable, disputed, corrected, and withdrawn states have verified display behavior.
12. Corrections preserve authoritative provenance while allowing public withdrawal of unsafe material.
13. Public-history retention and identifier-enumeration controls are defined.
14. Evidence links are restricted to validated public HTTPS destinations and checked for redirects.
15. Fixtures and automated tests contain no production or private records.
16. A pre-deployment artifact inspection checks the built output—not merely the source schema—for prohibited strings, URLs, identifiers, and fields.
17. A human disclosure review approves the first production snapshot.
18. Operator authorization to implement is recorded separately from authorization to publish the first populated snapshot.

A signed manifest is not a prerequisite for v0.1 if generation and deployment occur in a controlled CI boundary with immutable source references. It becomes necessary if snapshots are transferred between trust domains or generated outside the deployment chain.

## Requested definition changes

1. Replace the general statement permitting `operator-summary-only` records with an affirmative rule: private-derived material is excluded unless a separately approved public projection exists.
2. Define freshness windows by source class and require freshness to be computed rather than asserted.
3. Replace the visible `source-verified` label with `source checked`, or add the explicit non-approval disclaimer.
4. Replace default `Operator action required` output with `Further status is not publicly available`; permit the former only through explicit disclosure approval.
5. State that public GitHub data, evidence links, and Council records are candidates for review—not safe by default.
6. Add `disputed`, `corrected`, and `withdrawn` to the record-condition model.
7. Define failure-closed behavior for generator failure and schema drift.
8. Require per-record freshness when a snapshot is partial.
9. Add a bounded public-history policy and prohibit enumerable internal identifiers.
10. Distinguish authoritative append-only preservation from the public projection’s right to tombstone unsafe content.
11. Require strict URL-origin validation and redirect checking.
12. Extend prohibited-data rules to all deployable assets and client-readable snapshot content.
13. Require human approval of the initial populated snapshot separately from approval of the route definition.

## Recommendation

Proceed only after the requested boundary changes are incorporated and verified.

I do not oppose the public read-only Continuity concept. I support the boundary direction conditionally: Continuity may publish intentionally approved public facts, but it must not become an automatically sanitized window into private operations.

The central rule is:

> Nothing becomes safe for public disclosure merely because it has a source, a type, or a timestamp.

This position does not ratify CG-0029, authorize implementation, approve deployment, or certify the underlying system state.

## Attribution rule

This text is Osiris’s exact attributed position for CG-0029. If registered under `positions/`, preserve it verbatim. Any shortened form, paraphrase, reconciliation, or conflict analysis belongs only in synthesis and must not replace this position.