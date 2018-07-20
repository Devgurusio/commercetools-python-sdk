from .baseactions import BaseActions
from models.state import State
from deepdiff import DeepDiff
import re

# Order change actions (changeFieldDefinitionOrder, changeEnumValueOrder and changeLocalizedEnumValueOrder) will not be performed
class TypeActions(BaseActions):
  @classmethod
  def _get_diff(cls, old_obj: State, new_obj: State):
    return DeepDiff(old_obj, new_obj, ignore_order=True)
  
  @classmethod
  def _regular_attribute_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
      attr = root_attr.split('.')[1]
      if (attr == 'key'):
        actions.append({'action': 'changeKey', 'key': obj.key })
      elif (attr.startswith('name')):
        actions.append({'action': 'changeName', 'name': obj.name })
      elif (attr.startswith('description')):
          actions.append({'action': 'setDescription', 'description': obj.description })
      elif (attr.startswith('fieldDefinitions')):
        field = root_attr.split('.')[2]
        if (field == '_name'):
          actions.append({'action': 'removeFieldDefinition', 'fieldName': old_obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].name})
          actions.append({'action': 'addFieldDefinition', 'fieldDefinition': obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].toDict()})
    return actions
  
  @classmethod
  def _iterable_attribute_add_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
      attr = root_attr.split('.')[1]
      if (attr.__contains__('fieldDefinitions')):
        try:
          field = root_attr.split('.')[2]
          if field.__contains__("type['values']"):
            if obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].type['name'] == 'Enum':
              actions.append({'action': 'addEnumValue', 'fieldName': obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].name, 'value': diff[root_attr]})
            elif obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].type['name'] == 'LocalizedEnum':
              actions.append({'action': 'addLocalizedEnumValue', 'fieldName': obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].name, 'value': diff[root_attr]})
        except IndexError:
          actions.append({'action': 'addFieldDefinition', 'fieldDefinition': obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].toDict()})
    return actions
  
  @classmethod
  def _iterable_attribute_update_actions(cls, diff: dict, obj, old_obj):
    actions = []
    for root_attr in diff:
      attr = root_attr.split('.')[1]
      if (attr.__contains__('roles')):
        actions.append({'action': 'removeRoles', 'roles': [old_obj.roles[int(re.findall(r'[\d+]', attr)[0])]]})
        actions.append({'action': 'addRoles', 'roles': [obj.roles[int(re.findall(r'[\d+]', attr)[0])]]})
      elif (attr.__contains__('transitions')):
        actions.append({'action': 'setTransitions', 'transitions': [ transition.__dict__ for transition in obj.transitions ]})
    return actions

  @classmethod
  def _iterable_attribute_remove_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
      attr = root_attr.split('.')[1]
      if (attr.__contains__('fieldDefinitions')):
        actions.append({'action': 'removeFieldDefinition', 'fieldName': diff[root_attr].name })
    return actions
  
  @classmethod
  def _diccionary_attribute_add_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
      attr = root_attr.split('.')[1]
      if (attr.startswith('name')):
        actions.append({'action': 'changeName', 'name': obj.name })
      elif (attr.startswith('description')):
        actions.append({'action': 'setDescription', 'description': obj.description })
      elif (attr.startswith('fieldDefinitions')):
        field = root_attr.split('.')[2]
        if (field.startswith('label')):
          actions.append({'action': 'changeLabel', 'fieldName': obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].name, 'label': obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].label })
    return actions
  
  @classmethod
  def _diccionary_attribute_remove_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
      attr = root_attr.split('.')[1]
      if (attr.startswith('name')):
        actions.append({'action': 'changeName', 'name': obj.name })
      elif (attr.startswith('description')):
        actions.append({'action': 'setDescription', 'description': obj.description })
      elif (attr.startswith('fieldDefinitions')):
        field = root_attr.split('.')[2]
        if (field.startswith('label')):
          actions.append({'action': 'changeLabel', 'fieldName': obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].name, 'label': obj.fieldDefinitions[int(re.findall(r'[\d+]', attr)[0])].label })
    return actions