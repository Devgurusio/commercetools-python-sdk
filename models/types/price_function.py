from .basetype import BaseType


class PriceFunction(BaseType):
    currencyCode: str
    function: str

    def __init__(self, currencyCode: str = None, function: str = None):
        self.currencyCode = currencyCode
        self.function = function
