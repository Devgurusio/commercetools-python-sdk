from .basetype import BaseType
from .money import Money
from .price_function import PriceFunction
from decorators.decorators import ValidValues


class ShippingRatePriceTier(BaseType):
    _type: str
    isMatching: bool
    price: Money  # For every type except CartScore with function
    minimumCentAmount: float  # For CartValue type
    value: str  # For CartClassification type. Must be a valid key of the CartClassification
    score: float  # For CartScore
    priceFunction: PriceFunction

    _types = ['CartValue', 'CartClassification', 'CartScore']

    def __init__(self, type: str = None, freeAbove: Money = None, isMatching: bool = None):
        self.type = type

        if isinstance(price, dict):
            self.price = Money(**price)
        else:
            self.price = price
        if isinstance(freeAbove, dict):
            self.freeAbove = Money(**freeAbove)
        else:
            self.freeAbove = freeAbove
        self.isMatching = isMatching

    @property
    def type(self):
        return self._type

    @type.setter
    @ValidValues(_types)
    def type(self, value):
        self._type = value

    def toDict(self):
        d = super().toDict()
        if self._type is not None:
            d['type'] = self._type
        return d
