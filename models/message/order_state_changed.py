from .message import Message
from decorators.decorators import ValidValues


class OrderStateChanged(Message):
    type: 'OrderStateChanged'
    _orderState: str
    _oldOrderState: str

    _orderState_types = ['Open', 'Confirmed', 'Complete', 'Cancelled']

    def __init__(self, type: str = 'OrderStateChanged', orderState: str = None, oldOrderState: str = None, **kwargs):
        super().__init__(**kwargs)
        self.orderState = orderState
        self.oldOrderState = oldOrderState

    @property
    def orderState(self):
        return self._orderState

    @orderState.setter
    @ValidValues(_orderState_types)
    def orderState(self, value):
        self._orderState = value

    @property
    def oldOrderState(self):
        return self._oldOrderState

    @oldOrderState.setter
    @ValidValues(_orderState_types)
    def oldOrderState(self, value):
        self._oldOrderState = value

    def toDict(self):
        d = super().toDict()
        if self._orderState is not None:
            d['orderState'] = self._orderState
        if self._oldOrderState is not None:
            d['oldOrderState'] = self._oldOrderState
        return d
