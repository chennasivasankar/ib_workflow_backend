# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04GetTaskAPITestCase.test_case status_code'] = '403'

snapshots['TestCase04GetTaskAPITestCase.test_case body'] = {
    'http_status_code': 403,
    'res_status': 'USER_PERMISSION_DENIED',
    'response': "user doesn't have permission"
}
