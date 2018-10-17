from .basetype import BaseType
from .address import Address
from datetime import datetime


class DeliveryItem(BaseType):
    id: str
    quantity: int

    def __init__(self, id: str = None, quantity: int = None):
        self.id = id
        self.quantity = quantity
