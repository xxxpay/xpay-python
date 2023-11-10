from xpay.xpay_object import XPayObject


# This resource can only be instantiated when expanded on a BalanceTransaction
class RecipientTransfer(XPayObject):
    OBJECT_NAME = "recipient_transfer"
