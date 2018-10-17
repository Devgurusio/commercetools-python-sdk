from .basetype import BaseType


class AssetDimensions(BaseType):
    w: int
    h: int

    def __init__(self, w: int = None, h: int = None):
        self.w = w
        self.h = h
