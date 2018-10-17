from .message import Message
from models.types.delivery import Delivery


class DeliveryRemoved(Message):
    type: 'DeliveryRemoved'
    delivery: Delivery

    def __init__(self, type: str = 'DeliveryRemoved', delivery: Delivery = None, **kwargs):
        super().__init__(**kwargs)
        if delivery is not None:
            if isinstance(delivery, dict):
                self.delivery = Delivery(**delivery)
            else:
                self.delivery = delivery
