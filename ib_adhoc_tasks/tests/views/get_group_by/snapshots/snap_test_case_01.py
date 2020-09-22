# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetGroupByAPITestCase.test_given_valid_data_it_returns_group_by_response status_code'] = '200'

snapshots['TestCase01GetGroupByAPITestCase.test_given_valid_data_it_returns_group_by_response body'] = [
    {
        'group_by_display_name': 'ASSIGNEE',
        'group_by_id': 1,
        'order': 1
    },
    {
        'group_by_display_name': 'STAGE',
        'group_by_id': 2,
        'order': 2
    }
]
