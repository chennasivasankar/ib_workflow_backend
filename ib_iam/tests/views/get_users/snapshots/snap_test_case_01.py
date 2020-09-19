# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01GetUsersAPITestCase.test_given_user_is_not_admin_returns_user_has_no_access_response status_code'] = '403'

snapshots['TestCase01GetUsersAPITestCase.test_given_user_is_not_admin_returns_user_has_no_access_response body'] = {
    'http_status_code': 403,
    'res_status': 'USER_DOES_NOT_HAVE_PERMISSION',
    'response': 'forbidden access, user cannot access'
}

snapshots['TestCase01GetUsersAPITestCase.test_given_invalid_limit_returns_invalid_limit_response status_code'] = '400'

snapshots['TestCase01GetUsersAPITestCase.test_given_invalid_limit_returns_invalid_limit_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_LIMIT_VALUE',
    'response': 'given limit value is invalid, less than 0'
}

snapshots['TestCase01GetUsersAPITestCase.test_given_invalid_offset_returns_invalid_offset_response status_code'] = '400'

snapshots['TestCase01GetUsersAPITestCase.test_given_invalid_offset_returns_invalid_offset_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_OFFSET_VALUE',
    'response': 'given offset value is invalid, less than 0'
}
