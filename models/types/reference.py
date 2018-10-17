from .basetype import BaseType
from decorators.decorators import ValidValues
import models


class Reference(BaseType):
    _typeId: str
    id: str
    _obj: models.BaseModel

    _reference_types = {
        'cart': 'Cart',
        'cart-discount': 'CartDiscount',
        'category': 'Category',
        'channel': 'Channel',
        'customer': 'Customer',
        'customer-group': 'CustomerGroup',
        'discount-code': 'DiscountCode',
        'key-value-document': 'CustomObject',
        'payment': 'Payment',
        'product': 'Product',
        'product-discount': 'ProductDiscount',
        'product-price': 'Price',
        'product-type': 'ProductType',
        'order': 'Order',
        'shipping-method': 'ShippingMethod',
        'shopping-list': 'ShoppingList',
        'state': 'State',
        'tax-category': 'TaxCategory',
        'type': 'Type',
        'zone': 'Zone'
    }

    def __init__(self, typeId: str, id: str, obj: models.BaseModel = None):
        self.typeId = typeId
        self.id = id
        self.obj = obj

    @property
    def typeId(self):
        return self._typeId

    @typeId.setter
    @ValidValues(_reference_types.keys())
    def typeId(self, value):
        self._typeId = value

    @property
    def obj(self):
        return self._obj

    @obj.setter
    def obj(self, value):
        if self.typeId is not None and isinstance(obj, dict):
            model = getattr(models, _reference_types[self.typeId])
            self._obj = model(**obj)
        else:
            self._obj = value

    def toDict(self):
        d = super().toDict()
        if self._typeId is not None:
            d['typeId'] = self._typeId
        if self._obj is not None:
            d['obj'] = self._obj
        return d
