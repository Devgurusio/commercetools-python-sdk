from .message import Message
from models.category import Category


class CategoryCreated(Message):
    type: 'CategoryCreated'
    category: Category

    def __init__(self, type: str = 'CategoryCreated', category: Category = None, **kwargs):
        super().__init__(**kwargs)
        if category is not None:
            if isinstance(category, dict):
                self.category = Category(**category)
            else:
                self.category = category
