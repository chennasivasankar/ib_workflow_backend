# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04GetTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase04GetTaskAPITestCase.test_case body'] = {
    'gofs': [
    ],
    'stages_with_actions': [
        {
            'actions': [
            ],
            'stage_display_name': 'name_0',
            'stage_id': 'stage_id_0'
        },
        {
            'actions': [
            ],
            'stage_display_name': 'name_1',
            'stage_id': 'stage_id_1'
        },
        {
            'actions': [
            ],
            'stage_display_name': 'name_2',
            'stage_id': 'stage_id_2'
        }
    ],
    'task_id': 1,
    'template_id': 'template_0'
}
