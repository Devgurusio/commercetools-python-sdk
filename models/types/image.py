from .basetype import BaseType
from typing import Dict


class Image(BaseType):
    url: str
    dimensions: Dict
    label: str

    def __init__(self, url: str = None, dimensions: Dict = None, label: str = None):
        self.url = url
        self.dimensions = dimensions
        self.label = label
