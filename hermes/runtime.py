import sys, os, time
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Dict, Optional

sys.path.insert(0, str(Path(__file__).parent.parent))
os.environ.setdefault("CANON_ROOT", str(Path(__file__).parent.parent / "canon"))

from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from pydantic import BaseModel
from canon.contracts.sdk.audit import emit_audit

CHARTER_PATH = Path(os.environ["CANON_ROOT"]) / "charters" / "HERMES.md"
VERSION = "1.0.0"
BOOT_TIME = datetime.now(timezone.utc).isoformat()

# In-memory message queue (swap for Redis later)
message_queue: list = []

app = FastAPI(title="Hermes", description="Messenger & API Bridge — Communication Layer")

class OutboundRequest(BaseModel):
    url: str
    method: str = "POST"
    payload: Dict[str, Any] = {}
    headers: Dict[str, str] = {}

class RouteMessage(BaseModel):
    from_agent: str
    to_agent: str
    message_type: str
    payload: Dict[str, Any]
    priority: int = 5  # 1 (highest) to 10 (lowest)

@app.get("/health")
def health():
    return {
        "agent": "hermes",
        "role": "Messenger & API Bridge — Communication Layer",
        "status": "alive",
        "queue_depth": len(message_queue),
        "boot_time": BOOT_TIME,
        "ts": datetime.now(timezone.utc).isoformat()
    }

@app.get("/heartbeat")
def heartbeat():
    start = time.time()
    emit_audit(repo="hermes", event_type="agent_invocation",
               actor="system", verdict="SUCCESS",
               evidence={"event": "heartbeat", "error": None})
    latency_ms = round((time.time() - start) * 1000, 2)
    return {
        "engine": "hermes",
        "status": "alive",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "latency_ms": latency_ms,
        "version": VERSION,
        "queue_depth": len(message_queue),
        "role": "Messenger & API Bridge — Communication Layer"
    }

@app.get("/identity")
def identity():
    charter_text = CHARTER_PATH.read_text() if CHARTER_PATH.exists() else "Charter pending"
    return {"agent": "hermes", "charter": charter_text}

@app.post("/ingest")
async def ingest_webhook(request: Request, background_tasks: BackgroundTasks):
    """Ingest any inbound webhook and queue for routing."""
    body = await request.json()
    source = request.headers.get("x-source", "unknown")
    message = {
        "id": f"msg-{datetime.now(timezone.utc).timestamp()}",
        "received_at": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "payload": body,
        "status": "queued"
    }
    message_queue.append(message)
    emit_audit(repo="hermes", event_type="agent_invocation", actor="system",
               verdict="SUCCESS",
               evidence={"event": "webhook_ingested", "source": source,
                          "message_id": message["id"], "error": None})
    return {"received": True, "message_id": message["id"], "queue_depth": len(message_queue)}

@app.post("/route")
def route_message(msg: RouteMessage):
    """Route a message between lattice agents."""
    queued = {
        "id": f"msg-{datetime.now(timezone.utc).timestamp()}",
        "from": msg.from_agent,
        "to": msg.to_agent,
        "type": msg.message_type,
        "payload": msg.payload,
        "priority": msg.priority,
        "queued_at": datetime.now(timezone.utc).isoformat(),
        "status": "queued"
    }
    message_queue.append(queued)
    emit_audit(repo="hermes", event_type="agent_invocation", actor="system",
               verdict="SUCCESS",
               evidence={"event": "message_routed",
                          "from": msg.from_agent, "to": msg.to_agent,
                          "type": msg.message_type, "error": None})
    return {"routed": True, "message_id": queued["id"]}

@app.get("/queue")
def get_queue():
    """Inspect the current message queue."""
    return {"depth": len(message_queue), "messages": message_queue[-20:]}

@app.delete("/queue")
def flush_queue():
    """Flush the message queue (admin operation)."""
    count = len(message_queue)
    message_queue.clear()
    emit_audit(repo="hermes", event_type="execution", actor="system",
               verdict="SUCCESS",
               evidence={"event": "queue_flushed", "count": count, "error": None})
    return {"flushed": count}

if __name__ == "__main__":
    import uvicorn
    print("[HERMES] Booting — Messenger & API Bridge Communication Layer")
    emit_audit(repo="hermes", event_type="execution", actor="system",
               verdict="SUCCESS", evidence={"event": "boot", "error": None})
    uvicorn.run(app, host="0.0.0.0", port=7702)
