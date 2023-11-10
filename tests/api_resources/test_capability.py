import pytest

import xpay


TEST_RESOURCE_ID = "acap_123"


class TestCapability(object):
    def construct_resource(self):
        capability_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "capability",
            "account": "acct_123",
        }
        return xpay.Capability.construct_from(
            capability_dict, xpay.api_key
        )

    def test_has_instance_url(self, request_mock):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/v1/accounts/acct_123/capabilities/%s" % TEST_RESOURCE_ID
        )

    def test_is_not_modifiable(self, request_mock):
        with pytest.raises(NotImplementedError):
            xpay.Capability.modify(TEST_RESOURCE_ID, requested=True)

    def test_is_not_retrievable(self, request_mock):
        with pytest.raises(NotImplementedError):
            xpay.Capability.retrieve(TEST_RESOURCE_ID)

    def test_is_saveable(self, request_mock):
        resource = self.construct_resource()
        resource.requested = True
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/accounts/acct_123/capabilities/%s" % TEST_RESOURCE_ID
        )
