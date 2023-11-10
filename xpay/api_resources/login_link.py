# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay.xpay_object import XPayObject
from typing import ClassVar
from typing_extensions import Literal


class LoginLink(XPayObject):
    """
    Login Links are single-use login link for an Express account to access their XPay dashboard.
    """

    OBJECT_NAME: ClassVar[Literal["login_link"]] = "login_link"
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    object: Literal["login_link"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    url: str
    """
    The URL for the login link.
    """
