"""MIRRORNODE Canon — Dev Trigger Routes

CONTRACT REF: 56752dad | MIRRORNODE-CORE-HUB | 2026-05-05

Temporary diagnostic routes for Phase 1 pipeline validation.
Remove or gate behind DEV_MODE env flag before production promotion.

Mount in your FastAPI app:
    from canon.api.dev.routes import router as dev_router
    app.include_router(dev_router, prefix="/dev")
"""

import os
from datetime import datetime, timezone

from fastapi import APIRouter

from canon.api.invoke import dispatch_command

router = APIRouter()


@router.post("/code-ingest")
async def dev_code_ingest():
    """
    Phase 1 trigger: fire a manual code.ingest event.

    Verify output:
        ls canon/dossiers/$(date +%Y-%m)/

    You are looking for:
        event_type: code_ingest
        manifest_hash: ...
        repo_state_hash: ...
        audit_id: ...
        verdict: SUCCESS
    """
    return dispatch_command(
        "code.ingest",
        {
            "repo": "MIRRORNODE-CORE-HUB",
            "branch": "main",
            "commit": "manual-test",
            "files": [
                {
                    "path": "canon/api/handlers/code_ingest.py",
                    "change_type": "modified",
                    "sha": "local",
                }
            ],
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )
