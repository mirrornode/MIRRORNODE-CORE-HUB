"""MIRRORNODE Canon — execution Handler

CONTRACT REF: bf0dba8 | MIRRORNODE-CORE-HUB | 2026-05-09

Handler for the execution event in the audit chain.
Called automatically by code_ingest on SUCCESS — not invoked directly.

Do NOT bind at import time — handler assignment is always runtime-only.
"""

import hashlib
from canon.contracts.sdk.audit import emit_audit


def handle_execution(
    repo: str,
    command: str,
    node: str,
    parent_audit_id: str,
    commit: str,
    branch: str,
    actor: str = "agent",
) -> dict:
    """
    Emit an execution audit event linked to a parent ingest event.

    Args:
        repo            — repository name
        command         — canonical command that triggered execution (e.g. "code.ingest")
        node            — lattice node that executed (e.g. "CORE-HUB")
        parent_audit_id — audit_id from the preceding code_ingest event
        commit          — commit SHA being executed against
        branch          — branch name
        actor           — executing actor (default: "agent")

    Returns:
        dict with audit_id, execution_hash, parent_audit_id
    """
    execution_hash = hashlib.sha256(
        f"{repo}:{command}:{node}:{commit}:{parent_audit_id}".encode()
    ).hexdigest()

    audit_id = emit_audit(
        repo=repo,
        event_type="execution",
        actor=actor,
        verdict="SUCCESS",
        evidence={
            "inputs": {
                "command": command,
                "node": node,
                "branch": branch,
                "commit": commit,
                "parent_audit_id": parent_audit_id,
                "execution_hash": execution_hash,
            },
            "outputs": {},
            "duration_ms": 0,
            "error": None,
        },
    )

    return {
        "audit_id": audit_id,
        "execution_hash": execution_hash,
        "parent_audit_id": parent_audit_id,
    }
