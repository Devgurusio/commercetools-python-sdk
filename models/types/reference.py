from .basetype import BaseType
from repositories.baserepository import BaseRepository


class Reference(BaseType):
    typeId: str
    id: str
    obj: BaseRepository

    def __init__(self, typeId: str, id: str, obj: BaseRepository = None):
        self.typeId = typeId
        self.id = id
        if obj is not None:
            if isinstance(obj, dict):
                self.obj = BaseRepository(**obj)
            else:
                self.obj = obj
