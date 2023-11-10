from xpay.api_resources.abstract.api_resource import APIResource
from typing import TypeVar, cast
from xpay.xpay_object import XPayObject

T = TypeVar("T", bound=XPayObject)


class CreateableAPIResource(APIResource[T]):
    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        xpay_version=None,
        xpay_account=None,
        **params
    ) -> T:
        return cast(
            T,
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                xpay_version,
                xpay_account,
                params,
            ),
        )
