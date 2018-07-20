from .baseactions import BaseActions
from models.state import State
import re

class StateActions(BaseActions):
  @classmethod
  def _regular_attribute_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
      attr = root_attr.split('.')[1]
      if (attr == 'key'):
        actions.append({'action': 'changeKey', 'key': obj.key })
      elif (attr == '_type'):
        actions.append({'action': 'changeType', 'type': obj.type })
      elif (attr == 'initial'):
        actions.append({'action': 'changeInitial', 'initial': obj.initial })
      elif (attr == 'roles'):
        actions.append({'action': 'setRoles', 'roles': obj.roles })
      elif (attr == 'transitions'):
        actions.append({'action': 'setTransitions', 'transitions': [ transition.__dict__ for transition in obj.transitions ] })
      elif (attr.startswith('name')):
        actions.append({'action': 'setName', 'name': obj.name })
      elif (attr.startswith('description')):
          actions.append({'action': 'setDescription', 'description': obj.description })
    return actions
  
  @classmethod
  def _iterable_attribute_add_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
      attr = root_attr.split('.')[1]
      if (attr.__contains__('roles')):
        actions.append({'action': 'addRoles', 'roles': [diff[root_attr]] })
      elif (attr.__contains__('transitions')):
        actions.append({'action': 'setTransitions', 'transitions': [ transition.__dict__ for transition in obj.transitions ]})
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
      if (attr.__contains__('roles')):
        actions.append({'action': 'removeRoles', 'roles': [diff[root_attr]] })
      elif (attr.__contains__('transitions')):
        actions.append({'action': 'setTransitions', 'transitions': [ transition.__dict__ for transition in obj.transitions ]})
    return actions
  
  @classmethod
  def _diccionary_attribute_add_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
      attr = root_attr.split('.')[1]
      if (attr.startswith('name')):
        actions.append({'action': 'setName', 'name': obj.name })
      elif (attr.startswith('description')):
        actions.append({'action': 'setDescription', 'description': obj.description })
    return actions
  
  @classmethod
  def _diccionary_attribute_remove_actions(cls, diff: dict, obj, old_obj = None):
    actions = []
    for root_attr in diff:
      attr = root_attr.split('.')[1]
      if (attr.startswith('name')):
        actions.append({'action': 'setName', 'name': obj.name })
      elif (attr.startswith('description')):
        actions.append({'action': 'setDescription', 'description': obj.description })
    return actions