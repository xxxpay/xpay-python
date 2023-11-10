from typing import Optional
from typing_extensions import TYPE_CHECKING
from xpay.util import merge_dicts
from xpay.xpay_object import XPayObject

if TYPE_CHECKING:
    from xpay.api_resources.payment_intent import PaymentIntent
    from xpay.api_resources.setup_intent import SetupIntent
    from xpay.api_resources.source import Source
    from xpay.api_resources.payment_method import PaymentMethod


class ErrorObject(XPayObject):
    charge: Optional[str]
    code: int
    decline_code: Optional[str]
    doc_url: Optional[str]
    message: Optional[str]
    param: Optional[str]
    payment_intent: Optional["PaymentIntent"]
    payment_method: Optional["PaymentMethod"]
    setup_intent: Optional["SetupIntent"]
    source: Optional["Source"]
    type: str

    def refresh_from(
        self,
        values,
        api_key=None,
        partial=False,
        xpay_version=None,
        xpay_account=None,
        last_response=None,
    ):
        # Unlike most other API resources, the API will omit attributes in
        # error objects when they have a null value. We manually set default
        # values here to facilitate generic error handling.
        values = merge_dicts(
            {
                "charge": None,
                "code": None,
                "decline_code": None,
                "doc_url": None,
                "message": None,
                "param": None,
                "payment_intent": None,
                "payment_method": None,
                "setup_intent": None,
                "source": None,
                "type": None,
            },
            values,
        )
        return super(ErrorObject, self).refresh_from(
            values,
            api_key,
            partial,
            xpay_version,
            xpay_account,
            last_response,
        )


class OAuthErrorObject(XPayObject):
    def refresh_from(
        self,
        values,
        api_key=None,
        partial=False,
        xpay_version=None,
        xpay_account=None,
        last_response=None,
    ):
        # Unlike most other API resources, the API will omit attributes in
        # error objects when they have a null value. We manually set default
        # values here to facilitate generic error handling.
        values = merge_dicts(
            {"error": None, "error_description": None}, values
        )
        return super(OAuthErrorObject, self).refresh_from(
            values,
            api_key,
            partial,
            xpay_version,
            xpay_account,
            last_response,
        )
