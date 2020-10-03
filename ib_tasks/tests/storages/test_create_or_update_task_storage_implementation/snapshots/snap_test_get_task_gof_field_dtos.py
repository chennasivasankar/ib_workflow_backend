# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskGoFFieldDTOS.test_given_task_gof_ids_returns_task_gof_field_dtos task_gof_field_dtos'] = [
    GenericRepr("TaskGoFFieldDTO(task_gof_id=1, field_id='FIELD_ID-6', field_response='field_response_5')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=1, field_id='FIELD_ID-10', field_response='field_response_9')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=2, field_id='FIELD_ID-7', field_response='field_response_6')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=2, field_id='FIELD_ID-9', field_response='field_response_8')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=3, field_id='FIELD_ID-8', field_response='field_response_7')")
]
