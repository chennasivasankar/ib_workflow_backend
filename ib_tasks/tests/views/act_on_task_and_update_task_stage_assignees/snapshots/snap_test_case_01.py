# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case status_code'] = '404'

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_TASK_ID',
    'response': 'IBWF-1 is invalid task_id send valid task_id'
}
