# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase39CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase39CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'METHOD_NOT_FOUND',
    'response': 'method not found'
}

snapshots['TestCase39CreateTaskAPITestCase.test_case task_id'] = 1

snapshots['TestCase39CreateTaskAPITestCase.test_case template_id'] = 'template_1'

snapshots['TestCase39CreateTaskAPITestCase.test_case task_title'] = 'task_title'

snapshots['TestCase39CreateTaskAPITestCase.test_case task_description'] = 'task_description'

snapshots['TestCase39CreateTaskAPITestCase.test_case task_start_date'] = '2099-12-31 00:00:00'

snapshots['TestCase39CreateTaskAPITestCase.test_case task_due_date'] = '2099-12-31 12:00:00'

snapshots['TestCase39CreateTaskAPITestCase.test_case task_priority'] = 'HIGH'

snapshots['TestCase39CreateTaskAPITestCase.test_case same_gof_order_1'] = 1

snapshots['TestCase39CreateTaskAPITestCase.test_case gof_id_1'] = 'gof_1'

snapshots['TestCase39CreateTaskAPITestCase.test_case gof_task_id_1'] = 1

snapshots['TestCase39CreateTaskAPITestCase.test_case task_gof_1'] = 1

snapshots['TestCase39CreateTaskAPITestCase.test_case field_1'] = 'FIELD_ID-0'

snapshots['TestCase39CreateTaskAPITestCase.test_case field_response_1'] = 'field_0_response'
