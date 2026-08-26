# Hermes Spine Sequence v0.1

**Status:** Working sequence / non-canonical

1. Truth semantics: remove manufactured success and ambiguous routing claims.
2. Authority boundary: require governed invocation context before executable dispatch.
3. Durable transport: implement persistence, retry, replay, dead-letter, idempotency, and consumer acknowledgement against the provider-neutral contract.
4. Evidence binding: emit canonical transition receipts and operation/journey correlation.
5. MOPCON projection: surface lifecycle and failure-domain state without making MOPCON a substitute transport authority.
6. Provider qualification: evaluate TRANSPORT and EXECUTION candidates independently under MICC; no provider promotion by convenience.
7. Production conformance: restart, duplicate-delivery, retry, dead-letter, unknown-state, stale-authority, and approval-boundary tests.

The sequence is ordered so later infrastructure cannot harden false semantics into production behavior.
