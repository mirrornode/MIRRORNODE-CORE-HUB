"""canon.api — Command palette and invocation engine for MIRRORNODE lattice nodes.

This module binds all runtime handlers at import time.
Do NOT bind handlers in individual command definition files.
"""

from canon.api.commands import COMMANDS
from canon.api.handlers.code_ingest import handle_code_ingest

# Runtime handler binding — must happen here, never at definition time
COMMANDS["code.ingest"].handler = handle_code_ingest
