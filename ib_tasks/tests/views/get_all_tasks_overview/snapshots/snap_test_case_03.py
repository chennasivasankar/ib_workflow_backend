# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetAllTasksOverviewAPITestCase.test_case status_code'] = '200'

snapshots['TestCase03GetAllTasksOverviewAPITestCase.test_case body'] = {
    'tasks': [
    ],
    'total_tasks': 0
}
