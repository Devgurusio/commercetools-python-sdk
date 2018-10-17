from .message import Message
from decorators.decorators import ValidValues


class OrderShipmentStateChanged(Message):
    type: 'OrderShipmentStateChanged'
    _shipmentState: str
    _oldPaymentState: str

    _shipmentState_types = ['Shipped',
                            'Ready', 'Pending', 'Delayed', 'Partial', 'Backorder']

    def __init__(self, type: str = 'OrderShipmentStateChanged', shipmentState: str = None, oldPaymentState: str = None, **kwargs):
        super().__init__(**kwargs)
        self.shipmentState = shipmentState
        self.oldPaymentState = oldPaymentState

    @property
    def shipmentState(self):
        return self._shipmentState

    @shipmentState.setter
    @ValidValues(_shipmentState_types)
    def shipmentState(self, value):
        self._shipmentState = value

    @property
    def oldPaymentState(self):
        return self._oldPaymentState

    @oldPaymentState.setter
    @ValidValues(_shipmentState_types)
    def oldPaymentState(self, value):
        self._oldPaymentState = value

    def toDict(self):
        d = super().toDict()
        if self._shipmentState is not None:
            d['shipmentState'] = self._shipmentState
        if self._oldPaymentState is not None:
            d['oldPaymentState'] = self._oldPaymentState
        return d
