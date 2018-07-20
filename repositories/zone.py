from .baserepository import BaseRepository
from factories.zone import ZoneFactory
from .actions.zone import ZoneActions


class ZoneRepository(BaseRepository):
    _endpoint = 'zones'
    _factory = ZoneFactory
    _actions_module = ZoneActions
