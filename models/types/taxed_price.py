from .basetype import BaseType
from .money import Money
from .tax_portion import TaxPortion
from typing import List


class TaxedPrice(BaseType):
    totalNet: Money
    totalGross: Money
    taxPortions: List[TaxPortion]

    def __init__(self, totalNet: Money = None, totalGross: Money = None, taxPortions: List[TaxPortion] = None):
        if totalNet is not None:
            if isinstance(totalNet, dict):
                self.totalNet = Money(**totalNet)
            else:
                self.totalNet = totalNet
        if totalGross is not None:
            if isinstance(totalGross, dict):
                self.totalGross = Money(**totalGross)
            else:
                self.totalGross = totalGross
        if taxPortions is not None:
            _taxPortions = []
            for taxPortion in taxPortions:
                if isinstance(taxPortion, dict):
                    _taxPortions.append(TaxPortion(**taxPortion))
                else:
                    _taxPortions.append(taxPortion)
            self.taxPortions = _taxPortions
        else:
            self.taxPortions = taxPortions
