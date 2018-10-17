from .basetype import BaseType
from .money import Money
from .taxed_item_price import TaxedItemPrice
from .item_state import ItemState
from .reference import Reference
from .tax_rate import TaxRate
from .discounted_line_item_price_for_quantity import DiscountedLineItemPriceForQuantity
from .custom_fields import CustomFields
from .item_shipping_details import ItemShippingDetails
from typing import Dict, List


class CustomLineItem(BaseType):
    id: str
    name: Dict
    money: Money
    taxedPrice: TaxedItemPrice
    totalPrice: Money
    slug: str
    quantity: int
    state: List[ItemState]
    taxCategory: Reference
    taxRate: TaxRate
    discountedPricePerQuantity: DiscountedLineItemPriceForQuantity
    custom: CustomFields
    shippingDetails: ItemShippingDetails

    def __init__(self, id: str = None, name: dict = None, money: Money = None, taxedPrice: TaxedItemPrice = None, totalPrice: Money = None, slug: str = None, quantity: int = None, state: List[ItemState] = None, taxCategory: Reference = None, taxRate: TaxRate = None, discountedPricePerQuantity: DiscountedLineItemPriceForQuantity = None, custom: CustomFields = None, shippingDetails: ItemShippingDetails = None):
        self.id = id
        self.name = name
        if isinstance(money, dict):
            self.money = Money(**money)
        else:
            self.money = money
        if isinstance(taxedPrice, dict):
            self.taxedPrice = TaxedItemPrice(**taxedPrice)
        else:
            self.taxedPrice = taxedPrice
        if isinstance(totalPrice, dict):
            self.totalPrice = Money(**totalPrice)
        else:
            self.totalPrice = totalPrice
        self.slug = slug
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
        if isinstance(taxCategory, dict):
            self.taxCategory = Reference(**taxCategory)
        else:
            self.taxCategory = taxCategory
        if isinstance(taxRate, dict):
            self.taxRate = TaxRate(**taxRate)
        else:
            self.taxRate = taxRate
        if isinstance(discountedPricePerQuantity, dict):
            self.discountedPricePerQuantity = DiscountedLineItemPriceForQuantity(
                **discountedPricePerQuantity)
        else:
            self.discountedPricePerQuantity = discountedPricePerQuantity
        if isinstance(custom, dict):
            self.custom = CustomFields(**custom)
        else:
            self.custom = custom
        if isinstance(shippingDetails, dict):
            self.shippingDetails = ItemShippingDetails(**shippingDetails)
        else:
            self.shippingDetails = shippingDetails
