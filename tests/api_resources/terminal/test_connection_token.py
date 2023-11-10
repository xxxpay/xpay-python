import xpay


TEST_RESOURCE_ID = "rdr_123"


class TestConnectionToken(object):
    def test_is_creatable(self, request_mock):
        resource = xpay.terminal.ConnectionToken.create()
        request_mock.assert_requested("post", "/v1/terminal/connection_tokens")
        assert isinstance(resource, xpay.terminal.ConnectionToken)
