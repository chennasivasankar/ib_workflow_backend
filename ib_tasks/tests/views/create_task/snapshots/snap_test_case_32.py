# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase32CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase32CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FILE_FORMAT',
    'response': "Invalid format for a file: .mp4 for field: FIELD_ID-0! Try with these formats: ['.pdf', '.doc']"
}
