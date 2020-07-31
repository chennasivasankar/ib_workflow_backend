# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_task_id_returns_task_gof_dtos task_gof_dtos'] = [
    GenericRepr("TaskGoFDTO(task_gof_id=1, gof_id='gof_1', same_gof_order=1)"),
    GenericRepr("TaskGoFDTO(task_gof_id=2, gof_id='gof_2', same_gof_order=1)"),
    GenericRepr("TaskGoFDTO(task_gof_id=3, gof_id='gof_3', same_gof_order=1)")
]

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_task_gof_ids_returns_task_gof_field_dtos task_gof_field_dtos'] = [
    GenericRepr("TaskGoFFieldDTO(task_gof_id=1, field_id='FIELD_ID-0', field_response='response')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=1, field_id='FIELD_ID-4', field_response='response')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=2, field_id='FIELD_ID-1', field_response='response')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=2, field_id='FIELD_ID-3', field_response='response')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=3, field_id='FIELD_ID-2', field_response='response')")
]

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_gof_ids_and_user_roles_returns_gof_ids_having_permission_for_roles gof_ids_having_permission'] = [
    'gof_13',
    'gof_15',
    'gof_21',
    'gof_22'
]

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_field_ids_and_user_roles_returns_field_ids_having_permission_for_roles field_ids_having_permission'] = [
    'FIELD_ID-11',
    'FIELD_ID-15',
    'FIELD_ID-5'
]
