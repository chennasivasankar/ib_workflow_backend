# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase25UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase25UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INCORRECT_NAME_IN_GOF_SELECTOR_FIELD',
    'response': "Invalid gof selector name: gof_selector_name for field: FIELD-1! Try with these gof selector names: ['Individual', 'Company'] "
}
