import xpay


TEST_RESOURCE_ID = "ipi_123"


class TestTransaction(object):
    def test_is_listable(self, request_mock):
        resources = xpay.issuing.Transaction.list()
        request_mock.assert_requested("get", "/v1/issuing/transactions")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.issuing.Transaction)

    def test_is_modifiable(self, request_mock):
        resource = xpay.issuing.Transaction.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/issuing/transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.issuing.Transaction)

    def test_is_retrievable(self, request_mock):
        resource = xpay.issuing.Transaction.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/issuing/transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.issuing.Transaction)

    def test_is_saveable(self, request_mock):
        resource = xpay.issuing.Transaction.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        transaction = resource.save()
        request_mock.assert_requested(
            "post", "/v1/issuing/transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.issuing.Transaction)
        assert resource is transaction
