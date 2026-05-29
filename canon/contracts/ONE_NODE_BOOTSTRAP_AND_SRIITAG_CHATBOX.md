# ONE-NODE BOOTSTRAP AND SRIITAG-AWARE OPERATING INTERFACE

Version: 0.3
Status: Draft for canonization
Authority: Mirror prepares canon; Operator reviews and approves; Ptah enforces; THOTH verifies security posture.

## Purpose

This contract defines the one-node bootstrap path and the SRIITAG-aware chatbox operating interface for MIRRORNODE CORE-HUB.

It exists to allow a single registered node to start cleanly, receive bounded instructions, produce reviewable receipts, and remain inside canon-safe authority boundaries.

## Scope

This contract applies to:

- one-node bootstrap initialization
- SRIITAG-aware message intake
- machine identity records
- agent roster records
- bootstrap receipts
- chatbox-mediated proposal flow
- transition control out of ADVISE_AND_PREPARE

This contract does not grant runtime mutation authority by itself.

## Authority Separation

The contract is the governing source of truth.

Schemas are derived enforcement controls. They may validate structure, but they do not create authority beyond this contract.

Repair notes, installer scripts, local terminal output, and temporary validation helpers are not canon unless explicitly promoted through review.

Validator-only rules are external validation unless this contract defines the mechanism and authority for those rules.

Ptah remains the enforcement authority for governance decisions.

THOTH security verdicts remain binding security judgments and may not be bypassed by chatbox, installer, schema, or fallback identity behavior.

## Schema Status

The schemas placed with this contract are derived from this contract.

They exist to support validation of:

- machine identity
- SRIITAG message envelopes
- agent roster records
- bootstrap receipts

If a schema conflicts with this contract, this contract governs.

A schema update that changes authority, routing, execution, identity, revocation, receipt, or sign-off behavior requires contract review before canon lock.

## Operating States

The one-node bootstrap interface recognizes these states:

1. ADVISE_AND_PREPARE
2. REVIEW_REQUESTED
3. APPROVED_FOR_EXECUTION
4. EXECUTION_RECEIPT_REQUIRED
5. DENIED_OR_REVOKED

ADVISE_AND_PREPARE is the default state.

## Operator Sign-Off Enforcement

Operator sign-off is required for any transition out of ADVISE_AND_PREPARE.

No node, chatbox, schema, installer, local script, or fallback identity may mark a material action approved without explicit Operator sign-off.

Operator sign-off must be recorded in a receipt or review artifact.

A missing, ambiguous, stale, revoked, or unverifiable sign-off keeps the system in ADVISE_AND_PREPARE.

## Default-Deny Routing

After a Ptah denial, routing defaults to deny.

A denied message, instruction, action, identity, or transition may not be retried as approved through another local path unless a new Operator-signed review artifact and Ptah allow verdict exist.

Absence of a Ptah allow verdict is not permission.

When routing evidence is incomplete, the safe state is DENIED_OR_REVOKED or ADVISE_AND_PREPARE, depending on whether an explicit denial exists.

## Revocation-Aware Execution Gating

Execution gating must check revocation state before material action.

A revoked operator credential, machine identity, agent identity, fallback identity, or approval artifact blocks execution.

Revocation state must be evaluated before transition into APPROVED_FOR_EXECUTION.

Revocation state must also be evaluated before accepting any bootstrap receipt as valid.

## @mirror_sync Isolation

@mirror_sync is append-only.

@mirror_sync is isolated from canon and runtime policy.

Entries in @mirror_sync may support review, synchronization, and traceability, but they do not mutate canon and do not authorize runtime behavior by themselves.

No @mirror_sync entry may override Ptah, THOTH, Operator sign-off requirements, or this contract.

## Software Fallback Identity Restriction

Software fallback identity is restricted to registered Operator-signed fallback identities.

A fallback identity must have:

- a registry entry
- an Operator signature
- a bounded scope
- a revocation status
- a timestamped receipt trail

Unregistered fallback identities are denied.

A fallback identity may not expand its own authority.

A fallback identity may not approve transitions out of ADVISE_AND_PREPARE unless this contract, the registry, and an Operator-signed approval explicitly allow that role.

## Machine Identity

A machine identity record binds local execution to a named host, local user, repository path, branch, commit, and timestamp.

Machine identity does not create authority.

Machine identity only anchors evidence.

## SRIITAG Message Envelope

A SRIITAG message envelope records source, target, state, intent, proposed action, authority references, and receipt expectations.

A message may advise, prepare, request review, or submit evidence.

A message may not silently execute material change.

## Agent Roster

The agent roster records available agents, their roles, authority scope, status, revocation state, and fallback eligibility.

The roster is evidence for review.

The roster does not override this contract.

## Bootstrap Receipt

A bootstrap receipt records:

- machine identity reference
- branch
- commit
- installed files
- sha256 hashes
- schema validation status
- required clause validation status
- Operator sign-off reference when applicable

A bootstrap receipt is required before any claim that installation is complete.

## Review Gate

Material changes to code, canon, schemas, runtime behavior, security policy, deployment state, identity, authority, or execution flow require review before being marked complete.

The default path is:

Operator
→ Node
→ Plan
→ Review Gate
→ Approved Execution
→ Receipt

## Non-Authority Notes

Repair notes are not canon.

Terminal commands are not canon.

Installer behavior is not canon.

Local validation is not canon.

These may provide evidence, but only reviewed canon and approved receipts can carry governance force.

## Acceptance Conditions

This contract is acceptable for review only if:

- the branch is correct
- the working tree state is known
- the contract file exists
- all required schemas exist
- all schema files parse as JSON
- required contract clauses are present
- no commit occurs before Operator confirmation
