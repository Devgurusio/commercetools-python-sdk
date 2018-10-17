from .message import Message
from models.product_projection import ProductProjection


class ProductCreated(Message):
    type: 'ProductCreated'
    productProjection: ProductProjection

    def __init__(self, type: str = 'ProductCreated', productProjection: ProductProjection = None, **kwargs):
        super().__init__(**kwargs)
        if productProjection is not None:
            if isinstance(productProjection, dict):
                self.productProjection = ProductProjection(**productProjection)
            else:
                self.productProjection = productProjection
