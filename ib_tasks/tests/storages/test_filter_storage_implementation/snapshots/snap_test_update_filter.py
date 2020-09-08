# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestUpdateFilter.test_update_filter_with_valid_details filter_dto'] = GenericRepr("FilterDTO(filter_id=1, filter_name='filed_name_0', user_id='0', is_selected='ENABLED', template_id='template_0', template_name='Template 1')")

snapshots['TestUpdateFilter.test_update_filter_with_valid_details condition_dtos'] = [
    GenericRepr("ConditionDTO(filter_id=1, condition_id=4, field_id='field_0', field_name='DISPLAY_NAME-3', operator='EQ', value='value_0')"),
    GenericRepr("ConditionDTO(filter_id=1, condition_id=5, field_id='field_1', field_name='DISPLAY_NAME-4', operator='EQ', value='value_1')"),
    GenericRepr("ConditionDTO(filter_id=1, condition_id=6, field_id='field_2', field_name='DISPLAY_NAME-5', operator='EQ', value='value_2')")
]
