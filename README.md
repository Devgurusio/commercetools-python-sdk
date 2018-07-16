This SDK provides an ORM to work with the [commercetools platform](http://www.commercetools.com/) (formerly SPHERE.IO) rather than using plain HTTP calls.
Note that this library is under development now and it is not yet completely finished, so it not production ready at all.

## Requirements
* Ptyhon 3.6 or higher (https://www.python.org/downloads/)

## How to use it

### Create client
The first step is create a client to communicate with sphere.io
```
from commercetools.connection.client import Client

project_key = r'MY_PROJECT_KEY'
client_id = r'MY_CLIENT_ID'
client_secret = r'MY_CLIENT_SECRET'
auth_uri = 'https://auth.commercetools.co'
api_uri = 'https://api.commercetools.co'

# connect to CT
client = Client(project_key, client_id, client_secret, auth_uri, api_uri)
```

### Working with repositories 
Once we have create the client, we can instantiate the repository we want to work with.
```
from commercetools.repositories.customer import CustomerRepository

customer_repository = CustomerRepository(client)
```

Every repository provides a factory to instantiate a new model and all CRUD methods.
```
# Create a new customer
customer = customer_repository.new(key='testingcustomer', email='testingcustomer@domain.com', password='mypassword')
customer_repository.create(customer)

# Find a customer by key
testingcustomer = customer_repository.get(key='testingcustomer')

# Update a customer
testingcustomer.firstName = 'Myname'
customer_repoisitory.update(testingcustomer, old_obj=customer, force=True)
# if the old customer is not provided (second parameter), the update method will peform an find and update
# force parameter handles concurrent modification errors. Note that by default this attribute is set to false.

# Delete a customer
customer_repository(testingcustomer, force=True)
```

Alternatively we can work with models as an active record class
```
# Create a new customer (alternative mode)
customer = customer_repository.new(key='testingcustomer', email='testingcustomer@domain.com', password='mypassword')
customer.save()

# Find a customer by key
customer = customer_repository.get(key='testingcustomer')

# Update a customer
testingcustomer.firstName = 'Myname'
testingcustomer.save(force=True)

# Delete a customer
testingcustomer.delete(force=True)
```

### Helpers
Some resources, such as Carts, Customers, Orders, etc. has their own helpers classes that provides some actions out of the scope of a repository.
```
from commercetools.helpers.customer import CustomerHelper

customer_helper = CustomerHelper(client)

# authenticate a customer
customersigninresult = customer_helper.login(email='fede+test2@devgurus.io', password='mypassword')

# verify customer e-mail
token = customer_helper.get_verify_email_token(obj=customersigninresult.customer, ttlMinutes=10)
customer = customer_helper.verify_email(token.value)
```
