# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetProjectDiscussionsAPITestCase.test_invalid_offset_raise_exception status_code'] = '400'

snapshots['TestCase02GetProjectDiscussionsAPITestCase.test_invalid_offset_raise_exception body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_OFFSET',
    'response': 'Please send the valid offset value'
}

snapshots['TestCase02GetProjectDiscussionsAPITestCase.test_invalid_project_id_return_response status_code'] = '404'

snapshots['TestCase02GetProjectDiscussionsAPITestCase.test_invalid_project_id_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_PROJECT_ID',
    'response': 'Please send valid project id'
}

snapshots['TestCase02GetProjectDiscussionsAPITestCase.test_invalid_user_for_project_return_response status_code'] = '400'

snapshots['TestCase02GetProjectDiscussionsAPITestCase.test_invalid_user_for_project_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_USER_FOR_PROJECT',
    'response': 'Please send valid user for project'
}

snapshots['TestCase02GetProjectDiscussionsAPITestCase.test_user_profile_does_not_exist_raise_exception status_code'] = '400'

snapshots['TestCase02GetProjectDiscussionsAPITestCase.test_user_profile_does_not_exist_raise_exception body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_USER_ID',
    'response': 'Please send the valid user id'
}

snapshots['TestCase02GetProjectDiscussionsAPITestCase.test_invalid_limit_raise_exception status_code'] = '400'

snapshots['TestCase02GetProjectDiscussionsAPITestCase.test_invalid_limit_raise_exception body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_LIMIT',
    'response': 'Please send the valid limit value'
}
