import xpay


TEST_RESOURCE_ID = "ic_123"


class TestCard(object):
    def test_is_creatable(self, request_mock):
        resource = xpay.issuing.Card.create(currency="usd", type="physical")
        request_mock.assert_requested("post", "/v1/issuing/cards")
        assert isinstance(resource, xpay.issuing.Card)

    def test_is_listable(self, request_mock):
        resources = xpay.issuing.Card.list()
        request_mock.assert_requested("get", "/v1/issuing/cards")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.issuing.Card)

    def test_is_modifiable(self, request_mock):
        resource = xpay.issuing.Card.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/issuing/cards/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.issuing.Card)

    def test_is_retrievable(self, request_mock):
        resource = xpay.issuing.Card.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/issuing/cards/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.issuing.Card)

    def test_is_saveable(self, request_mock):
        resource = xpay.issuing.Card.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        card = resource.save()
        request_mock.assert_requested(
            "post", "/v1/issuing/cards/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.issuing.Card)
        assert resource is card
