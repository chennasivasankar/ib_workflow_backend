# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateTaskAPITestCase.test_case status_code'] = '405'

snapshots['TestCase01UpdateTaskAPITestCase.test_case body'] = b'Method Not Allowed'