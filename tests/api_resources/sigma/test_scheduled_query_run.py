import xpay


TEST_RESOURCE_ID = "sqr_123"


class TestTransaction(object):
    def test_is_listable(self, request_mock):
        resources = xpay.sigma.ScheduledQueryRun.list()
        request_mock.assert_requested("get", "/v1/sigma/scheduled_query_runs")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.sigma.ScheduledQueryRun)

    def test_is_retrievable(self, request_mock):
        resource = xpay.sigma.ScheduledQueryRun.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/sigma/scheduled_query_runs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.sigma.ScheduledQueryRun)
