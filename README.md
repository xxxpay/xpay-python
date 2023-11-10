# XPay Python Library

[![pypi](https://img.shields.io/pypi/v/xpay.svg)](https://pypi.python.org/pypi/xpay)
[![Build Status](https://github.com/xpay/xpay-python/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/xpay/xpay-python/actions?query=branch%3Amaster)
[![Coverage Status](https://coveralls.io/repos/github/xpay/xpay-python/badge.svg?branch=master)](https://coveralls.io/github/xpay/xpay-python?branch=master)

The XPay Python library provides convenient access to the XPay API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses which makes it compatible with a wide range of versions of the XPay
API.

## Documentation

See the [Python API docs](https://xpay.com/docs/api?lang=python).

See [video demonstrations][youtube-playlist] covering how to use the library.

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade xpay
```

Install from source with:

```sh
python setup.py install
```

### Requirements

- Python 3.6+ (PyPy supported)

#### Python 2.7 deprecation

[The Python Software Foundation (PSF)](https://www.python.org/psf-landing/) community [announced the end of support of Python 2](https://www.python.org/doc/sunset-python-2/) on 01 January 2020.
Starting with version 6.0.0 XPay SDK Python packages will no longer support Python 2.7. To continue to get new features and security updates, please make sure to update your Python runtime to Python 3.6+.

The last version of the XPay SDK that supports Python 2.7 is 5.5.0.

## Usage

The library needs to be configured with your account's secret key which is
available in your [XPay Dashboard][api-keys]. Set `xpay.api_key` to its
value:

```python
import xpay
xpay.api_key = "sk_test_..."

# list customers
customers = xpay.Customer.list()

# print the first customer's email
print(customers.data[0].email)

# retrieve specific Customer
customer = xpay.Customer.retrieve("cus_123456789")

# print that customer's email
print(customer.email)
```

### Handling exceptions

Unsuccessful requests raise exceptions. The class of the exception will reflect
the sort of error that occurred. Please see the [Api
Reference](https://xpay.com/docs/api/errors/handling) for a description of
the error classes you should handle, and for information on how to inspect
these errors.

### Per-request Configuration

Configure individual requests with keyword arguments. For example, you can make
requests with a specific [XPay Version](https://xpay.com/docs/api#versioning)
or as a [connected account](https://xpay.com/docs/connect/authentication#authentication-via-the-xpay-account-header):

```python
import xpay

# list customers
xpay.Customer.list(
    api_key="sk_test_...",
    xpay_account="acct_...",
    xpay_version="2019-02-19"
)

# retrieve single customer
xpay.Customer.retrieve(
    "cus_123456789",
    api_key="sk_test_...",
    xpay_account="acct_...",
    xpay_version="2019-02-19"
)
```

### Configuring a Client

The library can be configured to use `urlfetch`, `requests`, `pycurl`, or
`urllib2` with `xpay.default_http_client`:

```python
client = xpay.http_client.UrlFetchClient()
client = xpay.http_client.RequestsClient()
client = xpay.http_client.PycurlClient()
client = xpay.http_client.Urllib2Client()
xpay.default_http_client = client
```

Without a configured client, by default the library will attempt to load
libraries in the order above (i.e. `urlfetch` is preferred with `urllib2` used
as a last resort). We usually recommend that people use `requests`.

### Configuring a Proxy

A proxy can be configured with `xpay.proxy`:

```python
xpay.proxy = "https://user:pass@example.com:1234"
```

### Configuring Automatic Retries

You can enable automatic retries on requests that fail due to a transient
problem by configuring the maximum number of retries:

```python
xpay.max_network_retries = 2
```

Various errors can trigger a retry, like a connection error or a timeout, and
also certain API responses like HTTP status `409 Conflict`.

[Idempotency keys][idempotency-keys] are automatically generated and added to
requests, when not given, to guarantee that retries are safe.

### Logging

The library can be configured to emit logging that will give you better insight
into what it's doing. The `info` logging level is usually most appropriate for
production use, but `debug` is also available for more verbosity.

There are a few options for enabling it:

1. Set the environment variable `STRIPE_LOG` to the value `debug` or `info`

    ```sh
    $ export STRIPE_LOG=debug
    ```

2. Set `xpay.log`:

    ```python
    import xpay
    xpay.log = 'debug'
    ```

3. Enable it through Python's logging module:

    ```python
    import logging
    logging.basicConfig()
    logging.getLogger('xpay').setLevel(logging.DEBUG)
    ```

### Accessing response code and headers

You can access the HTTP response code and headers using the `last_response` property of the returned resource.

```python
customer = xpay.Customer.retrieve(
    "cus_123456789"
)

print(customer.last_response.code)
print(customer.last_response.headers)
```

### Writing a Plugin

If you're writing a plugin that uses the library, we'd appreciate it if you
identified using `xpay.set_app_info()`:

```py
xpay.set_app_info("MyAwesomePlugin", version="1.2.34", url="https://myawesomeplugin.info")
```

This information is passed along when the library makes calls to the XPay
API.

### Request latency telemetry

By default, the library sends request latency telemetry to XPay. These
numbers help XPay improve the overall latency of its API for all users.

You can disable this behavior if you prefer:

```python
xpay.enable_telemetry = False
```

### Beta SDKs

XPay has features in the beta phase that can be accessed via the beta version of this package.
We would love for you to try these and share feedback with us before these features reach the stable phase.
To install a beta version use `pip install` with the exact version you'd like to use:

```
pip install xpay==5.3.0b3
```

> **Note**
> There can be breaking changes between beta versions. Therefore we recommend pinning the package version to a specific beta version in your [requirements file](https://pip.pypa.io/en/stable/user_guide/#requirements-files) or `setup.py`. This way you can install the same version each time without breaking changes unless you are intentionally looking for the latest beta version.

We highly recommend keeping an eye on when the beta feature you are interested in goes from beta to stable so that you can move from using a beta version of the SDK to the stable version.

If your beta feature requires a `XPay-Version` header to be sent, use the `xpay.api_version` field to set it:

```python
xpay.api_version += "; feature_beta=v3"
```

## Support

New features and bug fixes are released on the latest major version of the XPay Python library. If you are on an older major version, we recommend that you upgrade to the latest in order to use the new features and bug fixes including those for security vulnerabilities. Older major versions of the package will continue to be available for use, but will not be receiving any updates.

## Development

The test suite depends on [xpay-mock], so make sure to fetch and run it from a
background terminal ([xpay-mock's README][xpay-mock] also contains
instructions for installing via Homebrew and other methods):

```sh
go install github.com/xpay/xpay-mock@latest
xpay-mock
```

Run the following command to set up the development virtualenv:

```sh
make
```

Run all tests on all supported Python versions:

```sh
make test
```

Run all tests for a specific Python version (modify `-e` according to your Python target):

```sh
TOX_ARGS="-e py37" make test
```

Run all tests in a single file:

```sh
TOX_ARGS="-e py37 -- tests/api_resources/abstract/test_updateable_api_resource.py" make test
```

Run a single test suite:

```sh
TOX_ARGS="-e py37 -- tests/api_resources/abstract/test_updateable_api_resource.py::TestUpdateableAPIResource" make test
```

Run a single test:

```sh
TOX_ARGS="-e py37 -- tests/api_resources/abstract/test_updateable_api_resource.py::TestUpdateableAPIResource::test_save" make test
```

Run the linter with:

```sh
make lint
```

The library uses [Black][black] for code formatting. Code must be formatted
with Black before PRs are submitted, otherwise CI will fail. Run the formatter
with:

```sh
make fmt
```

[api-keys]: https://dashboard.xpay.com/account/apikeys
[black]: https://github.com/ambv/black
[connect]: https://xpay.com/connect
[poetry]: https://github.com/sdispater/poetry
[xpay-mock]: https://github.com/xpay/xpay-mock
[idempotency-keys]: https://xpay.com/docs/api/idempotent_requests?lang=python
[youtube-playlist]: https://www.youtube.com/playlist?list=PLy1nL-pvL2M55YVn0mGoQ5r-39A1-ZypO

<!--
# vim: set tw=79:
-->
