from .basetype import BaseType
from .reference import Reference


class ItemState(BaseType):
    quantity: int
    state: Reference

    def __init__(self, quantity: int = None, zone: Reference = None):
        self.quantity = quantity
        if state is not None:
            if isinstance(state, dict):
                self.state = Reference(**state)
            else:
                self.state = state
