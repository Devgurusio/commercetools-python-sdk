from .basetype import BaseType
from datetime import datetime
from .parcel_measurements import ParcelMeasurements
from .tracking_data import TrackingData
from .delivery_item import DeliveryItem
from typing import List


class Parcel(BaseType):
    id: str
    createdAt: datetime
    measurements: ParcelMeasurements
    trackingData: TrackingData
    items: List[DeliveryItem]

    def __init__(self, id: str = None, createdAt: datetime = None, measurements: ParcelMeasurements = None, trackingData: TrackingData = None, items: List[DeliveryItem] = None):
        self.id = id
        self.createdAt = createdAt
        if measurements is not None:
            if isinstance(measurements, dict):
                self.measurements = ParcelMeasurements(**measurements)
            else:
                self.measurements = measurements
        if trackingData is not None:
            if isinstance(trackingData, dict):
                self.trackingData = TrackingData(**trackingData)
            else:
                self.trackingData = trackingData
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
