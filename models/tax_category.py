from .basemodel import BaseModel
from .types.tax_rate import TaxRate
from typing import List, Dict


class TaxCategory(BaseModel):
    key: str
    name: str
    description: str
    rates: List[TaxRate]

    def __init__(self, key: str = None, name: str = None, description: str = None, rates: List[TaxRate] = None, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.name = name
        self.description = description
        if rates is not None:
            _rates = []
            for rate in rates:
                if isinstance(rate, dict):
                    _rates.append(TaxRate(**rate))
                else:
                    _rates.append(rate)
            self.rates = _rates
        else:
            self.rates = rates
