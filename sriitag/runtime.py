import sys, os, time, json, hashlib
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))
os.environ.setdefault("CANON_ROOT", str(Path(__file__).parent.parent / "canon"))

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Optional
import httpx

from canon.contracts.sdk.audit import emit_audit

VERSION = "1.0.0"
BOOT_TIME = datetime.now(timezone.utc).isoformat()
CANON_ROOT = Path(os.environ["CANON_ROOT"])
LUCIAN_URL = f"http://localhost:{os.environ.get('LUCIAN_PORT', 7700)}"
ORACLE_URL  = f"http://localhost:{os.environ.get('ORACLE_PORT',  7707)}"

# SRIITAG operator token — set SRIITAG_TOKEN in .env
SRIITAG_TOKEN = os.environ.get("SRIITAG_TOKEN", "")

app = FastAPI(title="SRIITAG", description="Operator Trust Boundary — Sean Malm, Architect")

# High-risk commands that require SRIITAG sign-off before Lucian can dispatch
GUARDED_COMMANDS = {"halt", "audit-emit"}


def _audit(event: str, verdict: str, evidence: dict):
    evidence.setdefault("error", None)
    emit_audit(repo="sriitag", event_type="execution", actor="operator",
               verdict=verdict, evidence={"event": event, **evidence})


def _verify_token(token: str):
    if not SRIITAG_TOKEN:
        raise HTTPException(status_code=503, detail="SRIITAG_TOKEN not configured")
    if token != SRIITAG_TOKEN:
        _audit("auth_failure", "FAILURE", {"error": "Invalid operator token"})
        raise HTTPException(status_code=403, detail="Invalid operator token")


# ── Models ─────────────────────────────────────────────────────────────────
class ApprovalRequest(BaseModel):
    command: str
    kwargs: Optional[dict] = {}
    rationale: str  # operator must state why

class RiskPostureRequest(BaseModel):
    level: str  # NORMAL | ELEVATED | CRITICAL
    notes: Optional[str] = None


# ── Core ─────────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    return {"agent": "sriitag", "status": "alive", "version": VERSION,
            "boot_time": BOOT_TIME, "ts": datetime.now(timezone.utc).isoformat()}

@app.get("/identity")
def identity():
    return {
        "authority": "SRIITAG",
        "operator": "Sean Malm",
        "role": "Architect / Trust Boundary / Final Arbiter",
        "version": VERSION,
        "guarded_commands": list(GUARDED_COMMANDS),
        "charter": "canon/charters/MIRROR_SYNC.md",
    }


# ── Approve ──────────────────────────────────────────────────────────────
@app.post("/approve")
def approve(req: ApprovalRequest, x_sriitag_token: str = Header(...)):
    """Operator sign-off on a guarded command. Routes to Lucian after approval."""
    _verify_token(x_sriitag_token)

    approval_id = hashlib.sha256(
        f"{req.command}{req.rationale}{datetime.now(timezone.utc).isoformat()}".encode()
    ).hexdigest()[:16]

    _audit("approval_granted", "SUCCESS", {
        "command": req.command,
        "approval_id": approval_id,
        "rationale": req.rationale,
    })

    # Forward to Lucian dispatch
    try:
        with httpx.Client(timeout=5.0) as client:
            r = client.post(f"{LUCIAN_URL}/dispatch",
                            json={"command": req.command, "kwargs": req.kwargs})
            result = r.json()
    except Exception as e:
        _audit("dispatch_failed", "FAILURE", {"command": req.command, "error": str(e)})
        raise HTTPException(status_code=502, detail=f"Lucian unreachable: {e}")

    return {
        "approval_id": approval_id,
        "command": req.command,
        "rationale": req.rationale,
        "ts": datetime.now(timezone.utc).isoformat(),
        "dispatch_result": result,
    }


# ── Risk posture ──────────────────────────────────────────────────────────
RISK_STATE_PATH = CANON_ROOT / "state" / "risk_posture.json"

@app.post("/risk")
def set_risk(req: RiskPostureRequest, x_sriitag_token: str = Header(...)):
    """Operator sets the current lattice risk posture. Persisted to canon/state."""
    _verify_token(x_sriitag_token)
    valid = {"NORMAL", "ELEVATED", "CRITICAL"}
    if req.level not in valid:
        raise HTTPException(status_code=400, detail=f"level must be one of {valid}")
    state = {
        "level": req.level,
        "notes": req.notes,
        "set_by": "SRIITAG",
        "ts": datetime.now(timezone.utc).isoformat(),
    }
    RISK_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    RISK_STATE_PATH.write_text(json.dumps(state, indent=2))
    _audit("risk_posture_set", "SUCCESS", {"level": req.level})
    return state

@app.get("/risk")
def get_risk():
    """Return current risk posture."""
    if not RISK_STATE_PATH.exists():
        return {"level": "NORMAL", "notes": "Default — not explicitly set", "ts": None}
    return json.loads(RISK_STATE_PATH.read_text())


# ── Situation room ──────────────────────────────────────────────────────────
@app.get("/situation")
def situation():
    """The real situation room — pulls Oracle watch + Lucian manifest. Verified state only."""
    data = {"ts": datetime.now(timezone.utc).isoformat(), "operator": "Sean Malm (SRIITAG)"}
    try:
        with httpx.Client(timeout=3.0) as client:
            data["oracle_watch"] = client.get(f"{ORACLE_URL}/watch").json()
            data["lucian_manifest"] = client.get(f"{LUCIAN_URL}/manifest").json()
            data["risk_posture"] = get_risk()
    except Exception as e:
        data["error"] = str(e)
    _audit("situation_room", "SUCCESS", {})
    return data


if __name__ == "__main__":
    import uvicorn
    print("[SRIITAG] Booting — Operator Trust Boundary")
    _audit("boot", "SUCCESS", {"version": VERSION})
    uvicorn.run(app, host="0.0.0.0", port=7708)
