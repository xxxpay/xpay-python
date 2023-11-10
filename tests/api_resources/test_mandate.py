import xpay


TEST_RESOURCE_ID = "mandate_123"


class TestMandateSchedule(object):
    def test_is_retrievable(self, request_mock):
        resource = xpay.Mandate.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/mandates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Mandate)
