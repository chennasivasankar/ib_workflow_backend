# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase24UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase24UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_VALUE_FOR_DROPDOWN',
    'response': "Invalid dropdown value: dropdown_value for field: DISPLAY_NAME-0! Try with these dropdown values: ['interactors', 'storages']"
}
