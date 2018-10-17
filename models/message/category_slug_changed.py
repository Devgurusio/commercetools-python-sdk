from .message import Message
from typing import Dict


class CategorySlugChanged(Message):
    type: 'CategorySlugChanged'
    slug: Dict

    def __init__(self, type: str = 'CategorySlugChanged', slug: Dict = None, **kwargs):
        super().__init__(**kwargs)
        self.slug = slug
