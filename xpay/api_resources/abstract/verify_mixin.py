from typing import Optional, Any, Dict
from typing_extensions import Protocol

from xpay.xpay_object import XPayObject


class _Verifiable(Protocol):
    def instance_url(self) -> str:
        ...

    def _request(
        self,
        method: str,
        url: str,
        idempotency_key: Optional[str],
        params: Dict[str, Any],
    ) -> XPayObject:
        ...


class VerifyMixin(object):
    def verify(self: _Verifiable, idempotency_key=None, **params):
        url = self.instance_url() + "/verify"
        return self._request(
            "post", url, idempotency_key=idempotency_key, params=params
        )
