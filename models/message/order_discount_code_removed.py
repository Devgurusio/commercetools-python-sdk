from .message import Message
from models.types.reference import Reference


class OrderDiscountCodeRemoved(Message):
    type: 'OrderDiscountCodeRemoved'
    discountCode: Reference

    def __init__(self, type: str = 'OrderDiscountCodeRemoved', discountCode: Reference = None, **kwargs):
        super().__init__(**kwargs)
        if discountCode is not None:
            if isinstance(discountCode, dict):
                self.discountCode = Reference(**discountCode)
            else:
                self.discountCode = discountCode
