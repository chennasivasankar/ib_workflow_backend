# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestAssignUserRolesForGivenProject.test_with_valid_details_create_details project_user_roles'] = [
    {
        'project_role_id': 'ROLE_1',
        'user_id': '77be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'project_role_id': 'ROLE_3',
        'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'project_role_id': 'ROLE_4',
        'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
    }
]
