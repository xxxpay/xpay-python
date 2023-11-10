import xpay


TEST_RESOURCE_ID = "txn_123"


class TestBalanceTransaction(object):
    def test_is_listable(self, request_mock):
        resources = xpay.BalanceTransaction.list()
        request_mock.assert_requested("get", "/v1/balance_transactions")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.BalanceTransaction)

    def test_is_retrievable(self, request_mock):
        resource = xpay.BalanceTransaction.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/balance_transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.BalanceTransaction)
