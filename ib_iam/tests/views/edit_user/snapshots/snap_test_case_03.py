# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03EditUserAPITestCase.test_case body'] = {
    'http_status_code': 200,
    'res_status': 'EDIT_USER_SUCCESSFULLY',
    'response': 'Edit User successfully'
}

snapshots['TestCase03EditUserAPITestCase.test_case status_code'] = '200'
