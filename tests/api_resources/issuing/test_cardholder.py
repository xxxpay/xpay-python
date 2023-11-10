import xpay


TEST_RESOURCE_ID = "ich_123"


class TestCardholder(object):
    def test_is_creatable(self, request_mock):
        resource = xpay.issuing.Cardholder.create(
            billing={
                "address": {
                    "city": "city",
                    "country": "US",
                    "line1": "line1",
                    "postal_code": "postal_code",
                }
            },
            name="Jenny Rosen",
            type="individual",
        )
        request_mock.assert_requested("post", "/v1/issuing/cardholders")
        assert isinstance(resource, xpay.issuing.Cardholder)

    def test_is_listable(self, request_mock):
        resources = xpay.issuing.Cardholder.list()
        request_mock.assert_requested("get", "/v1/issuing/cardholders")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.issuing.Cardholder)

    def test_is_modifiable(self, request_mock):
        resource = xpay.issuing.Cardholder.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/issuing/cardholders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.issuing.Cardholder)

    def test_is_retrievable(self, request_mock):
        resource = xpay.issuing.Cardholder.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/issuing/cardholders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.issuing.Cardholder)

    def test_is_saveable(self, request_mock):
        resource = xpay.issuing.Cardholder.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        cardholder = resource.save()
        request_mock.assert_requested(
            "post", "/v1/issuing/cardholders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.issuing.Cardholder)
        assert resource is cardholder
