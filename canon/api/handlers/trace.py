"""MIRRORNODE Canon — trace Handler

CONTRACT REF: bf0dba8 | MIRRORNODE-CORE-HUB | 2026-05-09

Handler for the trace event — closes the audit chain.
Called automatically by execution on SUCCESS — not invoked directly.

A trace event is the terminal link in the chain:
    code_ingest (audit_id_1)
        → execution (audit_id_2, parent=audit_id_1)
            → trace (audit_id_3, parent=audit_id_2, root=audit_id_1)

Do NOT bind at import time — handler assignment is always runtime-only.
"""

import hashlib
from canon.contracts.sdk.audit import emit_audit


def handle_trace(
    repo: str,
    root_audit_id: str,
    parent_audit_id: str,
    execution_hash: str,
    manifest_hash: str,
    repo_state_hash: str,
    actor: str = "agent",
) -> dict:
    """
    Emit a trace audit event that closes and seals the audit chain.

    Args:
        repo             — repository name
        root_audit_id    — audit_id of the originating code_ingest event
        parent_audit_id  — audit_id of the preceding execution event
        execution_hash   — execution_hash from the execution event
        manifest_hash    — manifest_hash from the originating code_ingest
        repo_state_hash  — repo_state_hash from the originating code_ingest
        actor            — executing actor (default: "agent")

    Returns:
        dict with audit_id, chain_hash, root_audit_id, parent_audit_id
    """
    # Chain hash ties all three events into one verifiable fingerprint
    chain_hash = hashlib.sha256(
        f"{root_audit_id}:{parent_audit_id}:{execution_hash}:{manifest_hash}:{repo_state_hash}".encode()
    ).hexdigest()

    audit_id = emit_audit(
        repo=repo,
        event_type="trace",
        actor=actor,
        verdict="SUCCESS",
        evidence={
            "inputs": {
                "root_audit_id": root_audit_id,
                "parent_audit_id": parent_audit_id,
                "execution_hash": execution_hash,
                "manifest_hash": manifest_hash,
                "repo_state_hash": repo_state_hash,
                "chain_hash": chain_hash,
            },
            "outputs": {},
            "duration_ms": 0,
            "error": None,
        },
    )

    return {
        "audit_id": audit_id,
        "chain_hash": chain_hash,
        "root_audit_id": root_audit_id,
        "parent_audit_id": parent_audit_id,
    }
