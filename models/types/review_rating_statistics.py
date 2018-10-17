from .basetype import BaseType
from typing import Dict


class ReviewRatingStatistics(BaseType):
    averageRating: float
    highestRating: float
    lowestRating: float
    count: int
    ratingsDistribution: Dict

    def __init__(self, averageRating: float = None, highestRating: float = None, lowestRating: float = None, count: int = None, ratingsDistribution: Dict = None):
        self.averageRating = averageRating
        self.highestRating = highestRating
        self.lowestRating = lowestRating
        self.count = count
        self.ratingsDistribution = ratingsDistribution
