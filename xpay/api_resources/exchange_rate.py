# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay.api_resources.abstract import ListableAPIResource
from xpay.api_resources.list_object import ListObject
from xpay.request_options import RequestOptions
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class ExchangeRate(ListableAPIResource["ExchangeRate"]):
    """
    `ExchangeRate` objects allow you to determine the rates that XPay is currently
    using to convert from one currency to another. Since this number is variable
    throughout the day, there are various reasons why you might want to know the current
    rate (for example, to dynamically price an item for a user with a default
    payment in a foreign currency).

    Please refer to our [Exchange Rates API](https://xpay.com/docs/fx-rates) guide for more details.

    *[Note: this integration path is supported but no longer recommended]* Additionally,
    you can guarantee that a charge is made with an exchange rate that you expect is
    current. To do so, you must pass in the exchange_rate to charges endpoints. If the
    value is no longer up to date, the charge won't go through. Please refer to our
    [Using with charges](https://xpay.com/docs/exchange-rates) guide for more details.

    -----

    &nbsp;

    *This Exchange Rates API is a Beta Service and is subject to XPay's terms of service. You may use the API solely for the purpose of transacting on XPay. For example, the API may be queried in order to:*

    - *localize prices for processing payments on XPay*
    - *reconcile XPay transactions*
    - *determine how much money to send to a connected account*
    - *determine app fees to charge a connected account*

    *Using this Exchange Rates API beta for any purpose other than to transact on XPay is strictly prohibited and constitutes a violation of XPay's terms of service.*
    """

    OBJECT_NAME: ClassVar[Literal["exchange_rate"]] = "exchange_rate"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str"]
            """
            A cursor for use in pagination. `ending_before` is the currency that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with the exchange rate for currency X your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and total number of supported payout currencies, and the default is the max.
            """
            starting_after: NotRequired["str"]
            """
            A cursor for use in pagination. `starting_after` is the currency that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with the exchange rate for currency X, your subsequent call can include `starting_after=X` in order to fetch the next page of the list.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """

    id: str
    """
    Unique identifier for the object. Represented as the three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) in lowercase.
    """
    object: Literal["exchange_rate"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    rates: Dict[str, float]
    """
    Hash where the keys are supported currencies and the values are the exchange rate at which the base id currency converts to the key currency.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        xpay_version: Optional[str] = None,
        xpay_account: Optional[str] = None,
        **params: Unpack["ExchangeRate.ListParams"]
    ) -> ListObject["ExchangeRate"]:
        """
        Returns a list of objects that contain the rates at which foreign currencies are converted to one another. Only shows the currencies for which XPay supports.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            xpay_version=xpay_version,
            xpay_account=xpay_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["ExchangeRate.RetrieveParams"]
    ) -> "ExchangeRate":
        """
        Retrieves the exchange rates from the given currency to every supported currency.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance
