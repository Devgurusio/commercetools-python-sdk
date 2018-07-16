from .basetype import BaseType
from repositories.baserepository import BaseRepository

class Reference(BaseType):
  typeId: str
  id: str
  obj: BaseRepository

  def __init__(self, typeId: str, id: str, obj: BaseRepository = None):
    self.typeId = typeId
    self.id = id
    self.obj = obj