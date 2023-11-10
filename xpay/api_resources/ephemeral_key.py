# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay import api_requestor, util
from xpay.api_resources.abstract import DeletableAPIResource
from xpay.request_options import RequestOptions
from xpay.util import class_method_variant
from typing import ClassVar, List, Optional, cast, overload
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING
from urllib.parse import quote_plus


class EphemeralKey(DeletableAPIResource["EphemeralKey"]):
    OBJECT_NAME: ClassVar[Literal["ephemeral_key"]] = "ephemeral_key"
    if TYPE_CHECKING:

        class DeleteParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    expires: int
    """
    Time at which the key will expire. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["ephemeral_key"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    secret: Optional[str]
    """
    The key's secret. You can use this value to make authorized requests to the XPay API.
    """

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["EphemeralKey.DeleteParams"]
    ) -> "EphemeralKey":
        """
        Invalidates a short-lived API key for a given resource.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "EphemeralKey",
            cls._static_request("delete", url, params=params),
        )

    @overload
    @staticmethod
    def delete(
        sid: str, **params: Unpack["EphemeralKey.DeleteParams"]
    ) -> "EphemeralKey":
        """
        Invalidates a short-lived API key for a given resource.
        """
        ...

    @overload
    def delete(
        self, **params: Unpack["EphemeralKey.DeleteParams"]
    ) -> "EphemeralKey":
        """
        Invalidates a short-lived API key for a given resource.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["EphemeralKey.DeleteParams"]
    ) -> "EphemeralKey":
        """
        Invalidates a short-lived API key for a given resource.
        """
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        xpay_version=None,
        xpay_account=None,
        **params
    ):
        if xpay_version is None:
            raise ValueError(
                "xpay_version must be specified to create an ephemeral "
                "key"
            )

        requestor = api_requestor.APIRequestor(
            api_key, api_version=xpay_version, account=xpay_account
        )

        url = cls.class_url()
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request("post", url, params, headers)
        return util.convert_to_xpay_object(
            response, api_key, xpay_version, xpay_account
        )
