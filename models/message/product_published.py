from .message import Message
from models.product_projection import ProductProjection
from typing import List


class ProductPublished(Message):
    type: 'ProductPublished'
    scope: str
    productProjection: ProductProjection
    removedImageUrls: List[str]

    def __init__(self, type: str = 'ProductPublished', scope: str = None, productProjection: ProductProjection = None, removedImageUrls: List[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.scope = scope
        if productProjection is not None:
            if isinstance(productProjection, dict):
                self.productProjection = ProductProjection(**productProjection)
            else:
                self.productProjection = productProjection
        self.removedImageUrls = removedImageUrls
