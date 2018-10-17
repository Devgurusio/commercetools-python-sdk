from .message import Message
from models.types.reference import Reference
from decorators.decorators import ValidValues


class OrderDiscountCodeStateSet(Message):
    type: 'OrderDiscountCodeStateSet'
    discountCode: Reference
    _state: str
    _oldState: str

    _discountCodeState_types = ['NotActive', 'NotValid', 'DoesNotMatchCart',
                                'MatchesCart', 'MaxApplicationReached', 'ApplicationStoppedByPreviousDiscount']

    def __init__(self, type: str = 'OrderDiscountCodeStateSet', discountCode: Reference = None, state: str = None, oldState: str = None, **kwargs):
        super().__init__(**kwargs)
        if discountCode is not None:
            if isinstance(discountCode, dict):
                self.discountCode = Reference(**discountCode)
            else:
                self.discountCode = discountCode
        self.state = state
        self.oldState = oldState

    @property
    def state(self):
        return self._state

    @state.setter
    @ValidValues(_discountCodeState_types)
    def type(self, value):
        self._state = value

    @property
    def oldState(self):
        return self._oldState

    @oldState.setter
    @ValidValues(_discountCodeState_types)
    def oldState(self, value):
        self._oldState = value
    
    def toDict(self):
        d = super().toDict()
        if self._state is not None:
            d['state'] = self._state
        if self._oldState is not None:
            d['oldState'] = self._oldState
        return d
