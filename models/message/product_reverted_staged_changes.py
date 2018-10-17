from .message import Message
from typing import List


class ProductRevertedStagedChanges(Message):
    type: 'ProductRevertedStagedChanges'
    removedImageUrls: List[str]

    def __init__(self, type: str = 'ProductRevertedStagedChanges', removedImageUrls: List[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.removedImageUrls = removedImageUrls
