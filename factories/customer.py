from models.customer import Customer
from .basefactory import BaseFactory


class CustomerFactory(BaseFactory):
    _model = Customer
