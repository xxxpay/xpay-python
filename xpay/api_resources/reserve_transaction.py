# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay.xpay_object import XPayObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class ReserveTransaction(XPayObject):
    OBJECT_NAME: ClassVar[
        Literal["reserve_transaction"]
    ] = "reserve_transaction"
    amount: int
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://xpay.com/docs/currencies).
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["reserve_transaction"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
