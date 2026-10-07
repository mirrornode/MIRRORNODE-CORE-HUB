# PR #57 exact-head npm audit receipt — 2026-10-07

**Status:** OBSERVED / retained evidence; no risk waiver, merge authority, or release authority  
**Platform repository:** `mirrornode/mirrornode-platform`  
**Platform PR:** #57  
**Exact source head:** `3fec902883ab90acc0a8d47bc080735e01aa75a6`  
**Observation session started:** `2026-10-07T20:09:50Z`  
**Execution environment:** Operator-local isolated temporary tree produced from the exact commit with `git archive`  
**Source repository modified:** NO

## Environment and source identity

- Node: `v20.20.2`
- npm: `10.8.2`
- Declared Node engine: `>=20.19.0 <21`
- `package.json` SHA-256: `e92fbd33893ebf71e7d3a5a08b3b7743160a2e97aa7438b6fd6c0efda023f862`
- `package-lock.json` SHA-256: `5f7c84ae0ebd4b8cc55372afd2841102ae5cea64a659b512b1bb75e2b2a5cf0d`

The exact-head source was exported into a temporary directory before installation. The working Platform repository was not used as the install target.

## Commands executed

```sh
npm ci --ignore-scripts --audit=false
npm audit --json
npm audit --omit=dev --json
npm ls braces --all
npm ls source-map-js --all
npm ls --omit=dev source-map-js --all
```

The first receipt wrapper reached a zsh-only capture error after a successful `npm ci`; the install/audit sequence was then rerun in the same isolated exact-head tree with portable exit-code capture. The results below are from that completed rerun.

## Installation result

`npm ci --ignore-scripts --audit=false`:

- exit: `0`
- packages added: `413`
- lifecycle scripts: disabled

## Full audit result

`npm audit --json`:

- exit: `1`
- info: `0`
- low: `0`
- moderate: `0`
- high: `6`
- critical: `0`
- total: `6`

Observed development-chain path:

```text
eslint-config-next@16.3.8
└─ @next/eslint-plugin-next@16.3.8
   └─ fast-glob@3.3.1
      └─ micromatch@4.0.8
         └─ braces@3.0.3
```

Observed `source-map-js` paths in the full tree:

```text
@tailwindcss/postcss@4.2.2
├─ @tailwindcss/node@4.2.2
│  └─ source-map-js@1.2.1
└─ postcss@8.5.28
   └─ source-map-js@1.2.1

next@16.3.8
└─ postcss@8.5.23
   └─ source-map-js@1.2.1
```

## Production-scope audit result

`npm audit --omit=dev --json`:

- exit: `1`
- info: `0`
- low: `0`
- moderate: `0`
- high: `1`
- critical: `0`
- total: `1`

Observed production dependency path:

```text
next@16.3.8
└─ postcss@8.5.23
   └─ source-map-js@1.2.1
```

This receipt establishes package-tree and audit observations for the isolated exact-head install. It does **not** establish deployed reachability, exploitability, provider/deployed tree equivalence, or remediation sufficiency.

## Retained local receipt hashes

The Operator-local receipt directory was:

```text
/Users/platform/Documents/MIRRORNODE/receipts/pr57-exact-head-audit-20261007T200950Z
```

SHA-256 values captured at completion:

```text
41f991e021e4aa89a056cbb5080916ff8f7782271cbd95634b8153056dcdb599  00-environment.txt
6eea65698f85a4a4bbed56ce734b6df3d18d8ecc9d51c3cb2c861b82646f4e6b  01-npm-ci.txt
5c9c038b978a2caee396b0f4bd2d807b784afebd9641bbd850494a7c5fdb8027  02-audit-full.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  02-audit-full.stderr
9f9005c52860dcc99f46585626b3c19e9c46e620569e22f927ae91f70700adb5  03-audit-prod.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  03-audit-prod.stderr
fadd19d9f2b7e09036f19963b03c533ffb2dbacda1deed886ed2b4a50ee0e8cc  04-dependency-paths.txt
a6459158a38cd4997989402b62524b391ae7b1b7153e445ec498321d506684dd  05-summary.json
```

Empty stderr files hash to the standard SHA-256 empty-file value shown above.

## Bounded disposition

This receipt substantiates the exact-head isolated install/audit claims used by the companion continuity record. It does not clear the six-high/full or one-high/production findings, and it does not resolve deployed containment, consumer compatibility, historical credential revocation, qualifying review, merge, or release gates.
