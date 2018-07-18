from .basetype import BaseType

class Location(BaseType):
  country: str
  state: str

  def __init__(self, country: str, state: str = None):
    self.country = country
    self.state = state