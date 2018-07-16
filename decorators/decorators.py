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