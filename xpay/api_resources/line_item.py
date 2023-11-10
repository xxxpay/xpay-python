# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay.xpay_object import XPayObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from xpay.api_resources.discount import Discount as DiscountResource
    from xpay.api_resources.price import Price
    from xpay.api_resources.tax_rate import TaxRate


class LineItem(XPayObject):
    """
    A line item.
    """

    OBJECT_NAME: ClassVar[Literal["item"]] = "item"

    class Discount(XPayObject):
        amount: int
        """
        The amount discounted.
        """
        discount: "DiscountResource"
        """
        A discount represents the actual application of a [coupon](https://xpay.com/docs/api#coupons) or [promotion code](https://xpay.com/docs/api#promotion_codes).
        It contains information about when the discount began, when it will end, and what it is applied to.

        Related guide: [Applying discounts to subscriptions](https://xpay.com/docs/billing/subscriptions/discounts)
        """

    class Tax(XPayObject):
        amount: int
        """
        Amount of tax applied for this rate.
        """
        rate: "TaxRate"
        """
        Tax rates can be applied to [invoices](https://xpay.com/docs/billing/invoices/tax-rates), [subscriptions](https://xpay.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://xpay.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

        Related guide: [Tax rates](https://xpay.com/docs/billing/taxes/tax-rates)
        """
        taxability_reason: Optional[
            Literal[
                "customer_exempt",
                "not_collecting",
                "not_subject_to_tax",
                "not_supported",
                "portion_product_exempt",
                "portion_reduced_rated",
                "portion_standard_rated",
                "product_exempt",
                "product_exempt_holiday",
                "proportionally_rated",
                "reduced_rated",
                "reverse_charge",
                "standard_rated",
                "taxable_basis_reduced",
                "zero_rated",
            ]
        ]
        """
        The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
        """
        taxable_amount: Optional[int]
        """
        The amount on which tax is calculated, in cents (or local equivalent).
        """

    amount_discount: int
    """
    Total discount amount applied. If no discounts were applied, defaults to 0.
    """
    amount_subtotal: int
    """
    Total before any discounts or taxes are applied.
    """
    amount_tax: int
    """
    Total tax amount applied. If no tax was applied, defaults to 0.
    """
    amount_total: int
    """
    Total after discounts and taxes.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://xpay.com/docs/currencies).
    """
    description: str
    """
    An arbitrary string attached to the object. Often useful for displaying to users. Defaults to product name.
    """
    discounts: Optional[List[Discount]]
    """
    The discounts applied to the line item.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["item"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    price: Optional["Price"]
    """
    The price used to generate the line item.
    """
    quantity: Optional[int]
    """
    The quantity of products being purchased.
    """
    taxes: Optional[List[Tax]]
    """
    The taxes applied to the line item.
    """

    _inner_class_types = {"discounts": Discount, "taxes": Tax}
