from .baserepository import BaseRepository
from factories.custom_object import CustomObjectFactory
from decorators.repositories import RepositoryConnected
from decorators.decorators import RequiredParams
from requests.exceptions import HTTPError


class CustomObjectRepository(BaseRepository):
    _endpoint = 'custom-objects'
    _factory = CustomObjectFactory

    @RepositoryConnected()
    def _update(self, obj, force=False):
        try:
            return self._create(obj)
        except HTTPError as error:
            if force and error.response.status_code == 409:
                _obj = self.get(obj.id, obj.key)
                return self._update(_obj, force)
            raise error

    def update(self, obj, force=False):
        return self.new(**self._update(obj=obj, force=force))
