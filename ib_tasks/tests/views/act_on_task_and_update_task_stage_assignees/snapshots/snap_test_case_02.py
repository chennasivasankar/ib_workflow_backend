# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case body'] = {
    'current_board_details': {
        'board_id': 'board__1',
        'board_name': 'name_1',
        'column_details': [
            {
                'column_id': 'column_1',
                'column_name': 'name_1',
                'stage_with_actions': {
                    'actions': [
                    ],
                    'assignee': None,
                    'stage_color': 'orange',
                    'stage_display_name': 'name_1',
                    'stage_id': 2
                },
                'task_overview_fields': [
                ]
            },
            {
                'column_id': 'column_2',
                'column_name': 'name_2',
                'stage_with_actions': {
                    'actions': [
                    ],
                    'assignee': None,
                    'stage_color': 'green',
                    'stage_display_name': 'name_2',
                    'stage_id': 3
                },
                'task_overview_fields': [
                ]
            }
        ]
    },
    'other_board_details': [
    ],
    'task_current_stages_details': {
        'stages': [
            {
                'stage_display_name': 'name_0',
                'stage_id': 'stage_id_0'
            },
            {
                'stage_display_name': 'name_1',
                'stage_id': 'stage_id_1'
            },
            {
                'stage_display_name': 'name_2',
                'stage_id': 'stage_id_2'
            }
        ],
        'task_id': 'IBWF-1',
        'user_has_permission': True
    },
    'task_details': {
        'stage_with_actions': {
            'actions': [
            ],
            'assignee': None,
            'stage_color': 'orange',
            'stage_display_name': 'name_1',
            'stage_id': 2
        },
        'task_id': 'IBWF-1',
        'task_overview_fields': [
        ]
    },
    'task_id': 'IBWF-1'
}

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case stage_1'] = 3

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case assignee_1'] = None

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case left_1'] = None

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case stage_2'] = 1

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case assignee_2'] = '123e4567-e89b-12d3-a456-426614174004'

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case left_2'] = None

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case stage_4'] = 2

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case assignee_4'] = '123e4567-e89b-12d3-a456-427614174008'

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case left_4'] = None
