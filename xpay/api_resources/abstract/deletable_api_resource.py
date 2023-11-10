from xpay import util
from xpay.api_resources.abstract.api_resource import APIResource
from urllib.parse import quote_plus
from typing import TypeVar, cast
from xpay.xpay_object import XPayObject

T = TypeVar("T", bound=XPayObject)


class DeletableAPIResource(APIResource[T]):
    @classmethod
    def _cls_delete(cls, sid, **params) -> T:
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(T, cls._static_request("delete", url, params=params))

    @util.class_method_variant("_cls_delete")
    def delete(self, **params) -> T:
        return cast(
            T,
            self._request_and_refresh(
                "delete", self.instance_url(), params=params
            ),
        )
