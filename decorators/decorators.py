import re


class RequiredParams(object):
    def __init__(self, *args, **kwargs):
        self.required_params = args

    def __call__(self, func):
        def authorize_and_call(*args, **kwargs):
            print(args)
            print(kwargs)
            obj = args[0]
            # for params in self.required_params:
            #  for param in params:
            #    if obj.__getattribute__(param):

            # if obj == None or obj.client == None:
            #  raise Exception('Repository is not connected to a client')
            return func(*args, **kwargs)

        return authorize_and_call


class ValidValues(object):
    def __init__(self, valid_values, *args, **kwargs):
        self.valid_values = valid_values

    def __call__(self, func):
        def authorize_and_call(obj, value, *args, **kwargs):
            if value is not None and value not in self.valid_values:
                raise ValueError('Value not in %s' % (self.valid_values))
            return func(obj, value, *args, **kwargs)

        return authorize_and_call


class StringMatches(object):
    def __init__(self, pattern, flags=0, min_len=None, max_len=None, *args, **kwargs):
        self.pattern = pattern
        self.regular_expression_object = re.compile(pattern, flags)
        self.min_len = min_len
        self.max_len = max_len

    def __call__(self, func):
        def authorize_and_call(obj, value, *args, **kwargs):
            if value is not None:
                if self.min_len is not None and value.__len__() < self.min_len:
                    raise ValueError(
                        'Value length is less than %s' % self.min_len)
                if self.max_len is not None and value.__len__() > self.max_len:
                    raise ValueError(
                        'Value length is higher than %s' % self.max_len)
                if self.regular_expression_object.fullmatch(value) is None:
                    raise ValueError('Value doesn\'t match pattern "%s" with flags %s' % (
                        self.pattern, self.regular_expression_object.flags))
            return func(obj, value, *args, **kwargs)

        return authorize_and_call
