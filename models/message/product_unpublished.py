from .message import Message
from models.types.reference import Reference


class ProductUnpublished(Message):
    type: 'ProductUnpublished'

    def __init__(self, type: str = 'ProductUnpublished', **kwargs):
        super().__init__(**kwargs)
