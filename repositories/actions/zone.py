from .baseactions import BaseActions
from models.zone import Zone
import re


class ZoneActions(BaseActions):
    @classmethod
    def _regular_attribute_actions(cls, diff: dict, obj, old_obj=None):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr == 'name':
                actions.append({'action': 'changeName', 'name': obj.name})
            elif attr == 'description':
                actions.append({'action': 'setDescription',
                                'description': obj.description})
        return actions

    @classmethod
    def _iterable_attribute_add_actions(cls, diff: dict, obj, old_obj=None):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr.__contains__('locations'):
                actions.append(
                    {'action': 'addLocation', 'location': diff[root_attr].__dict__})
        return actions

    @classmethod
    def _iterable_attribute_update_actions(cls, diff: dict, obj, old_obj):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr.__contains__('locations'):
                actions.append({'action': 'removeLocation', 'location': old_obj.locations[int(
                    re.findall(r'[\d+]', attr)[0])].__dict__})
                actions.append({'action': 'addLocation', 'location': obj.locations[int(
                    re.findall(r'[\d+]', attr)[0])].__dict__})
        return actions

    @classmethod
    def _iterable_attribute_remove_actions(cls, diff: dict, obj, old_obj=None):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr.__contains__('locations'):
                actions.append({'action': 'removeLocation',
                                'location': diff[root_attr].__dict__})
        return actions
