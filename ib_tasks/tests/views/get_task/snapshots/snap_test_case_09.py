# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase09GetTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase09GetTaskAPITestCase.test_case body'] = {
    'description': 'description_0',
    'due_date': '2020-10-22 04:40:00',
    'gofs': [
        {
            'gof_fields': [
                {
                    'field_id': 'FIELD_ID-0',
                    'field_response': '{"id": 1, "value": "Hyderabad"}'
                }
            ],
            'gof_id': 'gof_1',
            'same_gof_order': 1
        },
        {
            'gof_fields': [
                {
                    'field_id': 'FIELD_ID-1',
                    'field_response': '{"id": "123e4567-e89b-12d3-a456-426614174000", "value": "{\\"name\\": \\"User1\\", \\"profile_pic_url\\": \\"https://ib-workflows-web-alpha.apigateway.in/boards?board=FINB_AV4_VENDOR_VERIFICATION\\"}"}'
                }
            ],
            'gof_id': 'gof_2',
            'same_gof_order': 1
        }
    ],
    'priority': 'HIGH',
    'project_info': {
        'project_id': 'project0',
        'project_logo_url': 'logo_url0',
        'project_name': 'project_name0'
    },
    'stages_with_actions': [
        {
            'actions': [
            ],
            'assignee': {
                'assignee_id': '123e4567-e89b-12d3-a456-426614174000',
                'name': 'name_0',
                'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
                'team_info': {
                    'team_id': 'team_0',
                    'team_name': 'team_name0'
                }
            },
            'stage_color': 'white',
            'stage_display_name': 'name_0',
            'stage_id': 1,
            'task_stage_id': 1
        },
        {
            'actions': [
            ],
            'assignee': {
                'assignee_id': '123e4567-e89b-12d3-a456-426614174001',
                'name': 'name_1',
                'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
                'team_info': {
                    'team_id': 'team_1',
                    'team_name': 'team_name1'
                }
            },
            'stage_color': 'black',
            'stage_display_name': 'name_1',
            'stage_id': 2,
            'task_stage_id': 2
        },
        {
            'actions': [
            ],
            'assignee': {
                'assignee_id': '123e4567-e89b-12d3-a456-426614174002',
                'name': 'name_2',
                'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
                'team_info': {
                    'team_id': 'team_2',
                    'team_name': 'team_name2'
                }
            },
            'stage_color': 'blue',
            'stage_display_name': 'name_2',
            'stage_id': 3,
            'task_stage_id': 3
        }
    ],
    'start_date': '2020-10-12 04:40:00',
    'task_id': 'iBWF-1',
    'template_id': 'template_0',
    'title': 'title_0'
}
