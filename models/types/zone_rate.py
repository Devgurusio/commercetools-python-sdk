from .basetype import BaseType
from .reference import Reference
from .shipping_rate import ShippingRate
from typing import List


class ZoneRate(BaseType):
    zone: Reference
    shippingRates: List[ShippingRate]

    def __init__(self, zone: Reference = None, shippingRates: List[ShippingRate] = None):
        if zone is not None:
            if isinstance(zone, dict):
                self.zone = Reference(**zone)
            else:
                self.zone = zone
        if shippingRates is not None:
            _shippingRates = []
            for shippingRate in shippingRates:
                if isinstance(shippingRate, dict):
                    _shippingRates.append(ShippingRate(**shippingRate))
                else:
                    _shippingRates.append(shippingRate)
            self.shippingRates = _shippingRates
        else:
            self.shippingRates = shippingRates
