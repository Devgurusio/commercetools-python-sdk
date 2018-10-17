from .message import Message
from models.types.delivery_item import DeliveryItem
from typing import List


class ParcelItemsUpdated(Message):
    type: 'ParcelItemsUpdated'
    deliveryId: str
    parcelId: str
    items: List[DeliveryItem]
    oldItems: List[DeliveryItem]

    def __init__(self, type: str = 'ParcelItemsUpdated', deliveryId: str = None, parcelId: str = None, items: List[DeliveryItem] = None, oldItems: List[DeliveryItem] = None, **kwargs):
        super().__init__(**kwargs)
        self.deliveryId = deliveryId
        self.parcelId = parcelId
        if items is not None:
            _items = []
            for item in items:
                if isinstance(item, dict):
                    _items.append(DeliveryItem(**item))
                else:
                    _items.append(item)
            self.items = _items
        else:
            self.items = items
        if oldItems is not None:
            _oldItems = []
            for oldItem in oldItems:
                if isinstance(oldItem, dict):
                    oldItems.append(DeliveryItem(**oldItem))
                else:
                    oldItems.append(oldItem)
            self.oldItems = oldItems
        else:
            self.oldItems = oldItems
