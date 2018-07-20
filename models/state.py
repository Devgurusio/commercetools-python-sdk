from .basemodel import BaseModel
from .types.reference import Reference
from typing import List
from decorators.decorators import ValidValues


class State(BaseModel):
    key: str
    _type: str
    name: dict
    description: dict
    initial: bool
    builtIn: bool
    roles: List[str]
    transitions: Reference

    _state_types = ['OrderState', 'LineItemState',
                    'ProductState', 'ReviewState', 'PaymentState']
    _state_roles = ['ReviewIncludedInStatistics', 'Return']

    def __init__(self, key: str = None, type: str = None, name: dict = None, description: dict = None, initial: bool = None, builtIn: bool = None, roles: List[str] = None, transitions: Reference = None, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.type = type
        self.name = name
        self.description = description
        self.initial = initial
        self.builtIn = builtIn
        self.roles = roles
        if transitions is not None:
            _transitions = []
            for transition in transitions:
                if isinstance(transition, dict):
                    _transitions.append(Reference(**transition))
                else:
                    _transitions.append(transition)
            self.transitions = _transitions
        else:
            self.transitions = transitions

    @property
    def type(self):
        return self._type

    @type.setter
    @ValidValues(_state_types)
    def type(self, value):
        self._type = value

    def toDict(self):
        d = super().toDict()
        if self._type is not None:
            d['type'] = self._type
        return d
