from .basetype import BaseType
from .item_shipping_target import ItemShippingTarget
from typing import List


class ItemShippingDetails(BaseType):
    targets: List[ItemShippingTarget]
    valid: bool

    def __init__(self, targets: List[ItemShippingTarget] = None, valid: bool = None):
        if targets is not None:
            _targets = []
            for target in targets:
                if isinstance(target, dict):
                    _targets.append(ItemShippingTarget(**target))
                else:
                    _targets.append(target)
            self.targets = _targets
        else:
            self.targets = targets
        self.valid = valid
