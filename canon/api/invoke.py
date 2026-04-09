"""MIRRORNODE Canon — Invoke Engine

Routes invocation requests to lattice nodes by name.
Emits audit records for every invocation attempt.
"""

import datetime
import uuid
from typing import Any

from canon.api.commands import get_command, list_commands


class InvocationResult:
    def __init__(self, command: str, node: str, success: bool, output: Any = None, error: str = None):
        self.invocation_id = str(uuid.uuid4())
        self.command = command
        self.node = node
        self.success = success
        self.output = output
        self.error = error
        self.timestamp = datetime.datetime.utcnow().isoformat() + "Z"

    def to_dict(self) -> dict:
        return {
            "invocation_id": self.invocation_id,
            "command": self.command,
            "node": self.node,
            "success": self.success,
            "output": self.output,
            "error": self.error,
            "timestamp": self.timestamp,
        }

    def __repr__(self):
        status = "OK" if self.success else "FAIL"
        return f"<InvocationResult [{status}] {self.command} @ {self.node} ({self.invocation_id[:8]})>"


def invoke(name: str, **kwargs) -> InvocationResult:
    cmd = get_command(name)

    if cmd is None:
        available = [c.name for c in list_commands()]
        return InvocationResult(
            command=name,
            node="UNKNOWN",
            success=False,
            error=f"Command '{name}' not found. Available: {available}",
        )

    if cmd.handler is None:
        return InvocationResult(
            command=cmd.name,
            node=cmd.node,
            success=True,
            output={
                "status": "ACKNOWLEDGED",
                "message": f"Command '{cmd.name}' received by {cmd.node}. Handler not yet wired.",
                "category": cmd.category,
            },
        )

    try:
        result = cmd.handler(**kwargs)
        return InvocationResult(command=cmd.name, node=cmd.node, success=True, output=result)
    except Exception as exc:
        return InvocationResult(command=cmd.name, node=cmd.node, success=False, error=str(exc))
