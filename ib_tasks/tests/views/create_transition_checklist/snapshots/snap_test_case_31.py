# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase31CreateTransitionChecklistAPITestCase.test_case status_code'] = '400'

snapshots['TestCase31CreateTransitionChecklistAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_FILE_URL',
    'response': 'Invalid url for a file: http://google.com/ for field: DISPLAY_NAME-0!'
}
