# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetListOfUserRolesForGivenProjectPresenterImplementation.test_prepare_success_response_for_get_list_of_user_roles_to_given_project_id get_team_specific_details'] = {
    'users': [
        {
            'name': 'name1',
            'roles': [
                {
                    'role_id': 'ROLE_1',
                    'role_name': 'role 1'
                },
                {
                    'role_id': 'ROLE_2',
                    'role_name': 'role 2'
                }
            ],
            'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
        },
        {
            'name': 'name2',
            'roles': [
                {
                    'role_id': 'ROLE_3',
                    'role_name': 'role 3'
                }
            ],
            'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
        },
        {
            'name': 'name3',
            'roles': [
            ],
            'user_id': '77be920b-7b4c-49e7-8adb-41a0c18da848'
        }
    ]
}
