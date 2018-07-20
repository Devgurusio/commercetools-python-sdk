from .baseactions import BaseActions
from models.tax_category import TaxCategory
import re


class TaxCategoryActions(BaseActions):
    @classmethod
    def _regular_attribute_actions(cls, diff: dict, obj, old_obj=None):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr == 'key':
                actions.append({'action': 'setKey', 'key': obj.key})
            elif attr == 'name':
                actions.append({'action': 'changeName', 'name': obj.name})
            elif attr == 'description':
                actions.append({'action': 'setDescription',
                                'description': obj.description})
            elif attr.__contains__('rates'):
                if obj.rates[int(re.findall(r'[\d+]', attr)[0])].id == old_obj.rates[int(re.findall(r'[\d+]', attr)[0])].id:
                    actions.append({'action': 'replaceTaxRate', 'taxRateId': obj.rates[int(re.findall(r'[\d+]', attr)[0])].id, 'taxRate': obj.rates[int(re.findall(r'[\d+]', attr)[0])].toDict()})
        return actions

    @classmethod
    def _iterable_attribute_add_actions(cls, diff: dict, obj, old_obj=None):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr.__contains__('rates'):
                try:
                    field = root_attr.split('.')[2]
                    if field.__contains__('subRates'):
                        actions.append({'action': 'replaceTaxRate', 'taxRateId': obj.rates[int(re.findall(r'[\d+]', attr)[0])].id, 'taxRate': obj.rates[int(re.findall(r'[\d+]', attr)[0])].toDict()})
                except IndexError:
                    actions.append({'action': 'addTaxRate', 'taxRate': diff[root_attr].__dict__})
        return actions

    @classmethod
    def _iterable_attribute_update_actions(cls, diff: dict, obj, old_obj):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr.__contains__('rates'):
                if obj.rates[int(re.findall(r'[\d+]', attr)[0])].id == old_obj.rates[int(re.findall(r'[\d+]', attr)[0])].id:
                    actions.append({'action': 'replaceTaxRate', 'taxRateId': obj.rates[int(re.findall(r'[\d+]', attr)[0])].id, 'taxRate': obj.rates[int(re.findall(r'[\d+]', attr)[0])].toDict()})
        return actions

    @classmethod
    def _iterable_attribute_remove_actions(cls, diff: dict, obj, old_obj=None):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr.__contains__('rates'):
                actions.append({'action': 'removeTaxRate',
                                'taxRateId': obj.rates[int(re.findall(r'[\d+]', attr)[0])].id})
        return actions
