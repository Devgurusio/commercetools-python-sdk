from .basetype import BaseType
from .attribute_definition import AttributeDefinition


class Attribute(BaseType):
    name: str
    value: AttributeDefinition

    def __init__(self, name: str = None, value: AttributeDefinition = None):
        self.name = name
        if value is not None:
            if isinstance(value, dict):
                self.value = AttributeDefinition(**value)
            else:
                self.value = value
