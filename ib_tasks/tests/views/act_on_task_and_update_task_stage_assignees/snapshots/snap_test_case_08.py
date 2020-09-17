# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case status_code'] = '404'

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'REASON_NOT_ADDED_FOR_TASK_DELAY',
    'response': '''Task IBWF-1 in Stage name_0 has missed the
                                  due date'''
}
