# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase08CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase08CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'PRIORITY_IS_REQUIRED',
    'response': 'task priority is required if action type is not no validations'
}