from .basemodel import BaseModel
from .types.reference import Reference
from .types.zone_rate import ZoneRate
from typing import List


class ShippingMethod(BaseModel):
    key: str
    name: str
    description: str
    taxCategory: Reference
    zoneRates: List[ZoneRate]
    isDefault: bool
    predicate: str

    def __init__(self, key: str = None, name: str = None, description: str = None, taxCategory: Reference = None, zoneRates: List[ZoneRate] = None, isDefault: bool = None, predicate: str = None, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.name = name
        self.description = description
        if taxCategory is not None:
            if isinstance(taxCategory, dict):
                self.taxCategory = Reference(**taxCategory)
            else:
                self.taxCategory = taxCategory
        if zoneRates is not None:
            _zoneRates = []
            for zoneRate in zoneRates:
                if isinstance(zoneRate, dict):
                    _zoneRates.append(ZoneRate(**zoneRate))
                else:
                    _zoneRates.append(zoneRate)
            self.zoneRates = _zoneRates
        else:
            self.zoneRates = zoneRates
        self.isDefault = isDefault
        self.predicate = predicate
