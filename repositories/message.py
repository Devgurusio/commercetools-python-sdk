from .baserepository import BaseRepository
from factories.message import MessageFactory


class MessageRepository(BaseRepository):
    _endpoint = 'messages'
    _factory = MessageFactory

    def create(self, obj):
        raise NotImplementedError('Messages can not be created')
    
    def update(self, obj, old_obj=None, force=False):
        raise NotImplementedError('Messages can not be updated')
    
    def delete(self, obj=None, id: str = None, key: str = None, version: int = None, data_erasure=False, force=True):
        raise NotImplementedError('Messages can not be deleted')