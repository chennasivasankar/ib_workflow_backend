# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddOrEditGroupByAPITestCase.test_edits_and_returns_group_by_response_dto status_code'] = '400'

snapshots['TestCase01AddOrEditGroupByAPITestCase.test_edits_and_returns_group_by_response_dto body'] = {
    'group_by_key': [
        'This field is required.'
    ]
}
