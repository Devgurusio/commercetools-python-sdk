from .baserepository import BaseRepository
from factories.zone import ZoneFactory
from .actions.zone import ZoneActions
from decorators.repositories import RepositoryConnected
from decorators.decorators import RequiredParams
from requests.exceptions import HTTPError

class ZoneRepository(BaseRepository):
  _endpoint = 'zones'
  _factory = ZoneFactory
  _actions_module = ZoneActions