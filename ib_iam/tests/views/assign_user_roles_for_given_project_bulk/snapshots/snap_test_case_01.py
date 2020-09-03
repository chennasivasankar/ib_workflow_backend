# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AssignUserRolesForGivenProjectBulkAPITestCase.test_with_valid_details_then_assign_user_roles_bulk_for_given_project status_code'] = '201'

snapshots['TestCase01AssignUserRolesForGivenProjectBulkAPITestCase.test_with_valid_details_then_assign_user_roles_bulk_for_given_project body'] = {
}

snapshots['TestCase01AssignUserRolesForGivenProjectBulkAPITestCase.test_with_valid_details_then_assign_user_roles_bulk_for_given_project project_user_roles'] = [
    {
        'project_role_id': 'ROLE_1',
        'user_id': '60be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'project_role_id': 'ROLE_3',
        'user_id': '40be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    {
        'project_role_id': 'ROLE_4',
        'user_id': '40be920b-7b4c-49e7-8adb-41a0c18da848'
    }
]
