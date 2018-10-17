from .message import Message
from models.types.line_item import LineItem


class OrderLineItemAdded(Message):
    type: 'OrderLineItemAdded'
    lineItem: LineItem
    addedQuantity: int

    def __init__(self, type: str = 'OrderLineItemAdded', lineItem: LineItem = None, addedQuantity: int = None, **kwargs):
        super().__init__(**kwargs)
        if lineItem is not None:
            if isinstance(lineItem, dict):
                self.lineItem = LineItem(**lineItem)
            else:
                self.lineItem = lineItem
        self.addedQuantity = addedQuantity
