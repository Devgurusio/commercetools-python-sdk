class RepositoryConnected(object):
    def __init__(self, *args, **kwargs):
        self.repository = None

    def __call__(self, func):
        def authorize_and_call(*args, **kwargs):
            obj = args[0]
            if obj is None or obj.client is None:
                raise Exception('Repository is not connected to a client')
            return func(*args, **kwargs)

        return authorize_and_call


class FactoryNeeded(object):
    def __call__(self, func):
        def authorize_and_call(*args, **kwargs):
            obj = args[0]
            if obj is None or obj._factory is None:
                raise Exception('Repository has no factory')
            return func(*args, **kwargs)

        return authorize_and_call


class ActionsModuleNeeded(object):
    def __call__(self, func):
        def authorize_and_call(*args, **kwargs):
            obj = args[0]
            if obj is None or obj._actions_module is None:
                raise Exception('Repository has no factory')
            return func(*args, **kwargs)

        return authorize_and_call


class EndpointNeeded(object):
    def __call__(self, func):
        def authorize_and_call(*args, **kwargs):
            obj = args[0]
            if obj is None or obj._endpoint is None:
                raise Exception('Repository has no _endpoint defined')
            return func(*args, **kwargs)

        return authorize_and_call
