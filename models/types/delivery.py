from .basetype import BaseType
from datetime import datetime
from typing import List
from .delivery_item import DeliveryItem
from .parcel import Parcel
from .address import Address


class Delivery(BaseType):
    id: str
    createdAt: datetime
    items: List[DeliveryItem]
    parcels: List[Parcel]
    address: Address

    def __init__(self, id: str = None, createdAt: datetime = None, items: List[DeliveryItem] = None, parcels: List[Parcel] = None, address: Address = None):
        self.id = id
        self.createdAt = createdAt
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
        if parcels is not None:
            _parcels = []
            for parcel in parcels:
                if isinstance(parcel, dict):
                    _parcels.append(Parcel(**parcel))
                else:
                    _parcels.append(parcel)
            self.parcels = _parcels
        else:
            self.parcels = parcels
        if address is not None:
            if isinstance(address, dict):
                self.address = Address(**address)
            else:
                self.address = address

    def toDict(self):
        if self.parcels is not None and self.parcels.__len__() > 0:
            d = super().toDict()
            d['parcels'] = [parcel.toDict() for parcel in d['parcels']]
            return d
        else:
            return super().toDict()
