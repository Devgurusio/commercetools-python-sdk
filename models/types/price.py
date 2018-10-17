from .basetype import BaseType
from .money import Money
from .reference import Reference
from .price_tier import PriceTier
from .discounted_price import DiscountedPrice
from .custom_fields import CustomFields
from datetime import datetime
from typing import List


class Price(BaseType):
    id: str
    value: Money
    country: str
    customerGroup: Reference
    channel: Reference
    validFrom: datetime
    validUntil: datetime
    tiers: List[PriceTier]
    discounted: DiscountedPrice
    custom: CustomFields

    def __init__(self, value: Money = None, discount: Reference = None):
        self.id = id
        if value is not None:
            if isinstance(value, dict):
                self.value = Money(**value)
            else:
                self.value = value
        self.country = cuntry
        if customerGroup is not None:
            if isinstance(customerGroup, dict):
                self.customerGroup = Reference(**customerGroup)
            else:
                self.customerGroup = customerGroup
        if channel is not None:
            if isinstance(channel, dict):
                self.channel = Reference(**channel)
            else:
                self.channel = channel
        self.validFrom = validFrom
        self.validUntil = validUntil
        if tiers is not None:
            _tiers = []
            for tier in tiers:
                if isinstance(tier, dict):
                    _tiers.append(PriceTier(**tier))
                else:
                    _tiers.append(tier)
            self.tiers = _tiers
        else:
            self.tiers = tiers
        if discounted is not None:
            if isinstance(discounted, dict):
                self.discounted = DiscountedPrice(**discounted)
            else:
                self.discounted = discounted
        if custom is not None:
            if isinstance(custom, dict):
                self.custom = CustomFields(**custom)
            else:
                self.custom = custom
