# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateSubTaskAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case body'] = {
    'response': 'Sub task created Successfully'
}

snapshots['TestCase01CreateSubTaskAPITestCase.test_case parent_task_id'] = 1

snapshots['TestCase01CreateSubTaskAPITestCase.test_case parent_task_template_id'] = 'template_1'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case parent_task_title'] = 'title_0'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case parent_task_description'] = 'description_0'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case parent_task_start_date'] = '2020-10-12 04:40:00'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case parent_task_due_date'] = '2020-10-22 04:40:00'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case parent_task_priority'] = 'HIGH'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task_id'] = 2

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task_template_id'] = 'template_1'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task_title'] = 'Sub Task'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task_description'] = 'description of sub task'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task_start_date'] = '2020-09-09 00:00:00'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task_due_date'] = '2099-10-09 00:00:00'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task_priority'] = 'HIGH'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case parent_task'] = 'IBWF-1'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task'] = 'IBWF-2'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task_request_body'] = '{"project_id": "project_1", "task_template_id": "template_1", "action_id": 1, "parent_task_id": "IBWF-1", "title": "Sub Task", "description": "description of sub task", "start_datetime": "2020-09-09 00:00:00", "due_datetime": "2099-10-09 00:00:00", "priority": "HIGH", "task_gofs": []}'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case task_log_sub_task_id'] = 'IBWF-2'

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task_performed_action_id'] = 1

snapshots['TestCase01CreateSubTaskAPITestCase.test_case sub_task_acted_at'] = '2020-09-09 12:00:00'
