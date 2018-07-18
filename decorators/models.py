class ModelRepository(object):
  def __init__(self, *args, **kwargs):
    self.obj = None
  
  def __call__(self, func):
    def authorize_and_call(*args, **kwargs):
      obj = args[0]
      if obj == None or obj._repository == None:
        raise Exception('This object is not connected with a repository. Please, create it using repository factory')
      return func(*args, **kwargs)
        
    return authorize_and_call

class ModelPersisted(object):
  def __call__(self, func):
    @ModelRepository(func)
    def authorize_and_call(*args, **kwargs):
      obj = args[0]
      if obj == None or obj.id == None:
        raise Exception('Object has no id. Maybe it is not in repository?')
      return func(*args, **kwargs)
      
    return authorize_and_call