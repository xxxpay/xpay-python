from urllib.parse import parse_qs, urlparse

import xpay


class TestOAuth(object):
    def test_authorize_url(self, request_mock):
        url = xpay.OAuth.authorize_url(
            scope="read_write",
            state="csrf_token",
            xpay_user={
                "email": "test@example.com",
                "url": "https://example.com/profile/test",
                "country": "US",
            },
        )
        o = urlparse(url)
        params = parse_qs(o.query)

        url_express = xpay.OAuth.authorize_url(
            express=True, scope="read_write", state="csrf_token"
        )
        o_express = urlparse(url_express)

        assert o.scheme == "https"
        assert o.netloc == "connect.xpay.com"
        assert o.path == "/oauth/authorize"
        assert o_express.path == "/express/oauth/authorize"

        assert params["client_id"] == ["ca_123"]
        assert params["scope"] == ["read_write"]
        assert params["xpay_user[email]"] == ["test@example.com"]
        assert params["xpay_user[url]"] == [
            "https://example.com/profile/test"
        ]
        assert params["xpay_user[country]"] == ["US"]

    def test_token(self, request_mock):
        request_mock.stub_request(
            "post",
            "/oauth/token",
            {
                "access_token": "sk_access_token",
                "scope": "read_only",
                "livemode": "false",
                "token_type": "bearer",
                "refresh_token": "sk_refresh_token",
                "xpay_user_id": "acct_test",
                "xpay_publishable_key": "pk_test",
            },
        )

        resp = xpay.OAuth.token(
            grant_type="authorization_code",
            code="this_is_an_authorization_code",
        )
        request_mock.assert_requested(
            "post",
            "/oauth/token",
            {
                "grant_type": "authorization_code",
                "code": "this_is_an_authorization_code",
            },
        )
        assert resp["access_token"] == "sk_access_token"

    def test_deauthorize(self, request_mock):
        request_mock.stub_request(
            "post",
            "/oauth/deauthorize",
            {"xpay_user_id": "acct_test_deauth"},
        )

        resp = xpay.OAuth.deauthorize(xpay_user_id="acct_test_deauth")
        request_mock.assert_requested(
            "post",
            "/oauth/deauthorize",
            {"client_id": "ca_123", "xpay_user_id": "acct_test_deauth"},
        )
        assert resp["xpay_user_id"] == "acct_test_deauth"
