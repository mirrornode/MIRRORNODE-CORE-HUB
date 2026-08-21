# MIRRORNODE Resource Identity Profile v0.1

**Status:** Draft under CG-0036

## 1. Purpose

Authorization must target a stable resource identity rather than an ambiguous display name, provider label, repository alias, URL shortcut, or UI route.

## 2. Canonical identifier

A protected resource must have one canonical URI-like identifier within its registry namespace, for example:

`mirrornode://github/repository/MIRRORNODE-CORE-HUB`

The exact scheme/registry is not canonized by this draft; the invariant is that policy evaluation resolves to one canonical identifier before authorization.

## 3. Registry record

A resource registry entry should include:

- canonical resource ID;
- resource type;
- provider/system binding where applicable;
- immutable or versioned provider-native identifiers where available;
- environment/trust domain;
- permitted aliases;
- parent/child or namespace relationships;
- integrity/version metadata;
- authority required to modify the record.

## 4. Alias handling

Aliases are navigation metadata, not authorization identities.

Before evaluation:

1. alias resolves through the authoritative registry;
2. resolution must be unique;
3. resulting canonical ID is placed in the authorization request;
4. policy evaluates only the canonical ID/type and trusted properties.

Unknown or ambiguous aliases fail closed.

## 5. Audience restriction principle

A grant intended for one resource must not be reusable at another merely because the operation name or provider scope is similar. Target resource identity and action/scope remain separate authorization dimensions.

## 6. Registry integrity

Resource-registry changes capable of broadening an actor's reachable scope are high-impact authority changes. A delegate whose authority depends on a resource mapping may not unilaterally rewrite that mapping to increase its own access.

The registry must emit attributable change history and support integrity/version references usable in authorization receipts.

## 7. Decision binding

Every authorization decision MUST carry:

- `resource.canonical_uri` — the canonical URI after alias resolution;
- `resource.id` — MUST equal `resource.canonical_uri`;
- `resource.type` — MUST equal the registry record type for that URI;
- `resource_registry_ref` — the registry/version reference used by the PDP;
- `resource_registry_snapshot_hash` — SHA-256 (RFC 8785) of the immutable registry snapshot covering that mapping, including provider/native target;
- `resource_record_hash` — SHA-256 of the specific registry record for that canonical URI.

Operator and Council approvals MUST carry the same `resource_registry_ref`, `resource_registry_snapshot_hash`, and `resource_record_hash`, and the same `resource.canonical_uri`. These MUST equal the decision and the live registry mapping at PEP time.

Envelope `resource_scope` is an array of those canonical URIs. A decision resource is in-scope iff `resource.canonical_uri` is a member of the evaluated grant's `resource_scope` after alias resolution.

The PEP MUST verify the pending physical/provider target against the bound snapshot. Same canonical URI with a substituted provider/native identifier fails closed.

## 8. Tests

Required negative tests:

- stale `resource_registry_snapshot_hash`;
- substituted provider/native target under the same canonical URI;
- approval issued before remap, then presented after remap (Operator and Council);
- `resource.id` ≠ `resource.canonical_uri`;
- decision URI not in envelope `resource_scope`;
- alias that resolves to two canonical URIs.
