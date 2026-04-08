import sys, os
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))
os.environ.setdefault("CANON_ROOT", str(Path(__file__).parent.parent / "canon"))

from fastapi import FastAPI
from canon.contracts.sdk.audit import emit_audit

CHARTER_PATH = Path(os.environ["CANON_ROOT"]) / "charters" / "LUCIAN_PRIME.md"

app = FastAPI(title="Lucian", description="Audit Oversight & Lattice Coherence Authority")

BOOT_TIME = datetime.now(timezone.utc).isoformat()

@app.get("/health")
def health():
    return {
        "agent": "lucian",
        "role": "Audit Oversight & Lattice Coherence Authority",
        "status": "alive",
        "boot_time": BOOT_TIME,
        "ts": datetime.now(timezone.utc).isoformat()
    }

@app.get("/heartbeat")
def heartbeat():
    emit_audit(
        repo="lucian",
        event_type="agent_invocation",
        actor="system",
        verdict="SUCCESS",
        evidence={"event": "heartbeat", "error": None}
    )
    return {"agent": "lucian", "pulse": True, "ts": datetime.now(timezone.utc).isoformat()}

@app.get("/identity")
def identity():
    if not CHARTER_PATH.exists():
        return {"error": "Charter not found", "path": str(CHARTER_PATH)}
    return {
        "agent": "lucian",
        "charter": CHARTER_PATH.read_text(),
        "charter_path": str(CHARTER_PATH)
    }

if __name__ == "__main__":
    import uvicorn
    print("[LUCIAN] Runtime starting — Audit Oversight & Lattice Coherence Authority")
    emit_audit(
        repo="lucian",
        event_type="execution",
        actor="system",
        verdict="SUCCESS",
        evidence={"event": "boot", "error": None}
    )
    uvicorn.run(app, host="0.0.0.0", port=7700)
