from .message import Message
from models.types.reference import Reference


class CustomerGroupSet(Message):
    type: 'CustomerGroupSet'
    customerGroup: Reference

    def __init__(self, type: str = 'CustomerGroupSet', customerGroup: Reference = None, **kwargs):
        super().__init__(**kwargs)
        if customerGroup is not None:
            if isinstance(customerGroup, dict):
                self.customerGroup = Reference(**customerGroup)
            else:
                self.customerGroup = customerGroup
