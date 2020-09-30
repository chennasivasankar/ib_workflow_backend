# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTemplateStageFlowAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetTemplateStageFlowAPITestCase.test_case body'] = {
    'actions': [
        {
            'action_name': 'action_name_1',
            'next_stage': 2,
            'previous_stage': 1
        }
    ],
    'stages': [
        {
            'color': 'orange',
            'name': 'name_1',
            'stage_id': 1
        },
        {
            'color': 'orange',
            'name': 'name_2',
            'stage_id': 2
        }
    ]
}
