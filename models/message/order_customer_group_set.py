from .message import Message
from models.types.reference import Reference


class OrderCustomerGroupSet(Message):
    type: 'OrderCustomerGroupSet'
    customerGroup: Reference
    oldCustomerGroup: Reference

    def __init__(self, type: str = 'OrderCustomerGroupSet', customerGroup: Reference = None, oldCustomerGroup: Reference = None, **kwargs):
        super().__init__(**kwargs)
        if customerGroup is not None:
            if isinstance(customerGroup, dict):
                self.customerGroup = Reference(**customerGroup)
            else:
                self.customerGroup = customerGroup
        if oldCustomerGroup is not None:
            if isinstance(oldCustomerGroup, dict):
                self.oldCustomerGroup = Reference(**oldCustomerGroup)
            else:
                self.oldCustomerGroup = oldCustomerGroup
