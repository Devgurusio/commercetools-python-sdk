from .basetype import BaseType
from .money import Money
from .taxed_price import TaxedPrice


class OrderExcerpt(BaseType):
    totalPrice: Money
    taxedPrice: TaxedPrice
    version: int

    def __init__(self, totalPrice: Money = None, taxedPrice: TaxedPrice = None, version: int = None):
        if totalPrice is not None:
            if isinstance(totalPrice, dict):
                self.totalPrice = Money(**totalPrice)
            else:
                self.totalPrice = totalPrice
        if taxedPrice is not None:
            if isinstance(taxedPrice, dict):
                self.taxedPrice = TaxedPrice(**taxedPrice)
            else:
                self.taxedPrice = taxedPrice
        self.version = version
