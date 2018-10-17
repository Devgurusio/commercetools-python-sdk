from .message import Message
from models.types.custom_fields import CustomFields


class PaymentInteractionAdded(Message):
    type: 'PaymentInteractionAdded'
    interaction: CustomFields

    def __init__(self, type: str = 'PaymentInteractionAdded', interaction: CustomFields = None, **kwargs):
        super().__init__(**kwargs)
        if interaction is not None:
            if isinstance(interaction, dict):
                self.interaction = CustomFields(**interaction)
            else:
                self.interaction = interaction
