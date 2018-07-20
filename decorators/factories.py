class ModelNeeded(object):
    def __call__(self, func):
        def authorize_and_call(*args, **kwargs):
            obj = args[0]
            if obj is None or obj._model is None:
                raise Exception('Factory has no model defined')
            return func(*args, **kwargs)

        return authorize_and_call
