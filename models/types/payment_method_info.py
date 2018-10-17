from .basetype import BaseType
from .reference import Reference
from typing import Dict


class PaymentMethodInfo(BaseType):
    paymentInterface: str
    method: str
    name: Dict

    def __init__(self, paymentInterface: str = None, method: str = None, name: Dict = None):
        self.paymentInterface = paymentInterface
        self.method = method
        self.name = name
