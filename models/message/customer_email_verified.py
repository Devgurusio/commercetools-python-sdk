from .message import Message


class CustomerEmailVerified(Message):
    type: 'CustomerEmailVerified'

    def __init__(self, type: str = 'CustomerEmailVerified', **kwargs):
        super().__init__(**kwargs)
