# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03EditUserAPITestCase.test_given_valid_details_returns_success_response status_code'] = '200'

snapshots['TestCase03EditUserAPITestCase.test_given_valid_details_returns_success_response body'] = {
    'http_status_code': 200,
    'res_status': 'EDIT_USER_SUCCESSFULLY',
    'response': 'Edit User successfully'
}
