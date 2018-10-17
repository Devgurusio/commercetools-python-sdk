from .message import Message
from models.types.item_state import ItemState
from models.types.money import Money
from models.types.taxed_item_price import TaxedItemPrice
from models.types.price import Price
from models.types.item_shipping_details import ItemShippingDetails
from typing import List


class OrderLineItemRemoved(Message):
    type: 'OrderLineItemRemoved'
    lineItemId: str
    removedQuantity: int
    newQuantity: int
    newState: List[ItemState]
    newTotalPrice: Money
    newTaxedPrice: TaxedItemPrice
    newPrice: Price
    newShippingDetail: ItemShippingDetails

    def __init__(self, type: str = 'OrderLineItemRemoved', lineItemId: str = None, removedQuantity: int = None, newQuantity: int = None, newState: List[ItemState] = None, newTotalPrice: Money = None, newTaxedPrice: TaxedItemPrice = None, newPrice: Price = None, newShippingDetail: ItemShippingDetails = None, **kwargs):
        super().__init__(**kwargs)
        self.lineItemId = lineItemId
        self.removedQuantity = removedQuantity
        self.newQuantity = newQuantity
        if newState is not None:
            _newState = []
            for state in newState:
                if isinstance(state, dict):
                    _newState.append(ItemState(**state))
                else:
                    _newState.append(state)
            self.newState = _newState
        else:
            self.newState = newState
        if newTotalPrice is not None:
            if isinstance(newTotalPrice, dict):
                self.newTotalPrice = Money(**newTotalPrice)
            else:
                self.newTotalPrice = newTotalPrice
        if newTaxedPrice is not None:
            if isinstance(newTaxedPrice, dict):
                self.newTaxedPrice = TaxedItemPrice(**newTaxedPrice)
            else:
                self.newTaxedPrice = newTaxedPrice
        if newPrice is not None:
            if isinstance(newPrice, dict):
                self.newPrice = Price(**newPrice)
            else:
                self.newPrice = newPrice
        if newShippingDetail is not None:
            if isinstance(newShippingDetail, dict):
                self.newShippingDetail = ItemShippingDetails(
                    **newShippingDetail)
            else:
                self.newShippingDetail = newShippingDetail
