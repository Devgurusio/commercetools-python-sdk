from models.customer import Customer

class CustomerSignInResult:
  customer : Customer
  #cart

  def __init__(self, customer: Customer, cart = None, repository = None):
    self.customer = Customer(_repository=repository, **customer)

  def __str__(self):
    return vars(self).__str__()