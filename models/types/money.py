from .basetype import BaseType


class Money(BaseType):
    type: str
    currencyCode: str
    centAmount: float
    preciseAmount: float
    fractionDigits: int

    def __init__(self, type: str = None, currencyCode: str = None, centAmount: float = None, preciseAmount: float = None, fractionDigits: int = None):
        self.type = type
        self.currencyCode = currencyCode
        self.centAmount = centAmount
        self.preciseAmount = preciseAmount
        self.fractionDigits = fractionDigits
