# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase46CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase46CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_PRESENT_STAGE_ACTION',
    'response': '1 is invalid present stage action'
}
