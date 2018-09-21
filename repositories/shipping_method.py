from .baserepository import BaseRepository
from factories.shipping_method import ShippingMethodFactory
from .actions.shipping_method import ShippingMethodActions


class ShippingMethodRepository(BaseRepository):
    _endpoint = 'shipping-methods'
    _factory = ShippingMethodFactory
    _actions_module = ShippingMethodActions
