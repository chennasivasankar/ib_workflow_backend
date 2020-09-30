# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_PARENT_TASK_ID',
    'response': 'IBWF-1 is an invalid parent task id, please give a valid parent task id'
}
