"""MIRRORNODE Canon — Handler Registry

Import and bind handlers at runtime, not at definition time.
Example:

    from canon.api.commands import COMMANDS
    from canon.api.handlers.code_ingest import handle_code_ingest

    COMMANDS["code.ingest"].handler = handle_code_ingest
"""
