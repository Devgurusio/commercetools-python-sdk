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

    _shippingRatePriceTier_types = [
        'CartValue', 'CartClassification', 'CartScore']

    def __init__(self, type: str = None, isMatching: bool = None, price: Money = None, minimumCentAmount: float = None, value: str = None, score: float = None, priceFunction: PriceFunction = None):
        self.type = type
        self.isMatching = isMatching
        if isinstance(price, dict):
            self.price = Money(**price)
        else:
            self.price = price
        self.minimumCentAmount = minimumCentAmount
        self.value = value
        self.score = score
        if isinstance(priceFunction, dict):
            self.priceFunction = PriceFunction(**priceFunction)
        else:
            self.priceFunction = priceFunction

    @property
    def type(self):
        return self._type

    @type.setter
    @ValidValues(_shippingRatePriceTier_types)
    def type(self, value):
        self._type = value

    def toDict(self):
        d = super().toDict()
        if self._type is not None:
            d['type'] = self._type
        return d
