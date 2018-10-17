from .message import Message


class PaymentStatusInterfaceCodeSet(Message):
    type: 'PaymentStatusInterfaceCodeSet'
    interfaceCode: str

    def __init__(self, type: str = 'PaymentStatusInterfaceCodeSet', interfaceCode: str = None, **kwargs):
        super().__init__(**kwargs)
        self.interfaceCode = interfaceCode
