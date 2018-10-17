from .message import Message
from models.types.reference import Reference


class ReviewRatingSet(Message):
    type: 'ReviewRatingSet'
    oldRating: float
    newRating: float
    includedInStatistics: bool
    target: Reference

    def __init__(self, type: str = 'ReviewRatingSet', oldRating: float = None, newRating: float = None, includedInStatistics: bool = None, target: Reference = None, **kwargs):
        super().__init__(**kwargs)
        self.oldRating = oldRating
        self.newRating = newRating
        self.includedInStatistics = includedInStatistics
        if target is not None:
            if isinstance(target, dict):
                self.target = Reference(**target)
            else:
                self.target = target
