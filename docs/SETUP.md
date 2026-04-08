# MIRRORNODE Setup Guide

## Prerequisites

- Python 3.12+
- Node.js 20+
- pnpm (`npm install -g pnpm`)
- A Stripe account ([dashboard.stripe.com](https://dashboard.stripe.com))
- A Vercel account ([vercel.com](https://vercel.com))
- Git configured with your real name and email

## 1. Clone & Configure

```bash
git clone https://github.com/mirrornode/MIRRORNODE-CORE-HUB.git
cd MIRRORNODE-CORE-HUB
cp .env.example .env
# Edit .env with your real Stripe keys
```

## 2. Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn stripe python-dotenv
```

## 3. Validate Stripe

```bash
python scripts/validate_stripe.py
```

Expected output: all green, account details confirmed.

## 4. Boot the Lattice

```bash
bash scripts/boot_lattice.sh
```

This boots Lucian (7700), Osiris (7701), and Hermes (7702) simultaneously.

## 5. Verify All Agents

```bash
curl http://localhost:7700/health   # Lucian
curl http://localhost:7701/health   # Osiris
curl http://localhost:7702/health   # Hermes

curl http://localhost:7701/stripe/status  # Stripe connection
```

## 6. Test Stripe Checkout (Test Mode)

```bash
curl -X POST http://localhost:7701/checkout \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "MIRRORNODE Scale",
    "amount_cents": 2900,
    "currency": "usd",
    "customer_email": "test@example.com"
  }'
```

You should get back a Stripe Checkout session URL. Open it in your browser to complete a test payment.

## 7. Deploy Platform to Vercel

1. Go to [vercel.com/new](https://vercel.com/new)
2. Import `mirrornode/mirrornode-platform` from GitHub
3. Set environment variables:
   - `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`
   - `NEXT_PUBLIC_MIRRORNODE_API_URL`
4. Deploy — Vercel auto-builds on every push to `main`

## 8. Configure Stripe Webhooks

1. In Stripe Dashboard → Developers → Webhooks → Add endpoint
2. URL: `https://api.mirrornode.io/osiris/webhook` (or your deployed URL)
3. Events to listen for:
   - `checkout.session.completed`
   - `invoice.paid`
   - `invoice.payment_failed`
   - `customer.subscription.created`
   - `customer.subscription.deleted`
4. Copy the webhook signing secret → add to `.env` as `STRIPE_WEBHOOK_SECRET`

## Agent Port Map

| Agent | Port | Role |
|---|---|---|
| Lucian | 7700 | Core Orchestrator / Audit |
| Osiris | 7701 | Payment & Commerce |
| Hermes | 7702 | Messenger & API Bridge |
| Thoth | 7703 | Knowledge & Memory (coming) |
| Theia | 7704 | Vision & Interface (coming) |
| Ptah | 7705 | Builder & Infrastructure (coming) |

## Git Identity

```bash
git config --global user.name "Sean Malm"
git config --global user.email "full.send.over@gmail.com"
```
