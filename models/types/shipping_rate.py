from .basetype import BaseType
from .money import Money
from .shipping_rate_price_tier import ShippingRatePriceTier
from typing import List

class ShippingRate(BaseType):
    price: Money
    freeAbove: Money
    tiers: List[ShippingRatePriceTier]
    isMatching: bool

    def __init__(self, price: Money = None, freeAbove: Money = None, tiers: List[ShippingRatePriceTier] = None, isMatching: bool = None):
        if isinstance(price, dict):
            self.price = Money(**price)
        else:
            self.price = price
        if isinstance(freeAbove, dict):
            self.freeAbove = Money(**freeAbove)
        else:
            self.freeAbove = freeAbove
        if tiers is not None:
            _tiers = []
            for tier in tiers:
                if isinstance(tier, dict):
                    _tiers.append(ShippingRatePriceTier(**tier))
                else:
                    _tiers.append(tier)
            self.tiers = _tiers
        else:
            self.tiers = tiers
        self.isMatching = isMatching
