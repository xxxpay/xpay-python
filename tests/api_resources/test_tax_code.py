import xpay


TEST_RESOURCE_ID = "txcd_123"


class TestTaxCode(object):
    def test_is_listable(self, request_mock):
        resources = xpay.TaxCode.list()
        request_mock.assert_requested("get", "/v1/tax_codes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.TaxCode)

    def test_is_retrievable(self, request_mock):
        resource = xpay.TaxCode.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/tax_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.TaxCode)
