import xpay


TEST_RESOURCE_ID = "price_123"


class TestPrice(object):
    def test_is_listable(self, request_mock):
        resources = xpay.Price.list()
        request_mock.assert_requested("get", "/v1/prices")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Price)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Price.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/prices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Price)

    def test_is_creatable(self, request_mock):
        resource = xpay.Price.create(
            unit_amount=1000,
            currency="usd",
            recurring={"interval": "month"},
            product_data={"name": "price_nickname"},
        )
        request_mock.assert_requested("post", "/v1/prices")
        assert isinstance(resource, xpay.Price)

    def test_is_saveable(self, request_mock):
        resource = xpay.Price.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/prices/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = xpay.Price.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/prices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Price)
