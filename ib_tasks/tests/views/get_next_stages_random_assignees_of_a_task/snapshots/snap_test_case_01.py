# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetNextStagesRandomAssigneesOfATaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetNextStagesRandomAssigneesOfATaskAPITestCase.test_case body'] = {
    'stage_assignees': [
        {
            'assignee': {
                'assignee_id': 'user_id_0',
                'name': 'name_0',
                'profile_pic_url': 'pic_url',
                'team_info': {
                    'team_id': 'team_0',
                    'team_name': 'team_name0'
                }
            },
            'stage_display_name': 'name_0',
            'stage_id': 1
        },
        {
            'assignee': {
                'assignee_id': 'user_id_0',
                'name': 'name_0',
                'profile_pic_url': 'pic_url',
                'team_info': {
                    'team_id': 'team_0',
                    'team_name': 'team_name0'
                }
            },
            'stage_display_name': 'name_1',
            'stage_id': 2
        },
        {
            'assignee': {
                'assignee_id': 'user_id_0',
                'name': 'name_0',
                'profile_pic_url': 'pic_url',
                'team_info': {
                    'team_id': 'team_0',
                    'team_name': 'team_name0'
                }
            },
            'stage_display_name': 'name_2',
            'stage_id': 3
        }
    ]
}
