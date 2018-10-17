from .message import Message
from models.types.product_variant import ProductVariant
from typing import List


class ProductVariantDeleted(Message):
    type: 'ProductVariantDeleted'
    removedImageUrls: List[str]
    variant: ProductVariant

    def __init__(self, type: str = 'ProductVariantDeleted', removedImageUrls: List[str] = None, variant: ProductVariant = None, **kwargs):
        super().__init__(**kwargs)
        self.removedImageUrls = removedImageUrls
        if variant is not None:
            if isinstance(variant, dict):
                self.variant = ProductVariant(**variant)
            else:
                self.variant = variant
