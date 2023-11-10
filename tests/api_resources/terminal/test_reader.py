import xpay


TEST_RESOURCE_ID = "rdr_123"


class TestReader(object):
    def test_is_creatable(self, request_mock):
        resource = xpay.terminal.Reader.create(
            registration_code="a-b-c", label="name"
        )
        request_mock.assert_requested("post", "/v1/terminal/readers")
        assert isinstance(resource, xpay.terminal.Reader)

    def test_is_listable(self, request_mock):
        resources = xpay.terminal.Reader.list()
        request_mock.assert_requested("get", "/v1/terminal/readers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.terminal.Reader)

    def test_is_modifiable(self, request_mock):
        resource = xpay.terminal.Reader.modify(
            TEST_RESOURCE_ID, label="new-name"
        )
        request_mock.assert_requested(
            "post", "/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.terminal.Reader)

    def test_is_retrievable(self, request_mock):
        resource = xpay.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.terminal.Reader)

    def test_is_saveable(self, request_mock):
        resource = xpay.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        resource.label = "new-name"
        reader = resource.save()
        request_mock.assert_requested(
            "post", "/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.terminal.Reader)
        assert resource is reader

    def test_is_deletable(self, request_mock):
        resource = xpay.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = xpay.terminal.Reader.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_present_payment_method(self, request_mock):
        resource = xpay.terminal.Reader.TestHelpers.present_payment_method(
            TEST_RESOURCE_ID
        )
        request_mock.assert_requested(
            "post",
            "/v1/test_helpers/terminal/readers/%s/present_payment_method"
            % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, xpay.terminal.Reader)
