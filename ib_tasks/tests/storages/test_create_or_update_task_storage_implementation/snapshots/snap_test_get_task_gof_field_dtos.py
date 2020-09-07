# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetTaskGoFFieldDTOS.test_given_task_gof_ids_returns_task_gof_field_dtos task_gof_field_dtos'] = [
    GenericRepr("TaskGoFFieldDTO(task_gof_id=1, field_id='FIELD_ID-31', field_response='field_response_7')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=1, field_id='FIELD_ID-35', field_response='field_response_11')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=2, field_id='FIELD_ID-32', field_response='field_response_8')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=2, field_id='FIELD_ID-34', field_response='field_response_10')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=3, field_id='FIELD_ID-33', field_response='field_response_9')")
]
