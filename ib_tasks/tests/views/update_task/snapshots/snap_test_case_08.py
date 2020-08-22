# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_GOFS_OF_TASK_TEMPLATE',
    'response': "invalid gofs ['GOF-1', 'GOF-2']  given to the task template TEMPLATE-1"
}

snapshots['TestCase08UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase08UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_GOFS_OF_TASK_TEMPLATE',
    'response': "invalid gofs ['GOF-1', 'GOF-2']  given to the task template TEMPLATE-1"
}
