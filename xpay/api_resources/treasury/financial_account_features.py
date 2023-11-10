# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from xpay.xpay_object import XPayObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class FinancialAccountFeatures(XPayObject):
    """
    Encodes whether a FinancialAccount has access to a particular Feature, with a `status` enum and associated `status_details`.
    XPay or the platform can control Features via the requested field.
    """

    OBJECT_NAME: ClassVar[
        Literal["treasury.financial_account_features"]
    ] = "treasury.financial_account_features"

    class CardIssuing(XPayObject):
        class StatusDetail(XPayObject):
            code: Literal[
                "activating",
                "capability_not_requested",
                "financial_account_closed",
                "rejected_other",
                "rejected_unsupported_business",
                "requirements_past_due",
                "requirements_pending_verification",
                "restricted_by_platform",
                "restricted_other",
            ]
            """
            Represents the reason why the status is `pending` or `restricted`.
            """
            resolution: Optional[
                Literal[
                    "contact_xpay",
                    "provide_information",
                    "remove_restriction",
                ]
            ]
            """
            Represents what the user should do, if anything, to activate the Feature.
            """
            restriction: Optional[Literal["inbound_flows", "outbound_flows"]]
            """
            The `platform_restrictions` that are restricting this Feature.
            """

        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """
        status: Literal["active", "pending", "restricted"]
        """
        Whether the Feature is operational.
        """
        status_details: List[StatusDetail]
        """
        Additional details; includes at least one entry when the status is not `active`.
        """
        _inner_class_types = {"status_details": StatusDetail}

    class DepositInsurance(XPayObject):
        class StatusDetail(XPayObject):
            code: Literal[
                "activating",
                "capability_not_requested",
                "financial_account_closed",
                "rejected_other",
                "rejected_unsupported_business",
                "requirements_past_due",
                "requirements_pending_verification",
                "restricted_by_platform",
                "restricted_other",
            ]
            """
            Represents the reason why the status is `pending` or `restricted`.
            """
            resolution: Optional[
                Literal[
                    "contact_xpay",
                    "provide_information",
                    "remove_restriction",
                ]
            ]
            """
            Represents what the user should do, if anything, to activate the Feature.
            """
            restriction: Optional[Literal["inbound_flows", "outbound_flows"]]
            """
            The `platform_restrictions` that are restricting this Feature.
            """

        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """
        status: Literal["active", "pending", "restricted"]
        """
        Whether the Feature is operational.
        """
        status_details: List[StatusDetail]
        """
        Additional details; includes at least one entry when the status is not `active`.
        """
        _inner_class_types = {"status_details": StatusDetail}

    class FinancialAddresses(XPayObject):
        class Aba(XPayObject):
            class StatusDetail(XPayObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                """
                Represents the reason why the status is `pending` or `restricted`.
                """
                resolution: Optional[
                    Literal[
                        "contact_xpay",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                """
                Represents what the user should do, if anything, to activate the Feature.
                """
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]
                """
                The `platform_restrictions` that are restricting this Feature.
                """

            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """
            status: Literal["active", "pending", "restricted"]
            """
            Whether the Feature is operational.
            """
            status_details: List[StatusDetail]
            """
            Additional details; includes at least one entry when the status is not `active`.
            """
            _inner_class_types = {"status_details": StatusDetail}

        aba: Optional[Aba]
        """
        Toggle settings for enabling/disabling the ABA address feature
        """
        _inner_class_types = {"aba": Aba}

    class InboundTransfers(XPayObject):
        class Ach(XPayObject):
            class StatusDetail(XPayObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                """
                Represents the reason why the status is `pending` or `restricted`.
                """
                resolution: Optional[
                    Literal[
                        "contact_xpay",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                """
                Represents what the user should do, if anything, to activate the Feature.
                """
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]
                """
                The `platform_restrictions` that are restricting this Feature.
                """

            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """
            status: Literal["active", "pending", "restricted"]
            """
            Whether the Feature is operational.
            """
            status_details: List[StatusDetail]
            """
            Additional details; includes at least one entry when the status is not `active`.
            """
            _inner_class_types = {"status_details": StatusDetail}

        ach: Optional[Ach]
        """
        Toggle settings for enabling/disabling an ACH specific feature
        """
        _inner_class_types = {"ach": Ach}

    class IntraXPayFlows(XPayObject):
        class StatusDetail(XPayObject):
            code: Literal[
                "activating",
                "capability_not_requested",
                "financial_account_closed",
                "rejected_other",
                "rejected_unsupported_business",
                "requirements_past_due",
                "requirements_pending_verification",
                "restricted_by_platform",
                "restricted_other",
            ]
            """
            Represents the reason why the status is `pending` or `restricted`.
            """
            resolution: Optional[
                Literal[
                    "contact_xpay",
                    "provide_information",
                    "remove_restriction",
                ]
            ]
            """
            Represents what the user should do, if anything, to activate the Feature.
            """
            restriction: Optional[Literal["inbound_flows", "outbound_flows"]]
            """
            The `platform_restrictions` that are restricting this Feature.
            """

        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """
        status: Literal["active", "pending", "restricted"]
        """
        Whether the Feature is operational.
        """
        status_details: List[StatusDetail]
        """
        Additional details; includes at least one entry when the status is not `active`.
        """
        _inner_class_types = {"status_details": StatusDetail}

    class OutboundPayments(XPayObject):
        class Ach(XPayObject):
            class StatusDetail(XPayObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                """
                Represents the reason why the status is `pending` or `restricted`.
                """
                resolution: Optional[
                    Literal[
                        "contact_xpay",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                """
                Represents what the user should do, if anything, to activate the Feature.
                """
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]
                """
                The `platform_restrictions` that are restricting this Feature.
                """

            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """
            status: Literal["active", "pending", "restricted"]
            """
            Whether the Feature is operational.
            """
            status_details: List[StatusDetail]
            """
            Additional details; includes at least one entry when the status is not `active`.
            """
            _inner_class_types = {"status_details": StatusDetail}

        class UsDomesticWire(XPayObject):
            class StatusDetail(XPayObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                """
                Represents the reason why the status is `pending` or `restricted`.
                """
                resolution: Optional[
                    Literal[
                        "contact_xpay",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                """
                Represents what the user should do, if anything, to activate the Feature.
                """
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]
                """
                The `platform_restrictions` that are restricting this Feature.
                """

            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """
            status: Literal["active", "pending", "restricted"]
            """
            Whether the Feature is operational.
            """
            status_details: List[StatusDetail]
            """
            Additional details; includes at least one entry when the status is not `active`.
            """
            _inner_class_types = {"status_details": StatusDetail}

        ach: Optional[Ach]
        """
        Toggle settings for enabling/disabling an ACH specific feature
        """
        us_domestic_wire: Optional[UsDomesticWire]
        """
        Toggle settings for enabling/disabling a feature
        """
        _inner_class_types = {"ach": Ach, "us_domestic_wire": UsDomesticWire}

    class OutboundTransfers(XPayObject):
        class Ach(XPayObject):
            class StatusDetail(XPayObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                """
                Represents the reason why the status is `pending` or `restricted`.
                """
                resolution: Optional[
                    Literal[
                        "contact_xpay",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                """
                Represents what the user should do, if anything, to activate the Feature.
                """
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]
                """
                The `platform_restrictions` that are restricting this Feature.
                """

            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """
            status: Literal["active", "pending", "restricted"]
            """
            Whether the Feature is operational.
            """
            status_details: List[StatusDetail]
            """
            Additional details; includes at least one entry when the status is not `active`.
            """
            _inner_class_types = {"status_details": StatusDetail}

        class UsDomesticWire(XPayObject):
            class StatusDetail(XPayObject):
                code: Literal[
                    "activating",
                    "capability_not_requested",
                    "financial_account_closed",
                    "rejected_other",
                    "rejected_unsupported_business",
                    "requirements_past_due",
                    "requirements_pending_verification",
                    "restricted_by_platform",
                    "restricted_other",
                ]
                """
                Represents the reason why the status is `pending` or `restricted`.
                """
                resolution: Optional[
                    Literal[
                        "contact_xpay",
                        "provide_information",
                        "remove_restriction",
                    ]
                ]
                """
                Represents what the user should do, if anything, to activate the Feature.
                """
                restriction: Optional[
                    Literal["inbound_flows", "outbound_flows"]
                ]
                """
                The `platform_restrictions` that are restricting this Feature.
                """

            requested: bool
            """
            Whether the FinancialAccount should have the Feature.
            """
            status: Literal["active", "pending", "restricted"]
            """
            Whether the Feature is operational.
            """
            status_details: List[StatusDetail]
            """
            Additional details; includes at least one entry when the status is not `active`.
            """
            _inner_class_types = {"status_details": StatusDetail}

        ach: Optional[Ach]
        """
        Toggle settings for enabling/disabling an ACH specific feature
        """
        us_domestic_wire: Optional[UsDomesticWire]
        """
        Toggle settings for enabling/disabling a feature
        """
        _inner_class_types = {"ach": Ach, "us_domestic_wire": UsDomesticWire}

    card_issuing: Optional[CardIssuing]
    """
    Toggle settings for enabling/disabling a feature
    """
    deposit_insurance: Optional[DepositInsurance]
    """
    Toggle settings for enabling/disabling a feature
    """
    financial_addresses: Optional[FinancialAddresses]
    """
    Settings related to Financial Addresses features on a Financial Account
    """
    inbound_transfers: Optional[InboundTransfers]
    """
    InboundTransfers contains inbound transfers features for a FinancialAccount.
    """
    intra_xpay_flows: Optional[IntraXPayFlows]
    """
    Toggle settings for enabling/disabling a feature
    """
    object: Literal["treasury.financial_account_features"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    outbound_payments: Optional[OutboundPayments]
    """
    Settings related to Outbound Payments features on a Financial Account
    """
    outbound_transfers: Optional[OutboundTransfers]
    """
    OutboundTransfers contains outbound transfers features for a FinancialAccount.
    """

    _inner_class_types = {
        "card_issuing": CardIssuing,
        "deposit_insurance": DepositInsurance,
        "financial_addresses": FinancialAddresses,
        "inbound_transfers": InboundTransfers,
        "intra_xpay_flows": IntraXPayFlows,
        "outbound_payments": OutboundPayments,
        "outbound_transfers": OutboundTransfers,
    }
