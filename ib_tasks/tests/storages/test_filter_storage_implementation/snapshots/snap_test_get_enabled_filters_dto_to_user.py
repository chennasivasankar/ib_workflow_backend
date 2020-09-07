# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetEnableFiltersDTO.test_get_enabled_filters_dto_to_user_with enabled_filters'] = [
    GenericRepr("ApplyFilterDTO(project_id='project_1', template_id='template_2', field_id='FIELD_ID-3', operator='GTE', value='value_4')"),
    GenericRepr("ApplyFilterDTO(project_id='project_1', template_id='template_2', field_id='FIELD_ID-4', operator='GTE', value='value_5')"),
    GenericRepr("ApplyFilterDTO(project_id='project_1', template_id='template_2', field_id='FIELD_ID-5', operator='GTE', value='value_6')")
]

snapshots['TestGetEnableFiltersDTO.test_get_enabled_filters_dto_to_user_with_all_filters_enabled enabled_filters'] = [
    GenericRepr("ApplyFilterDTO(project_id='project_1', template_id='template_1', field_id='FIELD_ID-0', operator='GTE', value='value_7')"),
    GenericRepr("ApplyFilterDTO(project_id='project_1', template_id='template_1', field_id='FIELD_ID-1', operator='GTE', value='value_8')"),
    GenericRepr("ApplyFilterDTO(project_id='project_1', template_id='template_1', field_id='FIELD_ID-2', operator='GTE', value='value_9')"),
    GenericRepr("ApplyFilterDTO(project_id='project_1', template_id='template_2', field_id='FIELD_ID-3', operator='GTE', value='value_10')"),
    GenericRepr("ApplyFilterDTO(project_id='project_1', template_id='template_2', field_id='FIELD_ID-4', operator='GTE', value='value_11')"),
    GenericRepr("ApplyFilterDTO(project_id='project_1', template_id='template_2', field_id='FIELD_ID-5', operator='GTE', value='value_12')")
]

snapshots['TestGetEnableFiltersDTO.test_get_enabled_filters_dto_to_user_with_no_filters_enabled enabled_filters'] = [
]
