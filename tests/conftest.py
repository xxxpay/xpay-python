import atexit
import os
import sys
from distutils.version import StrictVersion

import pytest

import xpay
from urllib.request import urlopen
from urllib.error import HTTPError

from tests.request_mock import RequestMock
from tests.xpay_mock import XPayMock

MOCK_MINIMUM_VERSION = "0.109.0"

# Starts xpay-mock if an OpenAPI spec override is found in `openapi/`, and
# otherwise fall back to `STRIPE_MOCK_PORT` or 12111.
if XPayMock.start():
    MOCK_PORT = XPayMock.port()
else:
    MOCK_PORT = os.environ.get("STRIPE_MOCK_PORT", 12111)


@atexit.register
def stop_xpay_mock():
    XPayMock.stop()


def pytest_configure(config):
    if not config.getoption("--nomock"):
        try:
            resp = urlopen("http://localhost:%s/" % MOCK_PORT)
            info = resp.info()
            version = info.get("XPay-Mock-Version")
            if version != "master" and StrictVersion(version) < StrictVersion(
                MOCK_MINIMUM_VERSION
            ):
                sys.exit(
                    "Your version of xpay-mock (%s) is too old. The minimum "
                    "version to run this test suite is %s. Please "
                    "see its repository for upgrade instructions."
                    % (version, MOCK_MINIMUM_VERSION)
                )

        except HTTPError as e:
            info = e.info()
        except Exception:
            sys.exit(
                "Couldn't reach xpay-mock at `localhost:%s`. Is "
                "it running? Please see README for setup instructions."
                % MOCK_PORT
            )


def pytest_addoption(parser):
    parser.addoption(
        "--nomock",
        action="store_true",
        help="only run tests that don't need xpay-mock",
    )


def pytest_runtest_setup(item):
    if "request_mock" in item.fixturenames and item.config.getoption(
        "--nomock"
    ):
        pytest.skip(
            "run xpay-mock locally and remove --nomock flag to run skipped tests"
        )


@pytest.fixture(autouse=True)
def setup_xpay():
    orig_attrs = {
        "api_base": xpay.api_base,
        "upload_api_base": xpay.upload_api_base,
        "api_key": xpay.api_key,
        "client_id": xpay.client_id,
        "default_http_client": xpay.default_http_client,
    }
    http_client = xpay.http_client.new_default_http_client()
    xpay.api_base = "http://localhost:%s" % MOCK_PORT
    xpay.upload_api_base = "http://localhost:%s" % MOCK_PORT
    xpay.api_key = "sk_test_123"
    xpay.client_id = "ca_123"
    xpay.default_http_client = http_client
    yield
    http_client.close()
    xpay.api_base = orig_attrs["api_base"]
    xpay.upload_api_base = orig_attrs["upload_api_base"]
    xpay.api_key = orig_attrs["api_key"]
    xpay.client_id = orig_attrs["client_id"]
    xpay.default_http_client = orig_attrs["default_http_client"]


@pytest.fixture
def request_mock(mocker):
    return RequestMock(mocker)
