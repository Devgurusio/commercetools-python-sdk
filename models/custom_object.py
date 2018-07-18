from .basemodel import BaseModel
from typing import List, Dict

class CustomObject(BaseModel):
  container: str
  key: str
  value: Dict

  def __init__(self, container: str = None, key: str = None, value: Dict = None, **kwargs):
    super().__init__(**kwargs)
    self.container = container
    self.key = key
    self.value = value