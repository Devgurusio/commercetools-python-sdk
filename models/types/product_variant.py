from .basetype import BaseType
from .price import Price
from .attribute import Attribute
from .image import Image
from .asset import Asset
from .product_variant_availability import ProductVariantAvailability
from .scoped_price import ScopedPrice
from typing import List


class ProductVariant(BaseType):
    id: str
    sku: str
    key: str
    prices: List[Price]
    attributes: List[Attribute]
    price: Price
    images: List[Image]
    assets: List[Asset]
    availability: ProductVariantAvailability
    isMatchingVariant: bool
    scopedPrice: ScopedPrice
    scopedPriceDiscounted: bool

    def __init__(self, id: str = None, sku: str = None, key: str = None, prices: List[Price] = None, attributes: List[Attribute] = None, price: Price = None, images: List[Image] = None, assets: List[Asset] = None, availability: ProductVariantAvailability = None, isMatchingVariant: bool = None, scopedPrice: ScopedPrice = None, scopedPriceDiscounted: bool = None):
        self.id = id
        self.sku = sku
        self.key = key
        if prices is not None:
            _prices = []
            for price in prices:
                if isinstance(price, dict):
                    _prices.append(Price(**price))
                else:
                    _prices.append(price)
            self.prices = _prices
        else:
            self.prices = prices
        if attributes is not None:
            _attributes = []
            for attribute in attributes:
                if isinstance(attribute, dict):
                    _attributes.append(Attribute(**attribute))
                else:
                    _attributes.append(attribute)
            self.attributes = _attributes
        else:
            self.attributes = attributes
        if price is not None:
            if isinstance(price, dict):
                self.price = Price(**price)
            else:
                self.price = price
        if images is not None:
            _images = []
            for image in images:
                if isinstance(image, dict):
                    _images.append(Image(**image))
                else:
                    _images.append(image)
            self.images = _images
        else:
            self.images = images
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
        if availability is not None:
            if isinstance(availability, dict):
                self.availability = ProductVariantAvailability(**availability)
            else:
                self.availability = availability
        self.isMatchingVariant = isMatchingVariant
        if scopedPrice is not None:
            if isinstance(scopedPrice, dict):
                self.scopedPrice = ScopedPrice(**scopedPrice)
            else:
                self.scopedPrice = scopedPrice
        self.scopedPriceDiscounted = scopedPriceDiscounted
