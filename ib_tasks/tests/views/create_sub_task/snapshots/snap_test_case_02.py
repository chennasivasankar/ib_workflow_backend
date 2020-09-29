# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreateSubTaskAPITestCase.test_case status_code'] = '201'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case body'] = {
    'created_task_id': 'IBWF-2',
    'task_current_stages_details': {
        'stages': [
            {
                'stage_display_name': 'name_0',
                'stage_id': '1'
            }
        ],
        'task_id': 'IBWF-2',
        'user_has_permission': True
    },
    'task_details': {
        'stage_with_actions': {
            'actions': [
                {
                    'action_id': 1,
                    'action_type': 'NO_VALIDATIONS',
                    'button_color': '#fafafa',
                    'button_text': 'hey',
                    'transition_template_id': 'template_2'
                }
            ],
            'assignee': None,
            'stage_color': 'blue',
            'stage_display_name': 'name_0',
            'stage_id': 1
        },
        'task_id': 'IBWF-2',
        'task_overview_fields': [
        ]
    }
}

snapshots['TestCase02CreateSubTaskAPITestCase.test_case parent_task_id'] = 1

snapshots['TestCase02CreateSubTaskAPITestCase.test_case parent_task_template_id'] = 'template_1'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case parent_task_title'] = 'title_0'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case parent_task_description'] = 'description_0'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case parent_task_start_date'] = '2020-10-12 04:40:00'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case parent_task_due_date'] = '2020-10-22 04:40:00'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case parent_task_priority'] = 'HIGH'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task_id'] = 2

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task_template_id'] = 'template_1'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task_title'] = 'Sub Task'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task_description'] = None

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task_start_date'] = 'None'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task_due_date'] = 'None'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task_priority'] = None

snapshots['TestCase02CreateSubTaskAPITestCase.test_case parent_task'] = 'IBWF-1'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task'] = 'IBWF-2'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task_request_body'] = '{"project_id": "project_1", "task_template_id": "template_1", "action_id": 1, "parent_task_id": "IBWF-1", "title": "Sub Task", "description": null, "start_datetime": "None", "due_datetime": "None", "priority": null, "task_gofs": []}'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case task_log_sub_task_id'] = 'IBWF-2'

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task_performed_action_id'] = 1

snapshots['TestCase02CreateSubTaskAPITestCase.test_case sub_task_acted_at'] = '2020-09-09 12:00:00'
