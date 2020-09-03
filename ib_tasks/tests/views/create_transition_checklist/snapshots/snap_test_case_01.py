# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case body'] = {
    'message': 'transition checklist created successfully'
}

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case task_id'] = 1

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case template_id'] = 'transition_template_1'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case task_title'] = 'title_0'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case task_description'] = 'description_0'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case task_start_date'] = '2020-10-12 04:40:00'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case task_due_date'] = '2020-10-22 04:40:00'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case task_priority'] = 'HIGH'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case same_gof_order_of_gof_1'] = 1

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case gof_id_of_gof_1'] = 'gof_1'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case task_id_for_gof_1'] = 1

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case same_gof_order_of_gof_2'] = 1

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case gof_id_of_gof_2'] = 'gof_2'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case task_id_for_gof_2'] = 1

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case gof_id_of_gof_field_1'] = 1

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case field_id_of_gof_field_1'] = 'field_1'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case field_response_of_gof_field_1'] = 'iBHubs'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case gof_id_of_gof_field_2'] = 1

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case field_id_of_gof_field_2'] = 'field_2'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case field_response_of_gof_field_2'] = 'ProYuga'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case gof_id_of_gof_field_3'] = 2

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case field_id_of_gof_field_3'] = 'field_3'

snapshots['TestCase01CreateTransitionChecklistAPITestCase.test_case field_response_of_gof_field_3'] = 'iB@123!'
