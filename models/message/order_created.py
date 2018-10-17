from .message import Message
from models.order import Order


class OrderCreated(Message):
    type: 'OrderCreated'
    order: Order

    def __init__(self, type: str = 'OrderCreated', order: Order = None, **kwargs):
        super().__init__(**kwargs)
        if order is not None:
            if isinstance(order, dict):
                self.order = Order(**order)
            else:
                self.order = order
