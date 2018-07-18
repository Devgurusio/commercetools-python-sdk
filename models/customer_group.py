from .basemodel import BaseModel

from typing import List

ENDPOINT = 'customer-groups'

class CustomerGroup(BaseModel):
  key: str
  name: str
  #custom - CustomFields - Optional

  def __init__(self, key: str = None, name: str = None, **kwargs):
    super().__init__(**kwargs)
    self.key = key
    self.name = name
    #self.custom = custom
