# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase21CreateTaskAPITestCase.test_case[iB] status_code'] = '400'

snapshots['TestCase21CreateTaskAPITestCase.test_case[iB] body'] = {
    'http_status_code': 400,
    'res_status': 'NOT_A_STRONG_PASSWORD',
    'response': 'Given a weak password: iB for field: DISPLAY_NAME-0! Try with at least 6 characters including special characters'
}

snapshots['TestCase21CreateTaskAPITestCase.test_case[iB_8293] status_code'] = '400'

snapshots['TestCase21CreateTaskAPITestCase.test_case[iB_8293] body'] = {
    'http_status_code': 400,
    'res_status': 'NOT_A_STRONG_PASSWORD',
    'response': 'Given a weak password: iB_8293 for field: DISPLAY_NAME-0! Try with at least 6 characters including special characters'
}
