import xpay


TEST_RESOURCE_ID = "250FF"


class TestPlan(object):
    def test_is_listable(self, request_mock):
        resources = xpay.Plan.list()
        request_mock.assert_requested("get", "/v1/plans")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Plan)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Plan.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v1/plans/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, xpay.Plan)

    def test_is_creatable(self, request_mock):
        resource = xpay.Plan.create(
            amount=100,
            currency="usd",
            id="plan_id",
            interval="month",
            nickname="plan_nickname",
        )
        request_mock.assert_requested("post", "/v1/plans")
        assert isinstance(resource, xpay.Plan)

    def test_is_saveable(self, request_mock):
        resource = xpay.Plan.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/plans/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = xpay.Plan.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/plans/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Plan)

    def test_is_deletable(self, request_mock):
        resource = xpay.Plan.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/plans/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = xpay.Plan.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/plans/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
