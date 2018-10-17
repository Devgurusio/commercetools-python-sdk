from .basetype import BaseType
from .reference import Reference
from decorators.decorators import ValidValues


class DiscountCodeInfo(BaseType):
    discountCode: Reference
    _state: str

    _discountCodeState_types = ['NotActive', 'NotValid', 'DoesNotMatchCart',
                                'MatchesCart', 'MaxApplicationReached', 'ApplicationStoppedByPreviousDiscount']

    def __init__(self, discountCode: Reference = None, state: str = None):
        if discountCode is not None:
            if isinstance(discountCode, dict):
                self.discountCode = Reference(**discountCode)
            else:
                self.discountCode = discountCode
        self.state = state

    @property
    def state(self):
        return self._state

    @state.setter
    @ValidValues(_discountCodeState_types)
    def state(self, value):
        self._state = value

    def toDict(self):
        d = super().toDict()
        if self._state is not None:
            d['state'] = self._state
        return d
