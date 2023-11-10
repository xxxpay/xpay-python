import xpay


TEST_RESOURCE_ID = "sub_123"


class TestSubscription(object):
    def test_is_listable(self, request_mock):
        resources = xpay.Subscription.list()
        request_mock.assert_requested("get", "/v1/subscriptions")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Subscription)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Subscription.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Subscription)

    def test_is_creatable(self, request_mock):
        resource = xpay.Subscription.create(customer="cus_123")
        request_mock.assert_requested("post", "/v1/subscriptions")
        assert isinstance(resource, xpay.Subscription)

    def test_is_saveable(self, request_mock):
        resource = xpay.Subscription.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = xpay.Subscription.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Subscription)

    def test_is_deletable(self, request_mock):
        resource = xpay.Subscription.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Subscription)

    def test_can_delete(self, request_mock):
        resource = xpay.Subscription.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/subscriptions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Subscription)

    def test_can_delete_discount(self, request_mock):
        sub = xpay.Subscription.retrieve(TEST_RESOURCE_ID)
        sub.delete_discount()
        request_mock.assert_requested(
            "delete", "/v1/subscriptions/%s/discount" % sub.id
        )

    def test_can_delete_discount_classmethod(self, request_mock):
        xpay.Subscription.delete_discount(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/subscriptions/%s/discount" % TEST_RESOURCE_ID
        )
