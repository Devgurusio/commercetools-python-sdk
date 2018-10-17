from .basetype import BaseType
from .money import Money
from .reference import Reference


class DiscountedPrice(BaseType):
    value: Money
    discount: Reference

    def __init__(self, value: Money = None, discount: Reference = None):
        if value is not None:
            if isinstance(value, dict):
                self.value = Money(**value)
            else:
                self.value = value
        if discount is not None:
            if isinstance(discount, dict):
                self.discount = Reference(**discount)
            else:
                self.discount = discount
