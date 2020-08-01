# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01DeleteUserAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01DeleteUserAPITestCase.test_case body'] = {
}

snapshots['TestCase01DeleteUserAPITestCase.test_case before_delete_user_count'] = 2

snapshots['TestCase01DeleteUserAPITestCase.test_case after_delete_user_count'] = 1
