from deepdiff import DeepDiff
from models.basemodel import BaseModel

class BaseActions:
  @classmethod
  def get_actions(cls, old_obj: BaseModel, new_obj: BaseModel):
    actions = []
    diffs = DeepDiff(old_obj, new_obj)
    if (diffs.__contains__('attribute_added')):
      actions.extend(cls._regular_attribute_actions(diffs['attribute_added'], new_obj))
    if (diffs.__contains__('type_changes')):
      actions.extend(cls._regular_attribute_actions(diffs['type_changes'], new_obj))
    if (diffs.__contains__('iterable_item_added')):
      actions.extend(cls._iterable_attribute_add_actions(diffs['iterable_item_added'], new_obj))
    if (diffs.__contains__('iterable_item_removed')):
      actions.extend(cls._iterable_attribute_remove_actions(diffs['iterable_item_removed'], new_obj))
    if (diffs.__contains__('values_changed')):
      actions.extend(cls._regular_attribute_actions(diffs['values_changed'], new_obj))
      actions.extend(cls._iterable_attribute_update_actions(diffs['values_changed'], new_obj, old_obj))
    return actions
  
  @classmethod
  def _regular_attribute_actions(cls, diff: dict, obj):
    return []
  
  @classmethod
  def _iterable_attribute_add_actions(cls, diff: dict, obj):
    return []

  @classmethod
  def _iterable_attribute_update_actions(cls, diff: dict, obj, old_obj = None):
    return []

  @classmethod
  def _iterable_attribute_remove_actions(cls, diff: dict, obj):
    return []