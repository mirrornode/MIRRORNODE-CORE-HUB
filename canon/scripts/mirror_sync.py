#!/usr/bin/env python3
# @mirror /lattice sync logic: full spectrum data packet
# Migrated from charter/sync.py

import os
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent.resolve()


def get_repo_state():
    try:
        import git
        repo = git.Repo(REPO_ROOT)
        return {
            "branch": repo.active_branch.name,
            "sha": repo.head.object.hexsha,
            "dirty": repo.is_dirty(),
            "untracked": repo.untracked_files,
        }
    except Exception as e:
        return {"error": str(e)}


def probe_endpoint(url):
    try:
        result = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url],
            capture_output=True,
            text=True,
            timeout=10,
        )
        return {"url": url, "status": int(result.stdout.strip()), "ok": result.returncode == 0}
    except Exception as e:
        return {"url": url, "status": None, "ok": False, "error": str(e)}


def build_packet():
    endpoints = [
        "https://mirrornode.xyz/standby/status",
        "https://api.mirrornode.xyz/standby/status",
    ]
    return {
        "source": "@mirror",
        "lattice": "LUCIAN + Oracle",
        "architect": "Sean (SRIITAG)",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sync_token": f"sync/{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}",
        "repo": get_repo_state(),
        "services": [probe_endpoint(url) for url in endpoints],
        "risk_posture": {
            "secrets_in_plain": False,
            "notes": "See repo and build logs for latest secrets scan.",
        },
        "charter_ratified": True,
        "charter_file": "canon/charters/MIRROR_SYNC.md",
    }


if __name__ == "__main__":
    packet = build_packet()
    dest = REPO_ROOT / "canon" / "dossiers" / f"mirror_sync_{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(packet, indent=2))
    print(f"@mirror lattice packet written to {dest}")
    print(json.dumps(packet, indent=2))
