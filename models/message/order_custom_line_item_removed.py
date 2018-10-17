from .message import Message
from models.types.custom_line_item import CustomLineItem


class OrderCustomLineItemRemoved(Message):
    type: 'OrderCustomLineItemRemoved'
    customLineItemId: str
    customLineItem: CustomLineItem

    def __init__(self, type: str = 'OrderCustomLineItemRemoved', customLineItemId: str = None, customLineItem: CustomLineItem = None, **kwargs):
        super().__init__(**kwargs)
        self.customLineItemId = customLineItemId
        if customLineItem is not None:
            if isinstance(customLineItem, dict):
                self.customLineItem = CustomLineItem(**customLineItem)
            else:
                self.customLineItem = customLineItem
