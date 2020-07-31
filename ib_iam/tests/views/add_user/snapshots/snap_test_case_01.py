# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddUserAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01AddUserAPITestCase.test_case body'] = {
    'name': [
        'This field may not be blank.'
    ]
}
