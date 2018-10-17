from .basetype import BaseType
from .money import Money
from .shipping_rate import ShippingRate
from .taxed_item_price import TaxedItemPrice
from .tax_rate import TaxRate
from .reference import Reference
from .delivery import Delivery
from .discounted_line_item_price import DiscountedLineItemPrice
from typing import List
from decorators.decorators import ValidValues


class ShippingInfo(BaseType):
    shippingMethodName: str
    price: Money
    shippingRate: ShippingRate
    taxedPrice: TaxedItemPrice
    taxRate: TaxRate
    taxCategory: Reference
    shippingMethod: Reference
    deliveries: List[Delivery]
    discountedPrice: DiscountedLineItemPrice
    _shippingMethodState: str
    _shippingMethodState_types = ['DoesNotMatchCart', 'MatchesCart']

    def __init__(self, shippingMethodName: str = None, price: Money = None, shippingRate: ShippingRate = None, taxedPrice: TaxedItemPrice = None, taxRate: TaxRate = None, taxCategory: Reference = None, shippingMethod: Reference = None, deliveries: List[Delivery] = None, discountedPrice: DiscountedLineItemPrice = None, shippingMethodState: str = None):
        self.shippingMethodName = shippingMethodName
        if price is not None:
            if isinstance(price, dict):
                self.price = Money(**price)
            else:
                self.price = price
        if shippingRate is not None:
            if isinstance(shippingRate, dict):
                self.shippingRate = ShippingRate(**shippingRate)
            else:
                self.shippingRate = shippingRate
        if taxedPrice is not None:
            if isinstance(taxedPrice, dict):
                self.taxedPrice = TaxedItemPrice(**taxedPrice)
            else:
                self.taxedPrice = taxedPrice
        if taxRate is not None:
            if isinstance(taxRate, dict):
                self.taxRate = TaxRate(**taxRate)
            else:
                self.taxRate = taxRate
        if taxCategory is not None:
            if isinstance(taxCategory, dict):
                self.taxCategory = Reference(**taxCategory)
            else:
                self.taxCategory = taxCategory
        if shippingMethod is not None:
            if isinstance(shippingMethod, dict):
                self.shippingMethod = Reference(**shippingMethod)
            else:
                self.shippingMethod = shippingMethod
        if deliveries is not None:
            _deliveries = []
            for delivery in deliveries:
                if isinstance(delivery, dict):
                    _deliveries.append(Delivery(**delivery))
                else:
                    _deliveries.append(delivery)
            self.deliveries = _deliveries
        else:
            self.deliveries = deliveries
        if discountedPrice is not None:
            if isinstance(discountedPrice, dict):
                self.discountedPrice = DiscountedLineItemPrice(**discountedPrice)
            else:
                self.discountedPrice = discountedPrice
        self.shippingMethodState = shippingMethodState
    
    @property
    def shippingMethodState(self):
        return self._shippingMethodState

    @shippingMethodState.setter
    @ValidValues(_shippingMethodState_types)
    def shippingMethodState(self, value):
        self._shippingMethodState = value
    
    def toDict(self):
        d = super().toDict()
        if self._shippingMethodState is not None:
            d['shippingMethodState'] = self._shippingMethodState
        return d
