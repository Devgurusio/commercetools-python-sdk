from .message import Message
from models.product_projection import ProductProjection
from typing import List


class ProductDeleted(Message):
    type: 'ProductDeleted'
    removedImageUrls: List[str]
    currentProjection: ProductProjection

    def __init__(self, type: str = 'ProductDeleted', removedImageUrls: List[str] = None, currentProjection: ProductProjection = None, **kwargs):
        super().__init__(**kwargs)
        self.removedImageUrls = removedImageUrls
        if currentProjection is not None:
            if isinstance(currentProjection, dict):
                self.currentProjection = ProductProjection(**currentProjection)
            else:
                self.currentProjection = currentProjection
