from .message import Message
from models.types.parcel import Parcel


class ParcelRemovedFromDelivery(Message):
    type: 'ParcelRemovedFromDelivery'
    deliveryId: str
    parcel: Parcel

    def __init__(self, type: str = 'ParcelRemovedFromDelivery', deliveryId: str = None, parcel: Parcel = None, **kwargs):
        super().__init__(**kwargs)
        self.deliveryId = deliveryId
        if parcel is not None:
            if isinstance(parcel, dict):
                self.parcel = Parcel(**parcel)
            else:
                self.parcel = parcel
