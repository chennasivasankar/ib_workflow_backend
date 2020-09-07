# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetNextStagesRandomAssigneesOfATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01GetNextStagesRandomAssigneesOfATaskAPITestCase.test_case body'] = {
    'action_id': [
        'This field is required.'
    ],
    'task_id': [
        'This field is required.'
    ]
}
