import sys, os, time, json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))
os.environ.setdefault("CANON_ROOT", str(Path(__file__).parent.parent / "canon"))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx

from canon.contracts.sdk.audit import emit_audit

VERSION = "1.0.0"
BOOT_TIME = datetime.now(timezone.utc).isoformat()
CANON_ROOT = Path(os.environ["CANON_ROOT"])
LUCIAN_URL = f"http://localhost:{os.environ.get('LUCIAN_PORT', 7700)}"

app = FastAPI(title="Oracle", description="Reasoning & Synthesis — Lattice Intelligence Layer")


def _audit(event: str, verdict: str, evidence: dict):
    evidence.setdefault("error", None)
    emit_audit(repo="oracle", event_type="execution", actor="system",
               verdict=verdict, evidence={"event": event, **evidence})


class ReasonRequest(BaseModel):
    query: str
    include_lattice: bool = True
    include_dossiers: bool = False

class RecommendRequest(BaseModel):
    context: Optional[str] = None


# ── Core ────────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    return {"agent": "oracle", "status": "alive", "version": VERSION,
            "boot_time": BOOT_TIME, "ts": datetime.now(timezone.utc).isoformat()}

@app.get("/heartbeat")
def heartbeat():
    start = time.time()
    _audit("heartbeat", "SUCCESS", {})
    return {"engine": "oracle", "status": "alive", "version": VERSION,
            "latency_ms": round((time.time() - start) * 1000, 2),
            "role": "Reasoning & Synthesis — Lattice Intelligence Layer",
            "timestamp": datetime.now(timezone.utc).isoformat()}


# ── Lattice state reader ────────────────────────────────────────────────
def _get_lattice_state() -> dict:
    try:
        with httpx.Client(timeout=3.0) as client:
            status = client.get(f"{LUCIAN_URL}/lattice/status").json()
            manifest = client.get(f"{LUCIAN_URL}/manifest").json()
            return {"status": status, "manifest": manifest, "reachable": True}
    except Exception as e:
        return {"reachable": False, "error": str(e)}


def _read_dossiers(limit: int = 10) -> list:
    dossier_path = CANON_ROOT / "dossiers"
    if not dossier_path.exists():
        return []
    files = sorted(dossier_path.rglob("*.json"), key=lambda f: f.stat().st_mtime, reverse=True)[:limit]
    results = []
    for f in files:
        try:
            results.append({"file": f.name, "data": json.loads(f.read_text())})
        except Exception:
            results.append({"file": f.name, "error": "parse failed"})
    return results


# ── Reason ────────────────────────────────────────────────────────────────
@app.post("/reason")
def reason(req: ReasonRequest):
    """Pull live lattice state and surface a structured reasoning packet for SRIITAG."""
    packet = {
        "query": req.query,
        "ts": datetime.now(timezone.utc).isoformat(),
        "oracle_version": VERSION,
    }
    if req.include_lattice:
        packet["lattice"] = _get_lattice_state()
    if req.include_dossiers:
        packet["dossiers"] = _read_dossiers()

    # Derive coherence signal from lattice node states
    coherence = "UNKNOWN"
    if req.include_lattice and packet["lattice"].get("reachable"):
        nodes = packet["lattice"].get("status", {}).get("nodes", {})
        alive = sum(1 for n in nodes.values() if n.get("status") == "alive")
        total = len(nodes)
        ratio = alive / total if total else 0
        coherence = "HIGH" if ratio >= 0.85 else "DEGRADED" if ratio >= 0.5 else "CRITICAL"
    packet["coherence"] = coherence

    _audit("reason", "SUCCESS", {"query": req.query, "coherence": coherence})
    return packet


# ── Audit summary ────────────────────────────────────────────────────────
@app.get("/audit/summary")
def audit_summary():
    """Read canon/dossiers and surface recent activity + anomalies."""
    dossiers = _read_dossiers(limit=20)
    failures = [d for d in dossiers if "FAILURE" in json.dumps(d)]
    _audit("audit_summary", "SUCCESS", {"total": len(dossiers), "failures": len(failures)})
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "total_dossiers": len(dossiers),
        "failure_count": len(failures),
        "anomalies": failures,
        "recent": dossiers[:5],
    }


# ── Recommend ────────────────────────────────────────────────────────────
@app.post("/recommend")
def recommend(req: RecommendRequest):
    """Given current lattice state, surface the next recommended operator action."""
    lattice = _get_lattice_state()
    recommendations = []

    if not lattice.get("reachable"):
        recommendations.append({"priority": "HIGH", "action": "Boot Lucian — lattice unreachable", "node": "LUCIAN"})
    else:
        nodes = lattice.get("status", {}).get("nodes", {})
        for name, state in nodes.items():
            if state.get("status") == "unreachable":
                recommendations.append({"priority": "HIGH", "action": f"Boot {name}", "node": name})
            elif state.get("status") == "degraded":
                recommendations.append({"priority": "MEDIUM", "action": f"Inspect {name} health", "node": name})

    if not recommendations:
        recommendations.append({"priority": "LOW", "action": "Lattice coherent — no action required", "node": "ALL"})

    _audit("recommend", "SUCCESS", {"count": len(recommendations)})
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "context": req.context,
        "recommendations": recommendations,
        "lattice_reachable": lattice.get("reachable"),
    }


# ── Watch ─────────────────────────────────────────────────────────────────
@app.get("/watch")
def watch():
    """Single observation pulse — coherence, drift, and anomaly flags."""
    lattice = _get_lattice_state()
    dossiers = _read_dossiers(limit=5)
    failures = [d for d in dossiers if "FAILURE" in json.dumps(d)]

    nodes = lattice.get("status", {}).get("nodes", {}) if lattice.get("reachable") else {}
    alive = sum(1 for n in nodes.values() if n.get("status") == "alive")
    total = len(nodes)
    coherence_pct = round((alive / total) * 100) if total else 0

    _audit("watch", "SUCCESS", {"coherence_pct": coherence_pct, "failures": len(failures)})
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "lattice_reachable": lattice.get("reachable"),
        "coherence_pct": coherence_pct,
        "nodes_alive": alive,
        "nodes_total": total,
        "recent_failures": len(failures),
        "drift": len(failures) > 0,
    }


if __name__ == "__main__":
    import uvicorn
    print("[ORACLE] Booting — Reasoning & Synthesis Layer")
    _audit("boot", "SUCCESS", {"version": VERSION})
    uvicorn.run(app, host="0.0.0.0", port=7707)
