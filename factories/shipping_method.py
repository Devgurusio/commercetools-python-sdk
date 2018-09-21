from models.shipping_method import ShippingMethod
from .basefactory import BaseFactory


class ShippingMethodFactory(BaseFactory):
    _model = ShippingMethod
