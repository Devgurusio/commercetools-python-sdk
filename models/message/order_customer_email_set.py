from .message import Message


class OrderCustomerEmailSet(Message):
    type: 'OrderCustomerEmailSet'
    email: str
    oldEmail: str

    def __init__(self, type: str = 'OrderCustomerEmailSet', email: str = None, oldEmail: str = None, **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.oldEmail = oldEmail
