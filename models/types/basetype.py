import json


class BaseType:
    def __str__(self):
        return self.toDict().__str__()

    def __repr__(self):
        return self.toDict().__str__()

    def copy(self):
        return type(self)(**self.__dict__)

    def _get_serialized_value(self, obj):
        try:
            return obj.toDict()
        except AttributeError:
            return obj

    def toDict(self):
        return {k: self._get_serialized_value(self.__dict__[k]) for k in self.__dict__ if self.__dict__[k] is not None and not k.startswith('_')}

    def toJson(self):
        return json.dumps(self, default=lambda o: o.toDict(), sort_keys=True, indent=4)