from .basemodel import BaseModel
from .types.line_item import LineItem
from .types.custom_line_item import CustomLineItem
from .types.money import Money
from .types.taxed_price import TaxedPrice
from .types.address import Address
from .types.reference import Reference
from .types.shipping_info import ShippingInfo
from .types.sync_info import SyncInfo
from .types.return_info import ReturnInfo
from .types.discount_code_info import DiscountCodeInfo
from .types.custom_fields import CustomFields
from .types.payment_info import PaymentInfo
from .types.shipping_rate_input import ShippingRateInput
from datetime import datetime
from typing import List
from decorators.decorators import ValidValues


class Order(BaseModel):
    completedAt: datetime
    orderNumber: str
    customerId: str
    customerEmail: str
    anonymousId: str
    lineItems: List[LineItem]
    customLineItems: List[CustomLineItem]
    totalPrice: Money
    taxedPrice: TaxedPrice
    shippingAddress: Address
    billingAddress: Address
    _taxMode: str
    _taxRoundingMode: str
    _taxCalculationMode: str
    customerGroup: Reference
    country: str
    _orderState: str
    state: Reference
    _shipmentState: str
    _paymentState: str
    shippingInfo: ShippingInfo
    syncInfo: SyncInfo
    returnInfo: ReturnInfo
    discountCodes: List[DiscountCodeInfo]
    refusedGifts: List[Reference]
    lastMessageSequenceNumber: int
    cart: Reference
    custom: CustomFields
    paymentInfo: PaymentInfo
    locale: str
    _inventoryMode: str
    shippingRateInput: ShippingRateInput
    _origin: str
    itemShippingAddresses: List[Address]

    _taxMode_types = ['Platform', 'External', 'ExternalAmount', 'Disabled']
    _roundingMode_types = ['HalfEven', 'HalfUp', 'HalfDown']
    _taxCalculationMode_types = ['LineItemLevel', 'UnitPriceLevel']
    _orderState_types = ['Open', 'Confirmed', 'Complete', 'Cancelled']
    _shipmentState_types = ['Shipped', 'Ready',
                            'Pending', 'Delayed', 'Partial', 'Backorder']
    _paymentState_types = ['BalanceDue',
                           'Failed', 'Pending', 'CreditOwed', 'Paid']
    _inventoryMode_types = ['TrackOnly', 'ReserveOnOrder', 'None']
    _cartOrigin_types = ['Customer', 'Merchant']

    def __init__(self, completedAt: datetime = None, orderNumber: str = None, customerId: str = None, customerEmail: str = None, anonymousId: str = None, lineItems: List[LineItem] = None, customLineItems: List[CustomLineItem] = None, totalPrice: Money = None, taxedPrice: TaxedPrice = None, shippingAddress: Address = None, billingAddress: Address = None, taxMode: str = None, taxRoundingMode: str = None, taxCalculationMode: str = None, customerGroup: Reference = None, country: str = None, orderState: str = None, state: Reference = None, shipmentState: str = None, paymentState: str = None, shippingInfo: ShippingInfo = None, syncInfo: SyncInfo = None, returnInfo: ReturnInfo = None, discountCodes: List[DiscountCodeInfo] = None, refusedGifts: List[Reference] = None, lastMessageSequenceNumber: int = None, cart: Reference = None, custom: CustomFields = None, paymentInfo: PaymentInfo = None, locale: str = None, inventoryMode: str = None, shippingRateInput: ShippingRateInput = None, origin: str = None, itemShippingAddresses: List[Address] = None, **kwargs):
        super().__init__(**kwargs)
        self.completedAt = completedAt
        self.orderNumber = orderNumber
        self.customerId = customerId
        self.customerEmail = customerEmail
        self.anonymousId = anonymousId
        if lineItems is not None:
            _lineItems = []
            for lineItem in lineItems:
                if isinstance(lineItem, dict):
                    _lineItems.append(LineItem(**lineItem))
                else:
                    _lineItems.append(lineItem)
            self.lineItems = _lineItems
        else:
            self.lineItems = lineItems
        if customLineItems is not None:
            _customLineItems = []
            for customLineItem in customLineItems:
                if isinstance(customLineItem, dict):
                    _customLineItems.append(CustomLineItem(**customLineItem))
                else:
                    _customLineItems.append(customLineItem)
            self.customLineItems = _customLineItems
        else:
            self.customLineItems = customLineItems
        if totalPrice is not None:
            if isinstance(totalPrice, dict):
                self.totalPrice = Price(**totalPrice)
            else:
                self.totalPrice = totalPrice
        if taxedPrice is not None:
            if isinstance(taxedPrice, dict):
                self.taxedPrice = TaxedPrice(**taxedPrice)
            else:
                self.taxedPrice = taxedPrice
        if shippingAddress is not None:
            if isinstance(shippingAddress, dict):
                self.shippingAddress = Address(**shippingAddress)
            else:
                self.shippingAddress = shippingAddress
        if billingAddress is not None:
            if isinstance(billingAddress, dict):
                self.billingAddress = Address(**billingAddress)
            else:
                self.billingAddress = billingAddress
        self.taxMode = taxMode
        self.taxRoundingMode = taxRoundingMode
        self.taxCalculationMode = taxCalculationMode
        if customerGroup is not None:
            if isinstance(customerGroup, dict):
                self.customerGroup = Reference(**customerGroup)
            else:
                self.customerGroup = customerGroup
        self.country = country
        self.orderState = orderState
        if state is not None:
            if isinstance(state, dict):
                self.state = Reference(**state)
            else:
                self.state = state
        self.shipmentState = shipmentState
        self.paymentState = paymentState
        if shippingInfo is not None:
            if isinstance(shippingInfo, dict):
                self.shippingInfo = ShippingInfo(**shippingInfo)
            else:
                self.shippingInfo = shippingInfo
        if syncInfo is not None:
            if isinstance(syncInfo, dict):
                self.syncInfo = SyncInfo(**syncInfo)
            else:
                self.syncInfo = syncInfo
        if returnInfo is not None:
            if isinstance(returnInfo, dict):
                self.returnInfo = ReturnInfo(**returnInfo)
            else:
                self.returnInfo = returnInfo
        if discountCodes is not None:
            _discountCodes = []
            for discountCode in discountCodes:
                if isinstance(discountCode, dict):
                    _discountCodes.append(DiscountCodeInfo(**discountCode))
                else:
                    _discountCodes.append(discountCode)
            self.discountCodes = _discountCodes
        else:
            self.discountCodes = discountCodes
        if refusedGifts is not None:
            _refusedGifts = []
            for refusedGift in refusedGifts:
                if isinstance(refusedGift, dict):
                    _refusedGifts.append(Reference(**refusedGift))
                else:
                    _refusedGifts.append(refusedGift)
            self.refusedGifts = _refusedGifts
        else:
            self.refusedGifts = refusedGifts
        self.lastMessageSequenceNumber = lastMessageSequenceNumber
        if cart is not None:
            if isinstance(cart, dict):
                self.cart = Reference(**cart)
            else:
                self.cart = cart
        if custom is not None:
            if isinstance(custom, dict):
                self.custom = CustomFields(**custom)
            else:
                self.custom = custom
        if paymentInfo is not None:
            if isinstance(paymentInfo, dict):
                self.paymentInfo = PaymentInfo(**paymentInfo)
            else:
                self.paymentInfo = paymentInfo
        self.locale = locale
        self.inventoryMode = inventoryMode
        if shippingRateInput is not None:
            if isinstance(shippingRateInput, dict):
                self.shippingRateInput = ShippingRateInput(**shippingRateInput)
            else:
                self.shippingRateInput = shippingRateInput
        self.origin = origin
        if itemShippingAddresses is not None:
            _itemShippingAddresses = []
            for itemShippingAddress in itemShippingAddresses:
                if isinstance(itemShippingAddress, dict):
                    _itemShippingAddresses.append(
                        Address(**itemShippingAddress))
                else:
                    _itemShippingAddresses.append(itemShippingAddress)
            self.itemShippingAddresses = _itemShippingAddresses
        else:
            self.itemShippingAddresses = itemShippingAddresses

    @property
    def taxMode(self):
        return self._taxMode

    @taxMode.setter
    @ValidValues(_taxMode_types)
    def taxMode(self, value):
        self._taxMode = value

    @property
    def taxRoundingMode(self):
        return self._taxRoundingMode

    @taxRoundingMode.setter
    @ValidValues(_roundingMode_types)
    def taxRoundingMode(self, value):
        self._taxRoundingMode = value

    @property
    def taxCalculationMode(self):
        return self._taxCalculationMode

    @taxCalculationMode.setter
    @ValidValues(_taxCalculationMode_types)
    def taxCalculationMode(self, value):
        self._taxCalculationMode = value

    @property
    def orderState(self):
        return self._orderState

    @orderState.setter
    @ValidValues(_orderState_types)
    def orderState(self, value):
        self._orderState = value

    @property
    def shipmentState(self):
        return self._shipmentState

    @shipmentState.setter
    @ValidValues(_shipmentState_types)
    def shipmentState(self, value):
        self._shipmentState = value

    @property
    def paymentState(self):
        return self._paymentState

    @paymentState.setter
    @ValidValues(_paymentState_types)
    def paymentState(self, value):
        self._paymentState = value

    @property
    def inventoryMode(self):
        return self._inventoryMode

    @inventoryMode.setter
    @ValidValues(_inventoryMode_types)
    def inventoryMode(self, value):
        self._inventoryMode = value

    @property
    def origin(self):
        return self._origin

    @origin.setter
    @ValidValues(_cartOrigin_types)
    def origin(self, value):
        self._origin = value

    def toDict(self):
        d = super().toDict()
        if self._taxMode is not None:
            d['taxMode'] = self._taxMode
        if self._taxRoundingMode is not None:
            d['taxRoundingMode'] = self._taxRoundingMode
        if self._taxCalculationMode is not None:
            d['taxCalculationMode'] = self._taxCalculationMode
        if self._orderState is not None:
            d['orderState'] = self._orderState
        if self._shipmentState is not None:
            d['shipmentState'] = self._shipmentState
        if self._paymentState is not None:
            d['paymentState'] = self._paymentState
        if self._inventoryMode is not None:
            d['inventoryMode'] = self._inventoryMode
        if self._origin is not None:
            d['origin'] = self._origin
        return d
