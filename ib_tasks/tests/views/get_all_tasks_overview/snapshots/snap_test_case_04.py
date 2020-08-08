# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04GetAllTasksOverviewAPITestCase.test_case status_code'] = '500'

snapshots['TestCase04GetAllTasksOverviewAPITestCase.test_case body'] = {
    'tasks': [
        {
        },
        {
        },
        {
            'stage_with_actions': {
                'actions': [
                    {
                        'action_type': [
                            '"action_type1" is not a valid choice.'
                        ]
                    }
                ]
            }
        }
    ]
}
