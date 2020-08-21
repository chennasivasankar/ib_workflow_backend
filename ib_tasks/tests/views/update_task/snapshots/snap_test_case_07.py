# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FIELD_IDS',
    'response': "invalid field ids: ['FIELD_ID-10', 'FIELD_ID-11', 'FIELD_ID-12']"
}

snapshots['TestCase07UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase07UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FIELD_IDS',
    'response': "invalid field ids: ['FIELD_ID-10', 'FIELD_ID-11', 'FIELD_ID-12']"
}
