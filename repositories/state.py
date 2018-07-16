from .baserepository import BaseRepository
from factories.state import StateFactory
from .actions.state import StateActions
from decorators.repositories import RepositoryConnected
from decorators.decorators import RequiredParams
from requests.exceptions import HTTPError

class StateRepository(BaseRepository):
  _endpoint = 'states'
  _factory = StateFactory
  _actions_module = StateActions