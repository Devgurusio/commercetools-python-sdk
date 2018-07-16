from datetime import datetime
import json
from decorators.models import ModelPersisted, ModelRepository

class BaseModel:
  id: str
  version: int
  createdAt: datetime
  lastModifiedAt: datetime

  def __init__(self, id: str = None, version: str = None, createdAt: datetime = None, lastModifiedAt: datetime = None, _repository = None, _helper = None):
    self.id = id
    self.version = version
    self.createdAt = createdAt
    self.lastModifiedAt = lastModifiedAt
    self._repository = _repository
    self._helper = _helper
  
  def __str__(self):
    return self.toDict().__str__()

  def copy(self):
    return type(self)(**self.__dict__)
  
  def __repr__(self):
    return self.toDict().__str__()

  @ModelRepository()
  def save(self, force = False):
    if self.id == None:
      self.__dict__.update(self._repository.create(self).__dict__)
    else:
      self.__dict__.update(self._repository.update(self).__dict__)
    return self
  
  @ModelPersisted()
  def delete(self, force = False):
    self.__dict__.update(self._repository.delete(self, force=force).__dict__)
    return self

  def toDict(self):
    return { k: self.__dict__[k] for k in self.__dict__ if self.__dict__[k] != None and not k.startswith('_') }

  def toJson(self):
    return json.dumps(self, default=lambda o: { k: o.__dict__[k] for k in o.__dict__ if o.__dict__[k] != None and not k.startswith('_') }, sort_keys=True, indent=4)