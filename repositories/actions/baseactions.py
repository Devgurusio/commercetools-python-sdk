from deepdiff import DeepDiff
from models.basemodel import BaseModel


class BaseActions:
    @classmethod
    def _get_diff(cls, old_obj: BaseModel, new_obj: BaseModel):
        return DeepDiff(old_obj, new_obj)

    @classmethod
    def get_actions(cls, old_obj: BaseModel, new_obj: BaseModel):
        actions = []
        diff = cls._get_diff(old_obj, new_obj)
        print('diff')
        print(diff)
        if diff.__contains__('attribute_added'):
            actions.extend(cls._regular_attribute_actions(
                diff['attribute_added'], new_obj, old_obj))
        if diff.__contains__('type_changes'):
            actions.extend(cls._regular_attribute_actions(
                diff['type_changes'], new_obj, old_obj))
        if diff.__contains__('iterable_item_added'):
            actions.extend(cls._iterable_attribute_add_actions(
                diff['iterable_item_added'], new_obj, old_obj))
        if diff.__contains__('iterable_item_removed'):
            actions.extend(cls._iterable_attribute_remove_actions(
                diff['iterable_item_removed'], new_obj, old_obj))
        if diff.__contains__('values_changed'):
            actions.extend(cls._regular_attribute_actions(
                diff['values_changed'], new_obj, old_obj))
            actions.extend(cls._iterable_attribute_update_actions(
                diff['values_changed'], new_obj, old_obj))
        if diff.__contains__('dictionary_item_added'):
            actions.extend(cls._diccionary_attribute_add_actions(
                diff['dictionary_item_added'], new_obj, old_obj))
        if diff.__contains__('dictionary_item_removed'):
            actions.extend(cls._diccionary_attribute_remove_actions(
                diff['dictionary_item_removed'], new_obj, old_obj))

        print('actions')
        print(actions)
        # remove duplicate actions
        [actions.remove(i) for i in actions if actions.count(i) > 1]
        print('actions cleaned')
        print(actions)
        return actions

    @classmethod
    def _regular_attribute_actions(cls, diff: dict, obj, old_obj=None):
        return []

    @classmethod
    def _iterable_attribute_add_actions(cls, diff: dict, obj, old_obj=None):
        return []

    @classmethod
    def _iterable_attribute_update_actions(cls, diff: dict, obj, old_obj=None):
        return []

    @classmethod
    def _iterable_attribute_remove_actions(cls, diff: dict, obj, old_obj=None):
        return []

    @classmethod
    def _diccionary_attribute_add_actions(cls, diff: dict, obj, old_obj=None):
        return []

    @classmethod
    def _diccionary_attribute_remove_actions(cls, diff: dict, obj, old_obj=None):
        return []
