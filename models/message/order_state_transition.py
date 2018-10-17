from .message import Message
from models.types.reference import Reference


class OrderStateTransition(Message):
    type: 'OrderStateTransition'
    state: Reference
    force: bool

    def __init__(self, type: str = 'OrderStateTransition', state: Reference = None, force: bool = None, **kwargs):
        super().__init__(**kwargs)
        if state is not None:
            if isinstance(state, dict):
                self.state = Reference(**state)
            else:
                self.state = state
        self.force = force
