# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase28SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase28SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_VALUE_FOR_DROPDOWN',
    'response': "Invalid dropdown value: dropdown_value for field: FIELD_ID-1! Try with these dropdown values: ['interactors', 'storages']"
}
