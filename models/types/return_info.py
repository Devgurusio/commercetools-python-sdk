from .basetype import BaseType
from .return_item import ReturnItem
from datetime import datetime
from typing import List


class ReturnInfo(BaseType):
    items: List[ReturnItem]
    returnTrackingId: str
    returnDate: datetime

    def __init__(self, items: List[ReturnItem] = None, returnTrackingId: str = None, returnDate: datetime = None):
        if items is not None:
            _items = []
            for item in items:
                if isinstance(item, dict):
                    _items.append(ReturnItem(**item))
                else:
                    _items.append(item)
            self.items = _items
        else:
            self.items = items
        self.returnTrackingId = returnTrackingId
        self.returnDate = returnDate
