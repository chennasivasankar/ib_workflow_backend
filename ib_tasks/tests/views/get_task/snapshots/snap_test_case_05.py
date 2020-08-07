# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05GetTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase05GetTaskAPITestCase.test_case body'] = {
    'gofs': [
    ],
    'stages_with_actions': [
    ],
    'task_id': '1',
    'template_id': 'template_0'
}
