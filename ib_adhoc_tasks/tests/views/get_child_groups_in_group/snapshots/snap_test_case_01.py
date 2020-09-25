# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetChildGroupsInGroupAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01GetChildGroupsInGroupAPITestCase.test_case body'] = {
    'group_by_value': [
        'This field is required.'
    ]
}
