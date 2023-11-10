import os
from codecs import open
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

os.chdir(here)

with open(
    os.path.join(here, "LONG_DESCRIPTION.rst"), "r", encoding="utf-8"
) as fp:
    long_description = fp.read()

version_contents = {}
with open(os.path.join(here, "xpay", "version.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)

setup(
    name="xpay",
    version=version_contents["VERSION"],
    description="Python bindings for the XPay API",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="XPay",
    author_email="support@xpay.com",
    url="https://github.com/xxxpay/xpay-python",
    license="MIT",
    keywords="xpay api payments",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"xpay": ["data/ca-certificates.crt", "py.typed"]},
    zip_safe=False,
    install_requires=[
        'typing_extensions <= 4.2.0, > 3.7.2; python_version < "3.7"',
        # The best typing support comes from 4.5.0+ but we can support down to
        # 3.7.2 without throwing exceptions.
        'typing_extensions >= 4.5.0; python_version >= "3.7"',
        'requests >= 2.20; python_version >= "3.0"',
    ],
    python_requires=">=3.6",
    project_urls={
        "Bug Tracker": "https://github.com/xxxpay/xpay-python/issues",
        "Changes": "https://github.com/xxxpay/xpay-python/blob/master/CHANGELOG.md",
        "Documentation": "https://xpay.com/docs/api/?lang=python",
        "Source Code": "https://github.com/xxxpay/xpay-python",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    setup_requires=["wheel"],
)
