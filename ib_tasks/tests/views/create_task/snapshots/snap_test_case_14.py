# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateTaskAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01CreateTaskAPITestCase.test_case body'] = {
    'created_task_id': 'IBWF-1',
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
        'due_date': '2020-10-31 00:00:00',
        'priority': 'HIGH',
        'stage_with_actions': {
            'actions': [
                {
                    'action_id': 1,
                    'action_type': '',
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
        'start_date': '2020-09-20 00:00:00',
        'task_id': 'IBWF-1',
        'task_overview_fields': [
            {
                'field_display_name': 'DISPLAY_NAME-0',
                'field_response': 'vendor payment details',
                'field_type': 'PLAIN_TEXT'
            }
        ],
        'title': 'task_title'
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

snapshots['TestCase01CreateTaskAPITestCase.test_case gof_id_1'] = 'FIN_PAYMENT_TYPE'

snapshots['TestCase01CreateTaskAPITestCase.test_case gof_task_id_1'] = 1

snapshots['TestCase01CreateTaskAPITestCase.test_case same_gof_order_2'] = 1

snapshots['TestCase01CreateTaskAPITestCase.test_case gof_id_2'] = 'FIN_VENDOR_PAYMENT_DETAILS'

snapshots['TestCase01CreateTaskAPITestCase.test_case gof_task_id_2'] = 1

snapshots['TestCase01CreateTaskAPITestCase.test_case task_gof_1'] = 1

snapshots['TestCase01CreateTaskAPITestCase.test_case field_1'] = 'FIN_TYPE_OF_PAYMENT_REQUEST'

snapshots['TestCase01CreateTaskAPITestCase.test_case field_response_1'] = 'Vendor Payment'

snapshots['TestCase01CreateTaskAPITestCase.test_case task_gof_2'] = 2

snapshots['TestCase01CreateTaskAPITestCase.test_case field_2'] = 'FIELD_ID-0'

snapshots['TestCase01CreateTaskAPITestCase.test_case field_response_2'] = 'vendor payment details'

snapshots['TestCase01CreateTaskAPITestCase.test_case task_id_1'] = 1

snapshots['TestCase01CreateTaskAPITestCase.test_case task_stage_1'] = 1
