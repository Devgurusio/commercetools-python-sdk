from .basetype import BaseType


class AttributeType(BaseType):
    name: str

    def __init__(self, name: str = None, **kwargs):
        self.name = name
        [ self.__setattr__(k, v) for k, v in kwargs.items() ]
