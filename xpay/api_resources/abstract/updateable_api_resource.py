from xpay import util
from xpay.api_resources.abstract.api_resource import APIResource
from urllib.parse import quote_plus
from typing import TypeVar, cast
from xpay.xpay_object import XPayObject

T = TypeVar("T", bound=XPayObject)


class UpdateableAPIResource(APIResource[T]):
    @classmethod
    def modify(cls, sid, **params) -> T:
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(T, cls._static_request("post", url, params=params))

    @util.deprecated(
        "The `save` method is deprecated and will be removed in a future major version of the library. Use the class method `modify` on the resource instead."
    )
    def save(self, idempotency_key=None):
        updated_params = self.serialize(None)
        if updated_params:
            self._request_and_refresh(
                "post",
                self.instance_url(),
                idempotency_key=idempotency_key,
                params=updated_params,
            )
        else:
            util.logger.debug("Trying to save already saved object %r", self)
        return self
