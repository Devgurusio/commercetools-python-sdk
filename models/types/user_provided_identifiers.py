from .basetype import BaseType
from typing import Dict


class UserProvidedIdentifiers(BaseType):
    key: str
    externalId: str
    orderNumber: str
    sku: str
    slug: Dict

    def __init__(self, key: str = None, externalId: str = None, orderNumber: str = None, sku: str = None, slug: Dict = None):
        self.key = key
        self.externalId = externalId
        self.orderNumber = orderNumber
        self.sku = sku
        self.slug = slug
