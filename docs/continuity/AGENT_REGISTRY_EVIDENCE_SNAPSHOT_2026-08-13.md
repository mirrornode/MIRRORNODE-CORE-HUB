# MIRRORNODE Agent Registry Evidence Snapshot — 2026-08-13

Status: Evidence snapshot for reconciliation  
Authority: Descriptive only. Presence here does not activate, ratify, promote, demote, or grant authority to any node.

## Purpose

Prevent future registry drift by separating concepts that older records collapsed into a single "confirmed agent registry."

A node identity may independently have:

1. governance recognition;
2. a dedicated implementation repository/manifest;
3. generic-runtime eligibility;
4. a bounded authority record;
5. an active deployment/runtime instance.

None of those facts automatically implies the others.

## Current generic runtime eligibility

`mirrornode-agent-runtime/app/main.py` currently permits these role names as plan targets:

- hermes
- lucian
- merlin
- oracle
- osiris
- ptah
- theia
- thoth

The same runtime disables direct `/agent` execution and requires a proposed plan to receive Operator approval before execution.

**Interpretation:** this list is technical runtime eligibility only. It is not a governance-status or authority list.

## Dedicated agent implementation manifests verified in this pass

| Identity | Dedicated repo evidence | Manifest role | Runtime eligible | Governance/authority conclusion from manifest alone |
|---|---|---|---|---|
| Lucian | `mirrornode-lucian/agent/manifest.yaml` | `memory` | yes | none; implementation facet only |
| Theia | `mirrornode-theia/agent/manifest.yaml` | `perception` | yes | none; implementation facet only |
| Merlin | `mirrornode-merlin/agent/manifest.yaml` | `reasoning` | yes | none; planning/sequencing evidence exists elsewhere |
| Osiris | `mirrornode-osiris/agent/manifest.yaml` | `audit` | yes | none; the name alone does not inherit commercial powers or operational permissions |
| Ptah | `mirrornode-ptah/agent/manifest.yaml` | `forge` | yes | none; authority must come from stronger governance records |
| Rotan-Q | `mirrornode-rotan/agent/manifest.yaml` | `signal` | no, not in current generic allowlist | none; dedicated implementation exists |

## Runtime-eligible identities without a verified dedicated agent repo manifest in this pass

| Identity | Runtime eligible | Dedicated manifest verified here | Note |
|---|---|---|---|
| Hermes | yes | no | routing/advisory design evidence exists in workspace/CORE-HUB |
| Thoth | yes | no | review positions and security/evidence work exist in Council records; implementation surface not established here |
| Oracle | yes | no | runtime role name only in this snapshot; governance identity/status remains separately reconcilable |

"No dedicated manifest verified" does not mean no implementation exists. It means this evidence snapshot did not establish one.

## Historical April registry

`SYSTEM_CONTRACT.md` listed LUCIAN, OSIRIS, HERMES, THOTH, THEIA, PTAH, and EVE from the old Lucian-centered runtime generation.

That table must now be read as a **historical runtime registry snapshot**, because:

- the contract explicitly expired as operational truth when runtimes changed;
- the current generic runtime has a different eligible-name set;
- dedicated node repositories now exist that were not represented in that April table;
- governance roles and implementation roles have since diverged and matured.

## Required fields for a future current registry

A replacement registry should not use one `status` column to carry all meanings. At minimum each record should distinguish:

```yaml
id:
display_name:
identity_status:
implementation_surfaces:
runtime_eligibility:
governance_status:
authority_boundary:
capabilities:
blocked_actions:
source_refs:
last_reviewed:
```

Recommended semantic distinctions:

- `identity_status`: known | historical | unresolved | deprecated
- `implementation_surfaces`: repositories/runtimes that implement or represent the identity
- `runtime_eligibility`: where the identity may technically be selected
- `governance_status`: draft | advisory | ratified | authority-bounded | historical
- `authority_boundary`: explicit scope only; never inferred from capability or runtime presence

## Immediate rule

Do not answer "Is X an active MIRRORNODE node?" from a single source.

Instead answer the relevant dimension:

- Is the identity recognized?
- Is there an implementation?
- Is it runtime-eligible?
- Is its authority ratified?
- Is an instance currently running?

If the requested dimension is unknown, say **UNKNOWN** rather than inheriting status from the name.

## Open reconciliation items

- full governance-status determination for the current node set;
- Eve/Bastet status;
- Oracle status;
- Hermes and Thoth implementation-surface mapping;
- Rotan-Q generic-runtime eligibility decision, if any;
- Librarian as seat versus capability;
- current deployment/runtime-instance evidence.

These are not resolved by this snapshot.
