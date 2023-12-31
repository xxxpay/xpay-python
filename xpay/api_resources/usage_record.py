# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay import api_requestor, util
from xpay.api_resources.abstract import APIResource
from typing import ClassVar
from typing_extensions import Literal


class UsageRecord(APIResource["UsageRecord"]):
    """
    Usage records allow you to report customer usage and metrics to XPay for
    metered billing of subscription prices.

    Related guide: [Metered billing](https://xpay.com/docs/billing/subscriptions/metered-billing)
    """

    OBJECT_NAME: ClassVar[Literal["usage_record"]] = "usage_record"
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["usage_record"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    quantity: int
    """
    The usage quantity for the specified date.
    """
    subscription_item: str
    """
    The ID of the subscription item this usage record contains data for.
    """
    timestamp: int
    """
    The timestamp when this usage occurred.
    """

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        xpay_version=None,
        xpay_account=None,
        **params
    ):
        if "subscription_item" not in params:
            raise ValueError("Params must have a subscription_item key")

        subscription_item = params.pop("subscription_item")

        requestor = api_requestor.APIRequestor(
            api_key, api_version=xpay_version, account=xpay_account
        )
        url = "/v1/subscription_items/%s/usage_records" % subscription_item
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request("post", url, params, headers)

        return util.convert_to_xpay_object(
            response, api_key, xpay_version, xpay_account
        )
