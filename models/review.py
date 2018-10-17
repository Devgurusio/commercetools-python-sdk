from .basemodel import BaseModel
from .types.reference import Reference
from .types.custom_fields import CustomFields


class Review(BaseModel):
    key: str
    uniquenessValue: str
    locale: str
    authorName: str
    title: str
    text: str
    target: Reference
    rating: int
    state: Reference
    includedInStatistics: bool
    customer: Reference
    custom: CustomFields

    def __init__(self, key: str = None, uniquenessValue: str = None, locale: str = None, authorName: str = None, title: str = None, text: str = None, target: Reference = None, rating: int = None, state: Reference = None, includedInStatistics: bool = None, customer: Reference = None, custom: CustomFields = None, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.uniquenessValue = uniquenessValue
        self.locale = locale
        self.authorName = authorName
        self.title = title
        self.text = text
        if target is not None:
            if isinstance(target, dict):
                self.target = Reference(**target)
            else:
                self.target = target
        self.rating = rating
        if state is not None:
            if isinstance(state, dict):
                self.state = Reference(**state)
            else:
                self.state = state
        self.includedInStatistics = includedInStatistics
        if customer is not None:
            if isinstance(customer, dict):
                self.customer = Reference(**customer)
            else:
                self.customer = customer
        if customer is not None:
            if isinstance(customer, dict):
                self.customer = Reference(**customer)
            else:
                self.customer = customer
        if custom is not None:
            if isinstance(custom, dict):
                self.custom = CustomFields(**custom)
            else:
                self.custom = custom
