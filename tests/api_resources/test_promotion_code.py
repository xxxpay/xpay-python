import xpay


TEST_RESOURCE_ID = "promo_123"


class TestPromotionCode(object):
    def test_is_listable(self, request_mock):
        resources = xpay.PromotionCode.list()
        request_mock.assert_requested("get", "/v1/promotion_codes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.PromotionCode)

    def test_is_retrievable(self, request_mock):
        resource = xpay.PromotionCode.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/promotion_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.PromotionCode)

    def test_is_creatable(self, request_mock):
        resource = xpay.PromotionCode.create(coupon="co_123", code="MYCODE")
        request_mock.assert_requested("post", "/v1/promotion_codes")
        assert isinstance(resource, xpay.PromotionCode)

    def test_is_saveable(self, request_mock):
        resource = xpay.PromotionCode.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/promotion_codes/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = xpay.PromotionCode.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/promotion_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.PromotionCode)
