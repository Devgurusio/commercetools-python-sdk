from .basetype import BaseType
from .money import Money
from .discounted_line_item_portion import DiscountedLineItemPortion
from typing import List


class DiscountedLineItemPrice(BaseType):
    value: Money
    includedDiscounts: List[DiscountedLineItemPortion]

    def __init__(self, value: Money = None, includedDiscounts: List[DiscountedLineItemPortion] = None):
        if value is not None:
            if isinstance(value, dict):
                self.value = Money(**value)
            else:
                self.value = value
        if includedDiscounts is not None:
            _includedDiscounts = []
            for includedDiscount in includedDiscounts:
                if isinstance(includedDiscount, dict):
                    _includedDiscounts.append(
                        DiscountedLineItemPortion(**includedDiscount))
                else:
                    _includedDiscounts.append(includedDiscount)
            self.includedDiscounts = _includedDiscounts
        else:
            self.includedDiscounts = includedDiscounts
