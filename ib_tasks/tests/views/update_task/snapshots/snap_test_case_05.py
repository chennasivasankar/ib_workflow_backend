# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUE_TIME_HAS_EXPIRED_FOR_TODAY',
    'response': 'give due time 11:00:00 has expired for today date'
}

snapshots['TestCase05UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase05UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUE_TIME_HAS_EXPIRED_FOR_TODAY',
    'response': 'give due time 11:00:00 has expired for today date'
}
