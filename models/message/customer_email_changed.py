from .message import Message


class CustomerEmailChanged(Message):
    type: 'CustomerEmailChanged'
    email: str

    def __init__(self, type: str = 'CustomerEmailChanged', email: str = None, **kwargs):
        super().__init__(**kwargs)
        self.email = email
