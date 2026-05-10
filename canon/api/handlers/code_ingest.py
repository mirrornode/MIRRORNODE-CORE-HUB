"""MIRRORNODE Canon — code.ingest Handler

CONTRACT REF: bf0dba8 | MIRRORNODE-CORE-HUB | 2026-05-09

Handler for the code.ingest command.
Bind this to COMMANDS["code.ingest"].handler at runtime.

Do NOT bind at import time — handler assignment is always runtime-only.

Chain: code_ingest → execution → trace
On SUCCESS, automatically calls handle_execution and handle_trace,
returning the full chain as a single response.
"""

import hashlib
import json
from canon.contracts.sdk.audit import emit_audit
from canon.api.handlers.execution import handle_execution
from canon.api.handlers.trace import handle_trace


def handle_code_ingest(**kwargs) -> dict:
    """
    Ingest repository code change metadata into the canonical audit stream.
    On success, automatically chains into execution → trace.

    Expected kwargs:
        repo        (str)   — repository name
        branch      (str)   — branch name
        commit      (str)   — commit SHA
        files       (list)  — list of dicts: {path, change_type, sha}
        node        (str)   — lattice node (default: "CORE-HUB")
        timestamp   (str)   — ISO8601Z origination timestamp (optional)

    Returns:
        dict with full chain: ingest, execution, trace audit IDs + hashes
    """
    repo = kwargs["repo"]
    branch = kwargs.get("branch", "unknown")
    commit = kwargs["commit"]
    files = kwargs.get("files", [])
    node = kwargs.get("node", "CORE-HUB")

    # Build lean file manifest — metadata + sha only, no content
    file_manifest = [
        {
            "path": f["path"],
            "change_type": f["change_type"],
            "sha": f.get("sha", ""),
        }
        for f in files
    ]

    # Deterministic hash of the full file manifest
    manifest_hash = hashlib.sha256(
        json.dumps(file_manifest, sort_keys=True).encode()
    ).hexdigest()

    # Cheap global fingerprint of repo state at this event
    repo_state_hash = hashlib.sha256(
        f"{repo}:{branch}:{commit}".encode()
    ).hexdigest()

    # ── 1. Emit code_ingest ─────────────────────────────────────────────────
    ingest_audit_id = emit_audit(
        repo=repo,
        event_type="code_ingest",
        actor="agent",
        verdict="SUCCESS",
        evidence={
            "inputs": {
                "event": "code.ingest",
                "branch": branch,
                "commit": commit,
                "file_count": len(files),
                "manifest_hash": manifest_hash,
                "repo_state_hash": repo_state_hash,
            },
            "outputs": {},
            "duration_ms": 0,
            "error": None,
        },
    )

    # ── 2. Chain → execution ────────────────────────────────────────────────
    execution_result = handle_execution(
        repo=repo,
        command="code.ingest",
        node=node,
        parent_audit_id=ingest_audit_id,
        commit=commit,
        branch=branch,
    )

    # ── 3. Chain → trace ────────────────────────────────────────────────────
    trace_result = handle_trace(
        repo=repo,
        root_audit_id=ingest_audit_id,
        parent_audit_id=execution_result["audit_id"],
        execution_hash=execution_result["execution_hash"],
        manifest_hash=manifest_hash,
        repo_state_hash=repo_state_hash,
    )

    return {
        "chain": [
            {"event": "code_ingest",  "audit_id": ingest_audit_id},
            {"event": "execution",    "audit_id": execution_result["audit_id"]},
            {"event": "trace",        "audit_id": trace_result["audit_id"]},
        ],
        "manifest_hash": manifest_hash,
        "repo_state_hash": repo_state_hash,
        "execution_hash": execution_result["execution_hash"],
        "chain_hash": trace_result["chain_hash"],
    }
