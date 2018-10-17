from .message import Message
from models.payment import Payment


class PaymentCreated(Message):
    type: 'PaymentCreated'
    payment: Payment

    def __init__(self, type: str = 'PaymentCreated', payment: Payment = None, **kwargs):
        super().__init__(**kwargs)
        if payment is not None:
            if isinstance(payment, dict):
                self.payment = Payment(**payment)
            else:
                self.payment = payment
