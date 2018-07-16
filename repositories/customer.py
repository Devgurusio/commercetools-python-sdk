from .baserepository import BaseRepository
from factories.customer import CustomerFactory
from connection.results.customersigninresult import CustomerSignInResult
from .actions.customer import CustomerActions
from decorators.repositories import RepositoryConnected
from decorators.decorators import RequiredParams
from requests.exceptions import HTTPError

class CustomerRepository(BaseRepository):
  _endpoint = 'customers'
  _factory = CustomerFactory
  _actions_module = CustomerActions

  @RepositoryConnected()
  def create(self, customer_draft):
    return CustomerSignInResult(repository=self, **super()._create(customer_draft))

  @RepositoryConnected()
  def get(self, id: str = None, key: str = None, email_token: str = None, password_token: str = None):
    if (email_token):
      return self.new(**self.client.get(path='customers/email-token=%s' % (email_token)).json())
    elif (password_token):
      return self.new(**self.client.get(path='customers/password-token=%s' % (email_token)).json())
    return super().get(id, key)

  #@RequiredParams(('obj'), ('id', 'version'))
  @RepositoryConnected()
  def change_password(self, current_password: str, new_password: str, obj = None, id: str = None, version: int = None, force = False):
    try:
      if (obj):
        return self.new(**self.client.post(path='customers/password', json={'id': obj.id, 'version': obj.version, 'currentPassword': current_password, 'newPassword': new_password}).json())
      if (not id or not version):
        raise Exception('Please, provide id and version')
      return self.new(**self.client.post(path='customers/password', json={'id': id, 'version': version, 'currentPassword': current_password, 'newPassword': new_password}).json())
    except HTTPError as error:
      if (force == True and error.response.status_code == 409):
        if (obj):
          _obj = self.get(obj.id)
        else:
          _obj = self.get(id)
        return self.change_password(current_password, new_password, _obj, id, _obj.version, force)
      raise error