# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetProjectsAPITestCase.test_with_invalid_limit_value status_code'] = '400'

snapshots['TestCase02GetProjectsAPITestCase.test_with_invalid_limit_value body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_LIMIT_VALUE',
    'response': 'given limit value is invalid, less than 0'
}

snapshots['TestCase02GetProjectsAPITestCase.test_with_invalid_offset_value status_code'] = '400'

snapshots['TestCase02GetProjectsAPITestCase.test_with_invalid_offset_value body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_OFFSET_VALUE',
    'response': 'given offset value is invalid, less than 0'
}

snapshots['TestCase02GetProjectsAPITestCase.test_with_non_admin_user_then_raise_exception status_code'] = '403'

snapshots['TestCase02GetProjectsAPITestCase.test_with_non_admin_user_then_raise_exception body'] = {
    'http_status_code': 403,
    'res_status': 'USER_HAS_NO_ACCESS_TO_GET_PROJECTS',
    'response': 'User has no access to get projects'
}
