from .basetype import BaseType
from typing import Dict
from decorators.decorators import ValidValues


class ShippingRateInput(BaseType):
    _type: str
    key: str
    label: Dict
    score: float

    _shippingRateInput_types = ['Classification', 'Score']

    def __init__(self, type: str = None, key: str = None, label: Dict = None, score: str = None):
        self.type = type
        self.key = key
        self.label = label
        self.score = score

    @property
    def type(self):
        return self._type

    @type.setter
    @ValidValues(_shippingRateInput_types)
    def type(self, value):
        self._type = value

    def toDict(self):
        d = super().toDict()
        if self._type is not None:
            d['type'] = self._type
        return d