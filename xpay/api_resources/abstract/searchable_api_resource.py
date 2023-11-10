from xpay.api_resources.abstract.api_resource import APIResource
from xpay.api_resources.search_result_object import SearchResultObject
from typing import TypeVar
from xpay.xpay_object import XPayObject


T = TypeVar("T", bound="XPayObject")


class SearchableAPIResource(APIResource[T]):
    @classmethod
    def _search(
        cls,
        search_url,
        api_key=None,
        xpay_version=None,
        xpay_account=None,
        **params
    ):
        ret = cls._static_request(
            "get",
            search_url,
            api_key=api_key,
            xpay_version=xpay_version,
            xpay_account=xpay_account,
            params=params,
        )
        if not isinstance(ret, SearchResultObject):
            raise TypeError(
                "Expected search result from API, got %s"
                % (type(ret).__name__,)
            )

        return ret

    @classmethod
    def search(cls, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        raise NotImplementedError
