"""MIRRORNODE Canon — Dev Server Bootstrap (Temporary)
CONTRACT REF: bf0dba8 | 2026-05-14

FastAPI app that mounts the dev trigger routes under /dev.
Use ONLY for local testing of code.ingest and other dev commands.
"""
from fastapi import FastAPI
from canon.api.dev.routes import router as dev_router

app = FastAPI(
    title="MIRRORNODE Canon Dev Server",
    description="Temporary dev trigger server for code.ingest testing",
    version="2026.05-dev"
)

app.include_router(dev_router, prefix="/dev")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7700, reload=True)
