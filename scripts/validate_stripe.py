#!/usr/bin/env python3
"""
MIRRORNODE — Stripe Validation Script
Run this to verify your Stripe keys and account status.

Usage:
    python scripts/validate_stripe.py
"""

import os
import sys
from pathlib import Path

# Load .env if present
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass

def validate_stripe():
    secret_key = os.environ.get("STRIPE_SECRET_KEY", "")
    pub_key = os.environ.get("STRIPE_PUBLISHABLE_KEY", "")
    webhook_secret = os.environ.get("STRIPE_WEBHOOK_SECRET", "")

    print("\n── MIRRORNODE Stripe Validation ─────────────────────")

    # Key presence
    print(f"  Secret key set:      {'✅' if secret_key and not secret_key.endswith('...') else '❌ Missing or placeholder'}")
    print(f"  Publishable key set: {'✅' if pub_key and not pub_key.endswith('...') else '❌ Missing or placeholder'}")
    print(f"  Webhook secret set:  {'✅' if webhook_secret and not webhook_secret.endswith('...') else '⚠️  Not set (needed for webhooks)'}")
    print(f"  Mode:                {'🔴 LIVE' if secret_key.startswith('sk_live') else '🟡 TEST' if secret_key.startswith('sk_test') else '❓ Unknown'}")

    if not secret_key or secret_key.endswith("..."):
        print("\n  ❌ STRIPE_SECRET_KEY not configured.")
        print("  Add it to your .env file. Get it from: https://dashboard.stripe.com/apikeys")
        return False

    try:
        import stripe
        stripe.api_key = secret_key
        account = stripe.Account.retrieve()
        print(f"\n  ✅ Stripe connected!")
        print(f"  Account ID:          {account.id}")
        print(f"  Email:               {account.get('email', 'N/A')}")
        print(f"  Country:             {account.get('country', 'N/A')}")
        print(f"  Charges enabled:     {'✅' if account.get('charges_enabled') else '❌'}")
        print(f"  Payouts enabled:     {'✅' if account.get('payouts_enabled') else '❌'}")
        print(f"  Details submitted:   {'✅' if account.get('details_submitted') else '❌ Incomplete — finish at dashboard.stripe.com'}")

        # List products
        products = stripe.Product.list(limit=5, active=True)
        print(f"\n  Active products ({len(products.data)}):")
        if products.data:
            for p in products.data:
                prices = stripe.Price.list(product=p.id, active=True, limit=3)
                for price in prices.data:
                    amount = price.unit_amount / 100 if price.unit_amount else 0
                    interval = price.recurring.interval if price.recurring else "one-time"
                    print(f"    - {p.name}: ${amount:.2f} / {interval} ({price.id})")
        else:
            print("    None yet — create your first product at dashboard.stripe.com/products")

        return True

    except ImportError:
        print("\n  ❌ stripe package not installed. Run: pip install stripe")
        return False
    except Exception as e:
        print(f"\n  ❌ Stripe connection failed: {e}")
        return False

    finally:
        print("──────────────────────────────────────────────────────\n")

if __name__ == "__main__":
    success = validate_stripe()
    sys.exit(0 if success else 1)
