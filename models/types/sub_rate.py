from .basetype import BaseType


class SubRate(BaseType):
    name: str
    amount: float

    def __init__(self, name: str = None, amount: float = None):
        self.name = name
        self.amount = amount
