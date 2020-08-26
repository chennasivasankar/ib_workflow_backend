# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetSpecificProjectDetailsPresenterImplementation.test_prepare_success_response_for_get_specific_team_details get_team_specific_details'] = {
    'users': [
        {
            'name': 'user_1',
            'roles': [
                {
                    'role_id': 'ROLE_1',
                    'role_name': 'NAME_1'
                },
                {
                    'role_id': 'ROLE_2',
                    'role_name': 'NAME_2'
                }
            ],
            'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
        },
        {
            'name': 'user_2',
            'roles': [
                {
                    'role_id': 'ROLE_3',
                    'role_name': 'NAME_3'
                }
            ],
            'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
        },
        {
            'name': 'user_3',
            'roles': [
            ],
            'user_id': '77be920b-7b4c-49e7-8adb-41a0c18da848'
        }
    ]
}
