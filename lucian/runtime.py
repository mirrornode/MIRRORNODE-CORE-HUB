import sys, os, time
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))
os.environ.setdefault("CANON_ROOT", str(Path(__file__).parent.parent / "canon"))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx

from canon.contracts.sdk.audit import emit_audit
from canon.api.invoke import invoke
from canon.api.commands import list_commands

CHARTER_PATH = Path(os.environ["CANON_ROOT"]) / "charters" / "LUCIAN_PRIME.md"
VERSION = "2.0.0"
BOOT_TIME = datetime.now(timezone.utc).isoformat()

app = FastAPI(title="Lucian", description="Audit Oversight & Lattice Coherence Authority")

# ── Node registry ───────────────────────────────────────────────────────────
LATTICE_NODES = {
    "LUCIAN":  {"layer": 1, "role": "Orchestration & Manifest",            "port": int(os.environ.get("LUCIAN_PORT",  7700))},
    "OSIRIS":  {"layer": 2, "role": "Payment & Commerce",                  "port": int(os.environ.get("OSIRIS_PORT",  7701))},
    "HERMES":  {"layer": 2, "role": "Messaging & Protocol",                "port": int(os.environ.get("HERMES_PORT",  7702))},
    "THOTH":   {"layer": 2, "role": "Services & Health",                   "port": int(os.environ.get("THOTH_PORT",   7703))},
    "THEIA":   {"layer": 3, "role": "Witness & Observation",               "port": int(os.environ.get("THEIA_PORT",   7704))},
    "PTAH":    {"layer": 3, "role": "Creation & Bridge",                   "port": int(os.environ.get("PTAH_PORT",    7705))},
    "EVE":     {"layer": 3, "role": "Embodiment & Physical Manifest",      "port": int(os.environ.get("EVE_PORT",     7706))},
}


def _audit(event: str, verdict: str, evidence: dict):
    evidence.setdefault("error", None)
    emit_audit(repo="lucian", event_type="execution", actor="system",
               verdict=verdict, evidence={"event": event, **evidence})


# ── Models ─────────────────────────────────────────────────────────────────
class DispatchRequest(BaseModel):
    command: str
    kwargs: Optional[dict] = {}


# ── Core routes ───────────────────────────────────────────────────────────
@app.get("/health")
def health():
    return {
        "agent": "lucian",
        "status": "alive",
        "version": VERSION,
        "boot_time": BOOT_TIME,
        "ts": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/heartbeat")
def heartbeat():
    start = time.time()
    _audit("heartbeat", "SUCCESS", {})
    latency_ms = round((time.time() - start) * 1000, 2)
    return {
        "engine": "lucian",
        "status": "alive",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "latency_ms": latency_ms,
        "version": VERSION,
        "role": "Audit Oversight & Lattice Coherence Authority",
    }

@app.get("/identity")
def identity():
    if not CHARTER_PATH.exists():
        return {"error": "Charter not found", "path": str(CHARTER_PATH)}
    return {"agent": "lucian", "charter": CHARTER_PATH.read_text(), "charter_path": str(CHARTER_PATH)}


# ── Manifest ────────────────────────────────────────────────────────────────
@app.get("/manifest")
def manifest():
    """Declared state of the lattice — single source of truth."""
    commands = [{"name": c.name, "node": c.node, "category": c.category, "description": c.description}
                for c in list_commands()]
    return {
        "lattice": "MIRRORNODE",
        "version": VERSION,
        "boot_time": BOOT_TIME,
        "architect": "Sean Malm (SRIITAG)",
        "charter": str(CHARTER_PATH),
        "nodes": LATTICE_NODES,
        "commands": commands,
        "canon_root": os.environ.get("CANON_ROOT"),
        "ts": datetime.now(timezone.utc).isoformat(),
    }


# ── Dispatch ────────────────────────────────────────────────────────────────
@app.post("/dispatch")
def dispatch(req: DispatchRequest):
    """Route a command from the canon palette through Lucian to the target node."""
    result = invoke(req.command, **(req.kwargs or {}))
    _audit("dispatch", "SUCCESS" if result.success else "FAILURE", {
        "command": req.command,
        "node": result.node,
        "invocation_id": result.invocation_id,
        "success": result.success,
    })
    return result.to_dict()


# ── Lattice status ──────────────────────────────────────────────────────────
@app.get("/lattice/status")
def lattice_status():
    """Fan out health checks to all registered nodes. Returns unified lattice snapshot."""
    results = {}
    for name, meta in LATTICE_NODES.items():
        if name == "LUCIAN":
            results[name] = {"status": "alive", "layer": meta["layer"], "role": meta["role"], "self": True}
            continue
        url = f"http://localhost:{meta['port']}/health"
        try:
            with httpx.Client(timeout=2.0) as client:
                r = client.get(url)
                results[name] = {
                    "status": "alive" if r.status_code == 200 else "degraded",
                    "http_status": r.status_code,
                    "layer": meta["layer"],
                    "role": meta["role"],
                }
        except Exception as e:
            results[name] = {
                "status": "unreachable",
                "error": str(e),
                "layer": meta["layer"],
                "role": meta["role"],
            }
    _audit("lattice_status", "SUCCESS", {"nodes_checked": len(results)})
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "version": VERSION,
        "nodes": results,
    }


if __name__ == "__main__":
    import uvicorn
    print("[LUCIAN] Booting v2.0.0 — Audit Oversight & Lattice Coherence Authority")
    _audit("boot", "SUCCESS", {"version": VERSION})
    uvicorn.run(app, host="0.0.0.0", port=7700)
