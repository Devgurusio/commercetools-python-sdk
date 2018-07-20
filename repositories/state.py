from .baserepository import BaseRepository
from factories.state import StateFactory
from .actions.state import StateActions


class StateRepository(BaseRepository):
    _endpoint = 'states'
    _factory = StateFactory
    _actions_module = StateActions
