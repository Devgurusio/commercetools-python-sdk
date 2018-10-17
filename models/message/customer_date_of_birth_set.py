from .message import Message
from datetime import date


class CustomerDateOfBirthSet(Message):
    type: 'CustomerDateOfBirthSet'
    dateOfBirth: date

    def __init__(self, type: str = 'CustomerDateOfBirthSet', dateOfBirth: date = None, **kwargs):
        super().__init__(**kwargs)
        self.dateOfBirth = dateOfBirth
