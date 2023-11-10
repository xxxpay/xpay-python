# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay.api_resources.list_object import ListObject
from xpay.xpay_object import XPayObject
from typing import ClassVar
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from xpay.api_resources.financial_connections.account_owner import (
        AccountOwner,
    )


class AccountOwnership(XPayObject):
    """
    Describes a snapshot of the owners of an account at a particular point in time.
    """

    OBJECT_NAME: ClassVar[
        Literal["financial_connections.account_ownership"]
    ] = "financial_connections.account_ownership"
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["financial_connections.account_ownership"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    owners: ListObject["AccountOwner"]
    """
    A paginated list of owners for this account.
    """
