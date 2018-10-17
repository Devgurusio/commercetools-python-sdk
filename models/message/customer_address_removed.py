from .message import Message
from models.types.address import Address


class CustomerAddressRemoved(Message):
    type: 'CustomerAddressRemoved'
    address: Address

    def __init__(self, type: str = 'CustomerAddressRemoved', address: Address = None, **kwargs):
        super().__init__(**kwargs)
        if address is not None:
            if isinstance(address, dict):
                self.address = Address(**address)
            else:
                self.address = address
