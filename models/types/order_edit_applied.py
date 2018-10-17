from .basetype import BaseType
from .order_excerpt import OrderExcerpt
from datetime import datetime


class OrderEditApplied(BaseType):
    type: str = "Applied"
    appliedAt: datetime
    excerptBeforeEdit: OrderExcerpt
    excerptAfterEdit: OrderExcerpt

    def __init__(self, type: str = "Applied", appliedAt: datetime = None, excerptBeforeEdit: OrderExcerpt = None, excerptAfterEdit: OrderExcerpt = None):
        self.appliedAt = appliedAt
        if excerptBeforeEdit is not None:
            if isinstance(excerptBeforeEdit, dict):
                self.excerptBeforeEdit = OrderExcerpt(**excerptBeforeEdit)
            else:
                self.excerptBeforeEdit = excerptBeforeEdit
        if excerptAfterEdit is not None:
            if isinstance(excerptAfterEdit, dict):
                self.excerptAfterEdit = OrderExcerpt(**excerptAfterEdit)
            else:
                self.excerptAfterEdit = excerptAfterEdit
