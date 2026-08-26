import sys, os, time, uuid
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Dict

sys.path.insert(0, str(Path(__file__).parent.parent))
os.environ.setdefault("CANON_ROOT", str(Path(__file__).parent.parent / "canon"))

from fastapi import FastAPI, Request
from pydantic import BaseModel
from canon.contracts.sdk.audit import emit_audit

CHARTER_PATH = Path(os.environ["CANON_ROOT"]) / "charters" / "HERMES.md"
VERSION = "1.0.0"
BOOT_TIME = datetime.now(timezone.utc).isoformat()
TRANSPORT_MODE = "volatile_memory"
PROTOTYPE_STATE = "VOLATILE_BUFFERED"

# Development prototype only. This list is process-local and non-durable.
# It must never be reported as persistent transport or confirmed delivery.
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


def _new_message_id() -> str:
    return f"msg-{uuid.uuid4()}"


@app.get("/health")
def health():
    return {
        "agent": "hermes",
        "role": "Messenger & API Bridge — Communication Layer",
        "status": "alive",
        "transport_mode": TRANSPORT_MODE,
        "durable": False,
        "queue_depth": len(message_queue),
        "boot_time": BOOT_TIME,
        "ts": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/heartbeat")
def heartbeat():
    start = time.time()
    emit_audit(
        repo="hermes",
        event_type="agent_invocation",
        actor="system",
        verdict="SUCCESS",
        evidence={
            "event": "heartbeat",
            "transport_mode": TRANSPORT_MODE,
            "durable": False,
            "error": None,
        },
    )
    latency_ms = round((time.time() - start) * 1000, 2)
    return {
        "engine": "hermes",
        "status": "alive",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "latency_ms": latency_ms,
        "version": VERSION,
        "transport_mode": TRANSPORT_MODE,
        "durable": False,
        "queue_depth": len(message_queue),
        "role": "Messenger & API Bridge — Communication Layer",
    }


@app.get("/identity")
def identity():
    charter_text = CHARTER_PATH.read_text() if CHARTER_PATH.exists() else "Charter pending"
    return {"agent": "hermes", "charter": charter_text}


@app.post("/ingest", status_code=202)
async def ingest_webhook(request: Request):
    """Buffer an inbound webhook in volatile process memory; no canonical transport state is claimed."""
    body = await request.json()
    source = request.headers.get("x-source", "unknown")
    message = {
        "id": _new_message_id(),
        "received_at": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "payload": body,
        "prototype_state": PROTOTYPE_STATE,
        "transport_state": None,
        "durable": False,
        "delivered": False,
    }
    message_queue.append(message)
    emit_audit(
        repo="hermes",
        event_type="agent_invocation",
        actor="system",
        verdict="SUCCESS",
        evidence={
            "event": "webhook_buffered_volatile",
            "source": source,
            "message_id": message["id"],
            "prototype_state": PROTOTYPE_STATE,
            "transport_state": None,
            "transport_mode": TRANSPORT_MODE,
            "durable": False,
            "delivered": False,
            "error": None,
        },
    )
    return {
        "buffered": True,
        "message_id": message["id"],
        "prototype_state": PROTOTYPE_STATE,
        "transport_state": None,
        "transport_mode": TRANSPORT_MODE,
        "durable": False,
        "delivered": False,
        "queue_depth": len(message_queue),
    }


@app.post("/route", status_code=202)
def route_message(msg: RouteMessage):
    """Buffer a message in volatile process memory; no routing or delivery occurs."""
    buffered = {
        "id": _new_message_id(),
        "from": msg.from_agent,
        "to": msg.to_agent,
        "type": msg.message_type,
        "payload": msg.payload,
        "priority": msg.priority,
        "buffered_at": datetime.now(timezone.utc).isoformat(),
        "prototype_state": PROTOTYPE_STATE,
        "transport_state": None,
        "durable": False,
        "delivered": False,
    }
    message_queue.append(buffered)
    emit_audit(
        repo="hermes",
        event_type="agent_invocation",
        actor="system",
        verdict="SUCCESS",
        evidence={
            "event": "message_buffered_volatile",
            "from": msg.from_agent,
            "to": msg.to_agent,
            "type": msg.message_type,
            "message_id": buffered["id"],
            "prototype_state": PROTOTYPE_STATE,
            "transport_state": None,
            "transport_mode": TRANSPORT_MODE,
            "durable": False,
            "delivered": False,
            "error": None,
        },
    )
    return {
        "buffered": True,
        "message_id": buffered["id"],
        "prototype_state": PROTOTYPE_STATE,
        "transport_state": None,
        "transport_mode": TRANSPORT_MODE,
        "durable": False,
        "delivered": False,
        "queue_depth": len(message_queue),
    }


@app.get("/queue")
def get_queue():
    """Inspect the current volatile development buffer."""
    return {
        "depth": len(message_queue),
        "transport_mode": TRANSPORT_MODE,
        "durable": False,
        "messages": message_queue[-20:],
    }


if __name__ == "__main__":
    import uvicorn

    print("[HERMES] Booting — Messenger & API Bridge Communication Layer")
    emit_audit(
        repo="hermes",
        event_type="execution",
        actor="system",
        verdict="SUCCESS",
        evidence={
            "event": "boot",
            "transport_mode": TRANSPORT_MODE,
            "durable": False,
            "error": None,
        },
    )
    uvicorn.run(app, host="0.0.0.0", port=7702)
