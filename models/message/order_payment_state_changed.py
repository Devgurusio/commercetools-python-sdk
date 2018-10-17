from .message import Message
from decorators.decorators import ValidValues


class OrderPaymentStateChanged(Message):
    type: 'OrderPaymentStateChanged'
    id: str
    _paymentState: str
    _oldPaymentState: str

    _paymentState_types = ['BalanceDue',
                           'Failed', 'Pending', 'CreditOwed', 'Paid']

    def __init__(self, type: str = 'OrderPaymentStateChanged', id: str = None, paymentState: str = None, oldPaymentState: str = None, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.paymentState = paymentState
        self.oldPaymentState = oldPaymentState

    @property
    def paymentState(self):
        return self._paymentState

    @paymentState.setter
    @ValidValues(_paymentState_types)
    def paymentState(self, value):
        self._paymentState = value

    @property
    def oldPaymentState(self):
        return self._oldPaymentState

    @oldPaymentState.setter
    @ValidValues(_paymentState_types)
    def oldPaymentState(self, value):
        self._oldPaymentState = value

    def toDict(self):
        d = super().toDict()
        if self._paymentState is not None:
            d['paymentState'] = self._paymentState
        if self._oldPaymentState is not None:
            d['oldPaymentState'] = self._oldPaymentState
        return d
