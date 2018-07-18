from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

oauth_uri = 'oauth/token'

class Client:
  def __init__(self, project_key: str, client_id: str, client_secret: str, auth_uri: str, api_uri: str):
    self.project_key = project_key
    self.api_uri = api_uri
    self.oauth = OAuth2Session(client=BackendApplicationClient(client_id=client_id))
    self.oauth.fetch_token(token_url='%s/%s' % (auth_uri, oauth_uri), client_id=client_id, client_secret=client_secret)

  def get(self, path: str, **kwargs):
    res = self.oauth.get('%s/%s/%s' % (self.api_uri, self.project_key, path), **kwargs)
    res.raise_for_status()
    return res
  
  def post(self, path: str, **kwargs):
    res = self.oauth.post('%s/%s/%s' % (self.api_uri, self.project_key, path), **kwargs)
    res.raise_for_status()
    return res
  
  def delete(self, path: str, **kwargs):
    res = self.oauth.delete('%s/%s/%s' % (self.api_uri, self.project_key, path), **kwargs)
    res.raise_for_status()
    return res