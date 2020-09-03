# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase41UpdateTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase41UpdateTaskAPITestCase.test_case body'] = {
    'task_details': None
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
