from .message import Message


class OrderCustomLineItemQuantityChanged(Message):
    type: 'OrderCustomLineItemQuantityChanged'
    customLineItemId: str
    quantity: int
    oldQuantity: int

    def __init__(self, type: str = 'OrderCustomLineItemQuantityChanged', customLineItemId: str = None, quantity: int = None, oldQuantity: int = None, **kwargs):
        super().__init__(**kwargs)
        self.customLineItemId = customLineItemId
        self.quantity = quantity
        self.oldQuantity = oldQuantity
