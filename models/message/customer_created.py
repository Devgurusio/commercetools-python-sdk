from .message import Message
from models.customer import Customer


class CustomerCreated(Message):
    type: 'CustomerCreated'
    customer: Customer

    def __init__(self, type: str = 'CustomerCreated', customer: Customer = None, **kwargs):
        super().__init__(**kwargs)
        if customer is not None:
            if isinstance(customer, dict):
                self.customer = Customer(**customer)
            else:
                self.customer = customer
