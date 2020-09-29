# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase18CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase18CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF',
    'response': "gof id FIN_PAYMENT_REQUESTER_DETAILS has duplicate field ids ['FIN_PAYMENT_REQUESTER_FIELD']"
}
