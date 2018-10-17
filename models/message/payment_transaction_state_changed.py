from .message import Message
from decorators.decorators import ValidValues


class PaymentTransactionStateChanged(Message):
    type: 'PaymentTransactionStateChanged'
    transactionId: str
    _state: str

    def __init__(self, type: str = 'PaymentTransactionStateChanged', transactionId: str = None, state: str = None, **kwargs):
        super().__init__(**kwargs)
        self.transactionId = transactionId
        self.state = state

    @property
    def state(self):
        return self._state

    @state.setter
    @ValidValues(Transaction._transactionState_types)
    def state(self, value):
        self._state = value

    def toDict(self):
        d = super().toDict()
        if self._state is not None:
            d['state'] = self._state
        return d
