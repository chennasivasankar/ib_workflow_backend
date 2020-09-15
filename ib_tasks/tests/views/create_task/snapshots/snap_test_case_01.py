# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateTaskAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01CreateTaskAPITestCase.test_case body'] = {
    'task_current_stages_details': {
        'stages': [
            {
                'stage_display_name': 'name_0',
                'stage_id': 'stage_1'
            }
        ],
        'task_id': 'IBWF-1',
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
            'stage_color': 'green',
            'stage_display_name': 'name_0',
            'stage_id': 1
        },
        'task_id': 'IBWF-1',
        'task_overview_fields': [
            {
                'field_display_name': 'DISPLAY_NAME-0',
                'field_response': 'field_0_response',
                'field_type': 'PLAIN_TEXT'
            }
        ]
    }
}

snapshots['TestCase01CreateTaskAPITestCase.test_case task_id'] = 1

snapshots['TestCase01CreateTaskAPITestCase.test_case template_id'] = 'template_1'

snapshots['TestCase01CreateTaskAPITestCase.test_case task_title'] = 'task_title'

snapshots['TestCase01CreateTaskAPITestCase.test_case task_description'] = 'task_description'

snapshots['TestCase01CreateTaskAPITestCase.test_case task_start_date'] = '2020-09-20 00:00:00'

snapshots['TestCase01CreateTaskAPITestCase.test_case task_due_date'] = '2020-10-31 00:00:00'

snapshots['TestCase01CreateTaskAPITestCase.test_case task_priority'] = 'HIGH'

snapshots['TestCase01CreateTaskAPITestCase.test_case same_gof_order_1'] = 1

snapshots['TestCase01CreateTaskAPITestCase.test_case gof_id_1'] = 'gof_1'

snapshots['TestCase01CreateTaskAPITestCase.test_case gof_task_id_1'] = 1

snapshots['TestCase01CreateTaskAPITestCase.test_case task_gof_1'] = 1

snapshots['TestCase01CreateTaskAPITestCase.test_case field_1'] = 'FIELD_ID-0'

snapshots['TestCase01CreateTaskAPITestCase.test_case field_response_1'] = 'field_0_response'
