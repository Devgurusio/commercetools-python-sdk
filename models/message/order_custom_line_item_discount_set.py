from .message import Message
from models.types.discounted_line_item_price_for_quantity import DiscountedLineItemPriceForQuantity
from models.types.taxed_item_price import TaxedItemPrice
from typing import List


class OrderCustomLineItemDiscountSet(Message):
    type: 'OrderCustomLineItemDiscountSet'
    customLineItemId: str
    discountedPricePerQuantity: List[DiscountedLineItemPriceForQuantity]
    taxedPrice: TaxedItemPrice

    def __init__(self, type: str = 'OrderCustomLineItemDiscountSet', customLineItemId: str = None, discountedPricePerQuantity: List[DiscountedLineItemPriceForQuantity] = None, taxedPrice: TaxedItemPrice = None, **kwargs):
        super().__init__(**kwargs)
        self.customLineItemId = customLineItemId
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
        if taxedPrice is not None:
            if isinstance(taxedPrice, dict):
                self.taxedPrice = TaxedItemPrice(**taxedPrice)
            else:
                self.taxedPrice = taxedPrice
