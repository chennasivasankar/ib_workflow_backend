# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAdhocTasksForKanbanViewAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetAdhocTasksForKanbanViewAPITestCase.test_case body'] = {
    'groups': [
        {
            'child_groups': [
                {
                    'group_by_display_name': 'string',
                    'group_by_value': 'string',
                    'tasks': [
                        {
                            'completed_sub_tasks_count': 1,
                            'description': 'string',
                            'due_date': '2099-12-31 00:00:00',
                            'priority': 'string',
                            'stage_with_actions': {
                                'actions': [
                                    {
                                        'action_id': 1,
                                        'action_type': 'NO_VALIDATIONS',
                                        'button_color': 'string',
                                        'button_text': 'string'
                                    }
                                ],
                                'assignee': {
                                    'assignee_id': 'string',
                                    'name': 'string',
                                    'profile_pic_url': 'string',
                                    'team_info': {
                                        'team_id': 'string',
                                        'team_name': 'string'
                                    }
                                },
                                'stage_color': 'string',
                                'stage_display_name': 'string',
                                'stage_id': 1
                            },
                            'start_date': '2099-12-31 00:00:00',
                            'sub_tasks_count': 1,
                            'task_id': 'string',
                            'task_overview_fields': [
                                {
                                    'field_display_name': 'string',
                                    'field_id': 'string',
                                    'field_response': 'string',
                                    'field_type': 'PLAIN_TEXT'
                                }
                            ],
                            'title': 'string'
                        }
                    ],
                    'total_tasks': 1
                }
            ],
            'group_by_display_name': 'string',
            'group_by_value': 'string',
            'total_groups': 1
        }
    ],
    'total_groups': 1
}
