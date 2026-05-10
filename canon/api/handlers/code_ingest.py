"""MIRRORNODE Canon — code.ingest Handler

CONTRACT REF: d742945 | MIRRORNODE-CORE-HUB | 2026-05-05

Handler for the code.ingest command.
Bind this to COMMANDS["code.ingest"].handler at runtime.

Do NOT bind at import time — handler assignment is always runtime-only.
"""

import hashlib
import json
from canon.contracts.sdk.audit import emit_audit


def handle_code_ingest(**kwargs) -> dict:
    """
    Ingest repository code change metadata into the canonical audit stream.

    Expected kwargs:
        repo        (str)   — repository name
        branch      (str)   — branch name
        commit      (str)   — commit SHA
        files       (list)  — list of dicts: {path, change_type, sha}
        timestamp   (str)   — ISO8601Z origination timestamp (optional)

    Returns:
        dict with audit_id, manifest_hash, repo_state_hash
    """
    repo = kwargs["repo"]
    branch = kwargs.get("branch", "unknown")
    commit = kwargs["commit"]
    files = kwargs.get("files", [])

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

    audit_id = emit_audit(
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

    return {
        "audit_id": audit_id,
        "manifest_hash": manifest_hash,
        "repo_state_hash": repo_state_hash,
    }
