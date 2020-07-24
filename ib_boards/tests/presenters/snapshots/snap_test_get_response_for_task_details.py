# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestTaskDetailsResponse.test_get_response_for_task_details list_of_task_details'] = {
    'tasks': [
        {
            'actions': [
                {
                    'action_id': 'action_id_0',
                    'button_color': None,
                    'button_text': 'button_text_0',
                    'name': 'name_0'
                }
            ],
            'fields': [
                {
                    'field_type': 'field_type_0',
                    'key': 'key_0',
                    'value': 'value_0'
                }
            ],
            'task_id': 'task_id_0'
        },
        {
            'actions': [
                {
                    'action_id': 'action_id_1',
                    'button_color': None,
                    'button_text': 'button_text_1',
                    'name': 'name_1'
                }
            ],
            'fields': [
                {
                    'field_type': 'field_type_1',
                    'key': 'key_1',
                    'value': 'value_1'
                }
            ],
            'task_id': 'task_id_1'
        },
        {
            'actions': [
                {
                    'action_id': 'action_id_2',
                    'button_color': None,
                    'button_text': 'button_text_2',
                    'name': 'name_2'
                }
            ],
            'fields': [
                {
                    'field_type': 'field_type_2',
                    'key': 'key_2',
                    'value': 'value_2'
                }
            ],
            'task_id': 'task_id_2'
        }
    ],
    'total_tasks_count': 3
}
