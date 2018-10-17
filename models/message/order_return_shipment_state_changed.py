from .message import Message
from decorators.decorators import ValidValues


class OrderReturnShipmentStateChanged(Message):
    type: 'OrderReturnShipmentStateChanged'
    returnItemId: str
    _returnShipmentState: str

    _returnShipmentState_types = ['Advised',
                                  'Returned', 'BackInStock', 'Unusable']

    def __init__(self, type: str = 'OrderReturnShipmentStateChanged', returnItemId: str = None, returnShipmentState: str = None, **kwargs):
        super().__init__(**kwargs)
        self.returnItemId = returnItemId
        self.returnShipmentState = returnShipmentState

    @property
    def returnShipmentState(self):
        return self._returnShipmentState

    @returnShipmentState.setter
    @ValidValues(_returnShipmentState_types)
    def returnShipmentState(self, value):
        self._returnShipmentState = value

    def toDict(self):
        d = super().toDict()
        if self._returnShipmentState is not None:
            d['returnShipmentState'] = self._returnShipmentState
        return d
