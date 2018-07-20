from factories.customer import CustomerFactory
from repositories.customer import CustomerRepository
from connection.results.customersigninresult import CustomerSignInResult
from .utils.customertoken import CustomerToken


class CustomerHelper:
    def new(self, **kwargs):
        return self.repository.new(**kwargs)

    def __init__(self, client):
        self.client = client
        self.repository = CustomerRepository(client)

    def login(self, email: str, password: str, anonymous_cart_id: str = None, anonymous_cart_sign_in_mode: str = None, anonymous_id: str = None, update_product_data: bool = False):
        return CustomerSignInResult(repository=self.repository, **self.client.post(path='login', json={'email': email, 'password': password, 'anonymous_cart_id': anonymous_cart_id, 'anonymous_cart_sign_in_mode': anonymous_cart_sign_in_mode, 'anonymous_id': anonymous_id, 'update_product_data': update_product_data}).json())

    def get_verify_email_token(self, ttlMinutes: int, id: str = None, version: int = None, obj=None):
        if obj:
            return CustomerToken(**self.client.post(path='customers/email-token', json={'id': obj.id, 'version': obj.version, 'ttlMinutes': ttlMinutes}).json())
        if not id:
            raise Exception('Please, provide id')
        return CustomerToken(**self.client.post(path='customers/email-token', json={'id': id, 'version': version, 'ttlMinutes': ttlMinutes}).json())

    def verify_email(self, token_value: str):
        return self.new(**self.client.post(path='customers/email/confirm', json={'tokenValue': token_value}).json())

    def get_reset_password_token(self, email: str = None, obj=None):
        if obj:
            return CustomerToken(**self.client.post(path='customers/password-token', json={'email': obj.email}).json())
        if not email:
            raise Exception('Please, provide email')
        return CustomerToken(**self.client.post(path='customers/password-token', json={'email': email}).json())

    def reset_password(self, token_value: str, new_password: str):
        return self.new(**self.client.post(path='customers/email/confirm', json={'tokenValue': token_value, 'newPassword': new_password}).json())
