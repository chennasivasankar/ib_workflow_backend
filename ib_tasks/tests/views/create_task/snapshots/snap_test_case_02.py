# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase02CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TASK_TEMPLATE_DB_ID',
    'response': 'template_1 invalid task template id, please give a valid task template id'
}
