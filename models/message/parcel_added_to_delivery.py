from .message import Message
from models.types.delivery import Delivery
from models.types.parcel import Parcel


class ParcelAddedToDelivery(Message):
    type: 'ParcelAddedToDelivery'
    delivery: Delivery
    parcel: Parcel

    def __init__(self, type: str = 'ParcelAddedToDelivery', delivery: Delivery = None, parcel: Parcel = None, **kwargs):
        super().__init__(**kwargs)
        if delivery is not None:
            if isinstance(delivery, dict):
                self.delivery = Delivery(**delivery)
            else:
                self.delivery = delivery
        if parcel is not None:
            if isinstance(parcel, dict):
                self.parcel = Parcel(**parcel)
            else:
                self.parcel = parcel
