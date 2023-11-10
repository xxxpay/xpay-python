import pytest

import xpay


TEST_RESOURCE_ID = "trr_123"


class TestReversal(object):
    def construct_resource(self):
        reversal_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "reversal",
            "metadata": {},
            "transfer": "tr_123",
        }
        return xpay.Reversal.construct_from(reversal_dict, xpay.api_key)

    def test_has_instance_url(self, request_mock):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/v1/transfers/tr_123/reversals/%s" % TEST_RESOURCE_ID
        )

    def test_is_not_modifiable(self, request_mock):
        with pytest.raises(NotImplementedError):
            xpay.Reversal.modify(TEST_RESOURCE_ID, metadata={"key": "value"})

    def test_is_not_retrievable(self, request_mock):
        with pytest.raises(NotImplementedError):
            xpay.Reversal.retrieve(TEST_RESOURCE_ID)

    def test_is_saveable(self, request_mock):
        resource = self.construct_resource()
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/transfers/tr_123/reversals/%s" % TEST_RESOURCE_ID
        )
