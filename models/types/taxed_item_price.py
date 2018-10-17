from .basetype import BaseType
from .money import Money


class TaxedItemPrice(BaseType):
    totalNet: Money
    totalGross: Money

    def __init__(self, totalNet: Money = None, totalGross: Money = None):
        if totalNet is not None:
            if isinstance(totalNet, dict):
                self.totalNet = Money(**totalNet)
            else:
                self.totalNet = totalNet
        if totalGross is not None:
            if isinstance(totalGross, dict):
                self.totalGross = Money(**totalGross)
            else:
                self.totalGross = totalGross
