# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase17SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase17SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF',
    'response': "gof id gof_1 has duplicate field ids ['FIELD_ID-1']"
}
