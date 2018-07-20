from .baserepository import BaseRepository
from factories.type import TypeFactory
from .actions.type import TypeActions


class TypeRepository(BaseRepository):
    _endpoint = 'types'
    _factory = TypeFactory
    _actions_module = TypeActions
