import pytest

import xpay


TEST_RESOURCE_ID = "card_123"


class TestCard(object):
    def construct_resource(self, **params):
        card_dict = {"id": TEST_RESOURCE_ID, "object": "card", "metadata": {}}
        card_dict.update(params)
        return xpay.Card.construct_from(card_dict, xpay.api_key)

    def test_has_account_instance_url(self):
        resource = self.construct_resource(account="acct_123")
        assert (
            resource.instance_url()
            == "/v1/accounts/acct_123/external_accounts/%s" % TEST_RESOURCE_ID
        )

    def test_has_customer_instance_url(self):
        resource = self.construct_resource(customer="cus_123")
        assert (
            resource.instance_url()
            == "/v1/customers/cus_123/sources/%s" % TEST_RESOURCE_ID
        )

    # The previous tests already ensure that the request will be routed to the
    # correct URL, so we only test the API operations once.

    def test_is_not_retrievable(self):
        with pytest.raises(NotImplementedError):
            xpay.Card.retrieve(TEST_RESOURCE_ID)

    def test_is_saveable(self, request_mock):
        resource = self.construct_resource(customer="cus_123")
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/customers/cus_123/sources/%s" % TEST_RESOURCE_ID
        )

    def test_is_not_modifiable(self):
        with pytest.raises(NotImplementedError):
            xpay.Card.modify(TEST_RESOURCE_ID, metadata={"key": "value"})

    def test_is_deletable(self, request_mock):
        resource = self.construct_resource(customer="cus_123")
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/customers/cus_123/sources/%s" % TEST_RESOURCE_ID
        )
