from .message import Message
from models.types.transaction import Transaction


class PaymentTransactionAdded(Message):
    type: 'PaymentTransactionAdded'
    transaction: Transaction

    def __init__(self, type: str = 'PaymentTransactionAdded', transaction: Transaction = None, **kwargs):
        super().__init__(**kwargs)
        if transaction is not None:
            if isinstance(transaction, dict):
                self.transaction = Transaction(**transaction)
            else:
                self.transaction = transaction
