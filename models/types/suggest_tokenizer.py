from .basetype import BaseType
from typing import List
from decorators.decorators import ValidValues


class SuggestTokenizer(BaseType):
    _type: str
    inputs: List[str]

    _tokenizer_types = ['whitespace', 'custom']

    def __init__(self, type: str = None, inputs: List[str] = None):
        self.type = type
        self.inputs = inputs

    @property
    def type(self):
        return self._type

    @type.setter
    @ValidValues(_tokenizer_types)
    def type(self, value):
        self._type = value

    def toDict(self):
        d = super().toDict()
        if self._type is not None:
            d['type'] = self._type
        return d
