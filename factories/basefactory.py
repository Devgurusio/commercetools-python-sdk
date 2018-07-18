from models.basemodel import BaseModel
from repositories.baserepository import BaseRepository
from decorators.factories import ModelNeeded

class BaseFactory:
  _model: BaseModel = None

  @classmethod
  @ModelNeeded()
  def new(cls, repository: BaseRepository = None, helper = None, **kwargs):
    return cls._model(_repository=repository, _helper=helper, **kwargs) # pylint: disable=E1102