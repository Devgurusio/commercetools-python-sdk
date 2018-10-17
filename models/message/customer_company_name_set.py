from .message import Message


class CustomerCompanyNameSet(Message):
    type: 'CustomerCompanyNameSet'
    companyName: str

    def __init__(self, type: str = 'CustomerCompanyNameSet', companyName: str = None, **kwargs):
        super().__init__(**kwargs)
        self.companyName = companyName
