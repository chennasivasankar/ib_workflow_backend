# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetSearchableValuesAPITestCase.test_case status_code'] = '200'

snapshots['TestCase03GetSearchableValuesAPITestCase.test_case body'] = [
    {
        'id': 'user_1',
        'name': 'user_name_1'
    },
    {
        'id': 'user_2',
        'name': 'user_name_2'
    }
]
