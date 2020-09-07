# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase15CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase15CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'USER_NEEDS_FILED_WRITABLE_PERMISSION',
    'response': 'user needs write access on field FIELD_ID-0, because user does not have at least one role in [] roles'
}
