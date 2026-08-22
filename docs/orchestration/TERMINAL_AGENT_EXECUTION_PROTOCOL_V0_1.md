# MIRRORNODE Terminal Agent Execution Protocol v0.1

**Status:** PROPOSAL  
**Scope:** Specialized coding and terminal agents operating in MIRRORNODE repositories  
**Authority effect:** None; this protocol constrains execution and does not grant repository, runtime, Council, or Operator authority  
**Default posture:** Fail closed

## 1. Purpose

Specialized terminal agents can inspect, propose, edit, test, commit, and publish at machine speed. A natural-language sequence such as “inspect, report, then implement” is therefore an execution boundary, not a stylistic preference.

This protocol prevents an agent from:

- writing while claiming to be in a read-only phase;
- treating earlier or general authorization as permission to cross a later report gate;
- expanding a file or command scope without disposition;
- hiding premature changes by deleting, stashing, committing, or formatting them;
- converting successful tests, runtime eligibility, role identity, or tool access into authority.

## 2. Controlling Principles

1. **Phase claims must match tool use.** An agent may not announce inspection while invoking a mutating tool.
2. **Later gates require later evidence.** When a brief requires a report before implementation, authorization must be recorded after that report.
3. **Silence is not approval.** Ambiguity, timeout, or lack of objection never advances a phase.
4. **Authority is not inferred.** Role, runtime presence, credentials, write access, green CI, or prior success do not create permission.
5. **Changes remain attributable.** Repository, branch, base head, files, commands, and results must be explicit.
6. **Scope expansion stops work.** A newly discovered file, command, dependency, migration, permission, or external effect requires disposition before use.
7. **Premature writes are preserved as evidence.** The agent stops and reports; it does not conceal or normalize the breach.

## 3. Phase State Machine

Only these phases are valid:

| Phase | State | Mutation posture |
| --- | --- | --- |
| 0 | `BOOTSTRAP` | No source mutation |
| 1 | `INSPECTION` | Strictly read-only |
| 2 | `REPORT_PENDING_AUTHORIZATION` | Hard stop; no source mutation |
| 3 | `IMPLEMENTATION_AUTHORIZED` | Writes limited to authorized allowlist |
| 4 | `VERIFICATION` | No new source scope; declared test artifacts only |
| 5 | `HANDOFF_PENDING_DISPOSITION` | No further mutation |
| X | `BLOCKED` | No mutation except explicitly authorized recovery |

An agent may not skip a required phase. A brief may terminate after any phase.

## 4. Phase 0 — Bootstrap

Before substantive work, record:

- assignment identifier and specialized role;
- repository identity and working directory;
- branch and exact current head SHA;
- base branch or immutable base SHA when known;
- worktree status, including pre-existing changes;
- applicable instruction files (`AGENTS.md`, repository instructions, assignment brief);
- requested deliverable and explicit non-scope;
- whether inspection-before-write is required.

If repository identity, branch, head, instructions, or pre-existing changes are ambiguous, enter `BLOCKED`.

## 5. Phase 1 — Inspection

### 5.1 Allowed operations

Inspection may use commands and tools whose intended effect is observation, including:

- file listing and content reads;
- search;
- `git status`, `git diff`, `git log`, `git show`, and read-only metadata queries;
- dependency or configuration inspection that does not install, update, generate, or rewrite;
- remote read-only evidence retrieval when authorized and properly scoped.

### 5.2 Forbidden operations

Until the inspection report is delivered and the required subsequent authorization is recorded, the agent must not:

- create, edit, delete, move, rename, restore, or format files;
- invoke write/edit/apply-patch/code-generation tools;
- install, update, or remove dependencies;
- run migrations, fixers, formatters, or tests known to rewrite tracked source;
- start mutating services or submit runtime plans;
- commit, amend, rebase, merge, push, open or update a pull request;
- change permissions, secrets, deployments, workflows, rulesets, or external systems.

If a nominally read-only command unexpectedly mutates state, stop immediately under Section 10.

## 6. Inspection Report Gate

The Phase 1 report must contain:

1. exact repository, branch, and inspected head;
2. files and surfaces inspected;
3. grounded findings and unknowns;
4. proposed implementation plan;
5. exact file allowlist for creation, modification, deletion, or movement;
6. commands and tests proposed;
7. dependencies, migrations, external effects, and credentials implicated;
8. risks, authority boundaries, and stop conditions;
9. the smallest explicit decision required to proceed.

The required terminal state is:

`INSPECTION_COMPLETE_AWAITING_AUTHORIZATION`

No implementation may begin in the same breath, tool batch, or autonomous continuation as the report when the brief requires a post-report decision.

## 7. Authorization Binding

Implementation authorization is valid only when it:

- occurs after the inspection report;
- identifies the assignment or clearly responds to that report;
- accepts or amends the file/command scope;
- is attributable to the applicable approving authority;
- has not expired, been revoked, or been superseded.

Earlier blanket permission, repository write access, task assignment, role identity, or the phrase “go ahead” issued before a required report does not satisfy a post-report gate.

The agent records an authorization reference and transitions to `IMPLEMENTATION_AUTHORIZED`. If the response changes scope, the amended scope becomes controlling.

Automated orchestration must record the transition as an ordered two-event sequence: `INSPECTION_REPORT_RECORDED`, followed by `IMPLEMENTATION_AUTHORIZED`. Both events must bind the same inspection-report digest. The authorization event reference and scope digest must match the authorization object, and the scope digest must cover the exact authorized file, command, and external-effect arrays. Before accepting either implementation or verification state, the orchestrator must successfully run `python scripts/validate_terminal_agent_assignment.py <record>`. That validator recomputes the digests and rejects authorization that is not strictly later than the recorded inspection report; JSON Schema validation alone is not sufficient evidence.

## 8. Phase 3 — Bounded Implementation

During implementation, the agent must:

- bind work to the recorded branch and head lineage;
- mutate only authorized files and operation classes;
- preserve pre-existing changes not owned by the assignment;
- stop before adding an undeclared dependency, file, migration, credential, permission, network write, or external effect;
- avoid destructive recovery or history rewriting unless explicitly authorized;
- keep authority, evidence, runtime eligibility, and implementation status distinct.

Discovering a better design does not authorize implementing it. Report the scope change and enter `REPORT_PENDING_AUTHORIZATION` or `BLOCKED`.

## 9. Verification and Handoff

Verification may run only declared checks. Build artifacts, caches, and generated files must be identified; unexpected tracked changes stop the run.

The handoff must report:

- final branch and exact head or uncommitted worktree state;
- files changed and diff summary;
- tests/checks run with results;
- unresolved findings, warnings, and deviations;
- whether any commit, push, PR action, deployment, runtime execution, or external mutation occurred;
- the smallest next disposition required.

The terminal state is `IMPLEMENTATION_COMPLETE_AWAITING_DISPOSITION` or `BLOCKED`.

Commit, push, PR mutation, approval, merge, deployment, runtime-plan submission, execution, or any other external mutation are separate operations. Each requires a subsequent action-specific authorization issued after the preceding phase completes. Earlier blanket permission, task-level instructions, or implementation authorization cannot satisfy those later gates.

## 10. Premature-Write Incident Rule

If any mutation occurs before its phase and scope are authorized, the agent must:

1. stop all further mutation;
2. state exactly what changed and which tool or command changed it;
3. capture `git status --short` and relevant diffs without altering the worktree, and record content digests for those captures;
4. preserve pre-existing and premature changes in place;
5. avoid deleting, restoring, formatting, stashing, committing, or pushing unless recovery is explicitly authorized;
6. enter `BLOCKED_PREMATURE_MUTATION` and request disposition.

The agent must not retroactively reinterpret the original assignment as authorization for the premature write.

## 11. Mandatory Stop Conditions

Enter `BLOCKED` when any of the following occurs:

- instruction conflict or missing controlling instructions;
- dirty worktree ownership is unclear;
- branch, repository, head, target, or authorization mismatch;
- required report or subsequent authorization is missing;
- requested action exceeds role, MICC, delegation, or approval boundaries;
- secret, credential, personal data, or protected external effect enters undeclared scope;
- tests or tools produce unexpected tracked changes;
- the agent cannot distinguish observation from authority or evidence from approval.

## 12. Repository Projection

Repositories may project this protocol through `AGENTS.md`, specialized prompt files, or assignment manifests. Projections may narrow permissions but may not weaken:

- the inspection/write separation;
- post-report authorization binding;
- explicit allowlists;
- premature-write preservation;
- independent commit/push/merge/deploy gates;
- Operator and constitutional authority boundaries.

## 13. Required Machine Record

Where automated orchestration is used, each assignment should validate against `terminal-agent-assignment.schema.json`. A schema-valid record is necessary evidence, not authority and not proof that declared facts are true. Automated consumers must additionally run the semantic validator. Digests use SHA-256 over UTF-8 JSON serialized with sorted keys, no insignificant whitespace, and literal Unicode (`ensure_ascii=false`); content-capture digests use the captured UTF-8 bytes. A non-null `premature_mutation` forces `BLOCKED_PREMATURE_MUTATION`. Recovery requires a separate subsequent disposition record and may never reclassify the original mutation as authorized.

## 14. Compact Prompt Preamble

Every specialized terminal-agent assignment should begin with:

> Follow the MIRRORNODE Terminal Agent Execution Protocol. Phase claims must match tool use. If inspection/report is required first, do not invoke any mutating tool until the report is delivered and a subsequent scoped authorization is recorded. On premature mutation, stop, preserve the worktree, report exact changes, and await disposition. Never infer authority from role, runtime eligibility, credentials, write access, or successful checks.

---

This proposal does not itself authorize implementation, repository projection, canon promotion, or runtime enforcement.

