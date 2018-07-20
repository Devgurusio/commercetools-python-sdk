from .baseactions import BaseActions
from models.customer import Customer
import re

class CustomerActions(BaseActions):
  @classmethod
  def _regular_attribute_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
        attr = root_attr.split('.')[1]
        if (attr == 'email'):
          actions.append({'action': 'changeEmail', 'email': obj.email })
        elif (attr == 'firstName'):
          actions.append({'action': 'setFirstName', 'firstName': obj.firstName })
        elif (attr == 'lastName'):
          actions.append({'action': 'setLastName', 'lastName': obj.lastName })
        elif (attr == 'middleName'):
          actions.append({'action': 'setMiddleName', 'middleName': obj.middleName })
        elif (attr == 'title'):
          actions.append({'action': 'setTitle', 'title': obj.title })
        elif (attr == 'salutation'):
          actions.append({'action': 'setSalutation', 'salutation': obj.salutation })
    return actions
  
  @classmethod
  def _iterable_attribute_add_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
        attr = root_attr.split('.')[1]
        if (attr.__contains__('addresses')):
          actions.append({'action': 'addAddress', 'address': diff[root_attr].__dict__ })
    return actions
  
  @classmethod
  def _iterable_attribute_update_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
        attr = root_attr.split('.')[1]
        if (attr.__contains__('addresses')):
          actions.append({'action': 'changeAddress', 'addressId': obj.addresses[int(re.findall(r'[\d+]', attr)[0])].id, 'address': obj.addresses[int(re.findall(r'[\d+]', attr)[0])].__dict__ })
    return actions

  @classmethod
  def _iterable_attribute_remove_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
        attr = root_attr.split('.')[1]
        if (attr.__contains__('addresses')):
          actions.append({'action': 'removeAddress', 'addressId': diff[root_attr].id })
    return actions