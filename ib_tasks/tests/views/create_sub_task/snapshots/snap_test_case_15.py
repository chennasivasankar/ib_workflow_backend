# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase15CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase15CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_GOF_IDS',
    'response': "invalid gof ids: ['FIN_PAYMENT_APPROVER_DETAILS']"
}
