from .message import Message
from models.types.shipping_rate_input import ShippingRateInput


class OrderShippingRateInputSet(Message):
    type: 'OrderShippingRateInputSet'
    shippingRateInput: ShippingRateInput
    oldShippingRateInput: ShippingRateInput

    def __init__(self, type: str = 'OrderShippingRateInputSet', shippingRateInput: ShippingRateInput = None, oldShippingRateInput: ShippingRateInput = None, **kwargs):
        super().__init__(**kwargs)
        if shippingRateInput is not None:
            if isinstance(shippingInfo, dict):
                self.shippingRateInput = ShippingRateInput(**shippingRateInput)
            else:
                self.shippingRateInput = shippingRateInput
        if oldShippingRateInput is not None:
            if isinstance(oldShippingRateInput, dict):
                self.oldShippingRateInput = ShippingRateInput(**oldShippingRateInput)
            else:
                self.oldShippingRateInput = oldShippingRateInput
