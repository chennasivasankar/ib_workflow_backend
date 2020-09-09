# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTeamMemberLevelsPresenterImplementation.test_response_for_level_details_dtos level_details_dtos_response'] = {
    'levels': [
        {
            'level_hierarchy': 0,
            'team_member_level_id': 'd6264b89-df8d-4b08-9ce1-f61004a0fbcc',
            'team_member_level_name': 'Geoffrey Barnes'
        },
        {
            'level_hierarchy': 1,
            'team_member_level_id': '55b28aac-db47-44b4-a76a-c42084979a83',
            'team_member_level_name': 'Scott Baker'
        },
        {
            'level_hierarchy': 2,
            'team_member_level_id': 'a762f699-a9b4-42c7-82b8-b702296ff764',
            'team_member_level_name': 'Dan Ramos'
        },
        {
            'level_hierarchy': 3,
            'team_member_level_id': '7e82dc48-0fde-4aad-9e82-7b1f9d77378d',
            'team_member_level_name': 'Jeffrey Clark'
        },
        {
            'level_hierarchy': 4,
            'team_member_level_id': '615ef7d5-c142-46b4-acd7-f37ab35bf83f',
            'team_member_level_name': 'Sarah Mason'
        }
    ]
}
