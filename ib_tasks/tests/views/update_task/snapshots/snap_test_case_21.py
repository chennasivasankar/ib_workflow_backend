# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase21UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase21UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'NOT_A_STRONG_PASSWORD',
    'response': 'Given a weak password: strong_password for field: FIELD-1! Try with at least 6 characters including special characters'
}
