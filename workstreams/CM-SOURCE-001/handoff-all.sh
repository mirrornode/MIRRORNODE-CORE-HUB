#!/usr/bin/env bash
set -euo pipefail

# CM-SOURCE-001 shared handoff generator.
# Produces one common-context packet plus bounded assignments for each principal.
# It does not grant permissions, promote canon, or execute external actions by itself.

ROOT="${1:-./cm-source-001-handoffs}"
mkdir -p "$ROOT"

COMMON=$(cat <<'EOF'
CM-SOURCE-001 — MIRRORNODE Source, Authority & Execution Reconstitution

STATUS
Approved for discovery/reconciliation by the Operator on 2026-08-09. Not canonical until Ptah evaluation and explicit Operator ratification.

OBJECTIVE
Reconcile governance, source-of-truth hierarchy, implementation ownership, principal roles, effective capabilities, evidence standards, @mirror handoffs, MOPCON projection, and public transparency into one auditable operating architecture.

SHARED RULES
1. Capability is never inferred from role.
2. Authority is never inferred from capability.
3. Observed state is never silently promoted to canon.
4. Implementation truth belongs to the owning repo/service.
5. Operational synthesis must retain provenance.
6. Conflicts are surfaced, classified, and resolved through the owning authority; never silently flattened.
7. Every consequential action must be attributable to a principal, authority envelope, evidence basis, changed artifact, and receipt.
8. Preserve historical canon and supersede explicitly.

SOURCE MODEL UNDER REVIEW
CANON = what governs; primary surface MIRRORNODE-CORE-HUB.
STATE = current operational truth resolved from owning sources.
IMPLEMENTATION = what exists/executes in the owning repo/service.
EVIDENCE = what proves a claim.
REFERENCE = bounded/versioned @mirror projections.
PUBLIC = approved provenance-backed disclosure subset.

KNOWN EARLY DISCREPANCIES
- CORE-HUB is authoritative but some role descriptions are stale relative to current operations.
- mirrornode-workspace has become a highly active operational synthesis surface but is explicitly not canon.
- MOPCON remote history appears behind later known local/runtime work and needs reconciliation.
- Perplexity's older research/Judge/Librarian description understates demonstrated execution responsibility; candidate role is Implementation & Execution Manager.
- Grok has an installed GitHub App with a recent updated-permissions request; exact effective scopes remain to verify.
- No single reconciled effective-capability registry currently exists.
- @mirror needs one current protocol definition.

COLLABORATION EXPECTATION
You are receiving the shared picture intentionally. Perform your bounded lane, but note dependencies, contradictions, risks, or improvements you see in adjacent lanes. Do not silently assume another principal's authority or overwrite another lane. Return evidence and explicit uncertainty.

RETURN FORMAT
- principal
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

write_packet "theia" "Own integration and reconciliation. Maintain the discrepancy register; verify repository ownership/current state; assemble the final source hierarchy and cross-lane synthesis. Do not self-ratify. Prepare candidate canon changes and promotion packet only after evidence/reviews are complete."

write_packet "perplexity" "Act as Implementation & Execution Manager. Inventory your own current actionable relationships and connected-service capabilities where you can verify them; distinguish granted permissions from actions you have merely been asked to perform. Review implementation repositories and identify concrete source/implementation gaps. Carry out low-risk approved implementation/documentation tasks within effective permissions when useful, returning exact evidence and receipts. Escalate governance, destructive, financial/legal, or security-sensitive changes."

write_packet "gemini" "Perform broad-context synthesis and adversarial review of the proposed source model. Look for conceptual gaps, duplicated authorities, user-facing/product implications, and places where the hierarchy will become confusing at scale. Review how the model should project into MOPCON and public/external documentation. Return proposed wording and contradictions; do not treat synthesis as ratification."

write_packet "merlin" "Own decomposition and dependency mapping. Turn CM-SOURCE-001 into a dependency-aware execution map: inputs, owners, blockers, review gates, sequencing, and handoffs. Identify which work can proceed in parallel and which must wait for evidence or authority disposition. Reconcile your current role with existing Merlin repository descriptions and report stale claims."

write_packet "oracle" "Perform evidence-sufficiency review. For each major claim in the source model and principal registry, classify whether evidence is sufficient for VERIFIED, PARTIALLY VERIFIED, OPERATOR-REPORTED, STALE, UNKNOWN, or CONTRADICTORY. Identify what evidence would close each gap. Do not decide policy; judge whether claims are adequately supported."

write_packet "ptah" "Evaluate candidate governance/source artifacts for promotion readiness. Check structural coherence, authority boundaries, supersession mechanics, source ownership, non-self-ratification, and whether the proposed Perplexity/Grok/action-capability language changes authority or merely records state. Return PASS / PASS WITH CONDITIONS / FAIL with exact required corrections."

write_packet "thoth" "Review security consequences of the source model, principal capability registry, @mirror protocol, MOPCON projection, and external-action principals. Identify credential leakage, privilege confusion, stale permission risk, unsafe execution paths, and required security verdict fields. Do not expand permissions."

write_packet "osiris" "Perform structural assurance review against declared governance. Check that source classes, evidence references, action provenance, implementation ownership, discrepancy handling, and public/private boundaries are internally consistent and auditable. Return findings and evidence gaps."

write_packet "grok" "Inventory and report your currently effective action capabilities with particular attention to GitHub: authenticated principal/app identity if visible, repository scope, read/write abilities, PR/issue/actions capabilities, and recent actions. Separately review the architecture adversarially and suggest implementation improvements. Do not infer governance authority from technical permissions and do not alter canon without an explicit bounded assignment."

cat > "$ROOT/README.md" <<'EOF'
# CM-SOURCE-001 handoffs

Generated by `handoff-all.sh`.

Each file contains the same shared operating picture plus a bounded assignment. Return results using the specified return format so they can be merged into the discrepancy register and promotion packet without losing attribution.
EOF

printf 'Generated CM-SOURCE-001 handoffs in %s\n' "$ROOT"
printf 'Packets: theia perplexity gemini merlin oracle ptah thoth osiris grok\n'
