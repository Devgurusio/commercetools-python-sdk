from .basetype import BaseType
from .reference import Reference
from .money import Money


class DiscountedLineItemPortion(BaseType):
    discount: Reference
    discountedAmount: Money

    def __init__(self, discount: Reference = None, discountedAmount: Money = None):
        if discount is not None:
            if isinstance(discount, dict):
                self.discount = Reference(**amount)
            else:
                self.discount = discount
        if discountedAmount is not None:
            if isinstance(discountedAmount, dict):
                self.discountedAmount = Money(**discountedAmount)
            else:
                self.discountedAmount = discountedAmount
