import json

class BaseType:
  def __str__(self):
    return self.toDict().__str__()

  def __repr__(self):
    return self.toDict().__str__()
  
  def copy(self):
    return type(self)(**self.__dict__)
  
  def toDict(self):
    return { k: self.__dict__[k] for k in self.__dict__ if self.__dict__[k] != None and not k.startswith('_') }

  def toJson(self):
    return json.dumps(self, default=lambda o: { k: o.__dict__[k] for k in o.__dict__ if o.__dict__[k] != None and not k.startswith('_') }, sort_keys=True, indent=4)