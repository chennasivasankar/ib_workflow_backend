# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05GetTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase05GetTaskAPITestCase.test_case body'] = {
    'description': 'description_0',
    'due_date': '2020-10-22 04:40:00',
    'gofs': [
    ],
    'priority': 'HIGH',
    'stages_with_actions': [
    ],
    'start_date': '2020-10-12 04:40:00',
    'task_id': 'IBWF-1',
    'template_id': 'template_0',
    'title': 'title_0'
}
