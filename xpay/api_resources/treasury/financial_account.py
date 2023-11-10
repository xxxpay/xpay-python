# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay import util
from xpay.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from xpay.api_resources.list_object import ListObject
from xpay.request_options import RequestOptions
from xpay.xpay_object import XPayObject
from xpay.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from xpay.api_resources.treasury.financial_account_features import (
        FinancialAccountFeatures,
    )


class FinancialAccount(
    CreateableAPIResource["FinancialAccount"],
    ListableAPIResource["FinancialAccount"],
    UpdateableAPIResource["FinancialAccount"],
):
    """
    XPay Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance.
    FinancialAccounts serve as the source and destination of Treasury's money movement APIs.
    """

    OBJECT_NAME: ClassVar[
        Literal["treasury.financial_account"]
    ] = "treasury.financial_account"

    class Balance(XPayObject):
        cash: Dict[str, int]
        """
        Funds the user can spend right now.
        """
        inbound_pending: Dict[str, int]
        """
        Funds not spendable yet, but will become available at a later time.
        """
        outbound_pending: Dict[str, int]
        """
        Funds in the account, but not spendable because they are being held for pending outbound flows.
        """

    class FinancialAddress(XPayObject):
        class Aba(XPayObject):
            account_holder_name: str
            """
            The name of the person or business that owns the bank account.
            """
            account_number: Optional[str]
            """
            The account number.
            """
            account_number_last4: str
            """
            The last four characters of the account number.
            """
            bank_name: str
            """
            Name of the bank.
            """
            routing_number: str
            """
            Routing number for the account.
            """

        aba: Optional[Aba]
        """
        ABA Records contain U.S. bank account details per the ABA format.
        """
        supported_networks: Optional[List[Literal["ach", "us_domestic_wire"]]]
        """
        The list of networks that the address supports
        """
        type: Literal["aba"]
        """
        The type of financial address
        """
        _inner_class_types = {"aba": Aba}

    class PlatformRestrictions(XPayObject):
        inbound_flows: Optional[Literal["restricted", "unrestricted"]]
        """
        Restricts all inbound money movement.
        """
        outbound_flows: Optional[Literal["restricted", "unrestricted"]]
        """
        Restricts all outbound money movement.
        """

    class StatusDetails(XPayObject):
        class Closed(XPayObject):
            reasons: List[
                Literal["account_rejected", "closed_by_platform", "other"]
            ]
            """
            The array that contains reasons for a FinancialAccount closure.
            """

        closed: Optional[Closed]
        """
        Details related to the closure of this FinancialAccount
        """
        _inner_class_types = {"closed": Closed}

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            features: NotRequired["FinancialAccount.CreateParamsFeatures"]
            """
            Encodes whether a FinancialAccount has access to a particular feature. XPay or the platform can control features via the requested field.
            """
            metadata: NotRequired["Dict[str, str]"]
            """
            Set of [key-value pairs](https://xpay.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            platform_restrictions: NotRequired[
                "FinancialAccount.CreateParamsPlatformRestrictions"
            ]
            """
            The set of functionalities that the platform can restrict on the FinancialAccount.
            """
            supported_currencies: List[str]
            """
            The currencies the FinancialAccount can hold a balance in.
            """

        class CreateParamsPlatformRestrictions(TypedDict):
            inbound_flows: NotRequired["Literal['restricted', 'unrestricted']"]
            """
            Restricts all inbound money movement.
            """
            outbound_flows: NotRequired[
                "Literal['restricted', 'unrestricted']"
            ]
            """
            Restricts all outbound money movement.
            """

        class CreateParamsFeatures(TypedDict):
            card_issuing: NotRequired[
                "FinancialAccount.CreateParamsFeaturesCardIssuing"
            ]
            """
            Encodes the FinancialAccount's ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount.
            """
            deposit_insurance: NotRequired[
                "FinancialAccount.CreateParamsFeaturesDepositInsurance"
            ]
            """
            Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.
            """
            financial_addresses: NotRequired[
                "FinancialAccount.CreateParamsFeaturesFinancialAddresses"
            ]
            """
            Contains Features that add FinancialAddresses to the FinancialAccount.
            """
            inbound_transfers: NotRequired[
                "FinancialAccount.CreateParamsFeaturesInboundTransfers"
            ]
            """
            Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.
            """
            intra_xpay_flows: NotRequired[
                "FinancialAccount.CreateParamsFeaturesIntraXPayFlows"
            ]
            """
            Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).
            """
            outbound_payments: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundPayments"
            ]
            """
            Includes Features related to initiating money movement out of the FinancialAccount to someone else's bucket of money.
            """
            outbound_transfers: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundTransfers"
            ]
            """
            Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner.
            """

        class CreateParamsFeaturesOutboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundTransfersAch"
            ]
            """
            Enables ACH transfers via the OutboundTransfers API.
            """
            us_domestic_wire: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundTransfersUsDomesticWire"
            ]
            """
            Enables US domestic wire transfers via the OutboundTransfers API.
            """

        class CreateParamsFeaturesOutboundTransfersUsDomesticWire(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class CreateParamsFeaturesOutboundTransfersAch(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class CreateParamsFeaturesOutboundPayments(TypedDict):
            ach: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundPaymentsAch"
            ]
            """
            Enables ACH transfers via the OutboundPayments API.
            """
            us_domestic_wire: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundPaymentsUsDomesticWire"
            ]
            """
            Enables US domestic wire transfers via the OutboundPayments API.
            """

        class CreateParamsFeaturesOutboundPaymentsUsDomesticWire(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class CreateParamsFeaturesOutboundPaymentsAch(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class CreateParamsFeaturesIntraXPayFlows(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class CreateParamsFeaturesInboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.CreateParamsFeaturesInboundTransfersAch"
            ]
            """
            Enables ACH Debits via the InboundTransfers API.
            """

        class CreateParamsFeaturesInboundTransfersAch(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class CreateParamsFeaturesFinancialAddresses(TypedDict):
            aba: NotRequired[
                "FinancialAccount.CreateParamsFeaturesFinancialAddressesAba"
            ]
            """
            Adds an ABA FinancialAddress to the FinancialAccount.
            """

        class CreateParamsFeaturesFinancialAddressesAba(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class CreateParamsFeaturesDepositInsurance(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class CreateParamsFeaturesCardIssuing(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class ListParams(RequestOptions):
            created: NotRequired["FinancialAccount.ListParamsCreated|int"]
            ending_before: NotRequired["str"]
            """
            An object ID cursor for use in pagination.
            """
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int"]
            """
            A limit ranging from 1 to 100 (defaults to 10).
            """
            starting_after: NotRequired["str"]
            """
            An object ID cursor for use in pagination.
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int"]
            """
            Maximum value to filter by (inclusive)
            """

        class ModifyParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            features: NotRequired["FinancialAccount.ModifyParamsFeatures"]
            """
            Encodes whether a FinancialAccount has access to a particular feature, with a status enum and associated `status_details`. XPay or the platform may control features via the requested field.
            """
            metadata: NotRequired["Dict[str, str]"]
            """
            Set of [key-value pairs](https://xpay.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            platform_restrictions: NotRequired[
                "FinancialAccount.ModifyParamsPlatformRestrictions"
            ]
            """
            The set of functionalities that the platform can restrict on the FinancialAccount.
            """

        class ModifyParamsPlatformRestrictions(TypedDict):
            inbound_flows: NotRequired["Literal['restricted', 'unrestricted']"]
            """
            Restricts all inbound money movement.
            """
            outbound_flows: NotRequired[
                "Literal['restricted', 'unrestricted']"
            ]
            """
            Restricts all outbound money movement.
            """

        class ModifyParamsFeatures(TypedDict):
            card_issuing: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesCardIssuing"
            ]
            """
            Encodes the FinancialAccount's ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount.
            """
            deposit_insurance: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesDepositInsurance"
            ]
            """
            Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.
            """
            financial_addresses: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesFinancialAddresses"
            ]
            """
            Contains Features that add FinancialAddresses to the FinancialAccount.
            """
            inbound_transfers: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesInboundTransfers"
            ]
            """
            Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.
            """
            intra_xpay_flows: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesIntraXPayFlows"
            ]
            """
            Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).
            """
            outbound_payments: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundPayments"
            ]
            """
            Includes Features related to initiating money movement out of the FinancialAccount to someone else's bucket of money.
            """
            outbound_transfers: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundTransfers"
            ]
            """
            Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner.
            """

        class ModifyParamsFeaturesOutboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundTransfersAch"
            ]
            """
            Enables ACH transfers via the OutboundTransfers API.
            """
            us_domestic_wire: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundTransfersUsDomesticWire"
            ]
            """
            Enables US domestic wire transfers via the OutboundTransfers API.
            """

        class ModifyParamsFeaturesOutboundTransfersUsDomesticWire(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class ModifyParamsFeaturesOutboundTransfersAch(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class ModifyParamsFeaturesOutboundPayments(TypedDict):
            ach: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundPaymentsAch"
            ]
            """
            Enables ACH transfers via the OutboundPayments API.
            """
            us_domestic_wire: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundPaymentsUsDomesticWire"
            ]
            """
            Enables US domestic wire transfers via the OutboundPayments API.
            """

        class ModifyParamsFeaturesOutboundPaymentsUsDomesticWire(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class ModifyParamsFeaturesOutboundPaymentsAch(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class ModifyParamsFeaturesIntraXPayFlows(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class ModifyParamsFeaturesInboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesInboundTransfersAch"
            ]
            """
            Enables ACH Debits via the InboundTransfers API.
            """

        class ModifyParamsFeaturesInboundTransfersAch(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class ModifyParamsFeaturesFinancialAddresses(TypedDict):
            aba: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesFinancialAddressesAba"
            ]
            """
            Adds an ABA FinancialAddress to the FinancialAccount.
            """

        class ModifyParamsFeaturesFinancialAddressesAba(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class ModifyParamsFeaturesDepositInsurance(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class ModifyParamsFeaturesCardIssuing(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """

        class RetrieveFeaturesParams(RequestOptions):
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """

        class UpdateFeaturesParams(RequestOptions):
            card_issuing: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsCardIssuing"
            ]
            """
            Encodes the FinancialAccount's ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount.
            """
            deposit_insurance: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsDepositInsurance"
            ]
            """
            Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.
            """
            expand: NotRequired["List[str]"]
            """
            Specifies which fields in the response should be expanded.
            """
            financial_addresses: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsFinancialAddresses"
            ]
            """
            Contains Features that add FinancialAddresses to the FinancialAccount.
            """
            inbound_transfers: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsInboundTransfers"
            ]
            """
            Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.
            """
            intra_xpay_flows: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsIntraXPayFlows"
            ]
            """
            Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).
            """
            outbound_payments: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundPayments"
            ]
            """
            Includes Features related to initiating money movement out of the FinancialAccount to someone else's bucket of money.
            """
            outbound_transfers: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundTransfers"
            ]
            """
            Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner.
            """

        class UpdateFeaturesParamsOutboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundTransfersAch"
            ]
            """
            Enables ACH transfers via the OutboundTransfers API.
            """
            us_domestic_wire: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundTransfersUsDomesticWire"
            ]
            """
            Enables US domestic wire transfers via the OutboundTransfers API.
            """

        class UpdateFeaturesParamsOutboundTransfersUsDomesticWire(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class UpdateFeaturesParamsOutboundTransfersAch(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class UpdateFeaturesParamsOutboundPayments(TypedDict):
            ach: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundPaymentsAch"
            ]
            """
            Enables ACH transfers via the OutboundPayments API.
            """
            us_domestic_wire: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundPaymentsUsDomesticWire"
            ]
            """
            Enables US domestic wire transfers via the OutboundPayments API.
            """

        class UpdateFeaturesParamsOutboundPaymentsUsDomesticWire(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class UpdateFeaturesParamsOutboundPaymentsAch(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class UpdateFeaturesParamsIntraXPayFlows(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class UpdateFeaturesParamsInboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsInboundTransfersAch"
            ]
            """
            Enables ACH Debits via the InboundTransfers API.
            """

        class UpdateFeaturesParamsInboundTransfersAch(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class UpdateFeaturesParamsFinancialAddresses(TypedDict):
            aba: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsFinancialAddressesAba"
            ]
            """
            Adds an ABA FinancialAddress to the FinancialAccount.
            """

        class UpdateFeaturesParamsFinancialAddressesAba(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class UpdateFeaturesParamsDepositInsurance(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

        class UpdateFeaturesParamsCardIssuing(TypedDict):
            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """

    active_features: Optional[
        List[
            Literal[
                "card_issuing",
                "deposit_insurance",
                "financial_addresses.aba",
                "inbound_transfers.ach",
                "intra_xpay_flows",
                "outbound_payments.ach",
                "outbound_payments.us_domestic_wire",
                "outbound_transfers.ach",
                "outbound_transfers.us_domestic_wire",
                "remote_deposit_capture",
            ]
        ]
    ]
    """
    The array of paths to active Features in the Features hash.
    """
    balance: Balance
    """
    Balance information for the FinancialAccount
    """
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    features: Optional["FinancialAccountFeatures"]
    """
    Encodes whether a FinancialAccount has access to a particular Feature, with a `status` enum and associated `status_details`.
    XPay or the platform can control Features via the requested field.
    """
    financial_addresses: List[FinancialAddress]
    """
    The set of credentials that resolve to a FinancialAccount.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://xpay.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["treasury.financial_account"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    pending_features: Optional[
        List[
            Literal[
                "card_issuing",
                "deposit_insurance",
                "financial_addresses.aba",
                "inbound_transfers.ach",
                "intra_xpay_flows",
                "outbound_payments.ach",
                "outbound_payments.us_domestic_wire",
                "outbound_transfers.ach",
                "outbound_transfers.us_domestic_wire",
                "remote_deposit_capture",
            ]
        ]
    ]
    """
    The array of paths to pending Features in the Features hash.
    """
    platform_restrictions: Optional[PlatformRestrictions]
    """
    The set of functionalities that the platform can restrict on the FinancialAccount.
    """
    restricted_features: Optional[
        List[
            Literal[
                "card_issuing",
                "deposit_insurance",
                "financial_addresses.aba",
                "inbound_transfers.ach",
                "intra_xpay_flows",
                "outbound_payments.ach",
                "outbound_payments.us_domestic_wire",
                "outbound_transfers.ach",
                "outbound_transfers.us_domestic_wire",
                "remote_deposit_capture",
            ]
        ]
    ]
    """
    The array of paths to restricted Features in the Features hash.
    """
    status: Literal["closed", "open"]
    """
    The enum specifying what state the account is in.
    """
    status_details: StatusDetails
    supported_currencies: List[str]
    """
    The currencies the FinancialAccount can hold a balance in. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        xpay_version: Optional[str] = None,
        xpay_account: Optional[str] = None,
        **params: Unpack["FinancialAccount.CreateParams"]
    ) -> "FinancialAccount":
        """
        Creates a new FinancialAccount. For now, each connected account can only have one FinancialAccount.
        """
        return cast(
            "FinancialAccount",
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

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        xpay_version: Optional[str] = None,
        xpay_account: Optional[str] = None,
        **params: Unpack["FinancialAccount.ListParams"]
    ) -> ListObject["FinancialAccount"]:
        """
        Returns a list of FinancialAccounts.
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
    def modify(
        cls, id: str, **params: Unpack["FinancialAccount.ModifyParams"]
    ) -> "FinancialAccount":
        """
        Updates the details of a FinancialAccount.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "FinancialAccount",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["FinancialAccount.RetrieveParams"]
    ) -> "FinancialAccount":
        """
        Retrieves the details of a FinancialAccount.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_retrieve_features(
        cls,
        financial_account: str,
        api_key: Optional[str] = None,
        xpay_version: Optional[str] = None,
        xpay_account: Optional[str] = None,
        **params: Unpack["FinancialAccount.RetrieveFeaturesParams"]
    ) -> "FinancialAccountFeatures":
        """
        Retrieves Features information associated with the FinancialAccount.
        """
        return cast(
            "FinancialAccountFeatures",
            cls._static_request(
                "get",
                "/v1/treasury/financial_accounts/{financial_account}/features".format(
                    financial_account=util.sanitize_id(financial_account)
                ),
                api_key=api_key,
                xpay_version=xpay_version,
                xpay_account=xpay_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def retrieve_features(
        financial_account: str,
        api_key: Optional[str] = None,
        xpay_version: Optional[str] = None,
        xpay_account: Optional[str] = None,
        **params: Unpack["FinancialAccount.RetrieveFeaturesParams"]
    ) -> "FinancialAccountFeatures":
        """
        Retrieves Features information associated with the FinancialAccount.
        """
        ...

    @overload
    def retrieve_features(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["FinancialAccount.RetrieveFeaturesParams"]
    ) -> "FinancialAccountFeatures":
        """
        Retrieves Features information associated with the FinancialAccount.
        """
        ...

    @class_method_variant("_cls_retrieve_features")
    def retrieve_features(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["FinancialAccount.RetrieveFeaturesParams"]
    ) -> "FinancialAccountFeatures":
        """
        Retrieves Features information associated with the FinancialAccount.
        """
        return cast(
            "FinancialAccountFeatures",
            self._request(
                "get",
                "/v1/treasury/financial_accounts/{financial_account}/features".format(
                    financial_account=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def _cls_update_features(
        cls,
        financial_account: str,
        api_key: Optional[str] = None,
        xpay_version: Optional[str] = None,
        xpay_account: Optional[str] = None,
        **params: Unpack["FinancialAccount.UpdateFeaturesParams"]
    ) -> "FinancialAccountFeatures":
        """
        Updates the Features associated with a FinancialAccount.
        """
        return cast(
            "FinancialAccountFeatures",
            cls._static_request(
                "post",
                "/v1/treasury/financial_accounts/{financial_account}/features".format(
                    financial_account=util.sanitize_id(financial_account)
                ),
                api_key=api_key,
                xpay_version=xpay_version,
                xpay_account=xpay_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def update_features(
        financial_account: str,
        api_key: Optional[str] = None,
        xpay_version: Optional[str] = None,
        xpay_account: Optional[str] = None,
        **params: Unpack["FinancialAccount.UpdateFeaturesParams"]
    ) -> "FinancialAccountFeatures":
        """
        Updates the Features associated with a FinancialAccount.
        """
        ...

    @overload
    def update_features(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["FinancialAccount.UpdateFeaturesParams"]
    ) -> "FinancialAccountFeatures":
        """
        Updates the Features associated with a FinancialAccount.
        """
        ...

    @class_method_variant("_cls_update_features")
    def update_features(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["FinancialAccount.UpdateFeaturesParams"]
    ) -> "FinancialAccountFeatures":
        """
        Updates the Features associated with a FinancialAccount.
        """
        return cast(
            "FinancialAccountFeatures",
            self._request(
                "post",
                "/v1/treasury/financial_accounts/{financial_account}/features".format(
                    financial_account=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    _inner_class_types = {
        "balance": Balance,
        "financial_addresses": FinancialAddress,
        "platform_restrictions": PlatformRestrictions,
        "status_details": StatusDetails,
    }
