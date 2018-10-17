from .basemodel import BaseModel
from .types.reference import Reference
from .types.search_keyword import SearchKeyword
from .types.product_variant import ProductVariant
from .types.review_rating_statistics import ReviewRatingStatistics
from typing import Dict, List


class ProductProjection(BaseModel):
    key: str
    productType: Reference
    name: Dict
    description: Dict
    slug: Dict
    categories: List[Reference]
    categoryOrderHints: Dict[str, float]
    metaTitle: Dict
    metaDescription: Dict
    metaKeywords: Dict
    searchKeywords: Dict[str, List[SearchKeyword]]
    hasStagedChanges: bool
    published: bool
    masterVariant: ProductVariant
    variants: List[ProductVariant]
    taxCategory: Reference
    state: Reference
    reviewRatingStatistics: ReviewRatingStatistics

    def __init__(self, key: str = None, productType: Reference = None, name: Dict = None, description: Dict = None, slug: Dict = None, categories: List[Reference] = None, categoryOrderHints: Dict[str, float] = None, metaTitle: Dict = None, metaDescription: Dict = None, metaKeywords: Dict = None, searchKeywords: Dict[str, List[SearchKeyword]] = None, hasStagedChanges: bool = None, published: bool = None, masterVariant: ProductVariant = None, variants: List[ProductVariant] = None, taxCategory: Reference = None, state: Reference = None, reviewRatingStatistics: ReviewRatingStatistics = None, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        if productType is not None:
            if isinstance(productType, dict):
                self.productType = Reference(**productType)
            else:
                self.productType = productType
        self.name = name
        self.description = description
        self.slug = slug
        self.categories = categories
        self.categoryOrderHints = categoryOrderHints
        self.metaTitle = metaTitle
        self.metaDescription = metaDescription
        self.metaKeywords = metaKeywords
        if searchKeywords is not None:
            _searchKeywords = {}
            for lang, searchKeywordList in searchKeywords.items():
                if searchKeywordList is not None:
                    _searchKeywordList = []
                    for searchKeyword in searchKeywordList:
                        if isinstance(searchKeyword, dict):
                            _searchKeywordList.append(
                                SearchKeyword(**searchKeyword))
                        else:
                            _searchKeywordList.append(searchKeyword)
                    _searchKeywords.__setitem__(lang, _searchKeywordList)
                else:
                    _searchKeywords.__setitem__(lang, searchKeywordList)
            self.searchKeywords = _searchKeywords
        else:
            self.searchKeywords = searchKeywords
        self.hasStagedChanges = hasStagedChanges
        self.published = published
        if masterVariant is not None:
            if isinstance(masterVariant, dict):
                self.masterVariant = ProductVariant(**masterVariant)
            else:
                self.masterVariant = masterVariant
        if variants is not None:
            _variants = []
            for variant in variants:
                if isinstance(variant, dict):
                    _variants.append(ProductVariant(**variant))
                else:
                    _variants.append(variant)
            self.variants = _variants
        else:
            self.variants = variants
        if taxCategory is not None:
            if isinstance(taxCategory, dict):
                self.taxCategory = Reference(**taxCategory)
            else:
                self.taxCategory = taxCategory
        if state is not None:
            if isinstance(state, dict):
                self.state = Reference(**state)
            else:
                self.state = state
        if reviewRatingStatistics is not None:
            if isinstance(reviewRatingStatistics, dict):
                self.reviewRatingStatistics = ReviewRatingStatistics(
                    **reviewRatingStatistics)
            else:
                self.reviewRatingStatistics = reviewRatingStatistics
