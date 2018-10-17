from .basetype import BaseType
from .asset_source import AssetSource
from .custom_fields import CustomFields
from typing import Dict, List


class Asset(BaseType):
    id: str
    key: str
    sources: List[AssetSource]
    name: Dict
    description: Dict
    tags: List[str]
    custom: CustomFields

    def __init__(self, id: str = None, key: str = None, sources: List[AssetSource] = None, name: Dict = None, description: Dict = None, tags: List[str] = None, custom: CustomFields = None):
        self.id = id
        self.key = key
        if sources is not None:
            _sources = []
            for source in sources:
                if isinstance(source, dict):
                    _sources.append(AssetSource(**source))
                else:
                    _sources.append(source)
            self.sources = _sources
        else:
            self.sources = sources
        self.name = name
        self.description = description
        self.tags = tags
        if custom is not None:
            if isinstance(custom, dict):
                self.custom = CustomFields(**custom)
            else:
                self.custom = custom
