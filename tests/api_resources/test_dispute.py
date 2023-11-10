import xpay


TEST_RESOURCE_ID = "dp_123"


class TestDispute(object):
    def test_is_listable(self, request_mock):
        resources = xpay.Dispute.list()
        request_mock.assert_requested("get", "/v1/disputes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Dispute)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Dispute.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Dispute)

    def test_is_saveable(self, request_mock):
        resource = xpay.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/disputes/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = xpay.Dispute.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/disputes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Dispute)

    def test_can_close(self, request_mock):
        resource = xpay.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.close()
        request_mock.assert_requested(
            "post", "/v1/disputes/%s/close" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Dispute)

    def test_can_close_classmethod(self, request_mock):
        resource = xpay.Dispute.close(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/disputes/%s/close" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Dispute)
