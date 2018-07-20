from .baserepository import BaseRepository
from factories.tax_category import TaxCategoryFactory
from .actions.tax_category import TaxCategoryActions


class TaxCategoryRepository(BaseRepository):
    _endpoint = 'tax-categories'
    _factory = TaxCategoryFactory
    _actions_module = TaxCategoryActions
