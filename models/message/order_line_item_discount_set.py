from .message import Message
from models.types.discounted_line_item_price_for_quantity import DiscountedLineItemPriceForQuantity
from models.types.money import Money
from models.types.taxed_item_price import TaxedItemPrice
from typing import List


class OrderLineItemDiscountSet(Message):
    type: 'OrderLineItemDiscountSet'
    lineItemId: str
    discountedPricePerQuantity: List[DiscountedLineItemPriceForQuantity]
    totalPrice: Money
    taxedPrice: TaxedItemPrice

    def __init__(self, type: str = 'OrderLineItemDiscountSet', lineItemId: str = None, discountedPricePerQuantity: List[DiscountedLineItemPriceForQuantity] = None, totalPrice: Money = None, taxedPrice: TaxedItemPrice = None, **kwargs):
        super().__init__(**kwargs)
        self.lineItemId = lineItemId
        if discountedPricePerQuantity is not None:
            _discountedPricePerQuantity = []
            for discount in discountedPricePerQuantity:
                if isinstance(discount, dict):
                    _discountedPricePerQuantity.append(
                        DiscountedLineItemPriceForQuantity(**discount))
                else:
                    _discountedPricePerQuantity.append(discount)
            self.discountedPricePerQuantity = _discountedPricePerQuantity
        else:
            self.discountedPricePerQuantity = discountedPricePerQuantity
        if totalPrice is not None:
            if isinstance(totalPrice, dict):
                self.totalPrice = Money(**totalPrice)
            else:
                self.totalPrice = totalPrice
        if taxedPrice is not None:
            if isinstance(taxedPrice, dict):
                self.taxedPrice = TaxedItemPrice(**taxedPrice)
            else:
                self.taxedPrice = taxedPrice
