# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestFilterStorageImplementation.test_create_filter_with_valid_details filter_dto'] = GenericRepr("FilterDTO(filter_id=1, filter_name='filed_name_0', user_id='0', is_selected='ENABLED', template_id='template_0', template_name='Template 6')")

snapshots['TestFilterStorageImplementation.test_create_filter_with_valid_details condition_dtos'] = [
    GenericRepr("ConditionDTO(filter_id=1, condition_id=1, field_id='field_0', field_name='DISPLAY_NAME-0', operator='GTE', value='value_0')"),
    GenericRepr("ConditionDTO(filter_id=1, condition_id=2, field_id='field_1', field_name='DISPLAY_NAME-1', operator='GTE', value='value_1')"),
    GenericRepr("ConditionDTO(filter_id=1, condition_id=3, field_id='field_2', field_name='DISPLAY_NAME-2', operator='GTE', value='value_2')")
]

snapshots['TestFilterStorageImplementation.test_update_filter_with_valid_details filter_dto'] = GenericRepr("FilterDTO(filter_id=1, filter_name='filed_name_0', user_id='4', is_selected='ENABLED', template_id='template_0', template_name='Template 7')")

snapshots['TestFilterStorageImplementation.test_update_filter_with_valid_details condition_dtos'] = [
    GenericRepr("ConditionDTO(filter_id=1, condition_id=4, field_id='field_0', field_name='DISPLAY_NAME-6', operator='GTE', value='value_0')"),
    GenericRepr("ConditionDTO(filter_id=1, condition_id=5, field_id='field_1', field_name='DISPLAY_NAME-7', operator='GTE', value='value_1')"),
    GenericRepr("ConditionDTO(filter_id=1, condition_id=6, field_id='field_2', field_name='DISPLAY_NAME-8', operator='GTE', value='value_2')")
]

snapshots['TestFilterStorageImplementation.test_get_enabled_filters_dto_to_user_with enabled_filters'] = [
    GenericRepr("ApplyFilterDTO(template_id='template_14', field_id='FIELD_ID-21', operator='GTE', value='value_3')"),
    GenericRepr("ApplyFilterDTO(template_id='template_14', field_id='FIELD_ID-22', operator='GTE', value='value_4')"),
    GenericRepr("ApplyFilterDTO(template_id='template_14', field_id='FIELD_ID-23', operator='GTE', value='value_5')")
]

snapshots['TestFilterStorageImplementation.test_get_enabled_filters_dto_to_user_with_all_filters_enabled enabled_filters'] = [
    GenericRepr("ApplyFilterDTO(template_id='template_15', field_id='FIELD_ID-24', operator='GTE', value='value_0')"),
    GenericRepr("ApplyFilterDTO(template_id='template_15', field_id='FIELD_ID-25', operator='GTE', value='value_1')"),
    GenericRepr("ApplyFilterDTO(template_id='template_15', field_id='FIELD_ID-26', operator='GTE', value='value_2')"),
    GenericRepr("ApplyFilterDTO(template_id='template_16', field_id='FIELD_ID-27', operator='GTE', value='value_3')"),
    GenericRepr("ApplyFilterDTO(template_id='template_16', field_id='FIELD_ID-28', operator='GTE', value='value_4')"),
    GenericRepr("ApplyFilterDTO(template_id='template_16', field_id='FIELD_ID-29', operator='GTE', value='value_5')")
]

snapshots['TestFilterStorageImplementation.test_get_enabled_filters_dto_to_user_with_no_filters_enabled enabled_filters'] = [
]
