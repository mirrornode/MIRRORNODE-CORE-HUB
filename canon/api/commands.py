"""MIRRORNODE Canon — Command Palette

Defines the full set of callable commands available across the lattice.
Each command maps to a node, an action, and an audit category.
"""

from dataclasses import dataclass, field
from typing import Callable, Optional


@dataclass
class Command:
    name: str
    node: str
    description: str
    category: str  # preflight | diagnostic | runtime | control
    handler: Optional[Callable] = field(default=None, repr=False)


COMMANDS: dict[str, Command] = {
    "preflight": Command(
        name="preflight",
        node="LUCIAN",
        description="Run full lattice preflight checks across all nodes.",
        category="preflight",
    ),
    "test-openai": Command(
        name="test-openai",
        node="HERMES",
        description="Validate OpenAI API connectivity and token auth.",
        category="diagnostic",
    ),
    "config-reload": Command(
        name="config-reload",
        node="THOTH",
        description="Hot-reload environment config without full restart.",
        category="runtime",
    ),
    "health-check": Command(
        name="health-check",
        node="THOTH",
        description="Return health status for all registered services.",
        category="diagnostic",
    ),
    "audit-emit": Command(
        name="audit-emit",
        node="OSIRIS",
        description="Force-emit an audit event to the audit trail.",
        category="runtime",
    ),
    "halt": Command(
        name="halt",
        node="LUCIAN",
        description="Emergency stop — graceful shutdown of all lattice nodes.",
        category="control",
    ),
}


def list_commands(category: Optional[str] = None) -> list[Command]:
    cmds = list(COMMANDS.values())
    if category:
        cmds = [c for c in cmds if c.category == category]
    return cmds


def get_command(name: str) -> Optional[Command]:
    return COMMANDS.get(name)
