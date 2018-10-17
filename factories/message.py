from models import message
from .basefactory import BaseFactory
from repositories.baserepository import BaseRepository
from decorators.factories import ModelNeeded

class MessageFactory(BaseFactory):
    _model = message

    @classmethod
    @ModelNeeded()
    def new(cls, repository: BaseRepository = None, helper=None, **kwargs):
        try:
            model = getattr(message, kwargs['type'])
            return model(_repository=repository, _helper=helper, **kwargs)  # pylint: disable=E1102
        except Exception as e:
            raise e
