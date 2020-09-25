# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskGoFDTOS.test_given_task_id_returns_task_gof_dtos task_gof_dtos'] = [
    GenericRepr("TaskGoFDTO(task_gof_id=1, gof_id='gof_1', same_gof_order=1)"),
    GenericRepr("TaskGoFDTO(task_gof_id=2, gof_id='gof_2', same_gof_order=1)"),
    GenericRepr("TaskGoFDTO(task_gof_id=3, gof_id='gof_3', same_gof_order=1)")
]

snapshots['TestGetTaskGoFDTOS.test_given_task_id_with_no_gof_ids_returns_empty_list task_gof_dtos'] = [
]
