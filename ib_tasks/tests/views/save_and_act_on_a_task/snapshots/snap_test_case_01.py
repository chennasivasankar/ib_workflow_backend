# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case body'] = {
    'stage_assignee': {
        'team_id': [
            'This field is required.'
        ]
    }
}

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case template_id'] = 'template_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case created_by_id'] = '123e4567-e89b-12d3-a456-426614174000'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_template_id'] = 'template_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_title'] = 'title_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_description'] = 'description_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_start_date'] = '2020-10-12 04:40:00'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_due_date'] = '2020-10-22 04:40:00'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_priority'] = 'HIGH'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case same_gof_order_1'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case gof_id_1'] = 'gof_1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_id_1'] = 'IBWF-2'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case same_gof_order_2'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case gof_id_2'] = 'gof_2'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_id_2'] = 'IBWF-2'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_gof_1'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_1'] = 'FIELD_ID-0'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_response_1'] = 'string'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_gof_2'] = 1

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_2'] = 'FIELD_ID-1'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_response_2'] = 'https://www.freepngimg.com/thumb/light/20246-4-light-transparent.png'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case task_gof_3'] = 2

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_3'] = 'FIELD_ID-2'

snapshots['TestCase01SaveAndActOnATaskAPITestCase.test_case field_response_3'] = '["interactors", "storages"]'
