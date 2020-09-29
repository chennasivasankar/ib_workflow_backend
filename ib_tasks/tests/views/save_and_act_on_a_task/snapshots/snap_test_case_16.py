# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase16SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase16SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_GOFS_OF_TASK_TEMPLATE',
    'response': "invalid gofs ['GOF_DISPLAY_NAME-0']  given to the task template template_1"
}
