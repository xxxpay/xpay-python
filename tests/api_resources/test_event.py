import xpay


TEST_RESOURCE_ID = "evt_123"


class TestEvent(object):
    def test_is_listable(self, request_mock):
        resources = xpay.Event.list()
        request_mock.assert_requested("get", "/v1/events")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Event)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Event.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/events/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Event)
