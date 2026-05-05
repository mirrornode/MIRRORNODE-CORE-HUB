"""Single execution entry point for task dispatch."""
import time
from fastapi import APIRouter
from pydantic import BaseModel
from canon.contracts.sdk.audit import emit_audit

router = APIRouter()

class TaskRequest(BaseModel):
    task: str
    payload: dict
    trace_id: str

def _audit(event: str, verdict: str, evidence: dict):
    evidence.setdefault("error", None)
    emit_audit(
        repo="osiris",
        event_type="execution",
        actor="system",
        verdict=verdict,
        evidence={"event": event, **evidence},
    )

@router.post("/execute-task")
async def execute_task(req: TaskRequest):
    start = time.time()
    result = {"message": f"Executed {req.task}", "input": req.payload}
    duration_ms = int((time.time() - start) * 1000)
    _audit("task_executed", "SUCCESS", {
        "task": req.task,
        "trace_id": req.trace_id,
        "duration_ms": duration_ms,
    })
    return {"status": "success", "output": result, "duration": duration_ms}

@router.post("/system/execute")
async def system_execute(req: TaskRequest):
    run_id = req.trace_id
    _audit("system_execute_received", "SUCCESS", {
        "task": req.task,
        "run_id": run_id,
    })
    response = await execute_task(req)
    return {"runId": run_id, "result": response["output"]}
