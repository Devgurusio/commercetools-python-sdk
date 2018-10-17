from .basetype import BaseType
from .reference import Reference
from typing import List


class PaymentInfo(BaseType):
    payments: List[Reference]

    def __init__(self, payments: List[Reference] = None):
        self.quantity = quantity
        if payments is not None:
            _payments = []
            for payment in payments:
                if isinstance(payment, dict):
                    _payments.append(Reference(**payment))
                else:
                    _payments.append(payment)
            self.payments = _payments
        else:
            self.payments = payments
