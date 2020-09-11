# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetListOfUserRolesForGivenProjectAPITestCase.test_with_invalid_project_id_return_response status_code'] = '403'

snapshots['TestCase02GetListOfUserRolesForGivenProjectAPITestCase.test_with_invalid_project_id_return_response body'] = {
    'http_status_code': 403,
    'res_status': 'USER_HAS_NO_ACCESS_TO_GET_USERS_WITH_ROLES',
    'response': 'User has no access to get users with roles'
}

snapshots['TestCase02GetListOfUserRolesForGivenProjectAPITestCase.test_with_user_is_not_admin_then_raise_exception status_code'] = '403'

snapshots['TestCase02GetListOfUserRolesForGivenProjectAPITestCase.test_with_user_is_not_admin_then_raise_exception body'] = {
    'http_status_code': 403,
    'res_status': 'USER_HAS_NO_ACCESS_TO_GET_USERS_WITH_ROLES',
    'response': 'User has no access to get users with roles'
}
