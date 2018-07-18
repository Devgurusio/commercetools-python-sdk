from typing import List
from connection.results.pagedqueryresult import PagedQueryResult
from decorators.repositories import EndpointNeeded, RepositoryConnected, FactoryNeeded, ActionsModuleNeeded
from requests.exceptions import HTTPError

class BaseRepository:
  _endpoint = None
  _factory = None
  _actions_module = None

  @EndpointNeeded()
  def __init__(self, client):
    self.client = client

  @FactoryNeeded()
  def new(self, **kwargs):
    return self._factory.new(repository=self, **kwargs)

  @RepositoryConnected()
  def _create(self, obj):
    return self.client.post(path=self._endpoint, json=obj.toDict()).json()

  def create(self, obj):
    return self.new(**self._create(obj))

  @RepositoryConnected()
  def get(self, id: str = None, key: str = None):
    if (id):
      r = self.client.get(path='%s/%s' % (self._endpoint, id))
    elif (key):
      r = self.client.get(path='%s/key=%s' % (self._endpoint, key))
    else:
      raise Exception('Please, provide id or key')
    
    return self.new(**r.json())
  
  @RepositoryConnected()
  def query(self, where: str = None, sort: str = None, expand: str = None, limit: int = None, offset: int = None):
    params = {}
    if (where != None):
      params.where = where
    if (sort != None):
      params.sort = sort
    if (expand != None):
      params.expand = expand
    if (limit != None):
      params.limit = limit
    if (offset != None):
      params.offset = offset
    
    if (params.keys().__len__() == 0):
      params = None
    
    return PagedQueryResult(**self.client.get(path=self._endpoint, params=params).json())
  
  @RepositoryConnected()
  def _update(self, actions: List, id: str = None, key: str = None, version = None, force = False):
    if (actions.__len__ == 0):
      return Exception('No actions given')
    
    try:
      if (id):
        return self.client.post(path='%s/%s' % (self._endpoint, id), json={'version': version, 'actions': actions}).json()
      elif (key):
        return self.client.post(path='%s/key=%s' % (self._endpoint, key), json={'version': version, 'actions': actions}).json()
    except HTTPError as error:
      if (force == True and error.response.status_code == 409):
        _obj = self.get(id, key)
        return self._update(actions, id, key, _obj.version, force)
      raise error

  @ActionsModuleNeeded()
  def update(self, obj, old_obj = None, force = False):
    if (old_obj == None):
      old_obj = self.get(obj.id)
    actions = self._actions_module.get_actions(old_obj, obj)
    return self.new(**self._update(actions=actions, id=obj.id, version=obj.version, force=force))

  @RepositoryConnected()
  def delete(self, obj = None, id: str = None, key: str = None, version: int = None, data_erasure = False, force = True):
    try:
      if (obj != None):
        if (not obj.version):
          obj.version = 1
        if (obj.id != None):
          return self.new(**self.client.delete(path='%s/%s' % (self._endpoint, obj.id), params={'version': obj.version, 'dataErasure': data_erasure}).json())
        elif (obj.key != None):
          return self.new(**self.client.delete(path='%s/key=%s' % (self._endpoint, obj.key), params={'version': obj.version, 'dataErasure': data_erasure}).json())
        else:
          raise Exception('Object has no id or key')
      if (id):
        return  self.new(**self.client.delete(path='%s/%s' % (self._endpoint, id), params={'version': version, 'dataErasure': data_erasure}).json())
      elif (key):
        return  self.new(**self.client.delete(path='%s/key=%s' % (self._endpoint, key), params={'version': version, 'dataErasure': data_erasure}).json())
      else:
        raise Exception('Please, provide id or key')
    except HTTPError as error:
      if (force == True and error.response.status_code == 409):
        if (obj):
          _obj = self.get(obj.id, obj.key)
        else:
          _obj = self.get(id, key)
        return self.delete(_obj, id, key, _obj.version, data_erasure, force)
      raise error
