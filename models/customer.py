from .basemodel import BaseModel
from .customer_group import CustomerGroup
from .types.address import Address
from .types.reference import Reference
from datetime import datetime
from decorators.models import ModelPersisted, ModelRepository
from typing import List


class Customer(BaseModel):
    customerNumber: str
    key: str
    email: str
    password: str
    firstName: str
    lastName: str
    middleName: str
    title: str
    salutation: str
    dateOfBirth: datetime
    companyName: str
    vatId: str
    addresses: List[Address]
    defaultShippingAddressId: str
    shippingAddressIds: List[str]
    defaultBillingAddressId: str
    billingAddressIds: List[str]
    isEmailVerified: bool
    externalId: str
    customerGroup: Reference
    # custom - CustomFields - Optional
    locale: str
    lastMessageSequenceNumber: int

    def __init__(self, customerNumber: str = None, key: str = None, email: str = None, password: str = None, firstName: str = None, lastName: str = None, middleName: str = None, title: str = None, salutation: str = None,
                 dateOfBirth: datetime = None, companyName: str = None, vatId: str = None, addresses: List[Address] = None, defaultShippingAddressId: str = None, shippingAddressIds: List[str] = None, defaultBillingAddressId: str = None,
                 billingAddressIds: List[str] = None, isEmailVerified: bool = None, externalId: str = None, customerGroup: Reference = None, custom=None, locale: str = None, lastMessageSequenceNumber: int = None, **kwargs):
        super().__init__(**kwargs)
        self.customerNumber = customerNumber
        self.key = key
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        self.title = title
        self.salutation = salutation
        self.dateOfBirth = dateOfBirth
        self.companyName = companyName
        self.vatId = vatId
        if addresses is not None:
            _addresses = []
            for addr in addresses:
                if isinstance(addr, dict):
                    _addresses.append(Address(**addr))
                else:
                    _addresses.append(addr)
            self.addresses = _addresses
        else:
            self.addresses = addresses
        self.defaultShippingAddressId = defaultShippingAddressId
        self.shippingAddressIds = shippingAddressIds
        self.defaultBillingAddressId = defaultBillingAddressId
        self.billingAddressIds = billingAddressIds
        self.isEmailVerified = isEmailVerified
        self.externalId = externalId
        if customerGroup is not None:
            if isinstance(customerGroup, dict):
                self.customerGroup = Reference(**customerGroup)
            else:
                self.customerGroup = customerGroup
        # self.custom = custom
        self.locale = locale
        self.lastMessageSequenceNumber = lastMessageSequenceNumber

    @ModelPersisted()
    def change_password(self, current_password: str, new_password: str, force=False):
        self.__dict__.update(self._repository.change_password(
            current_password=current_password, new_password=new_password, obj=self, force=force).__dict__)
        return self

    @ModelRepository()
    def save(self, force=False):
        if self.id is None:
            customerSigninResult = self._repository.create(self)
            self.__dict__.update(customerSigninResult.customer.__dict__)
        else:
            self.__dict__.update(self._repository.update(
                self, force=force).__dict__)
        return self
