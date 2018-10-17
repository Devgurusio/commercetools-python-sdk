from .message import Message
from models.types.image import Image


class ProductImageAdded(Message):
    type: 'ProductImageAdded'
    variantId: int
    image: Image
    staged: bool

    def __init__(self, type: str = 'ProductImageAdded', variantId: int = None, image: Image = None, staged: bool = None, **kwargs):
        super().__init__(**kwargs)
        self.variantId = variantId
        if image is not None:
            if isinstance(image, dict):
                self.image = Image(**image)
            else:
                self.image = image
        self.staged = staged
