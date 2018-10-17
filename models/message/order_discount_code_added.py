from .message import Message
from models.types.reference import Reference


class OrderDiscountCodeAdded(Message):
    type: 'OrderDiscountCodeAdded'
    discountCode: Reference

    def __init__(self, type: str = 'OrderDiscountCodeAdded', discountCode: Reference = None, **kwargs):
        super().__init__(**kwargs)
        if discountCode is not None:
            if isinstance(discountCode, dict):
                self.discountCode = Reference(**discountCode)
            else:
                self.discountCode = discountCode
