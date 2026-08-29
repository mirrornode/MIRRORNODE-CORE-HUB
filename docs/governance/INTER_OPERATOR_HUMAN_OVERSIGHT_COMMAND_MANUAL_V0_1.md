# INTER / OPERATOR HUMAN OVERSIGHT COMMAND MANUAL v0.1

**Status:** PROPOSED GOVERNANCE / OPERATIONAL MANUAL  
**Paired document:** `OUTER_AGENT_LATTICE_OPERATIONS_CHARTER_V0_1.md`  
**Scope:** Human/Operator command, approval, review, escalation, merge, release, automation, and incident oversight across MIRRORNODE.

## 1. Purpose

INTER defines the human-facing command surface of MIRRORNODE. It exists to make consequential authority explicit, preserve exact-target evidence, prevent accidental authority manufacture, and give the Operator a repeatable way to intervene when automation, repositories, providers, or agent lanes produce ambiguous states.

INTER is not a substitute for repository protections, runtime authorization checks, constitutional records, or provider-specific controls. It is the command manual that tells human oversight how to use and interpret those systems.

## 2. Foundational bylaws

1. **Human authority is explicit.** A consequential act may not be inferred from tone, prior enthusiasm, CI state, a green check, a model recommendation, or a previous approval against a different target.
2. **Exact target before disposition.** Review, approval, rejection, execution, merge, release, and exception handling bind to an immutable subject whenever the substrate supports one.
3. **Changed head, changed evidence.** A changed commit head invalidates review evidence unless an explicit carry-forward rule is mechanically justified and recorded.
4. **Green is evidence, not sovereignty.** Successful CI means the tested workflow succeeded. It does not itself grant approval, merge authority, release authority, constitutional standing, repository permissions, or runtime execution authority.
5. **Unknown means stop.** Missing evidence, unresolvable identity, unavailable protection state, ambiguous authority, or incomplete workflow execution is a HOLD unless a stricter FAIL rule applies.
6. **No retroactive authorization.** An action taken without required authorization cannot be made compliant by obtaining approval afterward.
7. **No self-certification.** The actor, agent, automation, or subsystem that prepared a consequential change cannot alone certify that change as cleared.
8. **Least consequential intervention.** Human intervention should use the smallest action that restores observability, correctness, or progress.
9. **Document the exception, not a fiction.** Infrastructure failures are recorded as infrastructure failures. Do not edit source code merely to manufacture green evidence when no source defect is evidenced.
10. **Operator disposition is separable from constitutional status.** A bounded operational approval does not silently ratify governance-registry membership, dispatch authority, constitutional standing, merge authority, or repository permissions.

## 3. Command states

- **OBSERVE** — gather evidence; no disposition yet.
- **PROPOSE** — a bounded change or action is prepared.
- **HOLD** — progress is stopped pending evidence, correction, or authority.
- **REJECT** — the proposed action is not acceptable in its present form.
- **CLEAR FOR REVIEW** — sufficient implementation evidence exists to request independent review.
- **CLEAR FOR MERGE DECISION** — exact-head checks and required review are complete; merge remains a separate human action.
- **AUTHORIZED** — a named actor may perform a named action against a named target within the stated validity window.
- **EXECUTED** — the authorized action occurred.
- **VERIFIED** — post-action evidence confirms the intended state.
- **CLOSED** — the matter is complete with evidence preserved.
- **CASUAL VIGILANCE** — no active intervention is required; low-noise condition monitoring remains in force.

## 4. Standard human command sequence

1. Establish the exact target.
2. Identify the requested operation class.
3. Resolve the authority source.
4. Inspect preconditions and known holds.
5. Permit bounded implementation or correction.
6. Run required automated checks against the exact target.
7. Request independent exact-target review.
8. Reconcile review findings.
9. **If reconciliation, correction, or any other material change alters the exact subject or head, return to step 6: re-run required checks and obtain fresh independent exact-target review of the successor subject. Ancestor-head review cannot clear a changed head.**
10. Make the human disposition only after the current exact subject has the required checks and independent review.
11. Execute only the authorized act.
12. Verify the resulting state.
13. Record the final evidence and residual risks.

The sequence may be shortened only when the skipped stages are mechanically irrelevant to the operation class. A subject-changing correction never qualifies as mechanically irrelevant to exact-target review.

## 5. Review-State Rebind Sequence (RSR-1)

### 5.1 Origin

RSR-1 was established during `MIRRORNODE-INFRA` PR #4 after a GitHub Actions execution anomaly.

Observed sequence:

- exact head `8c567544d78a698a75ef0c1475892939eecd86f2` showed a Repo Steward CI failure that was actually a cancelled job;
- rerunning that exact job produced success on the same head;
- `Validate Estate Wrapper` recorded `startup_failure` before any job was created, leaving no job-level artifact to rerun;
- a semantic no-op successor `4b1bd8685bfe168faf048c77d5de69b3d5ba65a9` was created solely to request fresh execution evidence;
- connector-originated PR mutations did not emit the expected fresh `pull_request` workflow event;
- the human Operator changed PR #4 from **Draft** to **Ready for review**;
- GitHub then emitted fresh PR workflow executions;
- both `Repo Steward CI` and `Validate Estate Wrapper` executed successfully on exact successor head `4b1bd8685bfe168faf048c77d5de69b3d5ba65a9`.

### 5.2 Rule

RSR-1 is a **recovery sequence for event-delivery gaps**, not a bypass.

Use RSR-1 only when:

- the desired required workflow or check is configured for, and eligible to run on, the human-visible PR state transition or equivalent native recovery event;
- no source defect is evidenced that would justify further code changes;
- existing execution evidence is missing because an event was not emitted, a workflow failed before job creation, or the integration could not cause the native event;
- the human action is itself permitted and does not expand repository authority.

RSR-1 cannot make an event-ineligible workflow pass. A required workflow that cannot run on the recovery event must be satisfied through its own supported trigger or remain an explicit HOLD.

### 5.3 RSR-1 procedure

1. Record the exact current head.
2. Classify the prior failure as code failure, job failure, cancellation, startup failure, event-delivery failure, or unknown.
3. If a real code defect exists, correct the code instead of using RSR-1.
4. If no code defect is evidenced, preserve HOLD.
5. Use the smallest native human state transition known to emit the required event.
6. Confirm that the new workflow run is bound to the same exact head intended for validation.
7. Require every **policy-required workflow/check that is eligible for that recovery event and exact subject** to execute and pass. Any required but event-ineligible workflow/check must be satisfied through its own supported trigger or remain HOLD; do not classify it as failed merely because RSR-1 cannot invoke it.
8. Preserve independent review as a separate gate.
9. Record the recovery path so later operators do not misclassify the incident as a source-code repair.

### 5.4 Prohibited uses

RSR-1 must not be used to bypass required review, bypass branch protections or rulesets, substitute a new event for a changed-head review, rerun until a flaky result happens to pass without investigating repeated instability, turn an UNKNOWN authority state into approval, conceal infrastructure reliability issues, treat an event-ineligible required workflow as satisfied, or create evidence for a head other than the release subject.

## 6. Human review rules

A human reviewer or Operator must distinguish review request from review submission; COMMENTED from APPROVED; automated review from independent human approval where human approval is required; current-head review from ancestor-head review; implementation quality from authority to merge; and mergeability from clearance.

A review should name the exact target whenever possible and explicitly state the review scope.

## 7. Merge bylaws

A merge may occur only when the expected head SHA is known; required checks have completed successfully on that head; all required independent review is bound to that head; no unresolved P1/P2 issue remains within scope; the PR is mergeable without hidden conflict; no constitutional or policy hold applies; and the human performing the merge actually holds merge authority.

Merge must use an expected-head guard when the tool supports it.

## 8. Runtime and dispatch oversight

Human approval for runtime execution must specify, where applicable: requesting actor, executing actor, operation class, policy version, execution nonce, current-state hash, target version, decision timestamp, expiration, reason code, and verification expectations.

Runtime approval does not automatically satisfy repository administration, release, finance, credential, or constitutional approval requirements.

## 9. Automation rules

Automations may observe, summarize, classify, notify, prepare bounded proposals, request review when explicitly authorized by policy, and perform narrowly authorized low-risk actions if a separate execution contract permits them.

Automations must not infer new standing authority from recurrence. Condition watches should be low-noise: if the condition is not met, they should remain silent.

## 10. Casual Vigilance

Casual Vigilance is appropriate when active critical corrections are closed or explicitly held; no unresolved high-severity regression demands continuous intervention; required protections are known and monitored; exact-head and provenance rules are functioning; and low-noise monitoring can surface meaningful regressions.

Casual Vigilance is not abandonment. It is a change in intervention frequency.

## 11. Incident command

- **P1 — Critical:** Immediate HOLD. Authority manufacture, secret exposure, direct unauthorized mutation, false release evidence, bypass of required approval.
- **P2 — Major:** HOLD affected lane. Stale exact-head evidence, fail-open validation, unverified producer identity, incomplete protection semantics.
- **P3 — Moderate:** May proceed only when the defect cannot alter authority, evidence validity, or release correctness and a tracked correction exists.
- **P4 — Advisory:** Non-blocking improvement.

## 12. Human escalation ladder

Use the minimum adequate escalation: local correction; independent review; security/governance review; Operator disposition; constitutional/council review where standing, authority, or covenant changes; external professional/legal/security escalation where the system cannot competently adjudicate internally.

## 13. Records and receipts

Every consequential action should leave enough evidence to answer: what target changed; who requested it; who authorized it; who executed it; which policy applied; what checks ran; what review applied; what changed after review; what final state resulted; and what residual risk remains.

## 14. Amendments

This manual may be amended only through the **then-current applicable governance and ratification path**. A reviewed documentation change is necessary evidence but is not, by itself, ratification.

Where the governing canon requires Ptah evaluation, explicit Operator ratification, Council review, or another named authority step, that requirement remains binding. No amendment to INTER may bypass, downgrade, or silently replace that path.

An amendment does not silently amend the paired OUTER Charter; paired changes must identify both documents, state whether the invariant contract remains compatible, and complete the applicable ratification path for each affected authority surface.

## 15. Paired invariant

INTER governs **human oversight of the boundary**. OUTER governs **agent conduct at the boundary**.

Neither volume may be interpreted alone to create authority that the other volume, repository policy, runtime policy, or constitutional record withholds.
