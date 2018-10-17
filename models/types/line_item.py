from .basetype import BaseType
from .reference import Reference
from .product_variant import ProductVariant
from .price import Price
from .taxed_item_price import TaxedItemPrice
from .money import Money
from .item_state import ItemState
from .tax_rate import TaxRate
from .discounted_line_item_price_for_quantity import DiscountedLineItemPriceForQuantity
from .custom_fields import CustomFields
from .item_shipping_details import ItemShippingDetails
from typing import Dict, List
from decorators.decorators import ValidValues


class LineItem(BaseType):
    id: str
    productId: str
    name: Dict
    productSlug: Dict
    productType: Reference
    variant: ProductVariant
    price: Price
    taxedPrice: TaxedItemPrice
    totalPrice: Money
    quantity: int
    state: List[ItemState]
    taxRate: TaxRate
    supplyChannel: Reference
    distributionChannel: Reference
    discountedPricePerQuantity: DiscountedLineItemPriceForQuantity
    _priceMode: str
    _lineItemMode: str
    custom: CustomFields
    shippingDetails: ItemShippingDetails

    _lineItemPriceMode_types = ['Platform', 'ExternalPrice', 'ExternalTotal']
    _lineItemMode_types = ['Standard', 'GiftLineItem']

    def __init__(self,
                 id: str = None,
                 productId: str = None,
                 name: dict = None,
                 productSlug: Dict = None,
                 productType: Reference = None,
                 variant: ProductVariant = None,
                 price: Price = None,
                 taxedPrice: TaxedItemPrice = None,
                 totalPrice: Money = None,
                 quantity: int = None,
                 state: List[ItemState] = None,
                 taxRate: TaxRate = None,
                 supplyChannel: Reference = None,
                 distributionChannel: Reference = None,
                 discountedPricePerQuantity: DiscountedLineItemPriceForQuantity = None,
                 priceMode: str = None,
                 lineItemMode: str = None,
                 custom: CustomFields = None,
                 shippingDetails: ItemShippingDetails = None):
        self.id = id
        self.productId = productId
        self.name = name
        self.productSlug = productSlug
        if isinstance(productType, dict):
            self.productType = Reference(**productType)
        else:
            self.variant = variant
        if isinstance(variant, dict):
            self.variant = ProductVariant(**variant)
        else:
            self.variant = variant
        if isinstance(price, dict):
            self.price = Money(**price)
        else:
            self.price = price
        if isinstance(taxedPrice, dict):
            self.taxedPrice = TaxedItemPrice(**taxedPrice)
        else:
            self.taxedPrice = taxedPrice
        if isinstance(totalPrice, dict):
            self.totalPrice = Money(**totalPrice)
        else:
            self.totalPrice = totalPrice
        self.quantity = quantity
        if state is not None:
            _state = []
            for itemState in state:
                if isinstance(itemState, dict):
                    _state.append(ItemState(**itemState))
                else:
                    _state.append(itemState)
            self.state = _state
        else:
            self.state = state
        if isinstance(taxRate, dict):
            self.taxRate = TaxRate(**taxRate)
        else:
            self.taxRate = taxRate
        if isinstance(productType, dict):
            self.productType = Reference(**productType)
        else:
            self.supplyChannel = supplyChannel
        if isinstance(supplyChannel, dict):
            self.supplyChannel = Reference(**supplyChannel)
        else:
            self.supplyChannel = supplyChannel
        if isinstance(distributionChannel, dict):
            self.distributionChannel = Reference(**distributionChannel)
        else:
            self.distributionChannel = distributionChannel
        if isinstance(discountedPricePerQuantity, dict):
            self.discountedPricePerQuantity = DiscountedLineItemPriceForQuantity(
                **discountedPricePerQuantity)
        else:
            self.discountedPricePerQuantity = discountedPricePerQuantity
        self.priceMode = priceMode
        self.lineItemMode = lineItemMode
        if isinstance(custom, dict):
            self.custom = CustomFields(**custom)
        else:
            self.custom = custom
        if isinstance(shippingDetails, dict):
            self.shippingDetails = ItemShippingDetails(**shippingDetails)
        else:
            self.shippingDetails = shippingDetails

    @property
    def priceMode(self):
        return self._priceMode

    @priceMode.setter
    @ValidValues(_lineItemPriceMode_types)
    def priceMode(self, value):
        self._priceMode = value

    @property
    def lineItemMode(self):
        return self._lineItemMode

    @lineItemMode.setter
    @ValidValues(_lineItemMode_types)
    def lineItemMode(self, value):
        self._lineItemMode = value

    def toDict(self):
        d = super().toDict()
        if self._priceMode is not None:
            d['priceMode'] = self._priceMode
        if self._lineItemMode is not None:
            d['lineItemMode'] = self._lineItemMode
        return d
