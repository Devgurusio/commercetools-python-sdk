class ModelNeeded(object):
  #def __init__(self, *args, **kwargs):
  #  self.obj = None
  
  def __call__(self, func):
    def authorize_and_call(*args, **kwargs):
      obj = args[0]
      if obj == None or obj._model == None:
        raise Exception('Factory has no model defined')
      return func(*args, **kwargs)
        
    return authorize_and_call