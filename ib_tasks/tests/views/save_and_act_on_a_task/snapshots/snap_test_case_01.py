# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case body'] = {
    'current_board_details': None,
    'other_board_details': [
    ],
    'task_current_stages_details': {
        'stages': [
            {
                'stage_display_name': 'name_0',
                'stage_id': 'stage_id_0'
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
            'stage_color': 'blue',
            'stage_display_name': 'name_0',
            'stage_id': 1
        },
        'task_id': 'IBWF-1',
        'task_overview_fields': [
            {
                'field_display_name': 'DISPLAY_NAME-1',
                'field_response': 'https://www.freepngimg.com/thumb/light/20246-4-light-transparent.png',
                'field_type': 'IMAGE_UPLOADER'
            },
            {
                'field_display_name': 'DISPLAY_NAME-2',
                'field_response': '["interactors", "storages"]',
                'field_type': 'CHECKBOX_GROUP'
            },
            {
                'field_display_name': 'DISPLAY_NAME-1',
                'field_response': 'https://image.flaticon.com/icons/svg/1829/1829070.svg',
                'field_type': 'IMAGE_UPLOADER'
            },
            {
                'field_display_name': 'DISPLAY_NAME-2',
                'field_response': '["interactors"]',
                'field_type': 'CHECKBOX_GROUP'
            }
        ]
    },
    'task_id': 'IBWF-1'
}

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case template_id'] = 'template_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case created_by_id'] = '123e4567-e89b-12d3-a456-426614174000'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_template_id'] = 'template_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_title'] = 'updated_title'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_description'] = 'updated_description'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_start_date'] = '2020-08-20 00:00:00'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_due_date'] = '2020-09-20 00:00:00'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_priority'] = 'HIGH'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case same_gof_order_1'] = 0

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case gof_id_1'] = 'gof_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_id_1'] = 'IBWF-1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case same_gof_order_2'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case gof_id_2'] = 'gof_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_id_2'] = 'IBWF-1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case same_gof_order_3'] = 0

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case gof_id_3'] = 'gof_2'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_id_3'] = 'IBWF-1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case same_gof_order_4'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case gof_id_4'] = 'gof_2'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_id_4'] = 'IBWF-1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_gof_1'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_1'] = 'FIELD_ID-0'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_response_1'] = 'string'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_gof_2'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_2'] = 'FIELD_ID-1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_response_2'] = 'https://www.freepngimg.com/thumb/light/20246-4-light-transparent.png'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_gof_3'] = 2

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_3'] = 'FIELD_ID-2'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_response_3'] = '["interactors", "storages"]'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_gof_4'] = 3

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_4'] = 'FIELD_ID-0'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_response_4'] = 'new updated string'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_gof_5'] = 3

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_5'] = 'FIELD_ID-1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_response_5'] = 'https://image.flaticon.com/icons/svg/1829/1829070.svg'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_gof_6'] = 4

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_6'] = 'FIELD_ID-2'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_response_6'] = '["interactors"]'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case current_task_stage_task_id_1'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_stage_1'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case stage_history_task_id_1'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case stage_1'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case team_id_1'] = 'team_alpha'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case assignee_id_1'] = 'assignee_id_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case joined_at_1'] = '2020-09-09 12:00:00'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case left_at_1'] = '2020-09-09 12:00:00'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case stage_history_task_id_2'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case stage_2'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case team_id_2'] = 'team_0'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case assignee_id_2'] = 'user_id_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case joined_at_2'] = '2020-09-09 12:00:00'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case left_at_2'] = 'None'
