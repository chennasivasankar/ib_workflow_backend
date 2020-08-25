# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase40UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase40UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FILE_FORMAT',
    'response': "Invalid format for a file: .tar for field: FIELD-1! Try with these formats: ['.zip', '.pdf']"
}
