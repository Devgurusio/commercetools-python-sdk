
from datetime import datetime

class CustomerToken:
  id:str
  customerId:str
  createdAt:datetime
  lastModifiedAt:datetime
  expiresAt:datetime
  value:str
  
  def __init__(self, id :str = None, customerId: str = None, createdAt: datetime = None, lastModifiedAt: datetime = None, expiresAt: datetime = None, value: str = None):
    self.id = id
    self.customerId = customerId
    self.createdAt = createdAt
    self.lastModifiedAt = lastModifiedAt
    self.expiresAt = expiresAt
    self.value = value
  
  def __str__(self):
    return vars(self).__str__()