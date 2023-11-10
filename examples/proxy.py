import os

import xpay


xpay.api_key = os.environ.get("STRIPE_SECRET_KEY")

print("Attempting charge...")

proxy = {
    "http": "http://<user>:<pass>@<proxy>:<port>",
    "https": "http://<user>:<pass>@<proxy>:<port>",
}

clients = (
    xpay.http_client.RequestsClient(
        verify_ssl_certs=xpay.verify_ssl_certs, proxy=proxy
    ),
    xpay.http_client.PycurlClient(
        verify_ssl_certs=xpay.verify_ssl_certs, proxy=proxy
    ),
    xpay.http_client.Urllib2Client(
        verify_ssl_certs=xpay.verify_ssl_certs, proxy=proxy
    ),
)

for c in clients:
    xpay.default_http_client = c
    resp = xpay.Charge.create(
        amount=200,
        currency="usd",
        card="tok_visa",
        description="customer@gmail.com",
    )
    print("Success: %s, %r" % (c.name, resp))
