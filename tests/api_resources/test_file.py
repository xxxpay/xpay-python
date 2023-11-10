import tempfile

import pytest

import xpay


TEST_RESOURCE_ID = "file_123"


class TestFile(object):
    @pytest.fixture(scope="function")
    def setup_upload_api_base(self):
        xpay.upload_api_base = xpay.api_base
        xpay.api_base = None
        yield
        xpay.api_base = xpay.upload_api_base
        xpay.upload_api_base = "https://files.stripe.com"

    def test_is_listable(self, request_mock):
        resources = xpay.File.list()
        request_mock.assert_requested("get", "/v1/files")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], xpay.File)

    def test_is_retrievable(self, request_mock):
        resource = xpay.File.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v1/files/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, xpay.File)

    def test_is_creatable(self, mocker):
        hc = mocker.Mock(xpay.http_client.HTTPClient)
        hc.name = "mockclient"
        xpay.default_http_client = hc
        hc.request_with_retries.return_value = ('{"object": "file"}', 200, {})
        xpay.multipart_data_generator.MultipartDataGenerator._initialize_boundary = (
            lambda self: 1234567890
        )
        test_file = tempfile.TemporaryFile()
        resource = xpay.File.create(
            purpose="dispute_evidence",
            file=test_file,
            file_link_data={"create": True},
        )
        method, url, headers, body = hc.request_with_retries.call_args[0]
        assert method == "post"
        assert url.endswith("/v1/files")
        assert (
            headers["Content-Type"]
            == "multipart/form-data; boundary=1234567890"
        )
        parts = body.split(b"--1234567890")
        assert len(parts) == 5
        assert parts[0] == b""
        assert b'name="purpose"' in parts[1]
        assert b'name="file"' in parts[2]
        assert b'name="file_link_data[create]"' in parts[3]
        assert isinstance(resource, xpay.File)

    def test_create_respects_xpay_version(
        self, setup_upload_api_base, request_mock
    ):
        test_file = tempfile.TemporaryFile()
        xpay.File.create(
            purpose="dispute_evidence", file=test_file, xpay_version="foo"
        )
        request_mock.assert_api_version("foo")

    # You can use api_version instead of xpay_version
    # in File.create. We preserve it for backwards compatibility
    def test_create_respects_api_version(
        self, setup_upload_api_base, request_mock
    ):
        test_file = tempfile.TemporaryFile()
        xpay.File.create(
            purpose="dispute_evidence", file=test_file, api_version="foo"
        )
        request_mock.assert_api_version("foo")

    def test_deserializes_from_file(self):
        obj = xpay.util.convert_to_xpay_object({"object": "file"})
        assert isinstance(obj, xpay.File)

    def test_deserializes_from_file_upload(self):
        obj = xpay.util.convert_to_xpay_object({"object": "file_upload"})
        assert isinstance(obj, xpay.File)
