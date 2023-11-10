import xpay


class TestBalance(object):
    def test_is_retrievable(self, request_mock):
        resource = xpay.Balance.retrieve()
        request_mock.assert_requested("get", "/v1/balance")
        assert isinstance(resource, xpay.Balance)
