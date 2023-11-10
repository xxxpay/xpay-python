import xpay


TEST_RESOURCE_ID = "US"


class TestCountrySpec(object):
    def test_is_listable(self, request_mock):
        resources = xpay.CountrySpec.list()
        request_mock.assert_requested("get", "/v1/country_specs")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.CountrySpec)

    def test_is_retrievable(self, request_mock):
        resource = xpay.CountrySpec.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/country_specs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.CountrySpec)
