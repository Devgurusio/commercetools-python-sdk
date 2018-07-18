from .basetype import BaseType
class Address(BaseType):
  id: str
  key: str
  title: str
  salutation: str
  firstName: str
  lastName: str
  streetName: str
  streetNumber: str
  additionalStreetInfo: str
  postalCode: str
  city: str
  region: str
  state: str
  country: str
  company: str
  department: str
  building: str
  apartment: str
  pOBox: str
  phone: str
  mobile: str
  email: str
  fax: str
  additionalAddressInfo: str
  externalId: str

  def __init__(self, country: str, id: str = None, key: str = None, title: str = None, salutation: str = None, firstName: str = None, lastName: str = None, streetName: str = None, 
    streetNumber: str = None, additionalStreetInfo: str = None, postalCode: str = None, city: str = None, region: str = None, state: str = None, company: str = None, department: str = None, building: str = None, apartment: str = None, 
    pOBox: str = None, phone: str = None, mobile: str = None, email: str = None, fax: str = None, additionalAddressInfo: str = None, externalId: str = None):
    self.id = id
    self.key = key
    self.salutation = salutation
    self.firstName = firstName
    self.lastName = lastName
    self.streetName = streetName
    self.streetNumber = streetNumber
    self.additionalStreetInfo = additionalStreetInfo
    self.postalCode = postalCode
    self.city = city
    self.region = region
    self.state = state
    self.country = country
    self.company = company
    self.department = department
    self.pOBox = pOBox
    self.phone = phone
    self.mobile = mobile
    self.email = email
    self.fax = fax
    self.additionalAddressInfo = additionalAddressInfo
    self.externalId = externalId