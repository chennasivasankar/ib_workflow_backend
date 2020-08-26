# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase22UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase22UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_NUMBER_VALUE',
    'response': 'Invalid number: number for field: FIELD-1! Number should only consists digits'
}
