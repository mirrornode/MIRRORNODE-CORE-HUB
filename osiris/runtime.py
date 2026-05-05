import sys, os, time
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))
os.environ.setdefault("CANON_ROOT", str(Path(__file__).parent.parent / "canon"))

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
from canon.contracts.sdk.audit import emit_audit
from osiris.routes.execute import router as execute_router

# ── Stripe ──────────────────────────────────────────────────────────────────
try:
    import stripe
    stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "")
    STRIPE_AVAILABLE = bool(stripe.api_key)
except ImportError:
    stripe = None
    STRIPE_AVAILABLE = False

CHARTER_PATH = Path(os.environ["CANON_ROOT"]) / "charters" / "OSIRIS.md"
VERSION = "1.1.0"
BOOT_TIME = datetime.now(timezone.utc).isoformat()

app = FastAPI(title="Osiris", description="Payment & Commerce — Financial State Authority")

app.include_router(execute_router)


@app.get("/")
def root():
    return {"status": "ok", "node": "CORE-HUB", "version": VERSION}



# ── Audit helper ────────────────────────────────────────────────────────────
def _audit(event: str, verdict: str, evidence: dict):
    """Emit a canon audit record for every Stripe operation."""
    evidence.setdefault("error", None)
    emit_audit(
        repo="osiris",
        event_type="execution",
        actor="system",
        verdict=verdict,
        evidence={"event": event, **evidence},
    )


# ── Models ──────────────────────────────────────────────────────────────────
class CheckoutRequest(BaseModel):
    product_name: str
    amount_cents: int
    currency: str = "usd"
    success_url: str = "https://mirrornode.xyz/success"
    cancel_url: str = "https://mirrornode.xyz/cancel"
    customer_email: Optional[str] = None

class InvoiceRequest(BaseModel):
    customer_email: str
    amount_cents: int
    currency: str = "usd"
    description: str

class RefundRequest(BaseModel):
    payment_intent_id: str
    amount_cents: Optional[int] = None  # None = full refund
    reason: Optional[str] = "requested_by_customer"  # duplicate | fraudulent | requested_by_customer

class SubscriptionRequest(BaseModel):
    customer_email: str
    price_id: str          # Stripe Price ID (price_...)
    trial_days: Optional[int] = None
    metadata: Optional[dict] = None

class SubscriptionCancelRequest(BaseModel):
    subscription_id: str
    immediately: bool = False  # False = cancel at period end


# ── Routes ──────────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    return {
        "agent": "osiris",
        "role": "Payment & Commerce — Financial State Authority",
        "status": "alive",
        "version": VERSION,
        "stripe_connected": STRIPE_AVAILABLE,
        "boot_time": BOOT_TIME,
        "ts": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/heartbeat")
def heartbeat():
    start = time.time()
    _audit("heartbeat", "SUCCESS", {})
    latency_ms = round((time.time() - start) * 1000, 2)
    return {
        "engine": "osiris",
        "status": "alive",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "latency_ms": latency_ms,
        "version": VERSION,
        "stripe_connected": STRIPE_AVAILABLE,
        "role": "Payment & Commerce — Financial State Authority",
    }

@app.get("/identity")
def identity():
    if not CHARTER_PATH.exists():
        return {"error": "Charter not found", "path": str(CHARTER_PATH)}
    return {
        "agent": "osiris",
        "charter": CHARTER_PATH.read_text(),
        "charter_path": str(CHARTER_PATH),
    }

@app.get("/stripe/status")
def stripe_status():
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


# ── Checkout ────────────────────────────────────────────────────────────────
@app.post("/checkout")
def create_checkout(req: CheckoutRequest):
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
        _audit("checkout_created", "SUCCESS", {"session_id": session.id, "amount_cents": req.amount_cents})
        return {"session_id": session.id, "url": session.url}
    except Exception as e:
        _audit("checkout_failed", "FAILURE", {"error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))


# ── Invoice ─────────────────────────────────────────────────────────────────
@app.post("/invoice")
def create_invoice(req: InvoiceRequest):
    if not STRIPE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Stripe not configured — set STRIPE_SECRET_KEY")
    try:
        customer = stripe.Customer.create(email=req.customer_email)
        stripe.InvoiceItem.create(
            customer=customer.id,
            amount=req.amount_cents,
            currency=req.currency,
            description=req.description,
        )
        invoice = stripe.Invoice.create(customer=customer.id, auto_advance=True)
        invoice = stripe.Invoice.finalize_invoice(invoice.id)
        _audit("invoice_created", "SUCCESS", {"invoice_id": invoice.id, "amount_cents": req.amount_cents})
        return {"invoice_id": invoice.id, "hosted_url": invoice.hosted_invoice_url, "status": invoice.status}
    except Exception as e:
        _audit("invoice_failed", "FAILURE", {"error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))


# ── Refund ──────────────────────────────────────────────────────────────────
@app.post("/refund")
def create_refund(req: RefundRequest):
    """Refund a charge by payment_intent_id. Partial or full."""
    if not STRIPE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Stripe not configured — set STRIPE_SECRET_KEY")
    try:
        params = {
            "payment_intent": req.payment_intent_id,
            "reason": req.reason,
        }
        if req.amount_cents:
            params["amount"] = req.amount_cents
        refund = stripe.Refund.create(**params)
        _audit("refund_created", "SUCCESS", {
            "refund_id": refund.id,
            "payment_intent_id": req.payment_intent_id,
            "amount_cents": refund.amount,
            "status": refund.status,
        })
        return {
            "refund_id": refund.id,
            "status": refund.status,
            "amount_cents": refund.amount,
            "currency": refund.currency,
        }
    except Exception as e:
        _audit("refund_failed", "FAILURE", {"payment_intent_id": req.payment_intent_id, "error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))


# ── Subscription ────────────────────────────────────────────────────────────
@app.post("/subscription")
def create_subscription(req: SubscriptionRequest):
    """Create a recurring subscription for a customer."""
    if not STRIPE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Stripe not configured — set STRIPE_SECRET_KEY")
    try:
        customer = stripe.Customer.create(email=req.customer_email)
        sub_params = {
            "customer": customer.id,
            "items": [{"price": req.price_id}],
            "payment_behavior": "default_incomplete",
            "payment_settings": {"save_default_payment_method": "on_subscription"},
            "expand": ["latest_invoice.payment_intent"],
        }
        if req.trial_days:
            sub_params["trial_period_days"] = req.trial_days
        if req.metadata:
            sub_params["metadata"] = req.metadata
        sub = stripe.Subscription.create(**sub_params)
        client_secret = sub.latest_invoice.payment_intent.client_secret
        _audit("subscription_created", "SUCCESS", {
            "subscription_id": sub.id,
            "customer_id": customer.id,
            "price_id": req.price_id,
            "status": sub.status,
        })
        return {
            "subscription_id": sub.id,
            "customer_id": customer.id,
            "status": sub.status,
            "client_secret": client_secret,
        }
    except Exception as e:
        _audit("subscription_failed", "FAILURE", {"error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/subscription")
def cancel_subscription(req: SubscriptionCancelRequest):
    """Cancel a subscription immediately or at period end."""
    if not STRIPE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Stripe not configured — set STRIPE_SECRET_KEY")
    try:
        if req.immediately:
            sub = stripe.Subscription.delete(req.subscription_id)
        else:
            sub = stripe.Subscription.modify(
                req.subscription_id,
                cancel_at_period_end=True,
            )
        _audit("subscription_cancelled", "SUCCESS", {
            "subscription_id": req.subscription_id,
            "immediately": req.immediately,
            "status": sub.status,
        })
        return {
            "subscription_id": sub.id,
            "status": sub.status,
            "cancel_at_period_end": sub.cancel_at_period_end,
        }
    except Exception as e:
        _audit("subscription_cancel_failed", "FAILURE", {"subscription_id": req.subscription_id, "error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))


# ── Webhook ─────────────────────────────────────────────────────────────────
WEBHOOK_AUDIT_MAP = {
    "checkout.session.completed": "checkout_completed",
    "invoice.payment_succeeded": "invoice_payment_succeeded",
    "invoice.payment_failed": "invoice_payment_failed",
    "customer.subscription.created": "subscription_webhook_created",
    "customer.subscription.updated": "subscription_webhook_updated",
    "customer.subscription.deleted": "subscription_webhook_deleted",
    "charge.refunded": "charge_refunded",
}

@app.post("/webhook")
async def stripe_webhook(request: Request):
    if not STRIPE_AVAILABLE:
        raise HTTPException(status_code=503, detail="Stripe not configured")
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")
    webhook_secret = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except stripe.error.SignatureVerificationError as e:
        _audit("webhook_signature_failed", "FAILURE", {"error": str(e)})
        raise HTTPException(status_code=400, detail=f"Webhook signature invalid: {e}")

    event_label = WEBHOOK_AUDIT_MAP.get(event["type"], "webhook_event")
    _audit(event_label, "SUCCESS", {"type": event["type"], "id": event["id"]})

    return {"received": True, "type": event["type"]}


if __name__ == "__main__":
    import uvicorn
    print("[OSIRIS] Booting — Payment & Commerce Financial State Authority")
    _audit("boot", "SUCCESS", {})
    uvicorn.run(app, host="0.0.0.0", port=7701)
