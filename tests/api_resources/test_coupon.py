import xpay


TEST_RESOURCE_ID = "250FF"


class TestCoupon(object):
    def test_is_listable(self, request_mock):
        resources = xpay.Coupon.list()
        request_mock.assert_requested("get", "/v1/coupons")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Coupon)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Coupon.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/coupons/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Coupon)

    def test_is_creatable(self, request_mock):
        resource = xpay.Coupon.create(
            percent_off=25,
            duration="repeating",
            duration_in_months=3,
            id="250FF",
        )
        request_mock.assert_requested("post", "/v1/coupons")
        assert isinstance(resource, xpay.Coupon)

    def test_is_saveable(self, request_mock):
        resource = xpay.Coupon.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/coupons/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = xpay.Coupon.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/coupons/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Coupon)

    def test_is_deletable(self, request_mock):
        resource = xpay.Coupon.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/coupons/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = xpay.Coupon.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/coupons/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
