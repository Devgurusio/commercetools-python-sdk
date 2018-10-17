from .basetype import BaseType
from datetime import datetime
from typing import List


class ParcelMeasurements(BaseType):
    heightInMillimeter: int
    lengthInMillimeter: int
    widthInMillimeter: int
    weightInGram: int

    def __init__(self, heightInMillimeter: int = None, lengthInMillimeter: int = None, widthInMillimeter: int = None, weightInGram: int = None):
        self.heightInMillimeter = heightInMillimeter
        self.lengthInMillimeter = lengthInMillimeter
        self.widthInMillimeter = widthInMillimeter
        self.weightInGram = weightInGram
