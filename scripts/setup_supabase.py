"""
Supabase client module for MIRRORNODE backend agents.

Loads SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY from .env and returns a
configured client. Service role key carries full DB access — backend only,
never expose to the browser.
"""
import os
import sys

from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

_url = os.environ.get("SUPABASE_URL")
_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

if not _url or not _key:
    missing = [k for k, v in [("SUPABASE_URL", _url), ("SUPABASE_SERVICE_ROLE_KEY", _key)] if not v]
    raise RuntimeError(
        f"Missing required env var(s): {', '.join(missing)}. "
        f"Populate .env from Supabase Dashboard → Settings → API Keys."
    )

supabase: Client = create_client(_url, _key)


def get_client() -> Client:
    """Return the singleton Supabase client."""
    return supabase


if __name__ == "__main__":
    # Smoke test: attempt a trivial query. The `_health` table does not need
    # to exist — a "relation does not exist" error still proves the client
    # reached the API. We treat auth/network errors as the real failure mode.
    try:
        supabase.table("_health").select("*").limit(1).execute()
        print("✓ Supabase connection OK")
    except Exception as e:
        # PGRST205 = table not in schema cache. PGRST116 = no rows.
        # Either proves we reached PostgREST and authed — only the table is absent.
        code = getattr(e, "code", None) or ""
        msg = str(e)
        benign = ("PGRST205", "PGRST116", "schema cache", "not find the table")
        if any(marker in code for marker in benign) or any(marker in msg for marker in benign):
            print("✓ Supabase reachable (auth + network OK; no _health table, expected)")
        else:
            print(f"✗ Supabase connection failed: {e}", file=sys.stderr)
            sys.exit(1)
