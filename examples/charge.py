import os

import xpay


xpay.api_key = os.environ.get("STRIPE_SECRET_KEY")

print("Attempting charge...")

resp = xpay.Charge.create(
    amount=200,
    currency="usd",
    card="tok_visa",
    description="customer@gmail.com",
)

print("Success: %r" % (resp))
