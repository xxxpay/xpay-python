import xpay


TEST_RESOURCE_ID = "in_123"


class TestInvoice(object):
    def test_is_listable(self, request_mock):
        resources = xpay.Invoice.list()
        request_mock.assert_requested("get", "/v1/invoices")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.Invoice)

    def test_is_retrievable(self, request_mock):
        resource = xpay.Invoice.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_is_creatable(self, request_mock):
        resource = xpay.Invoice.create(customer="cus_123")
        request_mock.assert_requested("post", "/v1/invoices")
        assert isinstance(resource, xpay.Invoice)

    def test_is_saveable(self, request_mock):
        resource = xpay.Invoice.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = xpay.Invoice.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_is_deletable(self, request_mock):
        resource = xpay.Invoice.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = xpay.Invoice.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_finalize_invoice(self, request_mock):
        resource = xpay.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.finalize_invoice()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_can_finalize_invoice_classmethod(self, request_mock):
        resource = xpay.Invoice.finalize_invoice(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_can_mark_uncollectible(self, request_mock):
        resource = xpay.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.mark_uncollectible()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/mark_uncollectible" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_can_mark_uncollectible_classmethod(self, request_mock):
        resource = xpay.Invoice.mark_uncollectible(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/mark_uncollectible" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_can_pay(self, request_mock):
        resource = xpay.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.pay()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/pay" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_can_pay_classmethod(self, request_mock):
        resource = xpay.Invoice.pay(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/pay" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_can_send_invoice(self, request_mock):
        resource = xpay.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.send_invoice()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/send" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_can_send_invoice_classmethod(self, request_mock):
        resource = xpay.Invoice.send_invoice(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/send" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_can_upcoming(self, request_mock):
        resource = xpay.Invoice.upcoming(customer="cus_123")
        request_mock.assert_requested("get", "/v1/invoices/upcoming")
        assert isinstance(resource, xpay.Invoice)

    def test_can_void_invoice(self, request_mock):
        resource = xpay.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.void_invoice()
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/void" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_can_void_invoice_classmethod(self, request_mock):
        resource = xpay.Invoice.void_invoice(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/invoices/%s/void" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, xpay.Invoice)

    def test_can_iterate_lines(self, request_mock):
        resource = xpay.Invoice.retrieve(TEST_RESOURCE_ID)
        assert isinstance(resource.lines.data, list)
        assert isinstance(resource.lines.data[0], xpay.InvoiceLineItem)
        seen = [item["id"] for item in resource.lines.auto_paging_iter()]

        assert seen.__len__() > 0
