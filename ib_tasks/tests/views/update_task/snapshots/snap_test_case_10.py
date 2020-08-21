# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase10UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase10UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FIELDS_OF_GOF',
    'response': "invalid fields ['FIELD-1', 'FIELD-2']  given to the gof GOF-1"
}
