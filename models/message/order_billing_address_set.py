from .message import Message
from models.types.address import Address


class OrderBillingAddressSet(Message):
    type: 'OrderBillingAddressSet'
    address: Address
    oldAddress: Address

    def __init__(self, type: str = 'OrderBillingAddressSet', address: Address = None, oldAddress: Address = None, **kwargs):
        super().__init__(**kwargs)
        if address is not None:
            if isinstance(address, dict):
                self.address = Address(**address)
            else:
                self.address = address
        if oldAddress is not None:
            if isinstance(oldAddress, dict):
                self.oldAddress = Address(**oldAddress)
            else:
                self.oldAddress = oldAddress
