from .basemodel import BaseModel
from .types.field_definition import FieldDefinition
from typing import List, Dict


class Type(BaseModel):
    key: str
    name: Dict
    description: Dict
    resourceTypeIds: List[str]
    fieldDefinitions: List[FieldDefinition]

    def __init__(self, key: str = None, name: Dict = None, description: Dict = None, resourceTypeIds: List[str] = None, fieldDefinitions: List[FieldDefinition] = None, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.name = name
        self.description = description
        self.resourceTypeIds = resourceTypeIds
        if fieldDefinitions is not None:
            _fieldDefinitions = []
            for fieldDefinition in fieldDefinitions:
                if isinstance(fieldDefinition, dict):
                    _fieldDefinitions.append(
                        FieldDefinition(**fieldDefinition))
                else:
                    _fieldDefinitions.append(fieldDefinition)
            self.fieldDefinitions = _fieldDefinitions
        else:
            self.fieldDefinitions = fieldDefinitions
