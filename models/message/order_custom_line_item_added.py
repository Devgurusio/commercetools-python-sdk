from .message import Message
from models.types.custom_line_item import CustomLineItem


class OrderCustomLineItemAdded(Message):
    type: 'OrderCustomLineItemAdded'
    customLineItem: CustomLineItem

    def __init__(self, type: str = 'OrderCustomLineItemAdded', customLineItem: CustomLineItem = None, **kwargs):
        super().__init__(**kwargs)
        if customLineItem is not None:
            if isinstance(customLineItem, dict):
                self.customLineItem = CustomLineItem(**customLineItem)
            else:
                self.customLineItem = customLineItem
