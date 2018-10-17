from .message import Message
from models.types.reference import Reference


class ProductStateTransition(Message):
    type: 'ProductStateTransition'
    state: Reference
    force: bool

    def __init__(self, type: str = 'ProductStateTransition', state: Reference = None, force: bool = None, **kwargs):
        super().__init__(**kwargs)
        if state is not None:
            if isinstance(state, dict):
                self.state = Reference(**state)
            else:
                self.state = state
        self.force = force
