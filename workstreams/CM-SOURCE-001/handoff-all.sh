#!/usr/bin/env bash
set -euo pipefail

# CM-SOURCE-001 shared handoff generator.
# Produces one common-context packet plus bounded assignments.
# It does not grant permissions, change node classification, promote canon,
# or execute external actions by itself.

ROOT="${1:-./cm-source-001-handoffs}"
mkdir -p "$ROOT"

COMMON=$(cat <<'EOF'
CM-SOURCE-001 — MIRRORNODE State, Authority & Source Reconciliation

STATUS
Approved for discovery/reconciliation by the Operator on 2026-08-09. Candidate only; no canon change without the established evaluation and Operator-ratification path.

VOCABULARY
- Operator / Siseon = final governance disposition and ratification.
- node = named MIRRORNODE lattice presence.
- collaborating intelligence = external AI collaborator unless canon explicitly classifies it as a MIRRORNODE node.
- role = operating responsibility; does not grant authority.
- capability = demonstrated technical ability.
- permission = authenticated access within a service/repository/account.
- governance authority = right to decide/approve/ratify within a defined governance envelope.
- runtime execution authority = narrower technical execution/dispatch authority.
- custody / owning source = repository/service responsibility; not an authority grant.
- canon = ratified governance state.
- operational state = current provenance-backed synthesis.
- implementation state = code/service behavior that actually exists.
- evidence = attributable support for a claim.
- projection = derived view such as MOPCON or @mirror.

OBJECTIVE
Reconcile governance, operational state, implementation custody, node/collaborator roles, verified capabilities and permissions, authority boundaries, evidence standards, @mirror handoffs, MOPCON projection, and external transparency into one readable and auditable operating model.

SHARED RULES
1. Role does not imply capability.
2. Capability does not imply permission.
3. Permission does not imply governance authority.
4. Runtime execution authority must not be confused with final governance authority.
5. Operational state does not silently supersede canon.
6. Canon does not prove that implementation still matches it.
7. Implementation claims must point to the owning repo/service and current evidence.
8. Conflicts are surfaced, classified, and resolved through the appropriate review/authority path; never silently flattened.
9. Consequential actions should retain actor, authority basis, changed artifact, evidence, and receipt where available.
10. Preserve historical canon and supersede explicitly.

KNOWN VERIFIED / ACTIVE DISCREPANCIES
- CORE-HUB remains the governed canon surface, but some role/runtime wording is stale.
- SYSTEM_CONTRACT.md is April 28, 2026; later agent-runtime implementation changed after that date and requires explicit contract reconciliation.
- CORE-HUB README uses Merlin as unqualified “Orchestrator”; current operating practice separates integration, planning, runtime dispatch, and implementation management.
- MOPCON later work is preserved: feat/f04-verified-topology is 11 commits ahead of MOPCON main.
- MOPCON feat/f04 runtime UI is NOT compatible with agent-runtime main: it targets the divergent Build Week /decision contract, while runtime main uses separate /approve and /execute endpoints.
- Canon Gate PR #35 and #36 passed configured CI before Codex found semantic false-negative paths. PR #37 is the current structural-parser correction and must clear both CI and fresh review-thread inspection.
- Perplexity's older research/Judge/Librarian description understates the Operator-reported implementation relationship; candidate operating title is Implementation & Execution Manager, not an authority grant.
- Copilot participation/permissions are not verified in this workstream; do not claim otherwise.

COLLABORATION EXPECTATION
You are receiving the shared picture intentionally. Perform your bounded lane, but note dependencies, contradictions, risks, or improvements you see in adjacent lanes. Do not silently assume another participant's authority, node classification, permission, or custody. Return evidence and explicit uncertainty.

RETURN FORMAT
- identity
- classification (node / collaborating intelligence / human / service)
- assignment
- sources inspected
- verified findings
- contradictions / stale claims
- proposed changes
- actions actually taken
- artifacts changed
- evidence refs
- unresolved questions
- authority/security escalations
- receipt / timestamp
EOF
)

write_packet() {
  local name="$1"
  local assignment="$2"
  cat > "$ROOT/${name}.md" <<EOF
$COMMON

BOUNDED ASSIGNMENT — ${name^^}
${assignment}
EOF
}

write_packet "theia" "Own integration and reconciliation. Maintain the discrepancy register and terminology consistency; verify repository custody/current state; assemble the cross-lane synthesis. Do not self-ratify. Preserve Ptah evaluation and Thoth security verdicts."

write_packet "perplexity" "Act under the candidate operating title Implementation & Execution Manager. Inventory verifiable connected-service permissions separately from technical capability and requested actions. Identify concrete implementation gaps and carry out only bounded, approved, low-risk actions within effective permissions, returning exact evidence and receipts."

write_packet "gemini" "Perform broad-context synthesis and adversarial review of the source/custody model and terminology. Look for overloaded language, duplicated responsibilities, missing audience distinctions, product implications, and confusing MOPCON/public projections. Return contradictions and replacement wording; do not treat synthesis as ratification."

write_packet "merlin" "Own decomposition and dependency mapping. Convert the current verified state into an execution map: inputs, custody, blockers, review gates, sequencing, and handoffs. Reconcile planning/dispatcher/orchestrator language and identify where older Merlin descriptions conflict with the candidate responsibility split."

write_packet "oracle" "Perform evidence-sufficiency review. For each major claim, classify whether evidence supports VERIFIED, PARTIALLY VERIFIED, OPERATOR-REPORTED, STALE, UNKNOWN, CONTRADICTORY, or VERIFIED FALSE. State what evidence would close each gap."

write_packet "ptah" "Evaluate candidate governance/source artifacts for promotion readiness. Check structural coherence, supersession mechanics, authority boundaries, node/collaborator classification, source custody, and whether candidate role language changes authority or only describes operating responsibility. Return PASS / PASS WITH CONDITIONS / FAIL with exact required corrections."

write_packet "thoth" "Review security consequences of the source model, identity/capability/permission registry, @mirror protocol, MOPCON projection, and external-action collaborators. Identify credential leakage, privilege confusion, stale permission risk, unsafe execution paths, and required security verdict fields. Do not expand permissions."

write_packet "osiris" "Perform structural assurance review against declared governance. Check source classes, evidence references, action provenance, implementation custody, discrepancy handling, public/private boundaries, and whether CI/review evidence is represented without overclaiming."

write_packet "grok" "Inventory currently effective action capabilities where directly verifiable, especially GitHub identity/scope, and separate capability from permission and authority. Also review the architecture adversarially and suggest implementation improvements. Do not alter canon without a separate bounded authorization."

write_packet "codex" "Perform adversarial code/review verification. Inspect Canon Gate PR #37 for false negatives/positives, unified-diff edge cases, terminology that overstates verifier guarantees, and regression-test adequacy. Separately inspect the runtime-main versus Build Week versus MOPCON API contract discrepancy and identify the smallest technically coherent reconciliation path. Return review evidence, not ratification."

cat > "$ROOT/README.md" <<'EOF'
# CM-SOURCE-001 handoffs

Generated by `handoff-all.sh`.

Each packet contains the same reconciled vocabulary and verified discrepancy baseline plus one bounded assignment. Participation does not imply MIRRORNODE node classification, service permission, or governance authority.
EOF

printf 'Generated CM-SOURCE-001 handoffs in %s\n' "$ROOT"
printf 'Packets: theia perplexity gemini merlin oracle ptah thoth osiris grok codex\n'
