class RequiredParams(object):
  def __init__(self, *args, **kwargs):
    self.required_params = args
  
  def __call__(self, func):
    def authorize_and_call(*args, **kwargs):
      print(args)
      print(kwargs)
      obj = args[0]
      #for params in self.required_params:
      #  for param in params:
      #    if obj.__getattribute__(param):

      
      #if obj == None or obj.client == None:
      #  raise Exception('Repository is not connected to a client')
      return func(*args, **kwargs)
      
    return authorize_and_call
  
class ValidValues(object):
  def __init__(self, valid_values, *args, **kwargs):
    self.valid_values = valid_values
  
  def __call__(self, func):
    def authorize_and_call(obj, value, *args, **kwargs):
      if value != None and not value in self.valid_values:
        raise ValueError('Value not in %s' % (self.valid_values))
      return func(obj, value, *args, **kwargs)
      
    return authorize_and_call