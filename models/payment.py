from .basemodel import BaseModel
from .types.reference import Reference
from .types.money import Money
from .types.payment_method_info import PaymentMethodInfo
from .types.payment_status import PaymentStatus
from .types.transaction import Transaction
from .types.custom_fields import CustomFields
from typing import List


class Payment(BaseModel):
    key: str
    customer: Reference
    anonymousId: str
    interfaceId: str
    amountPlanned: Money
    paymentMethodInfo: PaymentMethodInfo
    paymentStatus: PaymentStatus
    transactions: List[Transaction]
    interfaceInteractions: List[CustomFields]
    custom: CustomFields

    def __init__(self, key: str = None, customer: Reference = None, anonymousId: str = None, interfaceId: str = None, amountPlanned: Money = None, paymentMethodInfo: PaymentMethodInfo = None, paymentStatus: PaymentStatus = None, transactions: List[Transaction] = None, interfaceInteractions: List[CustomFields] = None, custom: CustomFields = None, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        if customer is not None:
            if isinstance(customer, dict):
                self.customer = Reference(**customer)
            else:
                self.customer = customer
        self.anonymousId = anonymousId
        self.interfaceId = interfaceId
        if amountPlanned is not None:
            if isinstance(amountPlanned, dict):
                self.amountPlanned = Money(**amountPlanned)
            else:
                self.amountPlanned = amountPlanned
        if paymentMethodInfo is not None:
            if isinstance(paymentMethodInfo, dict):
                self.paymentMethodInfo = PaymentMethodInfo(**paymentMethodInfo)
            else:
                self.paymentMethodInfo = paymentMethodInfo
        if paymentStatus is not None:
            if isinstance(paymentStatus, dict):
                self.paymentStatus = PaymentStatus(**paymentStatus)
            else:
                self.paymentStatus = paymentStatus
        if transactions is not None:
            _transactions = []
            for transaction in transactions:
                if isinstance(transaction, dict):
                    _transactions.append(Transaction(**transaction))
                else:
                    _transactions.append(transaction)
            self.transactions = _transactions
        else:
            self.transactions = transactions
        if interfaceInteractions is not None:
            _interfaceInteractions = []
            for interfaceInteraction in interfaceInteractions:
                if isinstance(interfaceInteraction, dict):
                    _interfaceInteractions.append(
                        CustomFields(**interfaceInteraction))
                else:
                    _interfaceInteractions.append(interfaceInteraction)
            self.interfaceInteractions = _interfaceInteractions
        else:
            self.interfaceInteractions = interfaceInteractions
        if custom is not None:
            if isinstance(custom, dict):
                self.custom = CustomFields(**custom)
            else:
                self.custom = custom
