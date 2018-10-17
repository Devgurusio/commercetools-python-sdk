from .basetype import BaseType
from .money import Money
from .reference import Reference
from .discounted_price import DiscountedPrice
from .custom_fields import CustomFields
from datetime import datetime


class ScopedPrice(BaseType):
    id: str
    value: Money
    currentValue: Money
    country: str
    customerGroup: Reference
    channel: Reference
    validFrom: datetime
    validUntil: datetime
    discounted: DiscountedPrice
    custom: CustomFields

    def __init__(self, id: str = None, value: Money = None, currentValue: Money = None, country: str = None, customerGroup: Reference = None, channel: Reference = None, validFrom: datetime = None, validUntil: datetime = None, discounted: DiscountedPrice = None, custom: CustomFields = None):
        self.id = id
        if value is not None:
            if isinstance(value, dict):
                self.value = Money(**value)
            else:
                self.value = value
        if currentValue is not None:
            if isinstance(currentValue, dict):
                self.currentValue = Money(**currentValue)
            else:
                self.currentValue = currentValue
        self.country = country
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
