from .message import Message
from models.types.shipping_info import ShippingInfo


class OrderShippingInfoSet(Message):
    type: 'OrderShippingInfoSet'
    shippingInfo: ShippingInfo
    oldShippingInfo: ShippingInfo

    def __init__(self, type: str = 'OrderShippingInfoSet', shippingInfo: ShippingInfo = None, oldShippingInfo: ShippingInfo = None, **kwargs):
        super().__init__(**kwargs)
        if shippingInfo is not None:
            if isinstance(shippingInfo, dict):
                self.shippingInfo = ShippingInfo(**shippingInfo)
            else:
                self.shippingInfo = shippingInfo
        if oldShippingInfo is not None:
            if isinstance(oldShippingInfo, dict):
                self.oldShippingInfo = ShippingInfo(**oldShippingInfo)
            else:
                self.oldShippingInfo = oldShippingInfo
