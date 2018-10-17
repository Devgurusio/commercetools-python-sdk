from .basetype import BaseType
from datetime import datetime
from .money import Money
from decorators.decorators import ValidValues


class Transaction(BaseType):
    id: str
    timestamp: datetime
    _type: str
    amount: Money
    interactionId: str
    _state: str

    _transactionType_types = [
        'Authorization', 'CancelAuthorization', 'Charge', 'Refund', 'Chargeback']
    _transactionState_types = ['Initial', 'Pending', 'Success', 'Failure']

    def __init__(self, id: str = None, timestamp: datetime = None, type: str = None, amount: Money = None, interactionId: str = None, state: str = None):
        self.id = id
        self.timestamp = timestamp
        self.type = type
        if amount is not None:
            if isinstance(amount, dict):
                self.amount = Money(**amount)
            else:
                self.amount = amount
        self.interactionId = interactionId
        self.state = state

    @property
    def type(self):
        return self._type

    @type.setter
    @ValidValues(_transactionType_types)
    def type(self, value):
        self._type = value

    @property
    def state(self):
        return self._state

    @state.setter
    @ValidValues(_transactionState_types)
    def state(self, value):
        self._state = value

    def toDict(self):
        d = super().toDict()
        if self._type is not None:
            d['type'] = self._type
        if self._state is not None:
            d['state'] = self._state
        return d
