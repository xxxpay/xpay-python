from xpay.api_resources.abstract.api_resource import APIResource
from xpay.api_resources.list_object import ListObject
from xpay.xpay_object import XPayObject
from typing import TypeVar

T = TypeVar("T", bound=XPayObject)


class ListableAPIResource(APIResource[T]):
    @classmethod
    def auto_paging_iter(cls, *args, **params):
        return cls.list(*args, **params).auto_paging_iter()

    @classmethod
    def list(
        cls, api_key=None, xpay_version=None, xpay_account=None, **params
    ) -> ListObject[T]:
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
                % (type(result).__name__,)
            )

        return result
