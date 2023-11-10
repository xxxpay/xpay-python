import xpay


TEST_RESOURCE_ID = "usd"


class TestExchangeRate(object):
    def test_is_listable(self, request_mock):
        resources = xpay.ExchangeRate.list()
        request_mock.assert_requested("get", "/v1/exchange_rates")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.ExchangeRate)

    def test_is_retrievable(self, request_mock):
        resource = xpay.ExchangeRate.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/exchange_rates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.ExchangeRate)
