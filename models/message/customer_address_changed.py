from .message import Message
from models.types.address import Address


class CustomerAddressChanged(Message):
    type: 'CustomerAddressChanged'
    address: Address

    def __init__(self, type: str = 'CustomerAddressChanged', address: Address = None, **kwargs):
        super().__init__(**kwargs)
        if address is not None:
            if isinstance(address, dict):
                self.address = Address(**address)
            else:
                self.address = address
