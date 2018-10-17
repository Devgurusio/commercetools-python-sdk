from models.basemodel import BaseModel
from models.types.user_provided_identifiers import UserProvidedIdentifiers
from models.types.reference import Reference


class Message(BaseModel):
    sequenceNumber: int
    resource: Reference
    resourceVersion: int
    resourceUserProvidedIdentifiers: UserProvidedIdentifiers
    type: str

    def __init__(self, type: str = None, sequenceNumber: int = None, resource: Reference = None, resourceVersion: int = None, resourceUserProvidedIdentifiers: UserProvidedIdentifiers = None, **kwargs):
        super().__init__(**kwargs)
        self.type = type
        self.sequenceNumber = sequenceNumber
        if resource is not None:
            if isinstance(resource, dict):
                self.resource = Reference(**resource)
            else:
                self.resource = resource
        self.resourceVersion = resourceVersion
        if resourceUserProvidedIdentifiers is not None:
            if isinstance(resourceUserProvidedIdentifiers, dict):
                self.resourceUserProvidedIdentifiers = UserProvidedIdentifiers(
                    **resourceUserProvidedIdentifiers)
            else:
                self.resourceUserProvidedIdentifiers = resourceUserProvidedIdentifiers
