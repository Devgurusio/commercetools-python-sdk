from .baseactions import BaseActions
from models.zone import Zone
import re


class ShippingMethodActions(BaseActions):
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
            elif attr == 'isDefault':
                actions.append({'action': 'changeIsDefault', 'isDefault': obj.isDefault})
            elif attr == 'predicate':
                actions.append({'action': 'setPredicate', 'predicate': obj.predicate})
            elif attr.__contains__('taxCategory'):
                actions.append({'action': 'changeTaxCategory', 'taxCategory': obj.taxCategory.toDict()})
        return actions

    @classmethod
    def _iterable_attribute_add_actions(cls, diff: dict, obj, old_obj=None):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr.__contains__('zoneRates'):
                try:
                    field = root_attr.split('.')[2]
                    if (field.__contains__('shippingRates')):
                        actions.append({'action': 'addShippingRate', 'zone': obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict(), 'shippingRate': obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].shippingRates[int(re.findall(r'[\d+]', field)[0])].toDict() })
                except IndexError:
                    actions.append({
                        'action': 'addZone',
                        'zone': obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict()
                    })
                    if obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].shippingRates:
                        actions.extend([ {'action': 'addShippingRate', 'zone': obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict(), 'shippingRate': shippingRate.toDict() } for shippingRate in obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].shippingRates ])
        return actions

    @classmethod
    def _iterable_attribute_update_actions(cls, diff: dict, obj, old_obj):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr.__contains__('zoneRates'):
                try:
                    field = root_attr.split('.')[2]
                    if (field.__contains__('zone')):
                        actions.append({'action': 'removeZone', 'zone': old_obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict()})
                        actions.append({
                            'action': 'addZone',
                            'zone': obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict()
                        })
                        if obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].shippingRates:
                            actions.extend([ {'action': 'addShippingRate', 'zone': obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict(), 'shippingRate': shippingRate.toDict() } for shippingRate in obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].shippingRates ])
                    elif (field.__contains__('shippingRates')):
                        actions.append({'action': 'removeShippingRate', 'zone': old_obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict(), 'shippingRate': old_obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].shippingRates[int(re.findall(r'[\d+]', field)[0])].toDict() })
                        actions.append({'action': 'addShippingRate', 'zone': obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict(), 'shippingRate': obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].shippingRates[int(re.findall(r'[\d+]', field)[0])].toDict() })
                except IndexError:
                    actions.append({'action': 'removeZone', 'zone': old_obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict()})
                    actions.append({
                        'action': 'addZone',
                        'zone': obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict()
                    })
                    if obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].shippingRates:
                        actions.extend([ {'action': 'addShippingRate', 'zone': obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict(), 'shippingRate': shippingRate.toDict() } for shippingRate in obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].shippingRates ])
        return actions

    @classmethod
    def _iterable_attribute_remove_actions(cls, diff: dict, obj, old_obj=None):
        actions = []
        for root_attr in diff:
            attr = root_attr.split('.')[1]
            if attr.__contains__('zoneRates'):
                try:
                    field = root_attr.split('.')[2]
                    if (field.__contains__('shippingRates')):
                        actions.append({'action': 'removeShippingRate', 'zone': old_obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict(), 'shippingRate': old_obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].shippingRates[int(re.findall(r'[\d+]', field)[0])].toDict() })
                except IndexError:
                    actions.append({'action': 'removeZone', 'zone': old_obj.zoneRates[int(re.findall(r'[\d+]', attr)[0])].zone.toDict()})
        return actions
