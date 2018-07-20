from .basetype import BaseType
from typing import Dict
from decorators.decorators import StringMatches, ValidValues
import re


class FieldDefinition(BaseType):
    type: Dict  # More definition could be added
    _name: str
    label: Dict
    required: bool
    _inputHint: str
    _inputHint_types = ['SingleLine', 'MultiLine']

    def __init__(self, type: Dict = None, name: str = None, label: Dict = None, required: bool = None, inputHint: str = None):
        self.type = type
        self.name = name
        self.label = label
        self.required = required
        self.inputHint = inputHint

    @property
    def name(self):
        return self._name

    @name.setter
    @StringMatches(pattern='[-_\\w]+', flags=re.ASCII, min_len=2, max_len=36)
    def name(self, value):
        self._name = value

    @property
    def inputHint(self):
        return self._inputHint

    @inputHint.setter
    @ValidValues(_inputHint_types)
    def inputHint(self, value):
        self._inputHint = value

    def toDict(self):
        d = super().toDict()
        if self._name is not None:
            d['name'] = self._name
        if self._inputHint is not None:
            d['inputHint'] = self._inputHint
        return d
