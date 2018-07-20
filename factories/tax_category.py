from models.tax_category import TaxCategory
from .basefactory import BaseFactory


class TaxCategoryFactory(BaseFactory):
    _model = TaxCategory
