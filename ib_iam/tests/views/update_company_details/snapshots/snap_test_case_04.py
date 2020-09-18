# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04UpdateCompanyDetailsAPITestCase.test_case status_code'] = '400'

snapshots['TestCase04UpdateCompanyDetailsAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_USER_IDS',
    'response': "Duplicate user are sent, try again"
}
