from .message import Message
from models.types.reference import Reference


class OrderCustomerSet(Message):
    type: 'OrderCustomerSet'
    customer: Reference
    customerGroup: Reference
    oldCustomer: Reference
    oldCustomerGroup: Reference

    def __init__(self, type: str = 'OrderCustomerSet', customer: Reference = None, customerGroup: Reference = None, oldCustomer: Reference = None, oldCustomerGroup: Reference = None, **kwargs):
        super().__init__(**kwargs)
        if customer is not None:
            if isinstance(customer, dict):
                self.customer = Reference(**customer)
            else:
                self.customer = customer
        if customerGroup is not None:
            if isinstance(customerGroup, dict):
                self.customerGroup = Reference(**customerGroup)
            else:
                self.customerGroup = customerGroup
        if oldCustomer is not None:
            if isinstance(oldCustomer, dict):
                self.oldCustomer = Reference(**oldCustomer)
            else:
                self.oldCustomer = oldCustomer
        if oldCustomerGroup is not None:
            if isinstance(oldCustomerGroup, dict):
                self.oldCustomerGroup = Reference(**oldCustomerGroup)
            else:
                self.oldCustomerGroup = oldCustomerGroup
