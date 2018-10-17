from .message import Message
from typing import Dict


class ProductSlugChanged(Message):
    type: 'ProductSlugChanged'
    slug: Dict

    def __init__(self, type: str = 'ProductSlugChanged', slug: Dict = None, **kwargs):
        super().__init__(**kwargs)
        self.slug = slug
