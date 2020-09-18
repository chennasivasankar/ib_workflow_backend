# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetFieldDetails.test_when_user_permitted_fields_exists_returns_field_details response'] = [
    GenericRepr("FieldDetailsDTOWithTaskId(field_type='SEARCHABLE', field_id='FIELD_ID-0', key='DISPLAY_NAME-0', value='field_response_0', field_values='USER', task_id=2)"),
    GenericRepr("FieldDetailsDTOWithTaskId(field_type='SEARCHABLE', field_id='FIELD_ID-1', key='DISPLAY_NAME-1', value='field_response_1', field_values='USER', task_id=1)"),
    GenericRepr("FieldDetailsDTOWithTaskId(field_type='SEARCHABLE', field_id='FIELD_ID-2', key='DISPLAY_NAME-2', value='field_response_2', field_values='USER', task_id=2)"),
    GenericRepr("FieldDetailsDTOWithTaskId(field_type='SEARCHABLE', field_id='FIELD_ID-2', key='DISPLAY_NAME-2', value='field_response_3', field_values='USER', task_id=1)"),
    GenericRepr("FieldDetailsDTOWithTaskId(field_type='SEARCHABLE', field_id='FIELD_ID-1', key='DISPLAY_NAME-1', value='field_response_4', field_values='USER', task_id=2)")
]
