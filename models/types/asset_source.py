from .basetype import BaseType
from .asset_dimensions import AssetDimensions


class AssetSource(BaseType):
    uri: str
    key: str
    dimensions: AssetDimensions
    contentType: str

    def __init__(self, uri: str = None, key: str = None, dimensions: AssetDimensions = None, contentType: str = None):
        self.uri = uri
        self.key = key
        if dimensions is not None:
            if isinstance(dimensions, dict):
                self.dimensions = AssetDimensions(**dimensions)
            else:
                self.dimensions = dimensions
        self.contentType = contentType
