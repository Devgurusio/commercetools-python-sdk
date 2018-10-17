from .message import Message
from models.types.reference import Reference
from models.types.order_edit_applied import OrderEditApplied as OrderEditAppliedType


class OrderEditApplied(Message):
    type: 'OrderEditApplied'
    edit: Reference
    result: OrderEditAppliedType

    def __init__(self, type: str = 'OrderEditApplied', edit: Reference = None, result: OrderEditAppliedType = None, **kwargs):
        super().__init__(**kwargs)
        if edit is not None:
            if isinstance(edit, dict):
                self.edit = Reference(**edit)
            else:
                self.edit = edit
        if result is not None:
            if isinstance(result, dict):
                self.result = OrderEditAppliedType(**result)
            else:
                self.result = result
