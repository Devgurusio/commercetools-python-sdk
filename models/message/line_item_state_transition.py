from .message import Message
from models.types.reference import Reference
from datetime import datetime


class LineItemStateTransition(Message):
    type: 'LineItemStateTransition'
    lineItemId: str
    transitionDate: datetime
    quantity: int
    fromState: Reference
    toState: Reference

    def __init__(self, type: str = 'LineItemStateTransition', lineItemId: int = None, transitionDate: datetime = None, quantity: int = None, fromState: Reference = None, toState: Reference = None, **kwargs):
        super().__init__(**kwargs)
        # self.type = type
        self.lineItemId = lineItemId
        self.transitionDate = transitionDate
        self.quantity = quantity
        if fromState is not None:
            if isinstance(fromState, dict):
                self.fromState = Reference(**fromState)
            else:
                self.fromState = fromState
        if toState is not None:
            if isinstance(toState, dict):
                self.toState = Reference(**toState)
            else:
                self.toState = toState
