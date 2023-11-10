import os

import xpay
from flask import Flask, request, redirect


xpay.api_key = os.environ.get("STRIPE_SECRET_KEY")
xpay.client_id = os.environ.get("STRIPE_CLIENT_ID")

app = Flask(__name__)


@app.route("/")
def index():
    return '<a href="/authorize">Connect with XPay</a>'


@app.route("/authorize")
def authorize():
    url = xpay.OAuth.authorize_url(scope="read_only")
    return redirect(url)


@app.route("/oauth/callback")
def callback():
    code = request.args.get("code")
    try:
        resp = xpay.OAuth.token(grant_type="authorization_code", code=code)
    except xpay.oauth_error.OAuthError as e:
        return "Error: " + str(e)

    return """
<p>Success! Account <code>{xpay_user_id}</code> is connected.</p>
<p>Click <a href="/deauthorize?xpay_user_id={xpay_user_id}">here</a> to
disconnect the account.</p>
""".format(
        xpay_user_id=resp["xpay_user_id"]
    )


@app.route("/deauthorize")
def deauthorize():
    xpay_user_id = request.args.get("xpay_user_id")
    try:
        xpay.OAuth.deauthorize(xpay_user_id=xpay_user_id)
    except xpay.oauth_error.OAuthError as e:
        return "Error: " + str(e)

    return """
<p>Success! Account <code>{xpay_user_id}</code> is disconnected.</p>
<p>Click <a href="/">here</a> to restart the OAuth flow.</p>
""".format(
        xpay_user_id=xpay_user_id
    )


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
