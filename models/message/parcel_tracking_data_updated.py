from .message import Message
from models.types.tracking_data import TrackingData


class ParcelTrackingDataUpdated(Message):
    type: 'ParcelTrackingDataUpdated'
    deliveryId: str
    parcelId: str
    trackingData: TrackingData

    def __init__(self, type: str = 'ParcelTrackingDataUpdated', deliveryId: str = None, parcelId: str = None, trackingData: TrackingData = None, **kwargs):
        super().__init__(**kwargs)
        self.deliveryId = deliveryId
        self.parcelId = parcelId
        if trackingData is not None:
            if isinstance(trackingData, dict):
                self.trackingData = TrackingData(**trackingData)
            else:
                self.trackingData = trackingData
