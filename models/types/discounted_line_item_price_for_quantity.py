from .basetype import BaseType
from .discounted_line_item_price import DiscountedLineItemPrice


class DiscountedLineItemPriceForQuantity(BaseType):
    quantity: int
    discountedPrice: DiscountedLineItemPrice

    def __init__(self, quantity: int = None, discountedPrice: DiscountedLineItemPrice = None):
        self.quantity = quantity
        if discountedPrice is not None:
            if isinstance(discountedPrice, dict):
                self.discountedPrice = DiscountedLineItemPrice(**discountedPrice)
            else:
                self.discountedPrice = discountedPrice
