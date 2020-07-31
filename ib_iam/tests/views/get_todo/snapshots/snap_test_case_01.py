# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTodoAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetTodoAPITestCase.test_case body'] = {
    'description': 'string',
    'id': 1,
    'is_completed': True,
    'remind_at': 'string'
}
