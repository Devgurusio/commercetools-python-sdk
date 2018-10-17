from .basetype import BaseType


class ItemShippingTarget(BaseType):
    addressKey: str
    quantity: int

    def __init__(self, addressKey: str = None, quantity: int = None):
        self.addressKey = addressKey
        self.quantity = quantity
