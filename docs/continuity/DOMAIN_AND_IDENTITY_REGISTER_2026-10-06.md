# MIRRORNODE Domain & Identity Register — 2026-10-06

**Status:** working authoritative continuity record pending review  
**Authority:** Operator-directed documentation update  
**Scope:** public domain identity, current production attachment, and unresolved domain-verification state  
**Boundary:** documentary reconciliation only; this record does not change DNS, email routing, registrar settings, deployment, or publication state

## Recording rule

Domain identity claims are separated into **OBSERVED**, **INFERRED**, **UNKNOWN**, and **ACTION REQUIRED**. A domain is not treated as a MIRRORNODE-controlled asset unless ownership/control evidence is registered. Production use is not inferred from registration alone.

## Current register

### D-001 — `mirrornode.xyz`

- **Classification:** canonical production domain
- **State:** OBSERVED
- **Ownership / registration evidence:** GoDaddy order confirmation from February 2026 records purchase of `mirrornode.xyz`; the same receipt states auto-renewal on 2027-02-07.
- **Current hosting / DNS evidence:** Vercel domain inventory observed 2026-10-06 lists `mirrornode.xyz` as verified, with Vercel nameservers, and attached to the `mirrornode-platform` project.
- **Canonical source:** `CANONICAL_SOURCES.md` already designates `mirrornode.xyz` as the Production Domain.
- **Open issue:** Atlassian is still unable to verify `mirrornode.xyz` as an email domain as of 2026-10-06. This is an unresolved Atlassian/DNS verification issue and must not be conflated with the verified Vercel production attachment.
- **Disposition:** retain as the canonical production domain unless an explicit Operator disposition supersedes it.

### D-002 — `mirrornodeconsulting.com`

- **Classification:** registered MIRRORNODE business / consulting domain
- **State:** OBSERVED
- **Ownership / registration evidence:** the same GoDaddy order confirmation records purchase of `mirrornodeconsulting.com`; the receipt states auto-renewal on 2027-02-07.
- **Current production attachment:** not present in the authenticated Vercel domain inventory observed 2026-10-06.
- **Current role:** no production role is established by the evidence reviewed so far.
- **Disposition:** treat as a controlled registered asset; preserve it while its intended business/public role is reconciled.

### D-003 — `mirrornode.com`

- **Classification:** unverified external domain
- **State:** UNKNOWN
- **Ownership / control evidence:** no registrar-account, purchase, transfer, billing, or authenticated platform evidence has been registered establishing MIRRORNODE control.
- **Disposition:** do **not** treat `mirrornode.com` as a MIRRORNODE-owned or controlled asset unless new evidence establishes control.
- **Documentation rule:** references that imply MIRRORNODE ownership or operational control of `mirrornode.com` require correction or an explicit provenance note.

## Current identity hierarchy

1. **Canonical production identity:** `mirrornode.xyz`
2. **Registered business / consulting asset:** `mirrornodeconsulting.com`
3. **Unverified / uncontrolled:** `mirrornode.com`

This hierarchy records present evidence only. It does not decide whether `mirrornodeconsulting.com` should later redirect to, replace, supplement, or host a separate public surface from `mirrornode.xyz`.

## Reference sweep — 2026-10-06

### GitHub organization

- **OBSERVED:** organization-wide code search returns multiple current references to `mirrornode.xyz`, including the platform README, active-production-surface documentation, canonical metadata for Osiris Audit, CORE-HUB setup material, infrastructure reconciliation records, and runtime examples. The sampled references are consistent with `.xyz` being the current production identity.
- **OBSERVED:** organization-wide code search returned no matches for `mirrornode.com` in the indexed default branches searched.
- **OBSERVED:** organization-wide code search returned no matches for `mirrornodeconsulting.com` in the indexed default branches searched.
- **Boundary:** absence from code search is evidence only for the indexed GitHub scope; it is not proof that no historical branch, local file, private external record, or unindexed source contains a reference.

### Operator Gmail

- **OBSERVED:** exact Gmail search for `mirrornode.com` returned no messages in the connected Operator account.
- **OBSERVED:** exact Gmail search for `mirrornodeconsulting.com` returned the GoDaddy purchase/marketing trail, including the February 2026 order confirmation; no reviewed result established it as a production hostname.
- **Boundary:** this search covers the connected Operator Gmail account, not every mailbox, document store, vendor portal, or historical export.

### Google Drive

- **OBSERVED:** search for `mirrornode.xyz` returns historical and working documents that consistently describe `.xyz` as the live/public production surface.
- **OBSERVED:** searches for `mirrornode.com` and `mirrornodeconsulting.com` returned no Drive results in the connected scope.
- **Boundary:** absence from Drive search is scope-limited and does not prove universal absence.

### ChatGPT Library / business records

- **OBSERVED — material discrepancy:** `MirrorNode LLC Banking Introduction Packet.png` contains `contact@mirrornode.com` in its company snapshot/contact block. That address depends on a domain whose MIRRORNODE ownership/control has not been established.
- **Disposition:** classify that contact line as **STALE / UNVERIFIED — DO NOT REUSE** until a controlled email domain and mailbox are proven. Preserve the historical packet; correct by issuing a superseding packet rather than silently overwriting the old record.
- **OBSERVED:** exact text checks of the later BECU banking packet, executive brief, and August 12 banking packet did not return `mirrornode.com` in their extracted text. This is useful negative evidence but not universal proof of absence.

## Open reconciliation items

### ACTION REQUIRED — banking/contact identity correction

The banking introduction image is the first confirmed source of the `mirrornode.com` misalignment. Before any future reuse of business-facing contact materials:

1. select and verify the controlled business email domain and mailbox;
2. issue a superseding banking/company-introduction packet with the verified contact identity;
3. mark the old packet as historical/superseded in the business record index;
4. check whether the stale address was supplied to any external institution and, if so, determine whether an administrative contact update is required.

No assumption is made that BECU or any other institution currently has that address on file; that must be verified from the institution's actual record before any update.

### ACTION REQUIRED — Atlassian email-domain verification

Atlassian continues to report that the DNS records for `mirrornode.xyz` do not match the records required to verify the email domain. Before changing DNS:

1. retrieve the exact Atlassian verification records currently requested;
2. compare them against the authoritative DNS zone;
3. distinguish missing, conflicting, stale, and provider-managed records;
4. record the proposed change and blast radius;
5. require explicit Operator authorization before mutation.

### ACTION REQUIRED — `mirrornodeconsulting.com` intended role

Define, without changing production yet, whether the domain is intended to be:

- a business/legal-facing identity,
- a redirect to the canonical production domain,
- a separate consulting surface,
- an email identity,
- or a reserved protective asset.

No role is canonical until an Operator disposition is recorded and implementation evidence exists.

### ACTION REQUIRED — stale identity references

Continue the sweep across business records, vendor portals, connected drives, printable packets, legal/financial paperwork, email signatures, and public-facing collateral. Classify each occurrence as correct, stale, ambiguous, or requiring migration. Preserve historical records rather than silently rewriting completed evidence packets.

## Evidence provenance

- GoDaddy transactional order confirmation reviewed 2026-10-06 for the February 2026 purchase of `mirrornode.xyz` and `mirrornodeconsulting.com`.
- Authenticated Vercel domain and project-domain inventory reviewed 2026-10-06.
- Atlassian administrator email dated 2026-10-06 reporting continued failure to verify the `mirrornode.xyz` email domain.
- `MIRRORNODE-CORE-HUB/CANONICAL_SOURCES.md` on `main`, reviewed 2026-10-06.
- GitHub organization code-search sweep for the three domain names, performed 2026-10-06.
- Connected Operator Gmail exact-search sweep for `mirrornode.com` and `mirrornodeconsulting.com`, performed 2026-10-06.
- Connected Google Drive search sweep for the three domain names, performed 2026-10-06.
- ChatGPT Library exact search for `contact@mirrornode.com`, which surfaced the banking introduction packet; later banking packet exact-text checks were also performed 2026-10-06.

## Change-control boundary

This register may be updated as additional evidence is gathered. DNS mutation, registrar mutation, email-routing changes, domain transfer, production-domain replacement, redirect activation, business-contact change at a financial institution, or public identity migration remain separate actions requiring explicit authorization and implementation evidence.
