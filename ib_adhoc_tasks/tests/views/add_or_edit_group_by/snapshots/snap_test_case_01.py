# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddOrEditGroupByAPITestCase.test_adds_and_returns_group_by_response_dto status_code'] = '200'

snapshots['TestCase01AddOrEditGroupByAPITestCase.test_adds_and_returns_group_by_response_dto body'] = {
    'display_name': 'ASSIGNEE',
    'group_by_id': 1,
    'group_by_key': 'ASSIGNEE',
    'order': 1
}

snapshots['TestCase01AddOrEditGroupByAPITestCase.test_edits_and_returns_group_by_response_dto status_code'] = '200'

snapshots['TestCase01AddOrEditGroupByAPITestCase.test_edits_and_returns_group_by_response_dto body'] = {
    'display_name': 'STAGE',
    'group_by_id': 1,
    'group_by_key': 'STAGE',
    'order': 2
}
