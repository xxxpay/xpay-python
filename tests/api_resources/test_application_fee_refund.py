import pytest

import xpay


TEST_RESOURCE_ID = "fr_123"
TEST_APPFEE_ID = "fee_123"


class TestApplicationFeeRefund(object):
    def test_is_saveable(self, request_mock):
        appfee = xpay.ApplicationFee.retrieve(TEST_APPFEE_ID)
        resource = appfee.refunds.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post",
            "/v1/application_fees/%s/refunds/%s"
            % (TEST_APPFEE_ID, TEST_RESOURCE_ID),
        )

    def test_is_modifiable(self, request_mock):
        resource = xpay.ApplicationFeeRefund.modify(
            TEST_APPFEE_ID, TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/application_fees/%s/refunds/%s"
            % (TEST_APPFEE_ID, TEST_RESOURCE_ID),
        )
        assert isinstance(resource, xpay.ApplicationFeeRefund)

    def test_is_not_retrievable(self):
        with pytest.raises(NotImplementedError):
            xpay.ApplicationFeeRefund.retrieve(TEST_RESOURCE_ID)