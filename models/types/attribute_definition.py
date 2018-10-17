from .basetype import BaseType
from .attribute_type import AttributeType
from typing import Dict
from decorators.decorators import ValidValues


class AttributeDefinition(BaseType):
    type: AttributeType
    name: str
    label: Dict
    isRequired: bool
    _attributeConstraint: str
    inputTip: Dict
    _inputHint: str
    isSearchable: bool

    _attributeConstraint_types = [
        'None', 'Unique', 'CombinationUnique', 'SameForAll']
    _textInputHint_types = ['SingleLine', 'MultiLine']

    def __init__(self, type: AttributeType = None, name: str = None, label: Dict = None, isRequired: bool = None, attributeConstraint: str = None, inputTip: Dict = None, inputHint: str = None, isSearchable: bool = None):
        if type is not None:
            if isinstance(type, dict):
                self.type = AttributeType(**type)
            else:
                self.type = type
        self.name = name
        self.label = label
        self.isRequired = isRequired
        self.attributeConstraint = attributeConstraint
        self.inputTip = inputTip
        self.inputHint = inputHint
        self.isSearchable = isSearchable

    @property
    def attributeConstraint(self):
        return self._attributeConstraint

    @attributeConstraint.setter
    @ValidValues(_attributeConstraint_types)
    def attributeConstraint(self, value):
        self._attributeConstraint = value

    @property
    def inputHint(self):
        return self._inputHint

    @inputHint.setter
    @ValidValues(_textInputHint_types)
    def inputHint(self, value):
        self._inputHint = value
    
    def toDict(self):
        d = super().toDict()
        if self._attributeConstraint is not None:
            d['attributeConstraint'] = self._attributeConstraint
        if self._inputHint is not None:
            d['inputHint'] = self._inputHint
        return d
