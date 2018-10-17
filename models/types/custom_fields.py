from .basetype import BaseType
from .reference import Reference
from .field_definition import FieldDefinition
from typing import List


class CustomFields(BaseType):
    type: Reference
    fields: List[FieldDefinition]

    def __init__(self, type: Reference = None, fields: List[FieldDefinition] = None):
        if type is not None:
            if isinstance(type, dict):
                self.type = Reference(**type)
            else:
                self.type = type
        if fields is not None:
            _fields = []
            for field in fields:
                if isinstance(field, dict):
                    _fields.append(FieldDefinition(**field))
                else:
                    _fields.append(field)
            self.fields = _fields
        else:
            self.fields = fields
        

    def toDict(self):
        if self.fields is not None and self.fields.__len__() > 0:
            d = super().toDict()
            d['fields'] = [field.toDict() for field in d['fields']]
            return d
        else:
            return super().toDict()
