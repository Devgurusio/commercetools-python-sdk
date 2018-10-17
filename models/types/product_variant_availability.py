from .basetype import BaseType
from typing import Dict


class ProductVariantAvailability(BaseType):
    isOnStock: bool
    restockableInDays: int
    availableQuantity: int
    channels: Dict

    def __init__(self, isOnStock: bool = None, restockableInDays: int = None, availableQuantity: int = None, channels: Dict = None):
        self.isOnStock = isOnStock
        self.restockableInDays = restockableInDays
        self.availableQuantity = availableQuantity
        if channels is not None:
            _channels = {}
            for channel, productVariantAvailability in channels.items():
                if isinstance(productVariantAvailability, dict):
                    _channels.__setitem__(channel, ProductVariantAvailability(
                        **productVariantAvailability))
                else:
                    _channels.__setitem__(channel, productVariantAvailability)
            self.channels = _channels
        else:
            self.channels = channels
