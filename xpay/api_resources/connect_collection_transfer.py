# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay.api_resources.expandable_field import ExpandableField
from xpay.xpay_object import XPayObject
from typing import ClassVar
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from xpay.api_resources.account import Account


class ConnectCollectionTransfer(XPayObject):
    OBJECT_NAME: ClassVar[
        Literal["connect_collection_transfer"]
    ] = "connect_collection_transfer"
    amount: int
    """
    Amount transferred, in cents (or local equivalent).
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://xpay.com/docs/currencies).
    """
    destination: ExpandableField["Account"]
    """
    ID of the account that funds are being collected for.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["connect_collection_transfer"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
