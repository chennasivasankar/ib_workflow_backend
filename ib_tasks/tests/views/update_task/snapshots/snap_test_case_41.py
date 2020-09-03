# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase41UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase41UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'EMPTY_STAGE_IDS_ARE_INVALID',
    'response': 'Stage Ids list should not be empty'
}

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_title'] = 'updated_title'

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_description'] = 'updated_description'

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_start_date'] = '2020-09-08 00:00:00'

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_due_date'] = '2020-09-09 11:00:00'

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_priority'] = 'HIGH'

snapshots['TestCase41UpdateTaskAPITestCase.test_case FIELD-1'] = 'https://www.url.com/file.zip'

snapshots['TestCase41UpdateTaskAPITestCase.test_case FIELD-1 response'] = 'https://www.url.com/file.zip'

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_stage_id'] = 1

snapshots['TestCase41UpdateTaskAPITestCase.test_case task_stage_assignee_id'] = 'assignee_id_1'
