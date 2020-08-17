# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase08UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase08UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TASK_ID',
    'response': '1 is invalid task_id send valid task_id'
}

snapshots['TestCase08UpdateTaskAPITestCase.test_case task_id'] = 1

snapshots['TestCase08UpdateTaskAPITestCase.test_case template_id'] = 'template_1'

snapshots['TestCase08UpdateTaskAPITestCase.test_case task_title'] = 'title_8'

snapshots['TestCase08UpdateTaskAPITestCase.test_case task_description'] = 'description_8'

snapshots['TestCase08UpdateTaskAPITestCase.test_case task_start_date'] = '2020-10-12 04:40:00'

snapshots['TestCase08UpdateTaskAPITestCase.test_case task_due_date'] = '2020-10-22 04:40:00'

snapshots['TestCase08UpdateTaskAPITestCase.test_case task_priority'] = 'HIGH'

snapshots['TestCase08UpdateTaskAPITestCase.test_case same_gof_order_1'] = 1

snapshots['TestCase08UpdateTaskAPITestCase.test_case gof_id_1'] = 'gof_1'
