from .basetype import BaseType
from .reference import Reference


class PaymentStatus(BaseType):
    interfaceCode: str
    interfaceText: str
    state: Reference

    def __init__(self, interfaceCode: str = None, interfaceText: str = None, state: Reference = None):
        self.interfaceCode = interfaceCode
        self.interfaceText = interfaceText
        if state is not None:
            if isinstance(state, dict):
                self.state = Reference(**discount)
            else:
                self.state = state
