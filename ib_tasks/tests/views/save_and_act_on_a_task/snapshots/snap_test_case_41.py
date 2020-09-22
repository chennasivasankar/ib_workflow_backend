# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase41SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase41SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FILE_URL',
    'response': 'Invalid url for a file: file_url.com for field: FIELD_ID-1!'
}
