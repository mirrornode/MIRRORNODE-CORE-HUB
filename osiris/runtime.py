import sys, os, time
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))
os.environ.setdefault("CANON_ROOT", str(Path(__file__).parent.parent / "canon"))

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
from canon.contracts.sdk.audit import emit_audit

# ── Stripe (optional — won't crash if key missing) ──────────────────────────
try:
    import stripe
    stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "")
    STRIPE_AVAILABLE = bool(stripe.api_key)
except ImportError:
    stripe = None
    STRIPE_AVAILABLE = False

CHARTER_PATH = Path(os.environ["CANON_ROOT"]) / "charters" / "OSIRIS.md"
VERSION = "1.0.0"
BOOT_TIME = datetime.now(timezone.utc).isoformat()

app = FastAPI(title="Osiris", description="Payment & Commerce — Financial State Authority")

# ── Models ──────────────────────────────────────────────────────────────────
class CheckoutRequest(BaseModel):
    product_name: str
    amount_cents: int
    currency: str = "usd"
    success_url: str = "https://mirrornode.io/success"
    cancel_url: str = "https://mirrornode.io/cancel"
    customer_email: Optional[str] = None

class InvoiceRequest(BaseModel):
    customer_email: str
    amount_cents: int
    currency: str = "usd"
    description: str

# ── Routes ──────────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    return {
        "agent": "osiris",
        "role": "Payment & Commerce — Financial State Authority",
        "status": "alive",
        "stripe_connected": STRIPE_AVAILABLE,
        "boot_time": BOOT_TIME,
        "ts": datetime.now(timezone.utc).isoformat()
    }

@app.get("/heartbeat")
def heartbeat():
    start = time.time()
    emit_audit(repo="osiris", event_type="agent_invocation",
               actor="system", verdict="SUCCESS",
               evidence={"event": "heartbeat", "error": None})
    latency_ms = round((time.time() - start) * 1000, 2)
    return {
        "engine": "osiris",
        "status": "alive",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "latency_ms": latency_ms,
        "version": VERSION,
        "stripe_connected": STRIPE_AVAILABLE,
        "role": "Payment & Commerce — Financial State Authority"
    }

@app.get("/identity")
def identity():
    if not CHARTER_PATH.exists():
        return {"error": "Charter not found", "path": str(CHARTER_PATH)}
    return {
        "agent": "osiris",
        "charter": CHARTER_PATH.read_text(),
        "charter_path": str(CHARTER_PATH)
    }

@app.post("/checkout")
def create_checkout(req: CheckoutRequest):
    """Create a Stripe Checkout session."""
    if not STRIPE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Stripe not configured — set STRIPE_SECRET_KEY")
    try:
        params = {
            "mode": "payment",
            "line_items": [{
                "price_data": {
                    "currency": req.currency,
                    "product_data": {"name": req.product_name},
                    "unit_amount": req.amount_cents,
                },
                "quantity": 1,
            }],
            "success_url": req.success_url,
            "cancel_url": req.cancel_url,
        }
        if req.customer_email:
            params["customer_email"] = req.customer_email
        session = stripe.checkout.Session.create(**params)
        emit_audit(repo="osiris", event_type="execution", actor="system",
                   verdict="SUCCESS",
                   evidence={"event": "checkout_created", "session_id": session.id,
                              "amount_cents": req.amount_cents, "error": None})
        return {"session_id": session.id, "url": session.url}
    except Exception as e:
        emit_audit(repo="osiris", event_type="execution", actor="system",
                   verdict="FAILURE",
                   evidence={"event": "checkout_failed", "error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/invoice")
def create_invoice(req: InvoiceRequest):
    """Create and send a Stripe Invoice."""
    if not STRIPE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Stripe not configured — set STRIPE_SECRET_KEY")
    try:
        customer = stripe.Customer.create(email=req.customer_email)
        invoice_item = stripe.InvoiceItem.create(
            customer=customer.id,
            amount=req.amount_cents,
            currency=req.currency,
            description=req.description,
        )
        invoice = stripe.Invoice.create(customer=customer.id, auto_advance=True)
        invoice = stripe.Invoice.finalize_invoice(invoice.id)
        emit_audit(repo="osiris", event_type="execution", actor="system",
                   verdict="SUCCESS",
                   evidence={"event": "invoice_created", "invoice_id": invoice.id,
                              "amount_cents": req.amount_cents, "error": None})
        return {"invoice_id": invoice.id, "hosted_url": invoice.hosted_invoice_url,
                "status": invoice.status}
    except Exception as e:
        emit_audit(repo="osiris", event_type="execution", actor="system",
                   verdict="FAILURE",
                   evidence={"event": "invoice_failed", "error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/webhook")
async def stripe_webhook(request: Request):
    """Receive and verify Stripe webhook events."""
    if not STRIPE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Stripe not configured")
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")
    webhook_secret = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except stripe.error.SignatureVerificationError as e:
        raise HTTPException(status_code=400, detail=f"Webhook signature invalid: {e}")
    emit_audit(repo="osiris", event_type="agent_invocation", actor="system",
               verdict="SUCCESS",
               evidence={"event": "stripe_webhook", "type": event["type"],
                          "id": event["id"], "error": None})
    return {"received": True, "type": event["type"]}

@app.get("/stripe/status")
def stripe_status():
    """Validate Stripe connection and return account details."""
    if not STRIPE_AVAILABLE:
        return {"connected": False, "reason": "STRIPE_SECRET_KEY not set"}
    try:
        account = stripe.Account.retrieve()
        return {
            "connected": True,
            "account_id": account.id,
            "email": account.get("email"),
            "country": account.get("country"),
            "charges_enabled": account.get("charges_enabled"),
            "payouts_enabled": account.get("payouts_enabled"),
            "details_submitted": account.get("details_submitted"),
        }
    except Exception as e:
        return {"connected": False, "reason": str(e)}

if __name__ == "__main__":
    import uvicorn
    print("[OSIRIS] Booting — Payment & Commerce Financial State Authority")
    emit_audit(repo="osiris", event_type="execution", actor="system",
               verdict="SUCCESS", evidence={"event": "boot", "error": None})
    uvicorn.run(app, host="0.0.0.0", port=7701)
