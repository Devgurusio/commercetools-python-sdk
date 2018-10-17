from .basetype import BaseType
from datetime import datetime
from decorators.decorators import ValidValues


class ReturnItem(BaseType):
    id: str
    quantity: int
    comment: str
    _shipmentState: str
    _paymentState: str
    lastModifiedAt: datetime
    createdAt: datetime

    _returnShipmentState = ['Advised', 'Returned', 'BackInStock', 'Unusable']
    _returnPaymentState = ['NonRefundable', 'Initial', 'Refunded', 'NotRefunded']

    def __init__(self, id: str = None, quantity: int = None, comment: str = None, shipmentState: str = None, paymentState: str = None, lastModifiedAt: datetime = None, createdAt: datetime = None):
        self.id = id
        self.quantity = quantity
        self.shipmentState = shipmentState
        self.paymentState = paymentState
        self.lastModifiedAt = lastModifiedAt
        self.createdAt = createdAt

    @property
    def shipmentState(self):
        return self._shipmentState

    @shipmentState.setter
    @ValidValues(_returnShipmentState)
    def shipmentState(self, value):
        self._shipmentState = value

    @property
    def paymentState(self):
        return self._paymentState

    @paymentState.setter
    @ValidValues(_returnPaymentState)
    def paymentState(self, value):
        self._paymentState = value

    def toDict(self):
        d = super().toDict()
        if self._shipmentState is not None:
            d['shipmentState'] = self._shipmentState
        if self._paymentState is not None:
            d['paymentState'] = self._paymentState
        return d
