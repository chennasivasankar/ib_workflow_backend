# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase41UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase41UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'TASK_DELAY_REASON_NOT_UPDATED',
    'response': 'Task delay reason not updated for task IBWF-1 in stage display_name_0 with missed due date 2020-09-09 11:00:00'
}

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_title'] = 'title_0'

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_description'] = 'description_0'

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_start_date'] = '2020-10-12 04:40:00'

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_due_date'] = '2020-10-22 04:40:00'

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_priority'] = 'HIGH'
