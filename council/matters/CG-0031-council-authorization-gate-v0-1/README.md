# CG-0031 — Council Authorization Gate v0.1

## Final State

**Workflow state:** Closed  
**Operator disposition:** `accepted-with-conditions`  
**Authority effect:** bounded Phase 0 verifier implementation and scoped non-required CI pilot only

CG-0031 authorizes implementation and local validation of a reusable **Council Authorization Gate** whose only role is to verify that a previously recorded Operator disposition already authorizes an exact implementation scope.

The gate does not create authority. It verifies previously recorded authority.

## Authority Model

```text
Operator disposition in Council Grounds
        ↓
Pinned, merged authority record
        ↓
Deterministic CI validation
        ↓
Scoped implementation check passes or fails
```

Council Grounds remains the authority record. The Operator remains final authority. The Operator Continuity Ledger remains non-operative. CI remains verifier-only. Runtime receives no new authority from this matter.

## Authorized Phase 0 Scope

Phase 0 may implement and locally validate:

- a strict machine-readable authorization-requirement contract;
- a reusable validator with deterministic pass/fail behavior and stable reason codes;
- exact matter, authority repository, immutable commit, record path, implementation repository, protected path, and scope matching;
- an accepting-disposition allowlist limited initially to `accepted` and `accepted-with-conditions`;
- machine-readable condition validation;
- supersession, revocation, conflict, and failure-closed checks;
- disclosure-minimized diagnostics;
- positive and negative fixtures;
- a scoped CI pilot in `mirrornode-platform` for CG-0030 and `/continuity`;
- an implementation evidence packet.

## Operator Conditions

### ANTI_SELF_MODIFICATION

The evaluated change must not be able to weaken the gate definition, authority binding, validator identity, or protected-path declaration and then validate itself against that weakened state.

Implementation evidence must prove either immutable authority-controlled gate configuration or equivalent detection that fails unauthorized self-modification.

A negative fixture must prove that narrowing or altering the protected `/continuity` declaration cannot evade the gate.

### PILOT_SCOPE_FIXED

The Phase 0 pilot is limited to:

- authority matter: CG-0030;
- authority repository: `mirrornode/MIRRORNODE-CORE-HUB`;
- implementation repository: `mirrornode/mirrornode-platform`;
- protected surface: `/continuity`.

## Explicitly Not Authorized

CG-0031 does not authorize:

- authority creation, inference, amendment, or revocation by CI;
- Council or Continuity Ledger writes;
- implementation-repository or runtime writes by the gate;
- mutable or unpinned authority sources;
- cached last-known-good authority;
- bypass, override, or emergency self-authorization;
- required merge-check activation;
- branch-protection changes;
- organization-wide or broader repository rollout;
- unrelated-path blocking;
- runtime or MOPCON enforcement/modification;
- deployment;
- publication;
- production-data ingestion;
- disclosure of private deliberation, rationale, credentials, customer data, or internal topology.

## Required Reviews

The required advisory reviews are recorded:

- **POS-0001 — Ptah:** `feasible-with-conditions`.
- **POS-0002 — Osiris:** `safe-with-conditions`.

Both positions converge on the anti-self-modification condition above. No unresolved conflict remains.

## Post-Implementation Gates

The following remain separate future decisions:

- required merge-check activation;
- branch-protection changes;
- broader repository rollout;
- additional protected paths or surfaces;
- runtime enforcement;
- deployment or publication.

## Operator Disposition

The Operator accepted CG-0031 with conditions on 2026-07-24 after CG-0030 / PR #31 were merged and after the required Ptah and Osiris reviews.

The recorded disposition authorizes only the bounded Phase 0 verifier implementation, local validation, and scoped non-required CI pilot described above.
