# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots[
    'TestGetTaskProjectIds.test_get_task_projects_given_task_ids ' \
    'task_project_dtos'] = [
    GenericRepr("TaskProjectDTO(task_id=1, project_id='project_id_1')"),
    GenericRepr("TaskProjectDTO(task_id=2, project_id='project_id_2')"),
    GenericRepr("TaskProjectDTO(task_id=3, project_id='project_id_3')"),
    GenericRepr("TaskProjectDTO(task_id=4, project_id='project_id_4')")
]
