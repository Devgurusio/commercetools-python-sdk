from .basetype import BaseType
from .money import Money

class PriceTier(BaseType):
    minimumQuantity: int
    value: Money


    def __init__(self, minimumQuantity: int = None, value: Money = None):
        self.minimumQuantity = minimumQuantity
        if value is not None:
            if isinstance(value, dict):
                self.value = Money(**value)
            else:
                self.value = value
