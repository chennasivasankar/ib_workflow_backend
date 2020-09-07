# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestCreateFilter.test_create_filter_with_valid_details filter_dto'] = GenericRepr("FilterDTO(filter_id=1, filter_name='filed_name_0', user_id='0', is_selected='ENABLED', template_id='template_0', template_name='Template 1')")

snapshots['TestCreateFilter.test_create_filter_with_valid_details condition_dtos'] = [
    GenericRepr("ConditionDTO(filter_id=1, condition_id=1, field_id='field_0', field_name='DISPLAY_NAME-0', operator='EQ', value='value_0')"),
    GenericRepr("ConditionDTO(filter_id=1, condition_id=2, field_id='field_1', field_name='DISPLAY_NAME-1', operator='EQ', value='value_1')"),
    GenericRepr("ConditionDTO(filter_id=1, condition_id=3, field_id='field_2', field_name='DISPLAY_NAME-2', operator='EQ', value='value_2')")
]
