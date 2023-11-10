# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay.xpay_object import XPayObject
from typing import ClassVar
from typing_extensions import Literal


class TaxDeductedAtSource(XPayObject):
    OBJECT_NAME: ClassVar[
        Literal["tax_deducted_at_source"]
    ] = "tax_deducted_at_source"
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["tax_deducted_at_source"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    period_end: int
    """
    The end of the invoicing period. This TDS applies to XPay fees collected during this invoicing period.
    """
    period_start: int
    """
    The start of the invoicing period. This TDS applies to XPay fees collected during this invoicing period.
    """
    tax_deduction_account_number: str
    """
    The TAN that was supplied to XPay when TDS was assessed
    """
