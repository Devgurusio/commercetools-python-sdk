from .message import Message
from models.review import Review


class ReviewCreated(Message):
    type: 'ReviewCreated'
    review: Review

    def __init__(self, type: str = 'ReviewCreated', review: Review = None, **kwargs):
        super().__init__(**kwargs)
        if review is not None:
            if isinstance(review, dict):
                self.review = Review(**review)
            else:
                self.review = review
