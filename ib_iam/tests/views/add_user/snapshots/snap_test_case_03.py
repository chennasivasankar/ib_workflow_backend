# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03AddUserAPITestCase.test_case status_code'] = '201'

snapshots['TestCase03AddUserAPITestCase.test_case body'] = {
    'http_status_code': 201,
    'res_status': 'CREATE_USER_SUCCESSFULLY',
    'response': 'User created successfully'
}
