# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_gof_ids_and_user_roles_returns_gof_ids_having_permission_for_roles gof_ids_having_permission'] = [
    'gof_10',
    'gof_11',
    'gof_2',
    'gof_4'
]

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_field_ids_and_user_roles_returns_field_ids_having_permission_for_roles field_ids_having_permission'] = [
    'FIELD_ID-0',
    'FIELD_ID-10',
    'FIELD_ID-6'
]

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_gof_ids_and_user_roles_not_having_permission_for_gof_ids_but_permission_for_all_roles_returns_gof_ids gof_ids_having_permission'] = [
    'gof_11'
]

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_field_ids_and_user_roles_not_having_permission_for_field_ids_but_permission_for_all_roles_returns_field_ids field_ids_having_permission'] = [
    'FIELD_ID-10'
]

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_task_id_with_no_gof_ids_returns_empty_list task_gof_dtos'] = [
]

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_task_id_returns_task_gof_dtos task_gof_dtos'] = [
    GenericRepr("TaskGoFDTO(task_gof_id=1, gof_id='gof_1', same_gof_order=1)"),
    GenericRepr("TaskGoFDTO(task_gof_id=2, gof_id='gof_2', same_gof_order=1)"),
    GenericRepr("TaskGoFDTO(task_gof_id=3, gof_id='gof_3', same_gof_order=1)")
]

snapshots['TestCreateOrUpdateTaskStorageImplementation.test_given_task_gof_ids_returns_task_gof_field_dtos task_gof_field_dtos'] = [
    GenericRepr("TaskGoFFieldDTO(task_gof_id=1, field_id='FIELD_ID-0', field_response='field_response_0')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=1, field_id='FIELD_ID-4', field_response='field_response_4')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=2, field_id='FIELD_ID-1', field_response='field_response_1')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=2, field_id='FIELD_ID-3', field_response='field_response_3')"),
    GenericRepr("TaskGoFFieldDTO(task_gof_id=3, field_id='FIELD_ID-2', field_response='field_response_2')")
]
