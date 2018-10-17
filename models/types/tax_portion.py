from .basetype import BaseType
from .money import Money


class TaxPortion(BaseType):
    name: str
    rate: float
    amount: Money

    def __init__(self, name: str = None, rate: float = None, amount: Money = None):
        self.name = name
        self.rate = rate
        if amount is not None:
            if isinstance(amount, dict):
                self.amount = Money(**amount)
            else:
                self.amount = amount
