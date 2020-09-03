# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase28CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase28CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INCORRECT_MULTI_SELECT_LABELS_SELECTED',
    'response': "Invalid multi select labels selected: ['Other'] for field: FIELD_ID-0! Try with these valid options: ['Mr', 'Mrs']"
}
