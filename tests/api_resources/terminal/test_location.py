import xpay


TEST_RESOURCE_ID = "loc_123"


class TestLocation(object):
    def test_is_creatable(self, request_mock):
        resource = xpay.terminal.Location.create(
            display_name="name",
            address={
                "line1": "line1",
                "country": "US",
                "state": "CA",
                "postal_code": "12345",
                "city": "San Francisco",
            },
        )
        request_mock.assert_requested("post", "/v1/terminal/locations")
        assert isinstance(resource, xpay.terminal.Location)

    def test_is_listable(self, request_mock):
        resources = xpay.terminal.Location.list()
        request_mock.assert_requested("get", "/v1/terminal/locations")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.terminal.Location)

    def test_is_modifiable(self, request_mock):
        resource = xpay.terminal.Location.modify(
            TEST_RESOURCE_ID, display_name="new-name"
        )
        request_mock.assert_requested(
            "post", "/v1/terminal/locations/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.terminal.Location)

    def test_is_retrievable(self, request_mock):
        resource = xpay.terminal.Location.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/terminal/locations/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.terminal.Location)

    def test_is_saveable(self, request_mock):
        resource = xpay.terminal.Location.retrieve(TEST_RESOURCE_ID)
        resource.display_name = "new-name"
        location = resource.save()
        request_mock.assert_requested(
            "post", "/v1/terminal/locations/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.terminal.Location)
        assert resource is location

    def test_is_deletable(self, request_mock):
        resource = xpay.terminal.Location.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/terminal/locations/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = xpay.terminal.Location.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/terminal/locations/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
