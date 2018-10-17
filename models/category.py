from .basemodel import BaseModel
from .types.reference import Reference
from .types.custom_fields import CustomFields
from .types.asset import Asset
from typing import Dict, List


class Category(BaseModel):
    key: str
    name: Dict
    slug: Dict
    description: Dict
    ancestors: List[Reference]
    parent: Reference
    orderHint: str
    externalId: str
    metaTitle: Dict
    metaDescription: Dict
    metaKeywords: Dict
    custom: CustomFields
    assets: List[Asset]

    def __init__(self, key: str = None, name: Dict = None, slug: Dict = None, description: Dict = None, ancestors: List[Reference] = None, parent: Reference = None, orderHint: str = None, externalId: str = None, metaTitle: Dict = None, metaDescription: Dict = None, metaKeywords: Dict = None, custom: CustomFields = None, assets: List[Asset] = None, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.name = name
        self.slug = slug
        self.description = description
        if ancestors is not None:
            _ancestors = []
            for ancestor in ancestors:
                if isinstance(ancestor, dict):
                    _ancestors.append(Reference(**ancestor))
                else:
                    _ancestors.append(ancestor)
            self.ancestors = _ancestors
        else:
            self.ancestors = ancestors
        if parent is not None:
            if isinstance(parent, dict):
                self.parent = Reference(**parent)
            else:
                self.parent = parent
        self.orderHint = orderHint
        self.externalId = externalId
        self.metaTitle = metaTitle
        self.metaDescription = metaDescription
        self.metaKeywords = metaKeywords
        if custom is not None:
            if isinstance(custom, dict):
                self.custom = CustomFields(**custom)
            else:
                self.custom = custom
        if assets is not None:
            _assets = []
            for asset in assets:
                if isinstance(asset, dict):
                    _assets.append(Asset(**asset))
                else:
                    _assets.append(asset)
            self.assets = _assets
        else:
            self.assets = assets
