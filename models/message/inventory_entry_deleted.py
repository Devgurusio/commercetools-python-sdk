from .message import Message
from models.types.reference import Reference


class InventoryEntryDeleted(Message):
    type: 'InventoryEntryDeleted'
    sku: str
    supplyChannel: Reference

    def __init__(self, type: str = 'InventoryEntryDeleted', sku: str = None, supplyChannel: Reference = None, **kwargs):
        super().__init__(**kwargs)
        self.sku = sku
        if supplyChannel is not None:
            if isinstance(supplyChannel, dict):
                self.supplyChannel = Reference(**supplyChannel)
            else:
                self.supplyChannel = supplyChannel
