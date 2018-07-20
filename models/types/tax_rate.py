from .basetype import BaseType
from .sub_rate import SubRate
from typing import List


class TaxRate(BaseType):
    id: str
    name: str
    amount: float
    includedInPrice: bool
    country: str
    state: str
    subRates: List[SubRate]

    def __init__(self, id: str = None, name: str = None, amount: float = None, includedInPrice: bool = None, country: str = None, state: str = None, subRates: List[SubRate] = None):
        self.id = id
        self.name = name
        self.amount = amount
        self.includedInPrice = includedInPrice
        self.country = country
        self.state = state
        if subRates is not None:
            _sub_rates = []
            for sub_rate in subRates:
                if isinstance(sub_rate, dict):
                    _sub_rates.append(SubRate(**sub_rate))
                else:
                    _sub_rates.append(sub_rate)
            self.subRates = _sub_rates
        else:
            self.subRates = subRates

    def toDict(self):
        if self.subRates is not None and self.subRates.__len__() > 0:
            d = super().toDict()
            d['subRates'] = [subRate.toDict() for subRate in d['subRates']]
            return d
        else:
            return super().toDict()
